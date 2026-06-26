# QA-TestCases - Playwright Automation

This repository contains **QA test automation** for the WebPOS/IMS application using **Playwright**. Tests run in a separate Jenkins pipeline from the main deployment pipeline.

## Overview

- **Framework:** Playwright (Python)
- **Test Runner:** Pytest
- **Reporting:** Allure Reports + HTML reports
- **CI/CD:** Jenkins (separate pipeline from deployment)
- **Application:** IMS/WebPOS on http://{}.variantqa.himshang.com.np

## Repository Structure

```
C:.
├───.pytest_cache
│   └───v
│       └───cache
├───downloads
├───invoices
├───Pages
│   ├───Masters
│   │   └───__pycache__
│   ├───Reports
│   │   └───__pycache__
│   ├───Transactions
│   │   └───__pycache__
│   └───__pycache__
├───Reports
│   ├───data
│   └───screenshots
├───scratch
├───screenshots
├───Tests
│   ├───IRD_Flow
│   │   └───__pycache__
│   ├───Masters
│   │   └───__pycache__
│   ├───Transactions
│   │   └───__pycache__
│   └───__pycache__
└───__pycache__
```

## Local Testing

### Prerequisites

- Python 3.10+
- Git

### Installation


# Clone the repository
git clone https://github.com/Unknown3369/Playwright-Practice-IMS.git
cd QA-TestCases

# Create virtual environment
python3 -m venv venv   || python -m venv [environment name]
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium



### Running Tests Locally

(If you want to run the rest in headless mode,update the conftest.py file 
change the following code
    browser = p.chromium.launch(
         headless=True
      )
)

# Run login tests
pytest -v -s

# Run with Playwright Reporting
pytest Tests/IRD_Flow/Test_execution.py -v --html=Reports/report.html --self-contained-html -s

# Skip Certain Tests
$env:SKIP_TESTS="TEST_NAME_HERE"
pytest Tests/IRD_Flow/Test_execution.py --reruns 2 -v --html=Reports/report.html --self-contained-html -s
