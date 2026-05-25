import re
from playwright.sync_api import sync_playwright

def test_login():
   with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      page = browser.new_page()
      link = "https://stc21.variantqa.himshang.com.np/#/login"
      username = "Testuser"
      password = "Test@1234"
      def login(link, username, password):
         page.goto(link)
         page.fill("input[placeholder='Username']", username)
         page.fill("input[placeholder='Password']", password)
         page.click("button[class='login-btn btn w-100']")
         try:
            page.wait_for_url("**#/pages/dashboard", timeout=5000)
            print("Login successful, dashboard reached.")


# with sync_playwright() as p:
#    browser = p.chromium.launch(headless=False)
#    page = browser.new_page()
#    page.goto("https://stc21.variantqa.himshang.com.np/#/login")
#    page.fill("input[placeholder='Username']", "Testuser")
#    page.fill("input[placeholder='Password']", "Test@1234")
#    page.click("button[class='login-btn btn w-100']")
#    try:
#       page.wait_for_url("**#/pages/dashboard", timeout=1000)
#       print("Login successful, dashboard reached.")
#    except:
#       logout_button = page.locator("button:has-text('Logout')")
#       logout_button.click()
#       page.wait_for_timeout(2000)
#       page.click("button.login-btn")
#       page.wait_for_url("**#/pages/dashboard")
#       assert "#/pages/dashboard" in page.url
#    page.screenshot(path="Screenshots/screenshot.png")
#    browser.close()