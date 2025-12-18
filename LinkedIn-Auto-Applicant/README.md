# LinkedIn Auto-Applicant

An automated LinkedIn job application tool that helps you apply to multiple jobs with a single click. Fill in your profile once, set your job preferences, and let the tool do the rest.

## Features

- **Profile Management**: Save your personal information, education, work experience, and skills
- **Job Preferences**: Configure job titles, locations, experience levels, and filters
- **Custom Answers**: Pre-configure answers for common application questions
- **Easy Apply Automation**: Automatically apply to LinkedIn Easy Apply jobs
- **Application Tracking**: Keep track of all applications with status and notes
- **Export Functionality**: Export your application history to CSV

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/LinkedIn-Auto-Applicant.git
cd LinkedIn-Auto-Applicant
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the example environment file:
```bash
cp .env.example .env
```

5. Edit `.env` with your settings (optional - you can also enter credentials in the web interface)

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`

3. Complete your profile:
   - Fill in personal information
   - Upload your resume
   - Add education and work experience
   - Set up custom answers for common questions

4. Configure job preferences:
   - Add job titles you're interested in
   - Set location preferences
   - Choose experience levels and job types
   - Add any companies or keywords to exclude

5. Run Auto-Apply:
   - Enter your LinkedIn credentials
   - Set maximum applications per session
   - Click "Start Auto-Apply"

## Project Structure

```
LinkedIn-Auto-Applicant/
├── app.py              # Flask web application
├── browser.py          # Selenium browser automation
├── linkedin.py         # LinkedIn-specific automation
├── models.py           # Data models for profiles and preferences
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
├── templates/          # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── profile.html
│   ├── preferences.html
│   ├── education.html
│   ├── experience.html
│   ├── custom_answers.html
│   ├── applications.html
│   └── run.html
├── data/               # User data storage
└── logs/               # Application logs
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Flask secret key | Auto-generated |
| `LINKEDIN_EMAIL` | LinkedIn email (optional) | - |
| `LINKEDIN_PASSWORD` | LinkedIn password (optional) | - |
| `HEADLESS_MODE` | Run browser in background | False |
| `BROWSER_TYPE` | Browser to use (chrome/firefox) | chrome |
| `MAX_APPLICATIONS_PER_SESSION` | Max applications limit | 50 |
| `DELAY_BETWEEN_APPLICATIONS` | Delay in seconds | 3 |

## Important Notes

### LinkedIn Terms of Service
This tool automates interactions with LinkedIn. Please be aware that:
- Automated tools may violate LinkedIn's Terms of Service
- Your account could be restricted or banned
- Use this tool responsibly and at your own risk

### Best Practices
- Keep applications under 50 per day
- Don't run the tool 24/7
- Review applications periodically
- Update your profile and answers regularly
- Start with visible browser mode to handle security checks

### Security
- Your credentials are used only during the session
- Data is stored locally in JSON files
- No data is sent to external servers

## Troubleshooting

### Security Verification
If LinkedIn asks for security verification:
1. Run in non-headless mode
2. Complete the verification manually
3. Press Enter in the terminal to continue

### Browser Issues
- Make sure Chrome or Firefox is installed
- The tool will automatically download the correct WebDriver

### Application Failures
- Check the application logs in the `logs/` directory
- Review skipped/failed applications in the history
- Update custom answers for common questions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This tool is for educational purposes only. The developers are not responsible for any consequences resulting from the use of this tool, including but not limited to account restrictions, bans, or violations of terms of service.

## License

MIT License - feel free to use and modify as needed.
