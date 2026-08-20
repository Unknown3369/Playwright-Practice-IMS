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

    def get_required_input(prompt):
        while True:
            value = input(prompt).strip()

            if value:
                return value

            print("This field is required. Please enter a value.")

    url = request.config.getoption("--url")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    customer_address = request.config.getoption("--customer-address")
    vender_address = request.config.getoption("--vender-address")

    # If values are not provided through command line,
    # ask for them and make them compulsory.
    if not url:
        url = get_required_input("\nEnter URL: ")

    if not username:
        username = get_required_input("Enter Username: ")

    if not password:
        password = get_required_input("Enter Password: ")

    if not customer_address:
        customer_address = get_required_input("Enter Customer Address: ")

    if not vender_address:
        vender_address = get_required_input("Enter Vender Address: ")

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