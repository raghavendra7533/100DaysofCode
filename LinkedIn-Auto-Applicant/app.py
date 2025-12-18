"""
Flask Web Application for LinkedIn Auto-Applicant
"""
import os
import json
import threading
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from werkzeug.utils import secure_filename
from config import Config
from models import UserProfile, JobPreferences, ApplicationTracker, PersonalInfo, Education, WorkExperience
from linkedin import LinkedInAutomation

app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config['UPLOAD_FOLDER'] = os.path.join(Config.DATA_DIR, 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Global state for automation
automation_state = {
    'running': False,
    'progress': 0,
    'status': 'idle',
    'results': None,
    'thread': None
}


@app.route('/')
def index():
    """Home page"""
    profile = UserProfile.load()
    preferences = JobPreferences.load()
    tracker = ApplicationTracker()
    stats = tracker.get_stats()
    recent = tracker.get_recent(5)

    return render_template('index.html',
                           profile=profile,
                           preferences=preferences,
                           stats=stats,
                           recent=recent)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    """User profile page"""
    user_profile = UserProfile.load()

    if request.method == 'POST':
        # Update personal info
        user_profile.personal_info = PersonalInfo(
            first_name=request.form.get('first_name', ''),
            last_name=request.form.get('last_name', ''),
            email=request.form.get('email', ''),
            phone=request.form.get('phone', ''),
            city=request.form.get('city', ''),
            state=request.form.get('state', ''),
            country=request.form.get('country', 'United States'),
            zip_code=request.form.get('zip_code', ''),
            linkedin_url=request.form.get('linkedin_url', ''),
            portfolio_url=request.form.get('portfolio_url', ''),
            github_url=request.form.get('github_url', '')
        )

        # Update application defaults
        user_profile.years_of_experience = int(request.form.get('years_of_experience', 0))
        user_profile.highest_education = request.form.get('highest_education', '')
        user_profile.work_authorization = request.form.get('work_authorization', 'Yes')
        user_profile.requires_sponsorship = request.form.get('requires_sponsorship', 'No')
        user_profile.willing_to_relocate = request.form.get('willing_to_relocate', 'Yes')
        user_profile.salary_expectation = request.form.get('salary_expectation', '')
        user_profile.start_date_availability = request.form.get('start_date_availability', 'Immediately')

        # Handle skills
        skills_text = request.form.get('skills', '')
        user_profile.skills = [s.strip() for s in skills_text.split(',') if s.strip()]

        # Handle resume upload
        if 'resume' in request.files:
            file = request.files['resume']
            if file and file.filename:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                user_profile.resume_path = filepath

        # Handle cover letter
        user_profile.cover_letter_template = request.form.get('cover_letter', '')

        # Save profile
        user_profile.save()
        flash('Profile saved successfully!', 'success')
        return redirect(url_for('profile'))

    return render_template('profile.html', profile=user_profile)


@app.route('/education', methods=['GET', 'POST'])
def education():
    """Education management page"""
    user_profile = UserProfile.load()

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            new_edu = Education(
                school_name=request.form.get('school_name', ''),
                degree=request.form.get('degree', ''),
                field_of_study=request.form.get('field_of_study', ''),
                start_date=request.form.get('start_date', ''),
                end_date=request.form.get('end_date', ''),
                gpa=request.form.get('gpa', '')
            )
            user_profile.education.append(new_edu)
            user_profile.save()
            flash('Education added!', 'success')

        elif action == 'delete':
            index = int(request.form.get('index', -1))
            if 0 <= index < len(user_profile.education):
                user_profile.education.pop(index)
                user_profile.save()
                flash('Education removed!', 'success')

        return redirect(url_for('education'))

    return render_template('education.html', profile=user_profile)


@app.route('/experience', methods=['GET', 'POST'])
def experience():
    """Work experience management page"""
    user_profile = UserProfile.load()

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            new_exp = WorkExperience(
                company_name=request.form.get('company_name', ''),
                job_title=request.form.get('job_title', ''),
                location=request.form.get('location', ''),
                start_date=request.form.get('start_date', ''),
                end_date=request.form.get('end_date', ''),
                is_current=request.form.get('is_current') == 'on',
                description=request.form.get('description', '')
            )
            user_profile.work_experience.append(new_exp)
            user_profile.save()
            flash('Experience added!', 'success')

        elif action == 'delete':
            index = int(request.form.get('index', -1))
            if 0 <= index < len(user_profile.work_experience):
                user_profile.work_experience.pop(index)
                user_profile.save()
                flash('Experience removed!', 'success')

        return redirect(url_for('experience'))

    return render_template('experience.html', profile=user_profile)


@app.route('/preferences', methods=['GET', 'POST'])
def preferences():
    """Job preferences page"""
    job_prefs = JobPreferences.load()

    if request.method == 'POST':
        # Job titles
        job_titles = request.form.get('job_titles', '')
        job_prefs.job_titles = [t.strip() for t in job_titles.split(',') if t.strip()]

        # Locations
        locations = request.form.get('locations', '')
        job_prefs.locations = [l.strip() for l in locations.split(',') if l.strip()]

        # Other preferences
        job_prefs.remote_preference = request.form.get('remote_preference', 'Any')
        job_prefs.easy_apply_only = request.form.get('easy_apply_only') == 'on'
        job_prefs.date_posted = request.form.get('date_posted', 'Past week')

        # Experience levels
        job_prefs.experience_levels = request.form.getlist('experience_levels')

        # Job types
        job_prefs.job_types = request.form.getlist('job_types')

        # Keywords
        keywords = request.form.get('keywords', '')
        job_prefs.keywords = [k.strip() for k in keywords.split(',') if k.strip()]

        # Exclusions
        excluded_companies = request.form.get('excluded_companies', '')
        job_prefs.excluded_companies = [c.strip() for c in excluded_companies.split(',') if c.strip()]

        excluded_keywords = request.form.get('excluded_keywords', '')
        job_prefs.excluded_keywords = [k.strip() for k in excluded_keywords.split(',') if k.strip()]

        job_prefs.save()
        flash('Preferences saved!', 'success')
        return redirect(url_for('preferences'))

    return render_template('preferences.html', preferences=job_prefs)


@app.route('/custom-answers', methods=['GET', 'POST'])
def custom_answers():
    """Custom answers for application questions"""
    user_profile = UserProfile.load()

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            question = request.form.get('question', '').strip()
            answer = request.form.get('answer', '').strip()
            if question and answer:
                user_profile.custom_answers[question] = answer
                user_profile.save()
                flash('Custom answer added!', 'success')

        elif action == 'delete':
            question = request.form.get('question', '')
            if question in user_profile.custom_answers:
                del user_profile.custom_answers[question]
                user_profile.save()
                flash('Custom answer removed!', 'success')

        return redirect(url_for('custom_answers'))

    return render_template('custom_answers.html', profile=user_profile)


@app.route('/applications')
def applications():
    """View application history"""
    tracker = ApplicationTracker()
    stats = tracker.get_stats()
    all_apps = tracker.applications

    # Sort by date, newest first
    all_apps = sorted(all_apps, key=lambda x: x.applied_at, reverse=True)

    return render_template('applications.html', applications=all_apps, stats=stats)


@app.route('/run', methods=['GET', 'POST'])
def run():
    """Run auto-apply page"""
    if request.method == 'POST':
        if automation_state['running']:
            flash('Auto-apply is already running!', 'warning')
            return redirect(url_for('run'))

        # Get settings from form
        linkedin_email = request.form.get('linkedin_email', '')
        linkedin_password = request.form.get('linkedin_password', '')
        max_applications = int(request.form.get('max_applications', 25))
        headless = request.form.get('headless') == 'on'

        if not linkedin_email or not linkedin_password:
            flash('LinkedIn credentials are required!', 'error')
            return redirect(url_for('run'))

        # Start automation in background thread
        thread = threading.Thread(
            target=run_automation,
            args=(linkedin_email, linkedin_password, max_applications, headless)
        )
        thread.daemon = True
        thread.start()

        automation_state['thread'] = thread
        flash('Auto-apply started!', 'success')
        return redirect(url_for('run'))

    profile = UserProfile.load()
    preferences = JobPreferences.load()
    return render_template('run.html', state=automation_state, profile=profile, preferences=preferences)


@app.route('/stop', methods=['POST'])
def stop():
    """Stop the auto-apply process"""
    automation_state['running'] = False
    automation_state['status'] = 'stopping'
    flash('Stopping auto-apply...', 'info')
    return redirect(url_for('run'))


@app.route('/status')
def status():
    """Get current automation status"""
    return jsonify({
        'running': automation_state['running'],
        'status': automation_state['status'],
        'progress': automation_state['progress'],
        'results': automation_state['results']
    })


@app.route('/export')
def export():
    """Export applications to CSV"""
    tracker = ApplicationTracker()
    filepath = tracker.export_to_csv()
    flash(f'Exported to {filepath}', 'success')
    return redirect(url_for('applications'))


def run_automation(email: str, password: str, max_apps: int, headless: bool):
    """Run the automation process in background"""
    global automation_state

    automation_state['running'] = True
    automation_state['status'] = 'initializing'
    automation_state['progress'] = 0
    automation_state['results'] = None

    try:
        profile = UserProfile.load()
        preferences = JobPreferences.load()

        automation = LinkedInAutomation(profile, preferences)
        automation.browser.headless = headless

        automation_state['status'] = 'starting browser'
        automation.start()

        automation_state['status'] = 'logging in'
        if not automation.login(email, password):
            automation_state['status'] = 'login failed'
            automation_state['running'] = False
            automation.quit()
            return

        automation_state['status'] = 'searching jobs'
        automation_state['progress'] = 10

        results = automation.run_auto_apply(max_apps)

        automation_state['results'] = results
        automation_state['status'] = 'completed'
        automation_state['progress'] = 100

        automation.quit()

    except Exception as e:
        automation_state['status'] = f'error: {str(e)}'

    finally:
        automation_state['running'] = False


if __name__ == '__main__':
    app.run(debug=True, port=5000)
