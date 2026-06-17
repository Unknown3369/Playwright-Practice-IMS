from playwright.sync_api import Page, expect
import os


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

        self.page.locator(
                self.run_btn
            ).click()

        print("Clicked RUN button.")

        download_pdf = self.page.locator("svg[role='img'][data-icon='file-pdf']")
        os.makedirs("downloads", exist_ok=True)

        with self.page.expect_download(timeout=60000) as download_info:
            download_pdf.click()

        download = download_info.value

        download.save_as(f"downloads/{download.suggested_filename}")

        print(f"Downloaded: {download.suggested_filename}")
        
        self.page.wait_for_timeout(2000)


