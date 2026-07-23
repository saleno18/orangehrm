"""
Global configuration for the OrangeHRM automation framework.
"""

BASE_URL = "https://opensource-demo.orangehrmlive.com"
LOGIN_URL = f"{BASE_URL}/web/index.php/auth/login"

# Explicit / implicit wait timeouts (seconds)
DEFAULT_TIMEOUT = 15
PAGE_LOAD_TIMEOUT = 20

# Browsers supported for cross-browser execution.
# Override at runtime with: pytest --browser=firefox
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]
DEFAULT_BROWSER = "chrome"
HEADLESS = True

# Data source for Test-Case-1 (data-driven login)
LOGIN_DATA_CSV = "data/login_data.csv"

# Details used to create a new user (Test-Case-5 / Test-Case-6)
NEW_USER = {
    "user_role": "ESS",
    "employee_name": "Peter",   # must match an existing employee first/last name fragment in demo data
    "status": "Enabled",
    "username": "auto_test_user",
    "password": "AutoTest@123",
    "confirm_password": "AutoTest@123",
}

# Leave assignment details (Test-Case-9)
LEAVE_ASSIGNMENT = {
    "employee_name": "Peter",
    "leave_type": "US Vacation",
    "duration": "Full Day",
}

# Claim request details (Test-Case-10)
CLAIM_REQUEST = {
    "event_name": "Travel Allowances",
    "currency": "US Dollar",
    "remarks": "Automated test claim submission",
}
