import os

from playwright.sync_api import sync_playwright

from Pages.Login import login
from Pages.Masters.bulk_price_change import BulkSalesPriceUpdate


def test_bulk_sales_price():

   with sync_playwright() as p:

      headless_mode = (
            os.getenv(
               "HEADLESS",
               "false"
            ).lower()
            in ["true", "1", "yes"]
      )

      browser = p.chromium.launch(
            headless=headless_mode
      )

      page = browser.new_page()

      try:

            login_page = login(page)

            login_page.perform_login(
               "Testuser",
               "Test@1234"
            )

            print("Logged into IMS")

            bulk_price = BulkSalesPriceUpdate(page)

            bulk_price.navigate_to_bulk_sales_price()

            bulk_price.select_category()

            bulk_price.update_prices()

            print(
               "Bulk Sales Price Update completed successfully."
            )

      finally:
            browser.close()