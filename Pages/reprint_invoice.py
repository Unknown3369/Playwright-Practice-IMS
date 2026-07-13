from playwright.sync_api import Page
import os
from datetime import datetime
import time

class Reprint_invoice:
    def  __init__(self, page: Page):
        self.page = page
    
    def reprint_invoice(self):
        self.page.get_by_title("Transactions").first.click()
        self.page.get_by_title("Sales Transaction").nth(1).click()
        self.page.get_by_role("link", name="Sales Tax Invoice").click()

        self.page.wait_for_timeout(1000)

        for i in range(3):

            self.page.get_by_role("button", name="VIEW F4").click()
            self.page.wait_for_timeout(1000)
            self.page.locator("tbody tr").first.locator("td").nth(1).dblclick()

            captured_pdf = []

            def handle_response(response):
                content_type = response.headers.get("content-type", "")
                if "pdf" in content_type or response.url.lower().endswith(".pdf"):
                    try:
                        captured_pdf.append(response.body())
                        print(f"PDF response captured from: {response.url}")
                    except Exception as ex:
                        print(f"Could not read PDF body: {ex}")

            self.page.on("response", handle_response)
            self.page.get_by_role("button", name="PRINT F8").click()

            timeout = 15
            import time as _time
            start = _time.time()
            while not captured_pdf and (_time.time() - start) < timeout:
                self.page.wait_for_timeout(500)

            self.page.remove_listener("response", handle_response)

            if captured_pdf:
                os.makedirs("invoices", exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                pdf_path = f"invoices/reprint_sales_invoice_{timestamp}.pdf"
                with open(pdf_path, "wb") as f:
                    f.write(captured_pdf[0])
                print(f"Invoice successfully saved to {pdf_path}")
            else:
                print("No PDF response detected within timeout. Invoice not saved.")

            self.page.reload()
            time.sleep(5)

        print("Settling page to prevent abrupt teardown errors...")
        self.page.wait_for_timeout(2000)
