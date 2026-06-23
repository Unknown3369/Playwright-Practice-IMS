import allure
from playwright.sync_api import Page
import os
from datetime import datetime
import csv

@allure.feature("Add Product Group Master")
class AddProductGroupMasterPage:

   def __init__(self, page: Page):
      self.page = page

   @allure.step("Navigate to Add Product Group Master page")
   def navigate_to_add_product(self):
         self.page.get_by_title("Inventory Info").nth(1).click()
         self.page.get_by_role("link", name="Product Group Master").click()
         self.page.get_by_role("button", name="Add Product Group").click()

   @allure.step("Select Item Group as TestGroup")
   def select_item_group(self):

      # self.page.locator(
      #    "//mat-icon[normalize-space(text())='open_in_new']"
      # ).click()

      # self.page.wait_for_timeout(1000)

      self.page.locator("//input[@type='checkbox']").first.click()
      # self.page.locator(
      #    "//input[@aria-autocomplete='list' and @type='text']"
      # ).first.fill("TestGroup")

      # self.page.locator(
      #    "//span[normalize-space()='TestGroup']"
      # ).click()

      # self.page.locator(
      #    "//span[normalize-space()='Ok']"
      # ).click()

      # print("Selected Parent Group : TestGroup")

      # self.page.wait_for_timeout(2000)

   def save_group_to_csv(
        self,
        group_name,
        group_code,
        recommended_margin,
        shelf_life
      ):
    os.makedirs("Reports/data", exist_ok=True)

    csv_file = "product_groups.csv"

    file_exists = os.path.isfile(csv_file)

    with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "Group Name",
                "Group Code",
                "Recommended Margin",
                "Shelf Life"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            group_name,
            group_code,
            recommended_margin,
            shelf_life
        ])

    print(f"Saved group '{group_name}' to CSV")

   @allure.step("Fill Product Group Details and Save")
   def fill_group_details_and_save(
        self,
        group_name,
        group_code,
        recommended_margin,
        shelf_life
):

    print("Filling Product Group Details")

    self.page.locator("#groupName").fill(group_name)

    self.page.locator("input#GC").fill(group_code)

    self.page.locator("#recommendedMargin").fill(
        str(recommended_margin)
    )

    self.page.locator("#shelfLife").fill(
        str(shelf_life)
    )

    self.page.locator(
        "//button[@id='save' and normalize-space()='SAVE']"
    ).click()

    print("Clicked Save Button")

    self.page.wait_for_timeout(3000)

    self.save_group_to_csv(
        group_name,
        group_code,
        recommended_margin,
        shelf_life
    )
   
