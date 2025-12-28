SauceDemo E2E UI Automation Testing

// Project Overview

This project contains end-to-end UI automation tests for the SauceDemo shopping application
(https://www.saucedemo.com/).

The tests validate:

1. Login functionality (positive & negative)
2. Product sorting and cart actions
3. Checkout flow (Step One → Step Two → Complete)
4. UI validations and error handling

The framework follows Page Object Model (POM) and uses explicit waits for stability.

// Tech Stack

1. Language: Python 3.11
2. Test Framework: PyTest
3. Automation Tool: Selenium WebDriver
4. Browser: Google Chrome
5. Reporting: pytest-html

// Setup Instructions

1. Clone the repository
git clone <your-repo-url>
cd saucedemo

2. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

// Run Tests Locally (Browser Visible)
pytest -v

// Run Tests in Headless Mode (CI Friendly)

Headless mode is already configured in conftest.py.

Just run:

pytest -v

The tests will run without opening the browser.

// Generate HTML Test Report

pytest --html=reports/test_report.html --self-contained-html

// View Report

Open this file in a browser:

reports/test_report.html

// Screenshots on Failure

Screenshots are automatically captured when a test fails

Stored inside the screenshots/ folder

Screenshot name = failed test name

Example:

screenshots/test_checkout_valid_information.png

// Project Structure

saucedemo/
│
├── pages/          # Page Object Model classes
├── tests/          # Test cases
├── reports/        # HTML test reports
├── screenshots/    # Failure screenshots
├── conftest.py     # PyTest fixtures
├── requirements.txt
└── README.md