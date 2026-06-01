import os
import pytest
import random
import uuid

from playwright.sync_api import sync_playwright
from Pages.Login import login
from Pages.Masters.add_category import AddProductCategoryPage

def random_category_name():

   prefixes = ["Liquor","Snacks"]
   return f"{random.choice(prefixes)}_{uuid.uuid4().hex[:6]}"

def test_add_product_category():

   with sync_playwright() as p:
      headless_mode = os.getenv("HEADLESS", "false").lower() in ["true", "1", "yes"]
      browser = p.chromium.launch(headless=headless_mode)
      page = browser.new_page()
      login_page = login(page)

      try:
         login_page.perform_login("Testuser","Test@1234")
         page.wait_for_load_state("networkidle")
         page.wait_for_timeout(3000)
         print("Logged into IMS successfully!")

         add_category = AddProductCategoryPage(page)
         add_category.navigate_to_add_product()
         category_name = random_category_name()
         print(f"Generated Random Category: {category_name}")
         add_category.add_product_category(category_name)

      except Exception as e:

         pytest.fail(
            f"Test failed due to: {e}"
         )

      finally:
         browser.close()