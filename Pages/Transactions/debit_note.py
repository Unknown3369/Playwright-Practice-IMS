from playwright.sync_api import Page, expect
import time
import csv

class DebitNote:
   def __init__(self, page: Page):

      page.add_init_script("""
         window.print = () => {
            console.log("window.print() suppressed");
         };
      """)

      self.page = page

      self.ref_no = "#invoiceNO"
      self.return_mode = "#paymentTerms"
      self.supplier = "#customerselectid"
      self.item_name = "#barcodeField"
      self.quantity = "#quantityBarcode"
      self.save_button = "//button[normalize-space(text())='SAVE [End]']"

   def get_vendor_name():
      with open("vendors.csv", newline="", encoding="utf-8") as file:
         reader = csv.DictReader(file)
         row = next(reader)  # First row
         return row["ACNAME"]

   def enter_debit_note(self):

      self.page.get_by_title("Transactions").first.click()
      self.page.get_by_title("Purchase Transaction").nth(1).click()
      self.page.get_by_role("link", name="Debit Note (Purchase Return)").click()

   def debit_note_entry(self, enter_ref_no: str):
      vendor_name = DebitNote.get_vendor_name()
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

      # self.page.locator(self.account).fill(vendor_name)

      vendor_select = self.page.locator(f"//div[normalize-space()='{vendor_name}']")
      vendor_select.wait_for(state="visible",timeout=30000)
      vendor_select.dblclick()
      print(f"Vendor '{vendor_name}' selected successfully!")

   def debit_note_test(self, item_code: str, enter_quantity: int):

      # Enter Item Code
      item_name = self.page.locator(self.item_name)
      item_name.clear()
      item_name.fill(item_code)
      self.page.wait_for_timeout(1000)
      item_name.press("Enter")
      self.page.wait_for_timeout(2000)
      # item_name.press("Enter")
      print("Item name entered successfully!")

      # Enter Quantity
      quantity = self.page.locator(self.quantity)
      quantity.clear()
      quantity.fill(str(enter_quantity))
      time.sleep(1)
      quantity.press("Enter")
      print("Quantity entered successfully!")
      self.page.wait_for_timeout(1000)

   def save_button_click(self):

      # Click Save Button
      save_button = self.page.locator(self.save_button)
      expect(save_button).to_be_enabled()
      save_button.click()
      print("Save button clicked successfully!")

      time.sleep(5)
      self.page.keyboard.press("Escape")
      time.sleep(10)
      