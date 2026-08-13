import pytest
import pytest_html
from datetime import datetime
import os
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        help="Application URL"
    )
    parser.addoption(
        "--username",
        action="store",
        help="Login username"
    )
    parser.addoption(
        "--password",
        action="store",
        help="Login password"
    )
    parser.addoption(
        "--customer-address",
        action="store",
        help="Customer address"
    )
    parser.addoption(
        "--vender-address",
        action="store",
        help="Vender address"
    )


@pytest.fixture(scope="session")
def config_data(request):

    url = request.config.getoption("--url") or ""
    username = request.config.getoption("--username") or ""
    password = request.config.getoption("--password") or ""
    customer_address = request.config.getoption("--customer-address") or ""
    vender_address = request.config.getoption("--vender-address") or ""

    if not url:
        url = input("\nEnter URL: ").strip()
    if not username:
        username = input("Enter Username: ").strip()
    if not password:
        password = input("Enter Password: ").strip()
    if not customer_address:
        customer_address = input("Enter Customer Address: ").strip()
    if not vender_address:
        vender_address = input("Enter Vender Address: ").strip()

    return {
        "url": url,
        "username": username,
        "password": password,
        "customer_address": customer_address,
        "vender_address": vender_address,
    }

@pytest.fixture(scope="session")
def browser():
   with sync_playwright() as p:
      browser = p.chromium.launch(
         headless=True,
         args=[
            "--kiosk-printing",
            "--disable-print-preview",
         ]
      )

      yield browser

      browser.close()


@pytest.fixture
def page(browser, config_data):
    context = browser.new_context(
        accept_downloads=True
    )

    page = context.new_page()

    # Open the URL provided from terminal
    page.goto(config_data["url"])

    yield page

    # # Always capture final state screenshot per test
    # os.makedirs("reports/screenshots", exist_ok=True)

    # screenshot_path = (
    #     f"reports/screenshots/final_"
    #     f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    # )

    # try:
    #     if not page.is_closed():
    #         page.screenshot(
    #             path=screenshot_path,
    #             full_page=True
    #         )
    # except Exception as e:
    #     print(f"Final screenshot failed: {e}")

    # context.close()


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