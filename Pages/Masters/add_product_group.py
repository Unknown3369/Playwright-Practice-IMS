import time
import allure
from playwright.sync_api import Page


@allure.feature("Add Product Group Master")
class AddProductGroupMasterPage:

   def __init__(self, page: Page):
      self.page = page

   @allure.step("Navigate to Add Product Group Master page")
   def navigate_to_add_product(self):
         self.page.get_by_title("Inventory Info").nth(1).click()
         self.page.get_by_role("link", name="Product Group Master").click()
         self.page.get_by_role("button", name="Add Product Group").click()

   @allure.step("Select Item Group as OCR test")
   def select_item_group(self):

      self.page.locator(
            "//mat-icon[normalize-space(text())='open_in_new']"
      ).click()

      self.page.wait_for_timeout(1000)

      self.page.locator(
            "//input[@aria-autocomplete='list' and @type='text']"
      ).fill("OCR")

      self.page.locator(
            "//span[normalize-space()='OCR test']"
      ).click()

      self.page.locator(
            "//span[normalize-space()='Ok']"
      ).click()

      print("Selected Parent Group : OCR test")

      self.page.wait_for_timeout(2000)

   @allure.step("Fill Product Group Details and Save")
   def fill_group_details_and_save(
            self,
            group_name,
            recommended_margin,
            shelf_life
   ):

      print("Filling Product Group Details")

      self.page.locator("#groupName").fill(group_name)
      print(f"Entered Group Name : {group_name}")

      self.page.locator("#recommendedMargin").fill(
            str(recommended_margin)
      )
      print(f"Entered Recommended Margin : {recommended_margin}")

      self.page.locator("#shelfLife").fill(
            str(shelf_life)
      )
      print(f"Entered Shelf Life : {shelf_life}")

      self.page.locator(
            "//button[@id='save' and normalize-space()='SAVE']"
      ).click()

      print("Clicked Save Button")

      self.page.wait_for_timeout(3000)