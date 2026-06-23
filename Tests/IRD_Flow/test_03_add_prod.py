from Tests.IRD_Flow import test_02_add_product_group
import pytest
from playwright.sync_api import sync_playwright
from Pages.Login import login
from Pages.Masters.add_product import Add_prod
import random
import uuid
import csv
import os
import time
MAX_PRODUCTS = 10

def random_name():
   return "IRD_PRODUCT_" + uuid.uuid4().hex[:8]

def clear_csv(filename="added_products.csv"):
   with open(filename, mode="w", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(["Item Code", "Item Name", "HS Code", "Description", "Purchase Price", "Sales Price", "Vatable"])
   print("CSV reset complete.")

def product_group(filename="product_groups.csv"):
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

        if not rows:
            raise Exception("No Product Groups found in CSV")

        # Get the most recently added group
        return rows[-1]["Group Name"]

def get_vendor_from_csv(filename="vendors.csv"):
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        raise Exception("No vendors found in CSV")

    return rows[-1]["ACNAME"]  # Use your actual column name

def save_product_to_csv(item_code,item_name,hs_code,description,purchase_price,sales_price,vatable,filename="product_details.csv"):

   header = ["Item Code", "Item Name", "HS Code", "Description", "Purchase Price", "Sales Price", "Vatable"]

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
   rows.append([item_code,item_name,hs_code,description,purchase_price,sales_price,vatable])

   #TRUE FIFO LOGIC (STRICT)
   while len(rows) > MAX_PRODUCTS:
      rows.pop(0)   # remove oldest ONE BY ONE

   # write back
   with open(filename, "w", newline="", encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerow(header)
      writer.writerows(rows)

   print(f"FIFO updated: {len(rows)} rows")


def test_add_prod(page, config_data):
   
   username = config_data["username"]
   password = config_data["password"]
   login_page = login(page)
   add_prod_page = Add_prod(page)
   login_page.perform_login(username, password)
   clear_csv("product_details.csv")
   page.wait_for_load_state("networkidle")
   page.wait_for_timeout(3000)
   
   for i in range(2):
      add_prod_page.masters_click_test()
      random_item_name = random_name()
      random_hs_code = str(random.randint(1000, 9999))
      
      random_description = "Test Product Description"
      random_purchase_price = random.randint(50, 180)
      random_sales_price = random.randint(200, 350)
      selected_group = product_group()
      selected_vendor = get_vendor_from_csv()
      item_code, vatable_status = add_prod_page.add_prod_test(
         input_itemname=random_item_name,
         input_hscode=random_hs_code,
         input_description=random_description,
         prod_group=selected_group,
         vendor_name=selected_vendor,
         input_purchase_price=random_purchase_price,
         input_sales_price=random_sales_price,
         iteration=i
      )

      add_prod_page.save_button()

      save_product_to_csv(item_code=item_code,item_name=random_item_name,hs_code=random_hs_code,description=random_description,purchase_price=random_purchase_price,sales_price=random_sales_price,vatable=vatable_status)

      page.wait_for_timeout(2000)
      time.sleep(10)