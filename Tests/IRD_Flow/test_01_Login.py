import os

from playwright.sync_api import sync_playwright
from Pages.Login import login


def test_login_to_ims(page, config_data):

      username = config_data["username"]
      password = config_data["password"]

      login_page = login(page)
      login_page.perform_login(username, password)

      print("Login process completed.")

      page.locator("xpath=//input[@id='Date']").wait_for(
         state="visible",
         timeout=30000
      )

      print("Dashboard page loaded successfully!")

      assert page.locator("xpath=//input[@id='Date']"), "Date input not found"
