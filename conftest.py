import pytest
import pytest_html
from datetime import datetime
import os

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
   outcome = yield
   report = outcome.get_result()

   if report.when == "call":
      page = item.funcargs.get("page")

      if page:
            os.makedirs("reports/screenshots", exist_ok=True)

            screenshot_path = (
               f"reports/screenshots/"
               f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            )

            page.screenshot(path=screenshot_path)

            extras = getattr(report, "extras", [])
            extras.append(pytest_html.extras.png(screenshot_path))
            report.extras = extras