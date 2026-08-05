from itertools import count
import random
import time
import pandas as pd


class BulkSalesPriceUpdate:

   def __init__(self, page):
      self.page = page

   def navigate_to_bulk_sales_price(self):

      self.page.get_by_title("Sales Price Info").nth(1).click()
      self.page.get_by_role("link",name="Bulk Price Change").click()

      print("Navigated to Bulk Price Change page.")

   def select_category(self):

      item_group = self.page.locator("//input[@placeholder='Press Enter to Select']").nth(0)
      item_group.wait_for(
         state="visible",timeout=30000
      )
      item_group.press("Enter")
      print("Pressed Enter to open category dropdown.")

      main_group = self.page.locator("#mainGroup")
      main_group.wait_for( state="visible",timeout= 30000)
      main_group.select_option(label="TestGroup")
      print("mainGroup selected: TestGroup")

      ok_button = self.page.get_by_role(
         "button",
         name="OK"
      )

      ok_button.wait_for(
         state="visible",
         timeout=30000
      )

      ok_button.click()
      print("OK button clicked.")
      time.sleep(15)

   def update_prices(self):

      item_names = self.page.locator("input[id^='itemname']")
      count = item_names.count()

      print(f"Found {count} products on page")

      for i in range(count):

         product_name = self.page.locator(f"#itemname{i}").input_value()
         new_price = random.randint(200, 250)
         price_input = self.page.locator(f"#newSpriceInc{i}")
         price_input.fill(str(new_price))
         print(f"{product_name} updated -> {new_price}")


      save_button = self.page.get_by_role("button", name="Save")
      save_button.wait_for(state="visible", timeout=30000)
      save_button.click()

      time.sleep(5)

      print("All prices updated and Save clicked.")