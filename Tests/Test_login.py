import os

from playwright.sync_api import sync_playwright
import pytest
import allure
from Pages.Login import login


@allure.title("Login to IMS Application")
@allure.description("This test logs into the IMS application using valid credentials and verifies the dashboard.")
def test_login_to_ims(page):

      login_page = login(page)

      login_page.perform_login("Testuser", "Test@1234")

      print("Login process completed.")

      page.locator("xpath=//input[@id='Date']").wait_for(
         state="visible",
         timeout=30000
      )

      print("Dashboard page loaded successfully!")

      assert page.locator("xpath=//input[@id='Date']"), "Date input not found"
