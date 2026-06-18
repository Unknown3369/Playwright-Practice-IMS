

from playwright.sync_api import Page, expect
import time


class DebitNote:
   def __init__(self, page: Page):
      self.page = page

      self.transactions = "//span[contains(text(), 'Transactions')]"
      self.pur_transaction = "text='Purchase Transaction'"
      self.debit_note = "//span[normalize-space()='Debit Note (Purchase Return)']"
      self.ref_no = "#invoiceNO"
      self.return_mode = "#paymentTerms"
      self.supplier = "#customerselectid"
      self.select_supplier = "//div[normalize-space()='11 QA Vendor']"
      self.item_name = "#barcodeField"
      self.quantity = "#quantityBarcode"
      self.save_button = "//button[normalize-space(text())='SAVE [End]']"

   def enter_debit_note(self):

      self.page.get_by_title("Transactions").first.click()
      self.page.get_by_title("Purchase Transaction").nth(1).click()
      self.page.get_by_role("link", name="Debit Note (Purchase Return)").click()

   def debit_note_entry(self, enter_ref_no: str):

      # Enter Reference Number
      ref_no = self.page.locator(self.ref_no)
      ref_no.click()
      ref_no.fill(enter_ref_no)

      print(f"Reference No '{enter_ref_no}' entered successfully!")

      # Select Return Mode
      self.page.select_option(self.return_mode, label="Cash")
      print("Return mode 'Cash' selected successfully!")

      # Select Supplier
      supplier = self.page.locator(self.supplier)
      supplier.press("Enter")

      select_supplier = self.page.locator(self.select_supplier)
      select_supplier.dblclick()
      print("Supplier selected successfully!")

   def debit_note_test(self, item_code: str, enter_quantity: int):

      # Enter Item Code
      item_name = self.page.locator(self.item_name)
      item_name.clear()
      item_name.fill(item_code)
      self.page.wait_for_timeout(2000)
      item_name.press("Enter")
      self.page.wait_for_timeout(2000)
      # item_name.press("Enter")
      print("Item name entered successfully!")

      # Enter Quantity
      quantity = self.page.locator(self.quantity)
      quantity.clear()
      quantity.fill(str(enter_quantity))
      quantity.press("Enter")
      print("Quantity entered successfully!")
      self.page.wait_for_timeout(2000)

   def save_button_click(self):

      # Click Save Button
      save_button = self.page.locator(self.save_button)
      expect(save_button).to_be_enabled()
      save_button.click()
      print("Save button clicked successfully!")
      
      try:
         print_voucher = self.page.get_by_role("button", name="Print")
         print_voucher.wait_for( state="visible", timeout=30000).click()
         print ("Print Voucher clicked successfully!")
      
      except:
         print ("Print button not found!")

      self.page.wait_for_timeout(5000)

      # Handle Alert
      dialog_message = None

      def handle_dialog(dialog):
            nonlocal dialog_message
            dialog_message = dialog.message
            print("Alert says:", dialog_message)
            dialog.accept()
      self.page.once("dialog", handle_dialog)

      try:
         #Handle Ok Button
         ok_btn = self.page.get_by_role("button", name="OK")
         ok_btn.wait_for(state="visible", timeout=30000)
         ok_btn.click()
      except Exception as e:
         print("OK button did not appear:", str(e))

      return dialog_message
