# tests/test_debit_note.py

import csv
import os
import random
import pytest
from playwright.sync_api import sync_playwright
from Pages.Login import login
from Pages.Transactions.debit_note import DebitNote


def read_products_from_csv(file_path):
   products = []

   with open(file_path, mode='r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
            products.append(row)
      return products

def test_debit_note(page):

   login_page = login(page)
   debit_note = DebitNote(page)
   page.wait_for_timeout(15000)
   login_page.perform_login("Testuser", "Test@1234")
   products = read_products_from_csv("product_details.csv")
   random_ref_no = "REF_NO" + str(random.randint(10000, 99999))
   debit_note.enter_debit_note()
   debit_note.debit_note_entry(str(random_ref_no))

   for product in products:
      item_code = product["Item Code"]
      random_quantity = random.randint(1, 5)
      debit_note.debit_note_test(item_code, random_quantity)
      page.wait_for_timeout(10000)

   dialog_message = debit_note.save_button_click()
   assert dialog_message is not None, "Popup did not appear!"

   expected_messages = ["saved", "success", "print bill"]

   assert any(msg in dialog_message.lower() for msg in expected_messages), \
      f"Unexpected popup message: {dialog_message}"
