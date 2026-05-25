import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
   browser = playwright.chromium.launch(headless=False)
   context = browser.new_context()
   page = context.new_page()
   page.goto("https://demo.playwright.dev/todomvc/#/")
   page.get_by_role("textbox", name="What needs to be done?").click()
   page.get_by_role("textbox", name="What needs to be done?").fill("go to link https://stc21.variantqa.himshang.com.np/#/login")
   page.get_by_role("textbox", name="What needs to be done?").press("Enter")
   page.get_by_role("textbox", name="What needs to be done?").fill("click on username")
   page.get_by_role("textbox", name="What needs to be done?").press("Enter")
   page.get_by_role("textbox", name="What needs to be done?").fill("enter Testuser")
   page.get_by_role("textbox", name="What needs to be done?").press("Enter")
   page.get_by_role("textbox", name="What needs to be done?").fill("go to password")
   page.get_by_role("textbox", name="What needs to be done?").press("Enter")
   page.get_by_role("textbox", name="What needs to be done?").fill("enter Test@1234")
   page.get_by_role("textbox", name="What needs to be done?").press("Enter")
   page.get_by_role("textbox", name="What needs to be done?").fill("click on login")
   page.get_by_role("textbox", name="What needs to be done?").press("Enter")
   # ---------------------
   context.close()
   browser.close()


with sync_playwright() as playwright:
   run(playwright)
