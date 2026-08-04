
from playwright.sync_api import Page, expect
import os
from datetime import datetime
import time

class MaterializedViewReportPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.run_btn = "//button[contains(@class,'confirm-btn') and normalize-space()='RUN']"
        self.report_table = page.locator("td.Regulartd span")

    def generate_materialized_view_report(self):

        self.page.get_by_title("Reports").first.click()
        self.page.get_by_title("VAT Report").nth(1).click()
        self.page.get_by_role("link", name="Materialized View").click()
        try:
            branch_select = self.page.locator("//select[contains(@class,'selectText')]")
            branch_select.select_option(label="ALL")
        except:
            print('Branch All Not Found')

        # Run Button
        self.page.locator(self.run_btn).click()
        time.sleep(5)

        print("Clicked RUN button")
    
    def download_materialized_view_report(self):

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