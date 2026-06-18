import pytest

from Pages.Login import login
from Pages.Reports.Stock_summary_report import StockSummaryReport


def test_stock_summary_report(page):

    login_page = login(page)

    login_page.perform_login(
        "Testuser", "Test@1234")

    print("Logged into IMS")

    stock_report = StockSummaryReport(page)
    stock_report.open_stock_summary_report()
    stock_report.run_report()

    print("Stock Summary Report generated successfully.")