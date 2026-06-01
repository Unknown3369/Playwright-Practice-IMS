import csv
import os
import random
import uuid

from playwright.sync_api import sync_playwright

from Pages.Login import login
from Pages.Masters.add_vendor import AddVendor


def random_name():
   return "Vend_" + uuid.uuid4().hex[:8]


def random_address(length=12):

   letters = "abcdefghijklmnopqrstuvwxyz"

   return "".join(
      random.choice(letters)
      for _ in range(length)
   )


def random_vat_no():

   return str(
      random.randint(
         100000000,
         999999999
      )
   )


def random_email():

   return (
      "Vend_"
      + uuid.uuid4().hex[:8]
      + "@gmail.com"
   )


def random_mobile():

   return (
      "98"
      + str(
         random.randint(
            10000000,
            99999999
         )
      )
   )


def write_vendor_to_csv(
   data,
   file_name="vendors.csv"
):

   file_exists = os.path.isfile(
      file_name
   )

   with open(
      file_name,
      mode="a",
      newline="",
      encoding="utf-8"
   ) as file:

      writer = csv.DictWriter(
         file,
         fieldnames=data.keys()
      )

      if not file_exists:
         writer.writeheader()

      writer.writerow(data)


def test_create_vendor():

   with sync_playwright() as p:

      headless_mode = (
         os.getenv(
            "HEADLESS",
            "false"
         ).lower()
         in ["true", "1", "yes"]
      )

      browser = p.chromium.launch(
         headless=headless_mode
      )

      page = browser.new_page()

      login_page = login(page)

      login_page.perform_login(
         "Testuser",
         "Test@1234"
      )

      print("Logged into IMS")

      vendor_page = AddVendor(page)

      vendor_page.open_add_vendor()

      vendor_name = random_name()
      vendor_address = random_address()
      vendor_vat = random_vat_no()
      vendor_email = random_email()
      vendor_mobile = random_mobile()

      vendor_page.add_vendor(
         vendor_name=vendor_name,
         vendor_address=vendor_address,
         vendor_vat_no=vendor_vat,
         vendor_email=vendor_email,
         vendor_mobile=vendor_mobile
      )

      vendor_data = {
         "MainGroup": "SUPPLIER",
         "ACNAME": vendor_name,
         "Address": vendor_address,
         "VATNO": vendor_vat,
         "PARTYTYPE": "Supplier"
      }

      write_vendor_to_csv(vendor_data)

      print(
         f"Vendor '{vendor_name}' created successfully!"
      )

      browser.close()