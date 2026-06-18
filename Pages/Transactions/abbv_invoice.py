from playwright.sync_api import Page
import random
import time

class AbbvInvoice:

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

   def enter_sales_invoice(self, ref_value):

      self.page.get_by_title("Transactions").first.click()
      self.page.get_by_title("Sales Transaction").nth(1).click()
      self.page.get_by_role("link", name="Abbreviated Tax Invoice").click()

    #   # Ref No
    #   self.page.locator(self.refno).fill(
    #      str(ref_value)
    #   )
    #   print(f"Reference No {ref_value} entered successfully!")

      # Customer
      customer = self.page.locator(
         self.customer_enter
      )
      customer.click()
      customer.press("Enter")
      print("Customer popup opened!")

      # Select Customer
      self.page.get_by_text(
         "11 QA Customer",
         exact=False
      ).dblclick()

      print("Customer selected successfully!")

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

      save_btn.wait_for(
            state="visible",
            timeout=30000
      )
      save_btn.click()
      print("Save button clicked!")

      amount_btn = self.page.locator(
         self.amount_btn
      )
      amount_btn.wait_for(
         state="visible",
         timeout=30000
      )
      amount_btn.click()
      print("Balance Amount clicked!")

      add_btn = self.page.locator(
         self.add_button
      )
      add_btn.wait_for(
         state="visible",
         timeout=30000
      )
      add_btn.click()
      print("Add button clicked!")

      final_save = self.page.locator(
         self.final_save
      )
      final_save.wait_for(
         state="visible",
         timeout=30000
      )
      final_save.click()
      print("Final Save clicked!")

      self.page.wait_for_timeout(5000)

      try:
         print_voucher = self.page.get_by_role("button", name="Print")
         print_voucher.wait_for( state="visible", timeout=30000).click()
         print ("Print Voucher clicked successfully!")
      
      except:
         print ("Print button not found!")

      self.page.wait_for_timeout(5000)