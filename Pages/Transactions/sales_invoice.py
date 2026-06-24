from conftest import browser
from conftest import page
from playwright.sync_api import Page
import random
import time
from datetime import datetime
from pywinauto import Desktop
import os
import csv

class SalesInvoice:

   def __init__(self, page: Page):
      self.page = page
      self.refno = "#refnoInput"
      self.customer_enter = "#customerselectid"
      self.item_enter = "#barcodeField"
      self.quantity = "//input[@id='quantityBarcode']"
      self.save = "//button[normalize-space()='SAVE [End]']"
      self.amount_btn = "//button[normalize-space()='Balance Amount']"
      self.add_button = "//button[normalize-space()='Add']"
      self.final_save = "(//button[contains(text(),'SAVE') and contains(@class,'btn-info')])[last()]"
      # The alert/toast modal that appears after SAVE [End] is clicked
      self.alert_modal = "alert .modal.fade.in.show"

   def enter_sales_invoice(self, ref_value):

      self.page.get_by_title("Transactions").first.click()
      self.page.get_by_title("Sales Transaction").nth(1).click()
      self.page.get_by_role("link", name="Sales Tax Invoice").click()

      # Ref No
      self.page.locator(self.refno).fill(
         str(ref_value)
      )
      print(f"Reference No {ref_value} entered successfully!")

      # Customer
      customer = self.page.locator(
         self.customer_enter
      )
      customer.click()
      customer.press("Enter")
      print("Customer popup opened!")

      # Select Customer
      with open("customers.csv", newline="", encoding="utf-8") as file:
         reader = csv.DictReader(file)
         customer = next(reader)["ACNAME"]

         print(f"Customer from CSV: '{customer}'")

         customer_row = self.page.get_by_text(customer,exact=True)
         customer_row.wait_for(state="visible",timeout=30000)
         customer_row.dblclick()

      print(f"Customer selected successfully: {customer}")

   def sales_invoice_test(self,item_code: str,enter_quantity: int):

      # Barcode
      barcode = self.page.locator(
         self.item_enter
      )

      barcode.wait_for(
         state="visible",
         timeout=30000
      )
      barcode.fill(item_code)
      barcode.press("Enter")
      print(
         f"Item Code {item_code} entered successfully!"
      )

      # Quantity
      quantity = self.page.locator(
         self.quantity
      )

      quantity.wait_for(
         state="visible",
         timeout=30000
      )

      time.sleep(1)

      quantity.fill(
         str(enter_quantity)
      )

      quantity.press("Enter")
      time.sleep(1)

      print(
         f"Quantity {enter_quantity} entered successfully!"
      )

      self.page.wait_for_timeout(1000)

   def save_btn(self):

      save_btn = self.page.locator(self.save)
      save_btn.wait_for(state="visible", timeout=30000)
      save_btn.click()
      print("Save button clicked!")

      # -------------------------------------------------------
      # Wait for the success alert modal to appear then vanish
      # The alert modal blocks all button clicks until it closes
      # -------------------------------------------------------
      try:
         # Wait for the alert modal to appear (up to 5s)
         self.page.wait_for_selector(
            "alert .modal.fade.in.show",
            state="visible",
            timeout=5000
         )
         print("Alert modal appeared — waiting for it to close...")
         # Wait for it to disappear (up to 10s)
         self.page.wait_for_selector(
            "alert .modal.fade.in.show",
            state="hidden",
            timeout=10000
         )
         print("Alert modal closed.")
      except Exception:
         # Alert may not appear or may have already closed
         pass

      # Now safely click Balance Amount
      amount_btn = self.page.locator(self.amount_btn)
      amount_btn.wait_for(state="visible", timeout=30000)
      amount_btn.click()
      print("Balance Amount clicked!")

      add_btn = self.page.locator(self.add_button)
      add_btn.wait_for(state="visible", timeout=30000)
      add_btn.click()
      print("Add button clicked!")

      final_save = self.page.locator(self.final_save)
      final_save.wait_for(state="visible", timeout=30000)

      # -----------------------------------------------------------
      # Intercept the PDF response the server sends after Final Save
      # The app returns the invoice as application/pdf from the server.
      # We capture the response body before Chrome's PDF viewer takes it.
      # -----------------------------------------------------------
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

      final_save.click(force=True)
      print("Final Save clicked!")

      for i in range(1):
         
         # Wait up to 15s for the PDF to arrive
         timeout = 15
         import time as _time
         start = _time.time()
         while not captured_pdf and (_time.time() - start) < timeout:
            self.page.wait_for_timeout(500)

         self.page.remove_listener("response", handle_response)

         if captured_pdf:
            os.makedirs("invoices", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            pdf_path = f"invoices/sales_invoice_{timestamp}.pdf"
            with open(pdf_path, "wb") as f:
               f.write(captured_pdf[0])
            print(f"Invoice successfully saved to {pdf_path}")
         else:
            print("No PDF response detected within timeout. Invoice not saved.")

      # -----------------------------------------------------------
      # Settle the browser page before the test closes
      # -----------------------------------------------------------
      print("Settling page to prevent abrupt teardown errors...")
      self.page.wait_for_timeout(2000)
