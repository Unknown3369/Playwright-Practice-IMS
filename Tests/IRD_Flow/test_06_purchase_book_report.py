import allure
import time
import os

from Pages.Login import login
from Pages.Reports.Purchase_book_report import PurchaseBookReport

def test_purchase_book_report(page,config_data):
    username = config_data["username"]
    password = config_data["password"]

    login_page = login(page)
    purchase_report = PurchaseBookReport(page)

    login_page.perform_login(username, password)

    purchase_report.open_purchase_book_report()

    time.sleep(10)

    with allure.step("Report Generated - capturing screenshot"):
        os.makedirs("screenshots", exist_ok=True)

        screenshot_path = (
            f"screenshots/purchase_report_{int(time.time())}.png"
        )

        page.screenshot(path=screenshot_path)

        allure.attach.file(
            screenshot_path,
            name="Purchase Report Generated",
            attachment_type=allure.attachment_type.PNG
        )