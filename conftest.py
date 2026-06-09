import pytest
import pytest_html
from datetime import datetime
import os
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
# def browser():

#    while True:
#       choice = input(
#             "Run in headless mode? (y/n): "
#       ).strip().lower()

#       if choice in ["y", "n"]:
#             break

#       print("Please enter y or n.")

#    headless_mode = choice == "y"

#    with sync_playwright() as p:
#       browser = p.chromium.launch(headless=headless_mode)
#       yield browser
#       browser.close()

def browser():

   with sync_playwright() as p:
      browser = p.chromium.launch(
         # headless=True
         headless=False
      )

      yield browser

      browser.close()


@pytest.fixture
def page(browser):
   context = browser.new_context()
   page = context.new_page()

   yield page

   # always capture final state screenshot per test
   os.makedirs("reports/screenshots", exist_ok=True)

   screenshot_path = (
      f"reports/screenshots/final_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
   )

   try:
      if not page.is_closed():
         page.screenshot(path=screenshot_path, full_page=True)
   except Exception as e:
      print(f"Final screenshot failed: {e}")

   context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

   outcome = yield
   report = outcome.get_result()

   if report.when == "call":
      page = item.funcargs.get("page")

      if page and not page.is_closed():
         os.makedirs("reports/screenshots", exist_ok=True)

         screenshot_path = (
               f"Reports/screenshots/"
               f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            )

         try:
            page.screenshot(
               path=screenshot_path,
               full_page=True
            )
         except Exception as e:
            print(f"Screenshot capture failed: {e}")
            return

            # attach to pytest-html report
         extras = getattr(report, "extras", [])
         extras.append(
            pytest_html.extras.png(screenshot_path)
         )
         report.extras = extras