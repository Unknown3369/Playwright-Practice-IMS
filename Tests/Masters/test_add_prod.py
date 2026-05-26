import pytest
from playwright.sync_api import sync_playwright
from Pages.Login import login
from Pages.Masters.add_product import Add_prod
import random
import uuid


def random_name():
   return "prod_" + uuid.uuid4().hex[:8]


def test_add_prod():
   with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      page = browser.new_page()

      login_page = login(page)
      add_prod_page = Add_prod(page)

      login_page.perform_login("Testuser", "Test@1234")
      page.wait_for_load_state("networkidle")
      page.wait_for_timeout(3000)

      add_prod_page.masters_click_test()

      random_item_name = random_name()
      random_hs_code = str(random.randint(1000, 9999))
      random_description = "Test Product Description"
      random_purchase_price = random.randint(50, 180)
      random_sales_price = random.randint(200, 350)

      item_code = add_prod_page.add_prod_test(
         input_itemname=random_item_name,
         input_hscode=random_hs_code,
         input_description=random_description,
         input_purchase_price=random_purchase_price,
         input_sales_price=random_sales_price
      )

      # print("Generated Item Code:", item_code)

      add_prod_page.save_button()

      browser.close()