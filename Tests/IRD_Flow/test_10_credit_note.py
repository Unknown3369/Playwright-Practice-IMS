import pytest
from Pages.Login import login
from Pages.Transactions.credit_note import CreditNotePage
import os
from playwright.sync_api import sync_playwright


def test_generate_credit_note(page,config_data):
   username = config_data["username"]
   password = config_data["password"]
   
   login_page = login(page)
   credit_note_page = CreditNotePage(page)
   login_page.perform_login(username, password)
   print("Logged into IMS")
   credit_note_page.navigate_to_credit_note()
   credit_note_page.create_credit_note()
   credit_note_page.save_credit_note()
   print("Credit Note created successfully")

   
