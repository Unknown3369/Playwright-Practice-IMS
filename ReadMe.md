# QA-TestCases - Playwright Automation

This repository contains **IRD Process automation** for the WebPOS/IMS application using **Playwright**.

## Overview

- **Framework:** Playwright (Python)
- **Test Runner:** Pytest
- **Application:** IMS/WebPOS on `http://{}.variantqa.himshang.com.np`

## Repository Structure

```
C:.
├───Pages
│   ├───Masters
│   ├───Reports
│   └───Transactions
├───Reports
│   ├───data
│   └───screenshots
├───Tests
│   ├───IRD_Flow
│   ├───Masters
│   └───Transactions
├───downloads
├───invoices
├───scratch
└───screenshots
```

## Local Testing

### Prerequisites

- Python 3.10+
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Unknown3369/Playwright-Practice-IMS.git
cd Playwright-Practice-IMS

# Create virtual environment
python3 -m venv venv   || python -m venv [environment name]
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

### Running Tests Locally

To run the tests in headless mode, update `conftest.py` (around line 50) as follows:

```python
browser = p.chromium.launch(
    headless=True
)
```

```bash
# Run tests [IRD Flow] with report
pytest Tests/IRD_Flow/Test_execution.py -v --html=Reports/report.html --self-contained-html -s

# Skip certain tests [IRD Flow]
$env:SKIP_TESTS="TEST_NAME_HERE"
pytest Tests/IRD_Flow/Test_execution.py --reruns 2 -v --html=Reports/report.html --self-contained-html -s
```

---

Updated By: Sagan Krishna Tamrakar
