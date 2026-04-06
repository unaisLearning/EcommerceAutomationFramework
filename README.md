# Ecommerce Test Automation Framework

A professional, Object-Oriented test automation framework for e-commerce web applications, built with Python, Selenium WebDriver, and Pytest.

## Features

- Page Object Model (POM) design pattern for maintainable test code
- Centralized configuration management
- Allure reporting integration with detailed test reports
- Automated logging with timestamped log files
- Screenshot capture on test failures
- Modular, reusable utility functions
- Cross-browser test execution support

## Tech Stack

- **Language:** Python 3.x
- **Automation:** Selenium WebDriver
- **Test Framework:** Pytest
- **Reporting:** Allure
- **IDE Config:** PyCharm (.idea)

## Project Structure

```
EcommerceAutomationFramework/
├── Pages/              # Page Object classes for each web page
├── TestCases/          # Test scripts organized by feature
├── Utilities/          # Reusable helper functions and base classes
├── ConfigurationData/  # Environment configs, URLs, credentials
├── Logs/               # Auto-generated test execution logs
├── .gitignore          # Git ignore rules
└── requirement.txt     # Python dependencies
```

## Setup & Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Chrome browser + ChromeDriver

### Installation

1. Clone the repository:
```bash
git clone https://github.com/unaisLearning/EcommerceAutomationFramework.git
cd EcommerceAutomationFramework
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

3. Install dependencies:
```bash
pip install -r requirement.txt
```

## Running Tests

Run all tests:
```bash
pytest TestCases/ -v
```

Run with Allure reporting:
```bash
pytest TestCases/ -v --alluredir=./allure-results
allure serve ./allure-results
```

## Design Principles

This framework follows industry-standard QA engineering practices:

- **Separation of Concerns** — test logic, page interactions, and utilities are fully decoupled
- **DRY (Don't Repeat Yourself)** — reusable base classes and utility functions
- **Maintainability** — locator changes require updates in one place only (Page Objects)
- **Scalability** — easily extendable for new test modules and pages

## License

This project is licensed under the MIT License.
