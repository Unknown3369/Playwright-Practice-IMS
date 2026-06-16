from playwright.sync_api import Page, expect
import os

class SalesBookReportPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.reports = "//span[contains(text(),'Reports')]"
        self.sales_report = "text='Sales Report'"
        self.sales_book_report = "//span[normalize-space()='Sales Book Report']"
        self.branch_dropdown = "//select[contains(@class, 'form-control') and contains(@class, 'selectText')]"
        self.user_dropdown = "//input[@type='checkbox' and @value='0']"
        self.select_customer = "//input[@type='text' and @placeholder='Press Enter or Tab for Account List']"
        self.search_customer = "//input[@placeholder='Enter keyword to search']"
        self.select_customer_list = "//div[normalize-space(text())='Cash Customer']"
        self.run_button = "//button[normalize-space(text())='RUN']"

    def open_sales_book_report(self):
        self.page.get_by_title("Reports").first.click()
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
        print("Run button clicked successfully!")

        download_pdf = self.page.locator("svg[role='img'][data-icon='file-pdf']")
        os.makedirs("downloads", exist_ok=True)

        with self.page.expect_download(timeout=60000) as download_info:
            download_pdf.click()

        download = download_info.value

        download.save_as(f"downloads/{download.suggested_filename}")

        print(f"Downloaded: {download.suggested_filename}")