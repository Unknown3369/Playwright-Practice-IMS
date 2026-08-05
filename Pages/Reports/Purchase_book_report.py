from playwright._impl import _download
from playwright.sync_api import Page, expect
import pytest
from datetime import datetime
import os   
import time

class PurchaseBookReport:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.reports = "//span[contains(text(),'Reports')]"
        self.purchase_report = "text='Purchase Reports'"
        self.purchase_book_report = "//span[normalize-space()='Purchase Book Report']"
        self.warehouse_alert_handle = "//button[contains(text(), 'OK')]"
        self.branch_dropdown = "//select[option[@disabled and normalize-space()='Select Branch']]"
        self.user_name = "//input[@placeholder='Press Enter for User List']"
        self.select_user = "//div[@title='Admin' and normalize-space()='Admin']"
        self.warehouse = "//select[@class='form-control input-text ng-untouched ng-pristine ng-valid']"
        self.select_supplier = "//input[@type='text' and @placeholder='Press Enter or Tab for Account List']"
        self.select_supplier_list = "//div[normalize-space(text())='Dark Chocolate Vendor']"
        self.run_button = "//button[normalize-space(text())='RUN']"
        self.load_button = "//div[@class='option-card' and .//span[normalize-space()='Load Report']]"
        self.ok_button = "//button[normalize-space()='OK']"

    def open_purchase_book_report(self):

        self.page.get_by_title("Reports").first.click()
        time.sleep(1)
        self.page.get_by_title("Purchase Reports").nth(1).click()
        self.page.get_by_role("link", name="Purchase Book Report").click()

        # Handle warehouse alert if present
        try:
            if self.page.locator(self.warehouse_alert_handle).is_visible(timeout=5000):
                self.page.locator(self.warehouse_alert_handle).click()
                print("Warehouse alert handled successfully!")
        except:
            print("No warehouse alert present.")

        # Branch Selection
        self.page.locator(self.branch_dropdown).select_option(label="ALL")
        print("Branch selected successfully!")

        # Run Report
        self.page.locator(self.run_button).click()
        print("Run button clicked successfully!")
        time.sleep(5)

        download_pdf = self.page.locator("svg[data-icon='file-export']")
        os.makedirs("downloads", exist_ok=True)

        with self.page.expect_download(timeout=60000) as download_info:
            download_pdf.click()
            self.page.wait_for_timeout(1000)
            default = self.page.locator("//span[normalize-space()='Default Format']")
            default.page.wait_for_timeout(1500)
            default.click()

        download = download_info.value

        # Download timestamp
        download_time = datetime.now()

        file_path = os.path.join(
            "downloads",
            download.suggested_filename
                )

        # Current time
        timestamp = datetime.now().strftime("%H-%M-%S")

        # Original filename
        filename = download.suggested_filename
        name, ext = os.path.splitext(filename)

        # New filename with timestamp
        new_filename = f"{name} {timestamp}{ext}"

        download.save_as(
            os.path.join("downloads", new_filename)
        )

        print(f"Downloaded: {new_filename}")

        self.page.wait_for_timeout(2000)

