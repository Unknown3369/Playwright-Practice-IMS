class AddVendor:

   def __init__(self, page):
      self.page = page

   def open_add_vendor(self):

      self.page.get_by_title("Customer & Vendor Info").nth(1).click()
      self.page.get_by_role("link", name="Vendor Master").click()
      self.page.get_by_role("button", name="Create Vendor").click()

   def add_vendor(
      self,
      vendor_name,
      vendor_address,
      vendor_vat_no,
      vendor_email,
      vendor_mobile
   ):

      self.page.locator("#vendorName").fill(vendor_name)
      print(f"Vendor Name: {vendor_name}")

      self.page.locator("#address").fill(vendor_address)
      print(f"Address: {vendor_address}")

      self.page.locator("#vatNo").fill(vendor_vat_no)
      print(f"VAT No: {vendor_vat_no}")

      self.page.locator("#email").fill(vendor_email)
      print(f"Email: {vendor_email}")

      self.page.locator("#Mobile").fill(vendor_mobile)
      print(f"Mobile: {vendor_mobile}")

      save_btn = self.page.get_by_role(
         "button",
         name="SAVE"
      )

      save_btn.wait_for(
         state="visible",
         timeout=30000
      )

      save_btn.click()

      print("Save button clicked!")

      try:
         ok_btn = self.page.get_by_role(
            "button",
            name="OK"
         )

         ok_btn.wait_for(
            state="visible",
            timeout=5000
         )

         ok_btn.click()

         print("Success popup handled!")

      except:
         pass