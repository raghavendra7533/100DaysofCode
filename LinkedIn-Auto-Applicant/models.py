"""
Data models for LinkedIn Auto-Applicant
"""
import json
import os
from dataclasses import dataclass, field, asdict
from typing import List, Optional
from datetime import datetime
from config import Config


@dataclass
class PersonalInfo:
    """User's personal information"""
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    phone: str = ""
    city: str = ""
    state: str = ""
    country: str = "United States"
    zip_code: str = ""
    linkedin_url: str = ""
    portfolio_url: str = ""
    github_url: str = ""


@dataclass
class Education:
    """Education entry"""
    school_name: str = ""
    degree: str = ""
    field_of_study: str = ""
    start_date: str = ""
    end_date: str = ""
    gpa: str = ""


@dataclass
class WorkExperience:
    """Work experience entry"""
    company_name: str = ""
    job_title: str = ""
    location: str = ""
    start_date: str = ""
    end_date: str = ""
    is_current: bool = False
    description: str = ""


@dataclass
class UserProfile:
    """Complete user profile for job applications"""
    personal_info: PersonalInfo = field(default_factory=PersonalInfo)
    education: List[Education] = field(default_factory=list)
    work_experience: List[WorkExperience] = field(default_factory=list)
    skills: List[str] = field(default_factory=list)
    resume_path: str = ""
    cover_letter_template: str = ""

    # Common application questions
    years_of_experience: int = 0
    highest_education: str = ""
    work_authorization: str = "Yes"
    requires_sponsorship: str = "No"
    willing_to_relocate: str = "Yes"
    salary_expectation: str = ""
    start_date_availability: str = "Immediately"

    # Additional questions answers (key: question pattern, value: answer)
    custom_answers: dict = field(default_factory=dict)

    def to_dict(self):
        """Convert profile to dictionary"""
        data = {
            'personal_info': asdict(self.personal_info),
            'education': [asdict(edu) for edu in self.education],
            'work_experience': [asdict(exp) for exp in self.work_experience],
            'skills': self.skills,
            'resume_path': self.resume_path,
            'cover_letter_template': self.cover_letter_template,
            'years_of_experience': self.years_of_experience,
            'highest_education': self.highest_education,
            'work_authorization': self.work_authorization,
            'requires_sponsorship': self.requires_sponsorship,
            'willing_to_relocate': self.willing_to_relocate,
            'salary_expectation': self.salary_expectation,
            'start_date_availability': self.start_date_availability,
            'custom_answers': self.custom_answers
        }
        return data

    @classmethod
    def from_dict(cls, data: dict):
        """Create profile from dictionary"""
        profile = cls()
        if 'personal_info' in data:
            profile.personal_info = PersonalInfo(**data['personal_info'])
        if 'education' in data:
            profile.education = [Education(**edu) for edu in data['education']]
        if 'work_experience' in data:
            profile.work_experience = [WorkExperience(**exp) for exp in data['work_experience']]
        if 'skills' in data:
            profile.skills = data['skills']
        if 'resume_path' in data:
            profile.resume_path = data['resume_path']
        if 'cover_letter_template' in data:
            profile.cover_letter_template = data['cover_letter_template']
        if 'years_of_experience' in data:
            profile.years_of_experience = data['years_of_experience']
        if 'highest_education' in data:
            profile.highest_education = data['highest_education']
        if 'work_authorization' in data:
            profile.work_authorization = data['work_authorization']
        if 'requires_sponsorship' in data:
            profile.requires_sponsorship = data['requires_sponsorship']
        if 'willing_to_relocate' in data:
            profile.willing_to_relocate = data['willing_to_relocate']
        if 'salary_expectation' in data:
            profile.salary_expectation = data['salary_expectation']
        if 'start_date_availability' in data:
            profile.start_date_availability = data['start_date_availability']
        if 'custom_answers' in data:
            profile.custom_answers = data['custom_answers']
        return profile

    def save(self, filename: str = 'user_profile.json'):
        """Save profile to JSON file"""
        filepath = os.path.join(Config.DATA_DIR, filename)
        os.makedirs(Config.DATA_DIR, exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
        return filepath

    @classmethod
    def load(cls, filename: str = 'user_profile.json'):
        """Load profile from JSON file"""
        filepath = os.path.join(Config.DATA_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                data = json.load(f)
            return cls.from_dict(data)
        return cls()


@dataclass
class JobPreferences:
    """Job search preferences"""
    job_titles: List[str] = field(default_factory=list)
    locations: List[str] = field(default_factory=list)
    remote_preference: str = "Any"  # Remote, On-site, Hybrid, Any
    experience_levels: List[str] = field(default_factory=list)
    job_types: List[str] = field(default_factory=list)  # Full-time, Part-time, Contract, etc.
    industries: List[str] = field(default_factory=list)
    company_sizes: List[str] = field(default_factory=list)
    min_salary: int = 0
    keywords: List[str] = field(default_factory=list)
    excluded_companies: List[str] = field(default_factory=list)
    excluded_keywords: List[str] = field(default_factory=list)
    easy_apply_only: bool = True
    date_posted: str = "Past week"  # Past 24 hours, Past week, Past month, Any time

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def save(self, filename: str = 'job_preferences.json'):
        filepath = os.path.join(Config.DATA_DIR, filename)
        os.makedirs(Config.DATA_DIR, exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
        return filepath

    @classmethod
    def load(cls, filename: str = 'job_preferences.json'):
        filepath = os.path.join(Config.DATA_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                data = json.load(f)
            return cls.from_dict(data)
        return cls()


@dataclass
class ApplicationRecord:
    """Record of a job application"""
    job_id: str
    job_title: str
    company_name: str
    job_url: str
    applied_at: str = ""
    status: str = "Applied"  # Applied, Failed, Skipped
    notes: str = ""

    def __post_init__(self):
        if not self.applied_at:
            self.applied_at = datetime.now().isoformat()


class ApplicationTracker:
    """Track all job applications"""

    def __init__(self, filename: str = 'applications.json'):
        self.filename = filename
        self.filepath = os.path.join(Config.DATA_DIR, filename)
        self.applications: List[ApplicationRecord] = []
        self.load()

    def load(self):
        """Load applications from file"""
        os.makedirs(Config.DATA_DIR, exist_ok=True)
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                data = json.load(f)
            self.applications = [ApplicationRecord(**app) for app in data]

    def save(self):
        """Save applications to file"""
        with open(self.filepath, 'w') as f:
            json.dump([asdict(app) for app in self.applications], f, indent=2)

    def add_application(self, record: ApplicationRecord):
        """Add a new application record"""
        self.applications.append(record)
        self.save()

    def has_applied(self, job_id: str) -> bool:
        """Check if already applied to a job"""
        return any(app.job_id == job_id for app in self.applications)

    def get_stats(self) -> dict:
        """Get application statistics"""
        total = len(self.applications)
        applied = sum(1 for app in self.applications if app.status == "Applied")
        failed = sum(1 for app in self.applications if app.status == "Failed")
        skipped = sum(1 for app in self.applications if app.status == "Skipped")

        return {
            'total': total,
            'applied': applied,
            'failed': failed,
            'skipped': skipped
        }

    def get_recent(self, limit: int = 10) -> List[ApplicationRecord]:
        """Get most recent applications"""
        sorted_apps = sorted(
            self.applications,
            key=lambda x: x.applied_at,
            reverse=True
        )
        return sorted_apps[:limit]

    def export_to_csv(self, filename: str = 'applications_export.csv'):
        """Export applications to CSV"""
        import csv
        filepath = os.path.join(Config.DATA_DIR, filename)
        with open(filepath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'job_id', 'job_title', 'company_name', 'job_url',
                'applied_at', 'status', 'notes'
            ])
            writer.writeheader()
            for app in self.applications:
                writer.writerow(asdict(app))
        return filepath
