from playwright.sync_api import Page, expect
import os
from datetime import datetime
import time

class SalesBookReportPage:
    def __init__(self, page: Page):
        self.page = page

        self.branch_dropdown = "//select[contains(@class, 'form-control') and contains(@class, 'selectText')]"
        self.user_dropdown = "//input[@type='checkbox' and @value='0']"
        self.select_customer = "//input[@type='text' and @placeholder='Press Enter or Tab for Account List']"
        self.search_customer = "//input[@placeholder='Enter keyword to search']"
        self.select_customer_list = "//div[normalize-space(text())='Cash Customer']"
        self.run_button = "//button[normalize-space(text())='RUN']"

    def open_sales_book_report(self):
        self.page.get_by_title("Reports").first.click()
        self.page.wait_for_timeout(1000)
        self.page.get_by_title("Sales Report").nth(1).click()
        self.page.get_by_role("link", name="Sales Book Report").click()

    def run_sales_book_report(self):
        # Branch Selection
        self.page.locator(self.branch_dropdown).select_option(label="ALL")
        print("Branch selected successfully!")

        # Select All User
        user_checkbox = self.page.locator(self.user_dropdown)

        if not user_checkbox.is_checked():
            user_checkbox.check()

        print("All users selected successfully!")

        # Click Run Button
        self.page.locator(self.run_button).click()
        self.page.locator("//th[normalize-space()='Date (A.D.)']").wait_for(
            state="visible",
            timeout=30000
        )

        print("Run button clicked successfully!")

        download_pdf = self.page.locator("svg[data-icon='file-export']")
        os.makedirs("downloads", exist_ok=True)

        with self.page.expect_download(timeout=100000) as download_info:
            download_pdf.click()
            self.page.wait_for_timeout(1500)
            default = self.page.locator("//span[normalize-space()='Default Format']")
            default.page.wait_for_timeout(1500)
            default.click()

        download = download_info.value

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