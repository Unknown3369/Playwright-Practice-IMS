from playwright.sync_api import Page

class AddCustomer:
   def __init__(self, page: Page):
      self.page = page
      self.customer_name = "#customerName"
      self.address = "#address"
      self.contact = "#Mobile"

   def open_add_customer(self):

      self.page.get_by_title("Customer & Vendor Info").nth(1).click()
      self.page.get_by_role("link",name="Customer Master").click()
      self.page.get_by_role("button",name="Create Customer").click()

   def add_customer(
      self,
      customer_name: str,
      customer_address: str,
      customer_contact: str
   ):

      # Customer Name
      name = self.page.locator(self.customer_name)
      name.wait_for(state="visible",timeout=30000)
      name.fill(customer_name)
      print(f"Customer Name entered: {customer_name}")

      # Address
      address = self.page.locator(self.address)
      address.wait_for(state="visible",timeout=30000)
      address.fill(customer_address)
      print(f"Address entered: {customer_address}")

      # Contact
      contact = self.page.locator(self.contact)
      contact.wait_for(state="visible",timeout=30000)
      contact.fill(customer_contact)
      print(f"Contact entered: {customer_contact}")

      # Save
      save_btn = self.page.get_by_role("button",name="SAVE")
      save_btn.wait_for(state="visible",timeout=30000)
      save_btn.click()
      print("Save button clicked successfully!")

      # Optional Success Popup
      try:
         ok_btn = self.page.get_by_role("button",name="OK")
         ok_btn.wait_for(state="visible",timeout=5000)
         ok_btn.click()

         print(
            "Success popup handled!"
         )

      except:

         pass
