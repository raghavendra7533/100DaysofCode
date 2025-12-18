"""
LinkedIn automation for job search and application
"""
import time
import re
import logging
from typing import List, Optional, Dict, Any
from urllib.parse import urlencode
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from browser import BrowserManager
from models import UserProfile, JobPreferences, ApplicationRecord, ApplicationTracker
from config import Config

logger = logging.getLogger(__name__)


class LinkedInAutomation:
    """LinkedIn job application automation"""

    def __init__(self, profile: UserProfile, preferences: JobPreferences):
        self.profile = profile
        self.preferences = preferences
        self.browser = BrowserManager()
        self.tracker = ApplicationTracker()
        self.is_logged_in = False
        self.applications_this_session = 0

    def start(self):
        """Start the browser"""
        self.browser.start()

    def quit(self):
        """Close the browser"""
        self.browser.quit()

    def login(self, email: str = None, password: str = None) -> bool:
        """Login to LinkedIn"""
        email = email or Config.LINKEDIN_EMAIL
        password = password or Config.LINKEDIN_PASSWORD

        if not email or not password:
            logger.error("LinkedIn credentials not provided")
            return False

        try:
            self.browser.get(Config.LINKEDIN_LOGIN_URL)
            self.browser.wait_for_page_load()
            self.browser.human_delay(1, 2)

            # Find and fill email field
            email_field = self.browser.find_element(By.ID, 'username')
            if not email_field:
                logger.error("Could not find email field")
                return False

            self.browser.safe_send_keys(email_field, email)
            self.browser.human_delay(0.3, 0.8)

            # Find and fill password field
            password_field = self.browser.find_element(By.ID, 'password')
            if not password_field:
                logger.error("Could not find password field")
                return False

            self.browser.safe_send_keys(password_field, password)
            self.browser.human_delay(0.3, 0.8)

            # Click login button
            login_button = self.browser.find_clickable(
                By.CSS_SELECTOR,
                'button[type="submit"]'
            )
            if login_button:
                self.browser.click_element(login_button)
            else:
                password_field.send_keys(Keys.RETURN)

            self.browser.human_delay(3, 5)
            self.browser.wait_for_page_load()

            # Check if login was successful
            if 'feed' in self.browser.get_current_url() or 'mynetwork' in self.browser.get_current_url():
                self.is_logged_in = True
                logger.info("Successfully logged in to LinkedIn")
                return True

            # Check for security verification
            if 'checkpoint' in self.browser.get_current_url():
                logger.warning("Security verification required - please complete manually")
                # Wait for manual verification
                input("Press Enter after completing verification...")
                self.browser.human_delay(2, 3)
                self.is_logged_in = True
                return True

            logger.error("Login failed - unexpected page")
            return False

        except Exception as e:
            logger.error(f"Login error: {e}")
            return False

    def build_search_url(self) -> str:
        """Build LinkedIn job search URL with filters"""
        params = {}

        # Keywords
        if self.preferences.job_titles:
            params['keywords'] = ' OR '.join(self.preferences.job_titles)

        # Location
        if self.preferences.locations:
            params['location'] = self.preferences.locations[0]

        # Easy Apply filter
        if self.preferences.easy_apply_only:
            params['f_AL'] = 'true'

        # Experience level mapping
        exp_level_map = {
            'Internship': '1',
            'Entry level': '2',
            'Associate': '3',
            'Mid-Senior level': '4',
            'Director': '5',
            'Executive': '6'
        }
        if self.preferences.experience_levels:
            levels = [exp_level_map.get(lvl, '') for lvl in self.preferences.experience_levels]
            levels = [l for l in levels if l]
            if levels:
                params['f_E'] = ','.join(levels)

        # Job type mapping
        job_type_map = {
            'Full-time': 'F',
            'Part-time': 'P',
            'Contract': 'C',
            'Temporary': 'T',
            'Internship': 'I',
            'Volunteer': 'V',
            'Other': 'O'
        }
        if self.preferences.job_types:
            types = [job_type_map.get(jt, '') for jt in self.preferences.job_types]
            types = [t for t in types if t]
            if types:
                params['f_JT'] = ','.join(types)

        # Remote filter
        remote_map = {
            'On-site': '1',
            'Remote': '2',
            'Hybrid': '3'
        }
        if self.preferences.remote_preference and self.preferences.remote_preference != 'Any':
            remote_val = remote_map.get(self.preferences.remote_preference)
            if remote_val:
                params['f_WT'] = remote_val

        # Date posted mapping
        date_map = {
            'Past 24 hours': 'r86400',
            'Past week': 'r604800',
            'Past month': 'r2592000',
            'Any time': ''
        }
        if self.preferences.date_posted:
            date_val = date_map.get(self.preferences.date_posted, '')
            if date_val:
                params['f_TPR'] = date_val

        url = Config.LINKEDIN_JOBS_URL
        if params:
            url += '?' + urlencode(params)

        return url

    def search_jobs(self) -> List[Dict[str, Any]]:
        """Search for jobs matching preferences"""
        jobs = []
        search_url = self.build_search_url()

        logger.info(f"Searching jobs: {search_url}")
        self.browser.get(search_url)
        self.browser.wait_for_page_load()
        self.browser.human_delay(2, 4)

        # Get total results count
        try:
            results_count = self.browser.find_element(
                By.CSS_SELECTOR,
                '.jobs-search-results-list__subtitle'
            )
            if results_count:
                logger.info(f"Found: {results_count.text}")
        except Exception:
            pass

        # Scroll to load more jobs
        for _ in range(3):
            self.browser.scroll_page(500)
            self.browser.human_delay(0.5, 1)

        # Find job cards
        job_cards = self.browser.find_elements(
            By.CSS_SELECTOR,
            '.jobs-search-results__list-item'
        )

        logger.info(f"Found {len(job_cards)} job listings")

        for card in job_cards:
            try:
                job_data = self._extract_job_data(card)
                if job_data:
                    # Check exclusions
                    if self._should_skip_job(job_data):
                        continue
                    # Check if already applied
                    if self.tracker.has_applied(job_data['job_id']):
                        continue
                    jobs.append(job_data)
            except Exception as e:
                logger.error(f"Error extracting job data: {e}")

        return jobs

    def _extract_job_data(self, card) -> Optional[Dict[str, Any]]:
        """Extract job information from card element"""
        try:
            job_data = {}

            # Get job ID from data attribute or link
            try:
                job_id = card.get_attribute('data-occludable-job-id')
                if not job_id:
                    link = card.find_element(By.CSS_SELECTOR, 'a[href*="/jobs/view/"]')
                    href = link.get_attribute('href')
                    job_id = re.search(r'/jobs/view/(\d+)', href)
                    job_id = job_id.group(1) if job_id else None
                job_data['job_id'] = job_id
            except Exception:
                return None

            # Get job title
            try:
                title_elem = card.find_element(By.CSS_SELECTOR, '.job-card-list__title')
                job_data['title'] = title_elem.text.strip()
            except Exception:
                job_data['title'] = 'Unknown Title'

            # Get company name
            try:
                company_elem = card.find_element(By.CSS_SELECTOR, '.job-card-container__primary-description')
                job_data['company'] = company_elem.text.strip()
            except Exception:
                job_data['company'] = 'Unknown Company'

            # Get location
            try:
                location_elem = card.find_element(By.CSS_SELECTOR, '.job-card-container__metadata-item')
                job_data['location'] = location_elem.text.strip()
            except Exception:
                job_data['location'] = 'Unknown Location'

            # Build job URL
            job_data['url'] = f"https://www.linkedin.com/jobs/view/{job_data['job_id']}"

            # Check for Easy Apply badge
            try:
                easy_apply = card.find_element(By.CSS_SELECTOR, '.job-card-container__apply-method')
                job_data['easy_apply'] = 'Easy Apply' in easy_apply.text
            except Exception:
                job_data['easy_apply'] = False

            job_data['element'] = card
            return job_data

        except Exception as e:
            logger.error(f"Error extracting job data: {e}")
            return None

    def _should_skip_job(self, job_data: Dict[str, Any]) -> bool:
        """Check if job should be skipped based on preferences"""
        # Check excluded companies
        company_lower = job_data.get('company', '').lower()
        for excluded in self.preferences.excluded_companies:
            if excluded.lower() in company_lower:
                logger.info(f"Skipping excluded company: {job_data['company']}")
                return True

        # Check excluded keywords
        title_lower = job_data.get('title', '').lower()
        for excluded in self.preferences.excluded_keywords:
            if excluded.lower() in title_lower:
                logger.info(f"Skipping excluded keyword in title: {job_data['title']}")
                return True

        # Must be Easy Apply if preference is set
        if self.preferences.easy_apply_only and not job_data.get('easy_apply', False):
            return True

        return False

    def apply_to_job(self, job_data: Dict[str, Any]) -> bool:
        """Apply to a single job"""
        if self.applications_this_session >= Config.MAX_APPLICATIONS_PER_SESSION:
            logger.warning("Max applications per session reached")
            return False

        job_id = job_data['job_id']
        job_title = job_data['title']
        company = job_data['company']

        logger.info(f"Applying to: {job_title} at {company}")

        try:
            # Navigate to job page
            self.browser.get(job_data['url'])
            self.browser.wait_for_page_load()
            self.browser.human_delay(2, 3)

            # Find and click Easy Apply button
            easy_apply_btn = self._find_easy_apply_button()
            if not easy_apply_btn:
                logger.warning(f"No Easy Apply button found for job {job_id}")
                self._record_application(job_data, 'Skipped', 'No Easy Apply button')
                return False

            self.browser.click_element(easy_apply_btn)
            self.browser.human_delay(1, 2)

            # Handle application modal/form
            success = self._complete_application()

            if success:
                self._record_application(job_data, 'Applied')
                self.applications_this_session += 1
                logger.info(f"Successfully applied to {job_title} at {company}")
                return True
            else:
                self._record_application(job_data, 'Failed', 'Could not complete application')
                return False

        except Exception as e:
            logger.error(f"Error applying to job: {e}")
            self._record_application(job_data, 'Failed', str(e))
            return False

    def _find_easy_apply_button(self):
        """Find the Easy Apply button on job page"""
        selectors = [
            'button.jobs-apply-button',
            'button[aria-label*="Easy Apply"]',
            '.jobs-apply-button--top-card',
            'button.jobs-s-apply-button',
        ]

        for selector in selectors:
            button = self.browser.find_clickable(By.CSS_SELECTOR, selector, timeout=3)
            if button and 'Easy Apply' in button.text:
                return button

        return None

    def _complete_application(self) -> bool:
        """Complete the application form"""
        max_steps = 10
        step = 0

        while step < max_steps:
            self.browser.human_delay(1, 2)

            # Check if we've submitted successfully
            if self._check_application_submitted():
                return True

            # Check for error messages
            if self._check_for_errors():
                return False

            # Fill current form step
            self._fill_form_fields()

            # Handle file upload (resume)
            self._handle_resume_upload()

            # Find next/submit button
            if self._click_next_or_submit():
                step += 1
            else:
                # Try to close any popup and check success
                self.browser.human_delay(1, 2)
                if self._check_application_submitted():
                    return True
                return False

        return False

    def _fill_form_fields(self):
        """Fill all visible form fields"""
        # Text inputs
        text_inputs = self.browser.find_elements(
            By.CSS_SELECTOR,
            'input[type="text"], input[type="email"], input[type="tel"]'
        )

        for input_field in text_inputs:
            try:
                if not input_field.is_displayed():
                    continue

                label = self._get_field_label(input_field)
                value = self._get_answer_for_field(label, input_field)

                if value and not input_field.get_attribute('value'):
                    self.browser.safe_send_keys(input_field, value)
                    self.browser.human_delay(0.2, 0.5)
            except Exception as e:
                logger.debug(f"Error filling text field: {e}")

        # Select dropdowns
        selects = self.browser.find_elements(By.TAG_NAME, 'select')
        for select in selects:
            try:
                if not select.is_displayed():
                    continue

                label = self._get_field_label(select)
                value = self._get_answer_for_field(label, select)

                if value:
                    self._select_option(select, value)
                    self.browser.human_delay(0.2, 0.5)
            except Exception as e:
                logger.debug(f"Error filling select field: {e}")

        # Radio buttons
        self._handle_radio_buttons()

        # Textareas
        textareas = self.browser.find_elements(By.TAG_NAME, 'textarea')
        for textarea in textareas:
            try:
                if not textarea.is_displayed():
                    continue

                label = self._get_field_label(textarea)
                value = self._get_answer_for_field(label, textarea)

                if value and not textarea.get_attribute('value'):
                    self.browser.safe_send_keys(textarea, value)
                    self.browser.human_delay(0.2, 0.5)
            except Exception as e:
                logger.debug(f"Error filling textarea: {e}")

    def _get_field_label(self, element) -> str:
        """Get the label text for a form field"""
        try:
            # Try to find associated label
            field_id = element.get_attribute('id')
            if field_id:
                label = self.browser.driver.find_element(
                    By.CSS_SELECTOR, f'label[for="{field_id}"]'
                )
                if label:
                    return label.text.strip().lower()

            # Try parent label
            parent = element.find_element(By.XPATH, './ancestor::label')
            if parent:
                return parent.text.strip().lower()

            # Try nearby text
            parent = element.find_element(By.XPATH, './..')
            return parent.text.strip().lower()
        except Exception:
            return ""

    def _get_answer_for_field(self, label: str, element) -> str:
        """Get answer for a form field based on label"""
        label = label.lower()
        pi = self.profile.personal_info

        # Check custom answers first
        for pattern, answer in self.profile.custom_answers.items():
            if pattern.lower() in label:
                return answer

        # Common field mappings
        mappings = {
            'first name': pi.first_name,
            'last name': pi.last_name,
            'full name': f"{pi.first_name} {pi.last_name}",
            'email': pi.email,
            'phone': pi.phone,
            'mobile': pi.phone,
            'city': pi.city,
            'state': pi.state,
            'zip': pi.zip_code,
            'postal': pi.zip_code,
            'country': pi.country,
            'linkedin': pi.linkedin_url,
            'portfolio': pi.portfolio_url,
            'website': pi.portfolio_url,
            'github': pi.github_url,
            'years of experience': str(self.profile.years_of_experience),
            'experience': str(self.profile.years_of_experience),
            'salary': self.profile.salary_expectation,
            'compensation': self.profile.salary_expectation,
            'start date': self.profile.start_date_availability,
            'availability': self.profile.start_date_availability,
        }

        # Authorization questions
        if any(word in label for word in ['authorized', 'authorization', 'legally']):
            return self.profile.work_authorization

        if any(word in label for word in ['sponsor', 'visa']):
            return self.profile.requires_sponsorship

        if any(word in label for word in ['relocate', 'relocation']):
            return self.profile.willing_to_relocate

        # Match against mappings
        for key, value in mappings.items():
            if key in label and value:
                return value

        return ""

    def _select_option(self, select_element, value: str):
        """Select an option from dropdown"""
        try:
            select = Select(select_element)
            options = [opt.text.lower() for opt in select.options]

            # Try exact match first
            value_lower = value.lower()
            for i, opt in enumerate(options):
                if value_lower == opt:
                    select.select_by_index(i)
                    return

            # Try partial match
            for i, opt in enumerate(options):
                if value_lower in opt or opt in value_lower:
                    select.select_by_index(i)
                    return

            # Try yes/no matching
            if value_lower in ['yes', 'true', '1']:
                for i, opt in enumerate(options):
                    if 'yes' in opt:
                        select.select_by_index(i)
                        return

            if value_lower in ['no', 'false', '0']:
                for i, opt in enumerate(options):
                    if 'no' in opt:
                        select.select_by_index(i)
                        return

        except Exception as e:
            logger.debug(f"Error selecting option: {e}")

    def _handle_radio_buttons(self):
        """Handle radio button groups"""
        fieldsets = self.browser.find_elements(By.TAG_NAME, 'fieldset')

        for fieldset in fieldsets:
            try:
                if not fieldset.is_displayed():
                    continue

                legend = fieldset.find_element(By.TAG_NAME, 'legend')
                label = legend.text.strip().lower() if legend else ""

                answer = self._get_answer_for_field(label, fieldset)
                if not answer:
                    continue

                radios = fieldset.find_elements(By.CSS_SELECTOR, 'input[type="radio"]')
                for radio in radios:
                    try:
                        radio_label = radio.find_element(By.XPATH, './following-sibling::label | ./parent::label')
                        if answer.lower() in radio_label.text.lower():
                            if not radio.is_selected():
                                self.browser.click_element(radio)
                            break
                    except Exception:
                        pass
            except Exception as e:
                logger.debug(f"Error handling radio buttons: {e}")

    def _handle_resume_upload(self):
        """Handle resume file upload"""
        if not self.profile.resume_path:
            return

        try:
            # Find file input
            file_inputs = self.browser.find_elements(
                By.CSS_SELECTOR,
                'input[type="file"]'
            )

            for file_input in file_inputs:
                try:
                    if file_input.is_displayed() or True:  # File inputs are often hidden
                        file_input.send_keys(self.profile.resume_path)
                        self.browser.human_delay(1, 2)
                        logger.info("Resume uploaded")
                        return
                except Exception:
                    pass
        except Exception as e:
            logger.debug(f"Error uploading resume: {e}")

    def _click_next_or_submit(self) -> bool:
        """Click next or submit button"""
        button_selectors = [
            'button[aria-label="Submit application"]',
            'button[aria-label="Continue to next step"]',
            'button[aria-label="Review your application"]',
            'button[data-control-name="submit_unify"]',
            'button[data-control-name="continue_unify"]',
            'footer button.artdeco-button--primary',
        ]

        for selector in button_selectors:
            button = self.browser.find_clickable(By.CSS_SELECTOR, selector, timeout=2)
            if button and button.is_enabled():
                button_text = button.text.lower()
                if any(word in button_text for word in ['submit', 'next', 'continue', 'review', 'apply']):
                    self.browser.click_element(button)
                    self.browser.human_delay(1, 2)
                    return True

        return False

    def _check_application_submitted(self) -> bool:
        """Check if application was successfully submitted"""
        success_indicators = [
            'application was sent',
            'application submitted',
            'applied successfully',
            'your application has been submitted'
        ]

        page_text = self.browser.get_page_source().lower()
        for indicator in success_indicators:
            if indicator in page_text:
                # Close success modal
                close_btn = self.browser.find_clickable(
                    By.CSS_SELECTOR,
                    'button[aria-label="Dismiss"]',
                    timeout=2
                )
                if close_btn:
                    self.browser.click_element(close_btn)
                return True

        return False

    def _check_for_errors(self) -> bool:
        """Check for application errors"""
        error_selectors = [
            '.artdeco-inline-feedback--error',
            '.fb-form-element__error-text',
        ]

        for selector in error_selectors:
            errors = self.browser.find_elements(By.CSS_SELECTOR, selector, timeout=1)
            if errors:
                visible_errors = [e for e in errors if e.is_displayed()]
                if visible_errors:
                    logger.warning(f"Form error: {visible_errors[0].text}")
                    return True

        return False

    def _record_application(self, job_data: Dict, status: str, notes: str = ""):
        """Record application in tracker"""
        record = ApplicationRecord(
            job_id=job_data['job_id'],
            job_title=job_data['title'],
            company_name=job_data['company'],
            job_url=job_data['url'],
            status=status,
            notes=notes
        )
        self.tracker.add_application(record)

    def run_auto_apply(self, max_applications: int = None) -> Dict[str, int]:
        """Run the auto-apply process"""
        max_apps = max_applications or Config.MAX_APPLICATIONS_PER_SESSION

        if not self.is_logged_in:
            logger.error("Not logged in to LinkedIn")
            return {'applied': 0, 'failed': 0, 'skipped': 0}

        jobs = self.search_jobs()
        logger.info(f"Found {len(jobs)} eligible jobs to apply")

        results = {'applied': 0, 'failed': 0, 'skipped': 0}

        for job in jobs:
            if results['applied'] >= max_apps:
                logger.info(f"Reached max applications limit: {max_apps}")
                break

            success = self.apply_to_job(job)

            if success:
                results['applied'] += 1
            else:
                results['failed'] += 1

            # Delay between applications
            time.sleep(Config.DELAY_BETWEEN_APPLICATIONS)

        logger.info(f"Auto-apply complete: {results}")
        return results
