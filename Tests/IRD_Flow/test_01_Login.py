import os

from playwright.sync_api import sync_playwright
from Pages.Login import login


def test_login_to_ims(page, config_data):

      username = config_data["username"]
      password = config_data["password"]

      login_page = login(page)
      login_page.perform_login(username, password)

      print("Login process completed.")

def verify_login(self):
   current_url = self.page.url

   if "#/pages/dashboard" in current_url:
      print(f"Test Successful, tested on {current_url}")
   else:
      print(f"Login failed or unexpected URL: {current_url}")

   


