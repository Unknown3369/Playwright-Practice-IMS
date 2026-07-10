import pytest

from Pages.Login import login
from Pages.Reports.Stock_summary_report import StockSummaryReport


def test_stock_summary_report(page,config_data):
    username = config_data["username"]
    password = config_data["password"]

    login_page = login(page)

    login_page.perform_login(username, password)

    print("Logged into IMS")

    stock_report = StockSummaryReport(page)
    stock_report.open_stock_summary_report()
    stock_report.run_report()
    stock_report.download_stock_summary_report()

    print("Stock Summary Report generated successfully.")