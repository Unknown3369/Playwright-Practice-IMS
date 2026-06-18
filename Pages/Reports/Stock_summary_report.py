from playwright.sync_api import Page, expect
import os


class StockSummaryReport:

    def __init__(self, page: Page):
        self.page = page
        self.run_button = (
            "//button[@type='button' and normalize-space(text())='RUN']"
        )

    def open_stock_summary_report(self):

        self.page.get_by_title("Reports").first.click()
        self.page.get_by_title("Inventory Report").nth(1).click()
        self.page.get_by_role("link", name="Stock Summary Report").click()

    def run_report(self):

        run_button = self.page.locator(
            self.run_button
        )

        run_button.scroll_into_view_if_needed()
        run_button.click()

        print("Run button clicked successfully!")
        download_pdf = self.page.locator("svg[role='img'][data-icon='file-pdf']")
        os.makedirs("downloads", exist_ok=True)

        with self.page.expect_download(timeout=60000) as download_info:
            download_pdf.click()

        download = download_info.value

        download.save_as(f"downloads/{download.suggested_filename}")

        print(f"Downloaded: {download.suggested_filename}")