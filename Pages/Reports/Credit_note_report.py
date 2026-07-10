
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

        #     # Customer Selection
        # print("Selecting customer...")

        # customer_input = self.page.locator(self.customer_input)
        # customer_input.scroll_into_view_if_needed()
        # customer_input.click()

        # self.page.wait_for_timeout(1000)

        # customer_input.press("Enter")

        # self.page.wait_for_timeout(2000)

        # self.page.locator(self.customer_option).dblclick()

        # print("Selected customer.")

        # self.page.wait_for_timeout(2000)

        # Detail Report Radio Button
        # print("Selecting 'Detail Report' option...")

        # detail_report_radio = self.page.locator(
        #         self.detail_report_radio
        #     )

        # detail_report_radio.scroll_into_view_if_needed()

        # if not detail_report_radio.is_checked():
        #         detail_report_radio.check(force=True)

        # print("Selected 'Detail Report' radio button.")

        # self.page.wait_for_timeout(2000)
    
        branch = self.page.get_by_role("group", name="Branch Selection:").get_by_role("combobox")

        branch.select_option(label="ALL")

            # Run Button
        print("Clicking 'RUN' button...")

        run_button = self.page.locator(
                self.run_button
            )

        run_button.scroll_into_view_if_needed()
        run_button.click()

        print("Clicked 'RUN' button successfully.")

        # download_pdf = self.page.locator("svg[role='img'][data-icon='file-pdf']")
        # os.makedirs("downloads", exist_ok=True)

        # with self.page.expect_download(timeout=60000) as download_info:
        #     download_pdf.click()

        # download = download_info.value

        # download.save_as(f"downloads/{download.suggested_filename}")

        # print(f"Downloaded: {download.suggested_filename}")
        
        # self.page.wait_for_timeout(2000)

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