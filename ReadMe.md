# QA-TestCases - Playwright Automation

This repository contains **IRD Process automation** for the WebPOS/IMS application using **Playwright**.

## Overview

- **Framework:** Playwright (Python)
- **Test Runner:** Pytest
- **Application:** IMS/WebPOS on `https://{link}.variantqa.himshang.com.np`

## Repository Structure

```
Playwright-Practice-IMS/
├── conftest.py                  
├── generate_pdf.py              
├── requirements.txt             
├── ReadMe.md                    
├── Flow.png                     
├── customers.csv                
├── vendors.csv                  
├── product_groups.csv           
├── product_details.csv          
├── Pages/                      
│   ├── Login.py                 
│   ├── invoice_reprint.py       
│   ├── reprint_invoice.py       
│   ├── Masters/                 
│   │   ├── Add_Category.py
│   │   ├── Add_Customer.py
│   │   ├── Add_Product.py
│   │   ├── Add_Product_Group.py
│   │   ├── Add_Vendor.py
│   │   └── Bulk_Price_Change.py
│   ├── Transactions/            
│   │   ├── Purchase_Invoice.py
│   │   ├── Sales_Invoice.py
│   │   ├── Abbreviated_Invoice.py
│   │   ├── Credit_Note.py
│   │   ├── Debit_Note.py
│   │   └── Opening_Stock.py
│   └── Reports/                 
│       ├── Purchase_Book_Report.py
│       ├── Sales_Book_Report.py
│       ├── Credit_Note_Book_Report.py
│       ├── Debit_Note_Book_Report.py
│       ├── VAT_Sales_Register.py
│       ├── VAT_Purchase_Register.py
│       ├── Stock_Summary_Report.py
│       ├── Transaction_Activity_Report.py
│       └── Materialized_View_Report.py
├── Tests/                       
│   ├── IRD_Flow/                
│   │   ├── Test_execution.py    
│   │   ├── printpreview.py      
│   │   └── test_run_reports.py  
│   ├── Masters/                 
│   │   └── test_*.py
│   └── Transactions/            
│       └── test_*.py
├── Reports/                     
│   ├── report.html              
│   ├── data/                    
│   └── screenshots/            
├── downloads/                   
├── invoices/                    
├── scratch/                     
├── venv/                        
│   ├── Include/
│   ├── Lib/
│   │   └── site-packages/
│   └── Scripts/
├── .pytest_cache/               
│   └── v/
│       └── cache/
└── __pycache__/                
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
python3 -m venv venv   || python -m venv [environment_name]
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
