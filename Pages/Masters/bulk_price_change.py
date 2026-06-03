import random


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

   def update_prices(self):

      price_fields = [
            "#newSpriceInc0",
            "#newSpriceInc1",
            "#newSpriceInc2",
            "#newSpriceInc3",
            "#newSpriceInc4"
      ]

      for field in price_fields:

         random_price = random.randint(200,250)

         price_input = self.page.locator(field)

         price_input.wait_for(
            state="visible",
            timeout=30000
         )

         price_input.clear()
         price_input.fill(str(random_price))

         print(
            f"{field} updated with price {random_price}"
         )

      save_button = self.page.get_by_role(
         "button",
         name="Save"
      )

      save_button.wait_for(
         state="visible",
         timeout=30000
      )

      save_button.click()

      print("Save button clicked.")