from playwright.sync_api import Page
import time


class PurchaseInvoice:
   def __init__(self, page: Page):
      self.page = page

      self.transactions = "//span[contains(text(), 'Transactions')]"
      self.pur_transaction = "text='Purchase Transaction'"
      self.purchase_invoice_link = "//span[normalize-space()='Purchase Invoice']"
      self.invoice_no = "#invoiceNO"
      self.account = "#accountfield"
      self.account_name = "//div[normalize-space()='11 QA Vendor']"
      self.item_name = "//input[@id='barcodeField' and @placeholder='Enter Barcode']"
      self.quantity = "#quantityBarcode"
      self.save_button = "//button[contains(text(),'SAVE')]"

   def purchase_invoice(self, invoice_value: int):
         self.page.get_by_title("Transactions").first.click()
         self.page.get_by_title("Purchase Transaction").nth(1).click()
         self.page.get_by_role("link", name="Purchase Invoice").click()
         # Enter invoice number
         self.page.locator(self.invoice_no).fill(str(invoice_value))
         print(f"Invoice No '{invoice_value}' entered successfully!")
         # Select Vendor
         self.page.locator(self.account).click()
         self.page.locator(self.account).press("Enter")
         self.page.wait_for_timeout(5000)
         print("Account field clicked successfully!")
         # Select account name
         self.page.locator(self.account_name).dblclick()
         print("Account name selected successfully!")

   def purchase_invoice_test(self, item_code: str, enter_quantity: int):

      # Enter item code
      self.page.locator(self.item_name).click()
      self.page.locator(self.item_name).fill(item_code)
      self.page.wait_for_timeout(2000)
      self.page.locator(self.item_name).press("Enter")
      self.page.wait_for_timeout(2000)
      print("Item name field clicked successfully!")
      # Enter quantity
      self.page.locator(self.quantity).click()
      self.page.locator(self.quantity).fill(str(enter_quantity))
      self.page.locator(self.quantity).press("Enter")
      print("Quantity entered successfully!")
      self.page.wait_for_timeout(2000)

   def save_button_click(self):

      # Click save button
      self.page.locator(self.save_button).click()
      print("Save button clicked successfully!")
      # Handle alert
      dialog_message = None
      def handle_dialog(dialog):
            nonlocal dialog_message
            dialog_message = dialog.message
            print("Alert says:", dialog_message)
            dialog.accept()

      self.page.once("dialog", handle_dialog)

      self.page.wait_for_timeout(3000)
      try:
         print_voucher = self.page.get_by_role("button", name="Print")
         print_voucher.wait_for( state="visible", timeout=30000).click()
         print ("Print Voucher clicked successfully!")
      
      except:
         print ("Print button not found!")

      self.page.wait_for_timeout(5000)