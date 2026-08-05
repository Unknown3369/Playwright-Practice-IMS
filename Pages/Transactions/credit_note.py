from playwright.sync_api import Page
import time as _time
import csv
from datetime import datetime
import os
import time

class CreditNotePage:
    def __init__(self, page: Page):

        page.add_init_script("""
            window.print = () => {
                console.log("window.print() suppressed");
            };
        """)
        
        self.page = page

        self.ref_bill = "#refbill"
        self.customer = "#customerselectid"
        self.item_name = "#barcodeField"
        self.quantity = "#quantityBarcode"
        self.remarks = "#remarksid"
        self.save_button = "//button[normalize-space(text())='SAVE [End]']"

    @staticmethod
    def get_customer_name():
        with open("customers.csv", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            row = next(reader)
            return row["ACNAME"]

    def navigate_to_credit_note(self):

        transactions = self.page.get_by_title("Transactions").first
        transactions.wait_for(state="visible", timeout=15000)
        transactions.click()
        self.page.wait_for_timeout(1000)

        sales_transaction = self.page.get_by_title("Sales Transaction").nth(1)
        sales_transaction.wait_for(state="visible", timeout=15000)
        sales_transaction.click()
        self.page.wait_for_timeout(1000)

        credit_note_link = self.page.get_by_role("link", name="Credit Note (Sales Return)")
        credit_note_link.wait_for(state="visible", timeout=15000)
        credit_note_link.click()
        self.page.wait_for_timeout(2000)


    def credit_note_entry(self):
        customer_name = CreditNotePage.get_customer_name()
        
        ref_bill = self.page.locator(self.ref_bill)
        ref_bill.scroll_into_view_if_needed()
        ref_bill.click()
        ref_bill.press("Enter")
        print("Ref Bill field clicked and ENTER pressed")

        voucher = self.page.locator("//div[contains(@class,'modal')]//tbody/tr[1]/td[2]")
        voucher.wait_for(state="visible")
        voucher.dblclick()
        print("Voucher selected")

        self.page.wait_for_timeout(3000)


    

    def save_credit_note(self):
        remarks = self.page.locator(self.remarks)
        remarks.fill("For IRD Document.")

        save_btn = self.page.locator("//button[contains(text(),'SAVE')]")

        print("Waiting for PDF response...")

        with self.page.expect_response(
            lambda r: r.url.endswith("/api/Pdf") and r.status == 200,
            timeout=60000
        ) as pdf_info:
            save_btn.click()

        pdf_response = pdf_info.value

        print("PDF API captured:", pdf_response.url)

        # Save raw response for inspection
        os.makedirs("invoices", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        body = pdf_response.body()
        print("Content-Type :", pdf_response.headers.get("content-type"))
        print("Body Length  :", len(body))

        try:
            print(body[:100].decode("utf-8"))
        except Exception:
            print(body[:20])

        with open("invoices/credit_note.pdf", "wb") as f:
            f.write(body)

        print("PDF response saved.")
        time.sleep(5)
        self.page.keyboard.press("Escape")
        time.sleep(10)

#------------------------------------------------------------------------------------

