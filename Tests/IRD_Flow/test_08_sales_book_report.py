import pytest
import time
import os

from Pages.Login import login
from Pages.Reports.Sales_book_report import SalesBookReportPage


def test_sales_book_report(page,config_data):
    username = config_data["username"]
    password = config_data["password"]
    
    try:
        login_page = login(page)
        login_page.perform_login(username, password)
    except:
        print('Already logged In')

    sales_report = SalesBookReportPage(page)
    sales_report.open_sales_book_report()
    sales_report.run_sales_book_report()

    page.wait_for_timeout(15000)
