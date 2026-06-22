
from playwright.sync_api import Page, expect
import os
from datetime import datetime

class DebitNoteBookReportPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.reports_btn = (
            "//span[contains(normalize-space(),'Reports')]"
        )

        self.purchase_reports_link = "text='Purchase Reports'"
        self.purchase_reports_xpath = (
            "//span[normalize-space()='Purchase Reports']"
        )

        self.debit_note_book_report = (
            "text='Debit Note Book Report'"
        )

        self.detail_report_radio = (
            "//input[@type='radio' and @name='reportType' and @value='1']"
        )

        self.run_button = (
            "//button[normalize-space(text())='RUN']"
        )

        self.report_table = (
            "//table[contains(@class,'table')]"
        )

    def generate_debit_note_book_report(self):

        self.page.get_by_title("Reports").first.click()
        self.page.get_by_title("Purchase Reports").nth(1).click()
        self.page.get_by_role("link", name="Debit Note Book Report").click()

            # Select Detail Report
            # print("Selecting 'Detail Report' option...")

            # detail_radio = self.page.locator(
            #     self.detail_report_radio
            # )

            # detail_radio.scroll_into_view_if_needed()

            # if not detail_radio.is_checked():
            #     detail_radio.check(force=True)

            # print(
            #     "Selected 'Detail Report' radio button."
            # )

            # self.page.wait_for_timeout(2000)

        # Click Run
        run_button = self.page.locator(self.run_button)

        run_button.scroll_into_view_if_needed()
        run_button.click()

        print("Clicked 'RUN' button successfully.")

        download_pdf = self.page.locator("svg[role='img'][data-icon='file-pdf']")
        os.makedirs("downloads", exist_ok=True)

        with self.page.expect_download(timeout=60000) as download_info:
            download_pdf.click()

        download = download_info.value

        # Download timestamp
        download_time = datetime.now()

        file_path = os.path.join(
            "downloads",
            download.suggested_filename
                )

        download.save_as(file_path)
        
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


