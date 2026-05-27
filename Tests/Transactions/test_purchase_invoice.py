import csv
import random
import pytest
from playwright.sync_api import sync_playwright

from Pages.Login import login
from Pages.Transactions.purchase_invoice import PurchaseInvoice


def read_products_from_csv(file_path):
   products = []

   with open(file_path, mode='r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)

      for row in reader:
            products.append(row)

   return products


@pytest.fixture(scope="function")
def page():

   with sync_playwright() as p:
      browser = p.chromium.launch(headless=True)
      page = browser.new_page()
      yield page
      browser.close()


def test_purchase_invoice(page):

   login_page = login(page)
   purchase_invoice = PurchaseInvoice(page)
   login_page.perform_login("Testuser", "Test@1234")
   products = read_products_from_csv("product_details.csv")
   random_invoice_no = random.randint(10000, 99999)
   purchase_invoice.purchase_invoice(random_invoice_no)
   for product in products:

      item_code = product['Item Code']
      random_quantity = random.randint(10, 100)
      purchase_invoice.purchase_invoice_test(
         item_code,
         random_quantity
      )

   purchase_invoice.save_button_click()