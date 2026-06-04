import pytest
from playwright.sync_api import sync_playwright
from Pages.Login import login
from Pages.Masters.add_product import Add_prod
import random
import uuid
import csv
import os
import time
MAX_PRODUCTS = 75


def random_name():
   return "prod_" + uuid.uuid4().hex[:8]


def save_product_to_csv(item_code,item_name,hs_code,description,purchase_price,sales_price,filename="product_details.csv"):

   header = ["Item Code", "Item Name", "HS Code", "Description", "Purchase Price", "Sales Price"]

   # read file
   rows = []

   if os.path.exists(filename):
      with open(filename, "r", newline="", encoding="utf-8") as f:
         reader = list(csv.reader(f))

         if reader:
            if reader[0] == header:
               rows = reader[1:]
            else:
               rows = reader

   # add new product
   rows.append([item_code,item_name,hs_code,description,purchase_price,sales_price])

   #TRUE FIFO LOGIC (STRICT)
   while len(rows) > MAX_PRODUCTS:
      rows.pop(0)   # remove oldest ONE BY ONE

   # write back
   with open(filename, "w", newline="", encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerow(header)
      writer.writerows(rows)

   print(f"FIFO updated: {len(rows)} rows")


def test_add_prod(page):
   
   login_page = login(page)
   add_prod_page = Add_prod(page)
   login_page.perform_login("Testuser", "Test@1234")
   page.wait_for_load_state("networkidle")
   page.wait_for_timeout(3000)
   
   for i in range(2):
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

      add_prod_page.save_button()

      save_product_to_csv(
         item_code=item_code,
         item_name=random_item_name,
         hs_code=random_hs_code,
         description=random_description,
         purchase_price=random_purchase_price,
         sales_price=random_sales_price
      )

      page.wait_for_timeout(2000)
      time.sleep(10)