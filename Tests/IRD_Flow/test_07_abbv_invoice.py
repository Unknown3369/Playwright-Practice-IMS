import csv
import os
import random
from playwright.sync_api import sync_playwright
from Pages.Login import login
from Pages.Transactions.abbv_invoice import AbbvInvoice

def read_products_from_csv(file_path):

   products = []

   with open(file_path,mode="r",newline="",encoding="utf-8") as file:
      reader = csv.DictReader(file)
      for row in reader:
            products.append(row)
   return products

def test_abbv_invoice(page,config_data):
   username = config_data["username"]
   password = config_data["password"]

   try:
      login_page = login(page)
      login_page.perform_login(username, password)
   except:
      print("Already Logged In")

   sales_invoice = AbbvInvoice(page)

   ref_no = "IRD_ABBV_REF" + str(random.randint(10,99)) + "-" + str(random.randint(1000,9999))
   sales_invoice.enter_sales_invoice(ref_no)

   products = read_products_from_csv(
      "product_details.csv"
   )

   for product in products:
         item_code = product["Item Code"]
         random_quantity = 10
         sales_invoice.sales_invoice_test(item_code,random_quantity)
   
   sales_invoice.save_btn()