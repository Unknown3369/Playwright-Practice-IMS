
from playwright.sync_api import Page, expect
import os
from datetime import datetime
import time

class CreditNoteBookReportPage:

    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.customer_input = ("//input[@placeholder='Press Enter or Tab for Account List']")
        self.customer_option = ("//div[@title='11 QA Customer ' and contains(@class,'ng-star-inserted')]")
        self.detail_report_radio = ("//input[@type='radio' and @name='reportType' and @value='1']")
        self.run_button = ("//button[normalize-space(text())='RUN']")
        self.report_table = ("//table[contains(@class,'table')]")

    def generate_credit_note_book_report(self):

        self.page.get_by_title("Reports").first.click()
        self.page.get_by_title("Sales Report").nth(1).click()
        self.page.get_by_role("link", name="Credit Note Book Report").click()
        expect(
            self.page.get_by_role(
            "group",
            name="Branch Selection:"
            )
        ).to_be_visible(timeout=60000)
        print("Current URL:", self.page.url)
    
        branch = self.page.get_by_role("group", name="Branch Selection:").get_by_role("combobox")

        branch.select_option(label="ALL")

        print("Clicking 'RUN' button...")

        run_button = self.page.locator(
                self.run_button
            )

        run_button.scroll_into_view_if_needed()
        run_button.click()

        print("Clicked 'RUN' button successfully.")

    def download_credit_note_report(self):
        download_pdf = self.page.locator("svg[data-icon='file-export']")
        os.makedirs("downloads", exist_ok=True)

        with self.page.expect_download(timeout=60000) as download_info:
            download_pdf.click()
            self.page.wait_for_timeout(1000)
            time.sleep(10)
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