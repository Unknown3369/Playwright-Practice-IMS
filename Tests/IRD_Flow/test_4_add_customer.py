import os
import random
import uuid

from playwright.sync_api import sync_playwright

from Pages.Login import login
from Pages.Masters.add_customer import AddCustomer


def random_name():
   return "cust_" + uuid.uuid4().hex[:8]


def random_address(length=12):

   letters = "abcdefghijklmnopqrstuvwxyz"

   return "".join(
      random.choice(letters)
      for _ in range(length)
   )


def random_phone():

   return "98" + str(
      random.randint(
         10000000,
         99999999
      )
   )


def test_add_customer(page):

      login_page = login(page)

      add_customer = AddCustomer(page)

      login_page.perform_login(
         "Testuser",
         "Test@1234"
      )

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

      print(
         f"Customer '{customer_name}' added successfully!"
      )