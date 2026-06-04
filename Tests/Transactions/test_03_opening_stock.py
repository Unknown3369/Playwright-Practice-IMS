import csv
import os
import random
import pytest

from playwright.sync_api import sync_playwright

from Pages.Login import login
from Pages.Transactions.opening_stock import OpeningStockPage


def read_products_from_csv(file_path):
   products = []
   with open(
      file_path,
      mode="r",
      newline="",
      encoding="utf-8"
   ) as file:
      reader = csv.DictReader(file)

      for row in reader:
         products.append(row)
   return products

def test_opening_stock_entry(page):

   login_page = login(page)
   login_page.perform_login(
      "Testuser",
      "Test@1234"
   )

   print("Logged into IMS")
   page.wait_for_load_state("networkidle")
   opening_stock = OpeningStockPage(page)
   products = read_products_from_csv(
      "product_details.csv"
   )

   opening_stock.enter_opening_stock()
   for index, product in enumerate(products):
      item_code = product["Item Code"]
      random_quantity = random.randint(100, 200)
      opening_stock.opening_stock_test(
         item_code,
         random_quantity,
         index
      )
      page.wait_for_timeout(1000)

   opening_stock.save_button_click()
   print("Opening Stock entry created successfully.")