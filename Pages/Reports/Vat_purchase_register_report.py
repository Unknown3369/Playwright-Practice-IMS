from playwright.sync_api import Page, expect
import os

class VatPurchaseRegisterReportPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.supplier_input = ("//input[@placeholder='Press Enter or Tab for Supplier List']")
        self.supplier_option = ("//div[text()[contains(.,'Sujata Vendor')]]")
        self.run_btn = ("//button[contains(@class,'confirm-btn') and normalize-space()='RUN']")
        self.report_table = ("//table[contains(@class,'table')]")

    def generate_vat_purchase_register_report(self):

        self.page.get_by_title("Reports").first.click()
        self.page.get_by_title("VAT Report").nth(1).click()
        self.page.get_by_role("link", name="VAT Purchase Register").click()

        run_btn = self.page.locator(
                self.run_btn
            )

        run_btn.scroll_into_view_if_needed()
        run_btn.click()

        print("RUN button clicked to generate report.")

        download_pdf = self.page.locator("svg[role='img'][data-icon='file-pdf']")
        os.makedirs("downloads", exist_ok=True)

        with self.page.expect_download(timeout=60000) as download_info:
            download_pdf.click()

        download = download_info.value
        download.save_as(f"downloads/{download.suggested_filename}")

        print(f"Downloaded: {download.suggested_filename}")
        
        self.page.wait_for_timeout(2000)