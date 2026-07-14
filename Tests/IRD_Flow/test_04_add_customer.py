import os
import random
import uuid
import csv

from playwright.sync_api import sync_playwright

from Pages.Login import login
from Pages.Masters.add_customer import AddCustomer


def random_name():
   return "IRD_Customer_" + uuid.uuid4().hex[:2]

def random_address(length=12):

   # letters = "abcdefghijklmnopqrstuvwxyz"

   # return "".join(
   #    random.choice(letters)
   #    for _ in range(length)
   # )
   return "Kath_mandu"


def random_phone():

   return "98" + str(
      random.randint(
         10000000,
         99999999
      )
   )

def clear_csv(filename="customers.csv"):
   with open(filename, mode="w", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(["MainGroup","ACNAME","Address","Contact","Email"])
   print("CSV reset complete.")

def write_customer_to_csv(data,file_name="customers.csv"):

   file_exists = os.path.isfile(
      file_name
   )

   with open(file_name,mode="a",newline="",encoding="utf-8") as file:

      writer = csv.DictWriter(
         file,
         fieldnames=data.keys()
      )

      if not file_exists:
         writer.writeheader()

      writer.writerow(data)

def test_add_customer(page,config_data):
   username = config_data["username"]
   password = config_data["password"]

   login_page = login(page)

   add_customer = AddCustomer(page)

   login_page.perform_login(username, password)

   clear_csv("customers.csv")

   page.wait_for_load_state(
         "networkidle"
      )

   add_customer.open_add_customer()

   customer_name = random_name()
   customer_address = random_address()
   customer_contact = random_phone()

   add_customer.add_customer(
      customer_name,
      customer_address,
      customer_contact
   )

   customer_data = {
      "MainGroup": "SUPPLIER",
      "ACNAME": customer_name,
      "Address": customer_address,
      "VATNO": customer_contact,
      "PARTYTYPE": "Customer"
   }

   write_customer_to_csv(customer_data)

   print(f"Customer '{customer_name}' added successfully!")