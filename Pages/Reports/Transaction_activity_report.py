from playwright.sync_api import Page, expect
import os
from datetime import datetime
import time

class TransactionActivityReport:

    def __init__(self, page: Page):
        self.page = page
        self.run_button = (
            "//button[@type='button' and normalize-space(text())='RUN']"
        )

    def open_transaction_activity_report(self):

        self.page.get_by_title("Reports").first.click()
        self.page.get_by_title("VAT Report").nth(1).click()
        self.page.get_by_role("link", name="Transaction Activity Log").click()

    def run_report(self):

        run_button = self.page.locator(
            self.run_button
        )

        run_button.scroll_into_view_if_needed()
        run_button.click()
        self.page.locator("//th[contains(normalize-space(.), 'UserId')]").wait_for(
            state="visible",
            timeout=30000
        )

        print("Run button clicked successfully!")

        download_pdf = self.page.locator("svg[data-icon='file-export']")
        os.makedirs("downloads", exist_ok=True)

        with self.page.expect_download(timeout=60000) as download_info:
            download_pdf.click()
            self.page.wait_for_timeout(1000)
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
