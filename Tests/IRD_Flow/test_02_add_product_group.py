import random
import uuid
import pytest
import csv
from Pages.Login import login
from Pages.Masters.add_product_group import (AddProductGroupMasterPage)

def clear_csv(filename="product_groups.csv"):
   with open(filename, mode="w", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(["Timestamp","Group Name","Group Code","Recommended Margin","Shelf Life"])
   print("CSV reset complete.")

def random_group_name():
   return f"IRD_Group"

def random_group_code():
   return f"{random.randint(1111, 9999)}"


def test_add_product_group_master(page, config_data):
   username = config_data["username"]
   password = config_data["password"]
   try:
      login_page = login(page)
      login_page.perform_login(username, password)
   except: 
      print("Already Logged In")

   clear_csv("product_groups.csv")

   try:
      add_group = AddProductGroupMasterPage(page)
      add_group.navigate_to_add_product()
      add_group.select_item_group()

      add_group.fill_group_details_and_save(
         group_name=random_group_name(),
         group_code=random_group_code(),
         recommended_margin=random.randint(5, 20),
         shelf_life=random.randint(15, 90)
      )
      print("Product Group Added Successfully")

   except Exception as e:
      pytest.fail(
         f"Test failed due to: {str(e)}"
      )