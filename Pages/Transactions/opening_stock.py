
import csv
from random import random

from playwright.sync_api import Page
import time

class OpeningStockPage:

   def __init__(self, page: Page):
      self.page = page

   def enter_opening_stock(self):
      self.page.get_by_title("Transactions").first.click()
      self.page.get_by_title("Inventory Movement").nth(1).click()
      self.page.get_by_role("link", name="Opening Stock").click()

   def opening_stock_test(
      self,item_code: str,enter_quantity: int,row_index: int):

      item_field = self.page.locator("#barcodeField")

      item_field.wait_for(
         state="visible",
         timeout=30000
      )

      item_field.clear()
      item_field.fill(item_code)
      self.page.wait_for_timeout(1000)
      item_field.press("Enter")
      print("Item name entered successfully!")
      self.page.wait_for_timeout(1000)
      time.sleep(1)

      quantity = self.page.locator("#quantityBarcode")
      quantity.wait_for(
            state="visible",
            timeout=30000
      )
      quantity.fill(str(enter_quantity))
      quantity.press("Enter")
      quantity.press("Enter")
      time.sleep(1)

      print(f"Quantity entered successfully! -> {enter_quantity}")
      self.page.wait_for_timeout(1000)

   def save_button_click(self):

      save_btn = self.page.locator("//button[normalize-space()='SAVE [End]']")
      save_btn.wait_for(state="visible", timeout=30000)
      save_btn.click()
      self.page.wait_for_timeout(3000)
      success_message = self.page.locator("//p[contains(text(),'has been saved successfully')]")

      success_message.wait_for(
         state="visible",
         timeout=30000
      )
      message_text = success_message.text_content()

      try:
         print_voucher = self.page.get_by_role("button", name="Print")
         print_voucher.wait_for( state="visible", timeout=30000).click()
         print ("Print Voucher clicked successfully!")
      
      except:
         print ("Print button not found!")

      self.page.wait_for_timeout(5000)