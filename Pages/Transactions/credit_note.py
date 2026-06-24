
import time

from playwright.sync_api import Page


class CreditNotePage:
   def __init__(self, page: Page):
      self.page = page

   def navigate_to_credit_note(self):

      self.page.get_by_title("Transactions").first.click()
      self.page.get_by_title("Sales Transaction").nth(1).click()
      self.page.get_by_role("link", name="Credit Note (Sales Return)").click()

   def create_credit_note(self):

      # --- Ref Bill No field ---
      ref_bill = self.page.locator("#refbill")
      ref_bill.scroll_into_view_if_needed()
      ref_bill.click()
      print("Clicked Ref Bill field")
      
         # Press ENTER to load vouchers
      ref_bill.press("Enter")
      print("Pressed ENTER to load vouchers")
      
         # --- Select voucher ---
      voucher = self.page.locator("//div[contains(@class,'modal')]//tbody/tr[1]/td[2]").nth(0)
      voucher.wait_for(state="visible")
      voucher.dblclick()
      print("Voucher selected")

      self.page.wait_for_timeout(5000)
      
      # --- Remarks ---
      remarks = self.page.locator("#remarksid")
      remarks.scroll_into_view_if_needed()
      remarks.fill("Credit note remarks.")
      print("Remarks entered")

   def save_credit_note(self):
         # --- Save ---
      save_btn = self.page.locator("xpath=//button[contains(text(),'SAVE')]")
      save_btn.scroll_into_view_if_needed()
      save_btn.click()
      print("Clicked SAVE")

      self.page.wait_for_timeout(5000)
      
