from playwright.sync_api import Page, expect
import os
from datetime import datetime
import time

class VatSalesRegisterReportPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.customer_input = ("//input[@placeholder='Press Enter or Tab for Customer List']")
        self.customer_select = "//div[@title='Carti']"
        self.run_btn = "//button[contains(text(),'RUN')]"
        self.report_table = "//table[contains(@class,'table')]"

    def generate_vat_sales_register_report(self):

        self.page.get_by_title("Reports").first.click()
        self.page.get_by_title("VAT Report").nth(1).click()
        self.page.get_by_role("link", name="VAT Sales Register").click()

        customer_input = self.page.locator(
                self.customer_input
            )

        # customer_input.click()
        # customer_input.press("Enter")

        # print("Customer list opened.")

        # self.page.wait_for_timeout(1500)

        # self.page.locator(
        #         self.customer_select
        #     ).dblclick()

        # print("Selected customer: Carti")

        branch = self.page.get_by_role("group", name="Branch Selection:").get_by_role("combobox")

        branch.select_option(label="ALL")

        self.page.locator(
                self.run_btn
            ).click()

        print("Clicked RUN button.")
        self.page.locator("//th[normalize-space()='INVOICE']").wait_for(
            state="visible",
            timeout=30000
        )

    def download_vat_sales_report(self):

        download_pdf = self.page.locator("svg[data-icon='file-export']")
        os.makedirs("downloads", exist_ok=True)

        with self.page.expect_download(timeout=60000) as download_info:
            download_pdf.click()
            self.page.wait_for_timeout(1000)
            self.page.locator("//span[normalize-space()='Default Format']").click()

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


