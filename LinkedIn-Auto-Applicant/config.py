"""
Configuration settings for LinkedIn Auto-Applicant
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')

    # LinkedIn settings
    LINKEDIN_EMAIL = os.environ.get('LINKEDIN_EMAIL', '')
    LINKEDIN_PASSWORD = os.environ.get('LINKEDIN_PASSWORD', '')

    # Browser settings
    HEADLESS_MODE = os.environ.get('HEADLESS_MODE', 'False').lower() == 'true'
    BROWSER_TYPE = os.environ.get('BROWSER_TYPE', 'chrome')  # chrome or firefox

    # Application settings
    MAX_APPLICATIONS_PER_SESSION = int(os.environ.get('MAX_APPLICATIONS_PER_SESSION', 50))
    DELAY_BETWEEN_APPLICATIONS = int(os.environ.get('DELAY_BETWEEN_APPLICATIONS', 3))  # seconds

    # Data paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    LOGS_DIR = os.path.join(BASE_DIR, 'logs')

    # Job search defaults
    DEFAULT_LOCATION = 'United States'
    DEFAULT_EXPERIENCE_LEVEL = ['Entry level', 'Associate', 'Mid-Senior level']
    DEFAULT_JOB_TYPE = ['Full-time']

    # LinkedIn URLs
    LINKEDIN_LOGIN_URL = 'https://www.linkedin.com/login'
    LINKEDIN_JOBS_URL = 'https://www.linkedin.com/jobs/search/'
    LINKEDIN_FEED_URL = 'https://www.linkedin.com/feed/'
