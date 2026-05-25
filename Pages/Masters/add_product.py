from playwright.sync_api import Page, expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
import time


class Add_prod:
   def __init__(self, page: Page):
      self.page = page

      # locators (kept same XPath logic)
      self.product_master = "//a[contains(@href, '/vendor-master/product')]"
      self.add_prod_btn = "//button[contains(text(), 'Add Product')]"
      self.add_prod_label = "//label[contains(text(), 'Add Product')]"

      self.item_group_input = "//input[@placeholder='-- Press Enter For Item Group --']"
      self.ng_select_box = "//ng-select[contains(@class,'ng-select-single')]//div[@role='combobox']"
      self.select_option = "//div[contains(@class,'ng-option')]//span[normalize-space()='0110']"
      self.ok_btn = "//button[.//span[contains(text(), 'Ok')]]"

      self.item_code_input = "//input[@placeholder='Enter Item Code']"
      self.item_name_input = "//input[@placeholder='Enter Item Name']"
      self.hs_code_input = "//input[@placeholder='Enter HS Code']"
      self.unit_dropdown = "//select[@id='unit']"
      self.description_input = "//input[@placeholder='Enter Product Description']"
      self.short_name = "//input[@placeholder='Enter Short Name']"
      self.purchase_price = "//input[@placeholder='Enter Purchase Price']"
      self.select_input = "//input[@placeholder='Press Enter to select']"
      self.supplier = "//td[normalize-space()='11 QA Vendor']"
      self.sales_price = "//input[@type='number' and @placeholder='0']"
      self.save_button_locator = "//button[@id='save' and text()='SAVE']"

   def masters_click_test(self):
      masters = self.page.locator("a[title='Masters']").filter(has_text="Masters").first
      masters.wait_for(state="visible", timeout=60000)
      masters.scroll_into_view_if_needed()
      masters.click()
      print("Masters clicked successfully!")

      inventory_info = self.page.locator("#side-navigation a[title='Inventory Info']")
      inventory_info.wait_for(state="visible", timeout=60000)
      inventory_info.scroll_into_view_if_needed()
      inventory_info.click()
      print("Inventory Info Clickced successfully!")

      product_master_link = self.page.locator(self.product_master)
      product_master_link.scroll_into_view_if_needed()
      product_master_link.click(force=True)
      print("Product Master clicked successfully!")
      time.sleep(2)

      add_product_btn = self.page.locator(self.add_prod_btn)
      add_product_btn.wait_for(state="visible")
      add_product_btn.click()
      print("Add Product button clicked successfully!")

      add_product_label = self.page.locator(self.add_prod_label)
      add_product_label.wait_for(state="visible")
      add_product_label.click()
      print("Add Product label clicked successfully!")

   def add_prod_test(self, input_itemname: str, input_hscode: str,
      input_description: str,
      input_purchase_price: int,
      input_sales_price: int):

      self.page.locator(self.item_group_input).press("Enter")
      time.sleep(1)

      self.page.locator(self.ng_select_box).click()
      print("ng-select box clicked")

      self.page.locator(self.select_option).click()
      print("option selected")

      self.page.locator(self.ok_btn).click()
      print("OK button clicked")

      item_name = self.page.locator(self.item_name_input)
      item_name.fill(input_itemname)
      print("Item Name entered:", input_itemname)

      hs_code = self.page.locator(self.hs_code_input)
      hs_code.fill(input_hscode)
      print("HS Code entered:", input_hscode)

      unit_dropdown = self.page.locator(self.unit_dropdown)
      unit_dropdown.click()
      self.page.select_option(self.unit_dropdown, label="Pkt.")
      print("Unit 'Pkt.' selected")

      self.page.locator(self.description_input).fill(input_description)
      print("Description entered:", input_description)

      self.page.locator(self.short_name).fill("TestProd")
      print("Short Name entered: TestProd")

      category_dropdown = self.page.locator("//select[@id='Category']")
      self.page.select_option("//select[@id='Category']", label="N/A")
      print("Category 'N/A' selected")

      purchase_price = self.page.locator(self.purchase_price)
      purchase_price.fill(str(input_purchase_price))
      print("Purchase Price entered:", input_purchase_price)

      self.page.locator(self.select_input).press("Enter")
      time.sleep(1)

      self.page.locator(self.supplier).dblclick()
      print("Supplier selected successfully!")

      sales_price = self.page.locator(self.sales_price)
      sales_price.fill(str(input_sales_price))
      print("Sales Price entered successfully!")

      item_code_locator = self.page.locator(
         "//input[@placeholder='Enter Item Code' and @readonly]"
      )

      self.page.wait_for_function(
         "el => el.value.trim() !== ''",
         item_code_locator.element_handle()
      )

      item_code = item_code_locator.input_value()
      return item_code
   
   def save_button(self):
      self.page.locator(self.save_button_locator).click()

      # handle browser alert
      try:
         self.page.wait_for_event("dialog", timeout=5000)
         dialog = self.page.on("dialog", lambda d: d.accept())
      except:
         pass

      # handle modal OK
      try:
         self.page.locator(
            "//button[normalize-space()='OK' or normalize-space()='Ok' or normalize-space()='Close']"
         ).click(timeout=10000)
      except:
         pass

      time.sleep(1)
