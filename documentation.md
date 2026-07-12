# Playwright-Practice-IMS — Automation Framework Documentation

## 1. Overview

| | |
|---|---|
| **Purpose** | End-to-end UI automation of the IRD (Inland Revenue Department) invoicing/reporting workflow for an Inventory Management System (IMS/WebPOS) |
| **Application under test** | `http://{env}.variantqa.himshang.com.np` (URL supplied at runtime) |
| **Language** | Python 3.10+ |
| **Automation library** | Playwright (sync API), `playwright==1.48.0` |
| **Test runner** | Pytest 9.x, run in **sequential, single-browser-session** style (not isolated per-test) |
| **Design pattern** | Page Object Model (POM), one class per screen/feature |
| **Reporting** | `pytest-html` report + full-page screenshots per test|
| **Author** | Sagan Krishna Tamrakar |

This is not a classic "one test = one independent scenario" suite. It automates a single **continuous business journey** — the full IRD tax-compliance flow of an IMS system, from login through creating masters, raising invoices, and pulling every statutory report — chained together into one long run (`test_ird_flow`).

---

## 2. Repository Structure

```
Playwright-Practice-IMS/
├── conftest.py                  # Pytest fixtures: config_data, browser, page + screenshot hooks
├── generate_pdf.py              # Standalone helper: renders an HTML invoice to PDF via headless Chromium
├── requirements.txt             # Pinned Python dependencies
├── ReadMe.md                    # Original project README
├── customers.csv                # Rolling log of customers created during runs
├── vendors.csv                  # Rolling log of vendors created during runs
├── product_groups.csv           # Rolling log of product groups created during runs
├── product_details.csv          # FIFO log (max 10 rows) of products created during runs
│
├── Pages/                       # Page Object Model classes
│   ├── Login.py                 # Login + "already logged in" popup handling
│   ├── invoice_reprint.py / reprint_invoice.py
│   ├── Masters/                 # Add Category / Customer / Product / Product Group / Vendor / Bulk price change
│   ├── Transactions/            # Purchase Invoice, Sales Invoice, Abbreviated Invoice, Credit Note, Debit Note, Opening Stock
│   └── Reports/                 # Purchase/Sales/Credit/Debit book reports, VAT registers, Stock Summary,
│                                 # Transaction Activity, Materialized View
│
├── Tests/                       # Pytest test modules
│   ├── IRD_Flow/                # The main, numbered end-to-end IRD journey (test_01 … test_18 + reprints)
│   │   └── Test_execution.py    # Orchestrator that calls each numbered test in business order
│   ├── Masters/                 # Standalone master-data tests (e.g. bulk price change) — hardcoded creds
│   └── Transactions/            # Standalone transaction tests (e.g. opening stock) — hardcoded creds
│
├── Reports/
│   ├── report.html              # Generated pytest-html report (after a run)
│   └── screenshots/             # Per-test + final-state screenshots, embedded into the HTML report
├── screenshots/                 # Ad-hoc screenshots saved by individual report page objects (e.g. purchase/sales reports)
├── downloads/                   # PDFs/exports downloaded during report tests
├── scratch/                     # Developer scratch scripts and DOM dumps used for debugging locators
└── .pytest_cache/
```

---

## 3. How the Framework Runs

### 3.1 Fixtures (`conftest.py`)

- **`config_data`** *(session scope)* — Reads `--url`, `--username`, `--password` from CLI options; if any are missing, **prompts interactively** via `input()`. This means the suite is not fully non-interactive unless all three CLI flags are passed.
- **`browser`** *(session scope)* — Launches a single Chromium instance for the whole session (`headless=False` by default). One browser instance is shared across all tests in the run.
- **`page`** *(function scope)* — Creates a fresh browser **context** per test (with `accept_downloads=True`), opens `config_data["url"]`, yields the page, then:
  - Takes a full-page "final state" screenshot into `reports/screenshots/final_<timestamp>.png`
  - Closes the context
- **`pytest_runtest_makereport`** hook — After every test's `call` phase, takes a full-page screenshot named `<test_name>_<timestamp>.png` into `Reports/screenshots/` and attaches it to the pytest-html report via `pytest_html.extras.png`.

> ⚠️ Because `page` is function-scoped but `browser` is session-scoped, **every test gets a brand-new context** (and therefore a fresh, logged-out page) — but the *orchestrator* (`Test_execution.py`) calls the individual `test_*` functions directly as plain Python functions within **one single test (`test_ird_flow`)**, so in practice the whole IRD journey runs inside **one shared page/context**, logging in once at the start.

### 3.2 Two ways this codebase is exercised

1. **Orchestrated end-to-end flow** — `Tests/IRD_Flow/Test_execution.py::test_ird_flow`
   Imports every numbered `test_XX_*` function from `Tests/IRD_Flow/` and calls them **in sequence, in one pytest test**, simulating a real user walking through the entire IRD compliance process. Skipping individual steps is supported via the `SKIP_TESTS` environment variable (see §4).
2. **Standalone/independent tests** — `Tests/Masters/test_10_bulk_price_change.py` and `Tests/Transactions/test_03_opening_stock.py`
   These are regular, independently runnable pytest tests with **hardcoded credentials** (`Testuser` / `Test@1234`) rather than pulling from `config_data`. They are not wired into `Test_execution.py`.

---

## 4. Running the Suite

### 4.1 Prerequisites

- Python 3.10+
- Git

### 4.2 Setup

```bash
git clone https://github.com/Unknown3369/Playwright-Practice-IMS.git
cd Playwright-Practice-IMS

# Create & activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Install the Chromium browser binary for Playwright
playwright install chromium
```

### 4.3 Run headless vs headed

By default the suite launches **headed** Chromium (`headless=False` in `conftest.py`, line ~50). To run headless, edit that fixture:

```python
browser = p.chromium.launch(headless=True)
```

### 4.4 Run the full IRD flow with an HTML report

```bash
pytest Tests/IRD_Flow/Test_execution.py -v --html=Reports/report.html --self-contained-html -s
```

You'll be prompted for `URL`, `Username`, and `Password` unless supplied via CLI flags:

```bash
pytest Tests/IRD_Flow/Test_execution.py \
  --url http://demo.variantqa.himshang.com.np \
  --username myuser \
  --password mypassword \
  -v --html=Reports/report.html --self-contained-html -s
```

### 4.5 Skip specific steps

Set the `SKIP_TESTS` environment variable to a comma-separated list of the internal step names, then rerun:

```powershell
# PowerShell (Windows)
$env:SKIP_TESTS="test_generate_credit_note,test_debit_note"
pytest Tests/IRD_Flow/Test_execution.py --reruns 2 -v --html=Reports/report.html --self-contained-html -s
```

```bash
# bash/Linux/macOS
export SKIP_TESTS="test_generate_credit_note,test_debit_note"
pytest Tests/IRD_Flow/Test_execution.py --reruns 2 -v --html=Reports/report.html --self-contained-html -s
```

Valid skip-names correspond to the identifiers checked in `Test_execution.py` (e.g. `test_login_to_ims`, `test_add_product_group_master`, `test_add_customer`, `test_create_vendor`, `test_add_prod`, `test_purchase_invoice`, `test_purchase_book_report`, `test_abbv_invoice`, `test_sales_invoice`, `test_reprint_sales_invoice`, `test_sales_book_report`, `test_vat_sales_register_report`, `test_materialized_view_report`, `test_generate_credit_note`, `test_reprint_credit_note`, `test_generate_credit_note_book_report`, `test_vat_purchase_register_report`, `test_debit_note`, `test_generate_debit_note_book_report`, `test_stock_summary_report`, `test_print_all_final_reports`, `test_transaction_activity_report`).

### 4.6 Run a standalone test

```bash
pytest Tests/Masters/test_10_bulk_price_change.py -v
pytest Tests/Transactions/test_03_opening_stock.py -v
```
(These use hardcoded credentials `Testuser` / `Test@1234` and don't require `--url`/`--username`/`--password`, but do rely on `config_data`'s URL prompt since the `page` fixture always calls it.)

---

## 5. The IRD Flow — Business Steps in Order

`test_ird_flow` (in `Test_execution.py`) walks through the following sequence on a single logged-in session:

1. **Login** (`test_01_Login.py`) — logs in, and handles a "previous session" popup by clicking Sign out and retrying.
2. **Add Product Group** (`test_02_add_product_group.py`) — creates a master product group; logs it to `product_groups.csv`.
3. **Add Customer** (`test_04_add_customer.py`) — creates a customer master.
4. **Add Vendor** (`test_04_add_vendor.py`) — creates a vendor master; logs to `vendors.csv`.
5. **Add Product** (`test_03_add_prod.py`) — creates a product using the most recently added group/vendor; logs to `product_details.csv` (FIFO capped at 10 rows).
6. **Purchase Invoice** (`test_05_purchase_invoice.py`) — raises a purchase invoice against the new vendor/product.
7. **Purchase Book Report** (`test_06_purchase_book_report.py`) — runs and downloads the report as PDF.
8. **Abbreviated Invoice** (`test_07_abbv_invoice.py`) — generates an abbreviated sales bill.
9. **Sales Invoice** (`test_07_sales_invoice.py`) — generates a full sales invoice; also renders/downloads a PDF via `generate_pdf.py`.
10. **Reprint Sales Invoice** (`test_reprint_sales_invoice.py`) — reprints the invoice 3 times.
11. **Sales Book Report** (`test_08_sales_book_report.py`).
12. **VAT Sales Register Report** (`test_11_vat_sales_register_report.py`).
13. **Materialized View Report** (`test_09_materialized_report.py`).
14. **Credit Note** (`test_10_credit_note.py`) — generates a credit note against the sales invoice.
15. **Reprint Credit Note** (`test_reprint_credit_note.py`) — reprinted 3 times.
16. **Credit Note Book Report** (`test_11_credit_note_report.py`).
17. **Materialized View Report** (re-run).
18. **VAT Sales Register Report** (re-run).
19. **VAT Purchase Register Report** (`test_16_vat_purchase_report.py`).
20. **Debit Note** (`test_14_debit_note.py`).
21. **Debit Note Book Report** (`test_15_debit_note_report.py`).
22. **VAT Purchase Register Report** (re-run).
23. **Stock Summary Report** (`test_17_stock_summary_report.py`).
24. **Print All Final Reports** (`test_run_reports.py` → `test_print_all_final_reports`) — re-runs and downloads Materialized View, Credit Note Book, Debit Note Book, VAT Sales Register, VAT Purchase Register and Stock Summary reports back-to-back.
25. **Transaction Activity Report** (`test_18_transaction_activity_report.py`).

Each report step (steps 7, 11–13, 16, 18–19, 21–24, 25) downloads a PDF into `downloads/` and takes screenshots — some pages also save extra copies into `screenshots/`.

---

## 6. Page Object Model Conventions

- Every screen has a dedicated class in `Pages/<Area>/<name>.py` (`Masters`, `Transactions`, `Reports`, or top-level for shared screens like `Login`).
- Constructors take a Playwright `Page` and store it as `self.page`; most locators are defined as XPath strings in `__init__` (a carry-over from an earlier Selenium suite, per the code comments), though newer Report page objects mix in Playwright's built-in role/title locators (`get_by_role`, `get_by_title`).
- Business actions are exposed as methods (e.g. `perform_login`, `add_prod_test`, `save_button`, `generate_materialized_view_report`, `download_materialized_view_report`) that test modules call in sequence.
- Data created during a run (product groups, vendors, customers, products) is persisted to CSV files at the repo root so downstream steps (e.g. "add a product to the most recently created group") can look it up without holding shared in-memory state across the numbered test modules.
- Report downloads follow a common pattern: click **Run** → click an export/PDF icon → intercept via `page.expect_download()` → save into `downloads/` with a timestamped filename.

---

## 7. Data & Artifacts Generated by a Run

| File/Folder | Purpose |
|---|---|
| `customers.csv`, `vendors.csv`, `product_groups.csv` | Append-only logs of masters created, used by later steps to reference "the most recent" record |
| `product_details.csv` | Same, but capped at 10 rows (FIFO) |
| `downloads/` | PDF/Excel report exports downloaded during the run |
| `Reports/screenshots/` | Screenshot per test + a final full-page screenshot per test, embedded in the HTML report |
| `screenshots/` | Extra screenshots saved directly by some report page objects (purchase/sales report runs) |
| `Reports/report.html` | Self-contained pytest-html report with embedded screenshots |
| `scratch/dom_dump_*.html` | Saved DOM snapshots used while debugging locators (developer artifact, not part of test execution) |

---

## 8. Key Dependencies (from `requirements.txt`)

- `playwright==1.48.0`, `pytest-playwright==0.8.0`
- `pytest==9.0.3`, `pytest-html==4.1.1`, `pytest-base-url==2.1.0`, `pytest-rerunfailures==16.3`, `pytest-xdist==3.8.0`, `pytest-metadata==3.1.1`
- `pandas`, `openpyxl` (data/report handling)
- `PyAutoGUI`, `keyboard`, `pyperclip` (native OS interaction, likely used for file-download dialogs or clipboard-based debugging in `scratch/`)
- `Flask`, `Flask-SocketIO` (present but not referenced by the test flow itself — likely for an auxiliary tool, not required to run the suite)

---

## 9. Known Gotchas / Notes for Future Maintainers

- **Interactive prompts**: If `--url`/`--username`/`--password` aren't passed on the CLI, the suite will block on `input()` — this will hang unattended CI runs. Always pass all three flags in automated pipelines.
- **Not test-isolated**: `test_ird_flow` is a single giant test made of 20+ chained steps sharing one page/session. A failure partway through will short-circuit the rest of the journey (report steps depend on data created by earlier steps).
- **Hardcoded credentials** in `Tests/Masters/test_10_bulk_price_change.py` and `Tests/Transactions/test_03_opening_stock.py` — these will need updating if the test account changes, and should ideally be migrated to `config_data`.
- **Headed by default**: `conftest.py` launches Chromium with `headless=False`; switch to `headless=True` for CI.
- **XPath-heavy locators**: many Page Objects use verbose XPath strings inherited from a prior Selenium suite; some (e.g. `select_supplier_list` in `Purchase_book_report.py`) hardcode specific business values (like a vendor name) and will break if that reference data changes.
- **Timing**: the suite relies heavily on `page.wait_for_timeout(...)` and `time.sleep(...)` fixed delays rather than pure Playwright auto-waiting, which can make runs slower and occasionally flaky on slower environments.
- **`SKIP_TESTS` scope**: skipping only prevents the *named* step from running — it does not automatically adjust or skip downstream steps that depend on data the skipped step would have produced.

---

## 10. Quick Reference — Common Commands

```bash
# Full IRD flow, headed, with HTML report
pytest Tests/IRD_Flow/Test_execution.py -v --html=Reports/report.html --self-contained-html -s

# Full IRD flow, credentials passed inline (good for CI)
pytest Tests/IRD_Flow/Test_execution.py --url <url> --username <user> --password <pass> -v --html=Reports/report.html --self-contained-html -s

# Skip specific steps
SKIP_TESTS="test_debit_note,test_generate_debit_note_book_report" pytest Tests/IRD_Flow/Test_execution.py -v --html=Reports/report.html --self-contained-html -s

# Run only the bulk price change master test
pytest Tests/Masters/test_10_bulk_price_change.py -v

# Run only the opening stock transaction test
pytest Tests/Transactions/test_03_opening_stock.py -v
```