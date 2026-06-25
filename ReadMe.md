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

```bash
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
```

### Running Tests Locally

```bash
# Run login tests (headed mode - browser visible)
pytest -v -s

# Run with Playwright Reporting
pytest Tests/IRD_Flow/Test_execution.py -v --html=Reports/report.html 
--self-contained-html -s

```

## Jenkins Pipeline

### Triggering the QA Pipeline

The QA pipeline runs **separately** from the main deployment pipeline.

**Two ways to trigger:**

#### Option 1: Manual Trigger (Recommended for now)

1. Go to Jenkins: http://202.51.0.104:8080
2. Select **QA-TestCases** job
3. Click "Build with Parameters"
4. Set:
   - **DEPLOY_URL**: Application URL (default: https://automation.variantqa.himshang.com.np)
   - **BUILD_VERSION**: Version being tested (e.g., 57, 58)
   - **TEST_SUITE**: login or all (for now, only login works)
5. Click "Build"

#### Option 2: Automatic Trigger (Future)

Add trigger to main deployment pipeline:

```groovy
stage('Trigger QA Tests') {
    steps {
        trigger job: 'QA-TestCases',
               parameters: [
                   string(name: 'DEPLOY_URL', value: 'https://automation.variantqa.himshang.com.np'),
                   string(name: 'BUILD_VERSION', value: env.BUILD_NUMBER)
               ]
    }
}
```

### Pipeline Parameters

| Parameter       | Type   | Default                                      | Description                 |
| --------------- | ------ | -------------------------------------------- | --------------------------- |
| `DEPLOY_URL`    | string | https://automation.variantqa.himshang.com.np | URL of deployed app         |
| `BUILD_VERSION` | string | latest                                       | Build number or version     |
| `TEST_SUITE`    | choice | login                                        | Tests to run (login or all) |

### Pipeline Stages

1. **Environment Info** — Display test configuration
2. **Setup Python Environment** — Create venv, install dependencies
3. **Install Playwright Browsers** — Download Chromium
4. **Run QA Tests** — Execute tests in headless mode
5. **Generate Allure Report** — Create HTML reports
6. **Test Summary** — Generate test summary

### Pipeline Artifacts

- `allure-results/` — JSON test results
- `test-report.html` — Pytest HTML report
- `allure-report/` — Allure HTML report (if available)
- `test-summary.txt` — Test execution summary

## Test Cases

### Current Tests

#### 1. Login Test (`Tests/Test_login.py`)

- **Purpose:** Verify user can log in to the application
- **Flow:**
  1. Navigate to application URL
  2. Enter username
  3. Enter password
  4. Click login button
  5. Handle existing session popup (if any)
  6. Verify dashboard loads (check for Date input field)
- **Status:** Passing locally and in Jenkins
- **Execution Time:** ~10-20 seconds (headless)

### Future Tests

- Product management
- Order processing
- Reporting features
- (As QA team develops more tests)

## Test Credentials

The test uses hardcoded credentials in the test file:

```python
login_page.perform_login(UserName, Password)
```

For security in production, consider:

- Using environment variables: `${TEST_USERNAME}`, `${TEST_PASSWORD}`
- Jenkins credentials store
- Secrets management tools

## Maintenance

### Updating Tests

1. Clone the repo locally
2. Create a feature branch
3. Update test files
4. Test locally: `pytest Tests/ -v`
5. Commit and push
6. Jenkins will automatically use the latest version

### Troubleshooting

#### Test Fails with "Missing X server"

- Use `HEADLESS=true` environment variable
- Jenkins runs without display server

#### Test Fails with "Connection refused"

- Check DEPLOY_URL is correct
- Verify application is accessible
- Check firewall rules

#### Allure report not generating

- Allure CLI may not be installed on Jenkins
- HTML report is still available (`test-report.html`)
- Allure results JSON is always generated (`allure-results/`)

## Links

- **Repository:** https://github.com/devopsims/QA-TestCases
- **Jenkins:** http://202.51.0.104:8080
- **Application (QA):** http://stc21.webredirect.himshang.com.np
- **Main CI/CD Repo:** https://github.com/devopsims/webpos-cicd

## Contributing

1. Create feature branch from `main`
2. Write/update tests
3. Test locally with `pytest`
4. Submit PR with results
5. After merge, changes automatically used in next Jenkins run

## Support

For issues:

1. Check test logs in Jenkins
2. Review pytest output
3. Check Playwright browser logs
4. Verify application accessibility
