

class AddProductCategoryPage:

   def __init__(self, page):
      self.page = page


   def navigate_to_add_product(self):
         self.page.get_by_title("Inventory Info").nth(1).click()
         self.page.get_by_role("link", name="Product Category").click()
         self.page.get_by_role("button", name="Add Category").click()

   def add_product_category(self,category_name="Liquor"):
      try:
         category_input = self.page.locator("#catName")
         category_input.wait_for(state="visible",timeout=30000)
         category_input.fill(category_name)
         print(f"Category Name entered: {category_name}")

         save_btn = self.page.get_by_role("button", name="Save")
         save_btn.wait_for(state="visible",timeout=30000)
         assert save_btn.is_enabled()
         save_btn.click()
         print("Save button clicked!")

         ok_btn = self.page.get_by_role("button",name="OK")
         ok_btn.wait_for(state="visible",timeout=30000)
         ok_btn.click()
         print(f"Product category '{category_name}' added successfully!")

      except Exception as e:
         raise AssertionError(f"Failed to add product category. Error: {e}")
      


      