import pytest
import allure
import time
import os

from Pages.Login import login
from Pages.Reports.Sales_book_report import SalesBookReportPage


def test_sales_book_report(page,config_data):
    username = config_data["username"]
    password = config_data["password"]
    
    login_page = login(page)
    sales_report = SalesBookReportPage(page)

    login_page.perform_login(username, password)

    sales_report.open_sales_book_report()
    sales_report.run_sales_book_report()

    page.wait_for_timeout(15000)

    with allure.step("Report Generated - capturing screenshot"):
        os.makedirs("screenshots", exist_ok=True)

        screenshot_path = (
            f"screenshots/sales_report_{int(time.time())}.png"
        )

        page.screenshot(
            path=screenshot_path,
            full_page=True
        )

        allure.attach.file(
            screenshot_path,
            name="Sales Report Generated",
            attachment_type=allure.attachment_type.PNG
        )