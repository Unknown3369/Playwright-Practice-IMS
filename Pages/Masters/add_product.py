from playwright.sync_api import Page, expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
import time


class Add_prod:
   def __init__(self, page: Page):
      self.page = page

      #self.item_code_input = page.get_by_role("textbox", name="Enter Item Code")

   def masters_click_test(self):
      try:
         self.page.get_by_title("Inventory Info").nth(1).click()
         self.page.get_by_role("link", name="Product Master").click()
         self.page.get_by_role("button", name="Add Product").click()
         self.page.locator("a").filter(has_text="Add Product").first.click()


      except PlaywrightTimeoutError as e:
         self.page.goto("https://stc21.variantqa.himshang.com.np/#/pages/masters/vendor-master/product/new-product")
         print("Timeout while navigating to Add Product page, navigated directly instead.")

   def add_prod_test(self, input_itemname: str, input_hscode: str,input_description: str,input_purchase_price: int,input_sales_price: int):

      self.page.get_by_role("textbox", name="-- Press Enter For Item Group").press("Enter")

      self.page.locator(self.page.locator(".ng-input > input")).first.click()
      print("ng-select box clicked")

      self.page.locator(self.page.get_by_role("option", name="TESTTT")).click()
      print("option selected")

      self.page.locator(self.page.get_by_role("button", name="Ok")).click()
      print("OK button clicked")

      item_name = self.page.locator(self.page.get_by_role("textbox", name="Enter Item Name"))
      item_name.fill(input_itemname)
      print("Item Name entered:", input_itemname)

      hs_code = self.page.locator(self.page.get_by_role("textbox", name="Enter HS Code"))
      hs_code.fill(input_hscode)
      print("HS Code entered:", input_hscode)

      unit_dropdown = self.page.locator(self.page.locator("#unit"))
      unit_dropdown.click()
      self.page.select_option(self.page.locator("#unit"), label="Pkt.")
      print("Unit 'Pkt.' selected")

      self.page.locator(self.page.get_by_role("textbox", name="Enter Product Description")).fill(input_description)
      print("Description entered:", input_description)

      self.page.locator(self.page.get_by_role("textbox", name="Enter Short Name")).fill("TestProd")
      print("Short Name entered: TestProd")

      category_dropdown = self.page.locator("//select[@id='Category']")
      self.page.select_option("//select[@id='Category']", label="N/A")
      print("Category 'N/A' selected")

      purchase_price = self.page.locator(self.page.get_by_role("textbox", name="Enter Purchase Price"))
      purchase_price.fill(str(input_purchase_price))
      print("Purchase Price entered:", input_purchase_price)

      self.page.locator(self.page.locator("//input[@placeholder='Press Enter to select']")).press("Enter")
      time.sleep(1)

      self.page.locator(self.page.get_by_role("textbox", name="Press Enter to select")).dblclick()
      print("Supplier selected successfully!")

      sales_price = self.page.locator(self.page.get_by_role("textbox", name="0"))
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
      self.page.locator(self.page.get_by_role("button", name="SAVE")).click()

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
