import pytest
import allure

from Pages.Login import login
from Pages.Reports.Materialized_View import MaterializedViewReportPage



def test_materialized_view_report(page):

    login_page = login(page)

    login_page.perform_login(
        "Testuser", "Test@1234"
    )

    print("Logged into IMS")

    materialized_view_report = MaterializedViewReportPage(page)
    materialized_view_report.generate_materialized_view_report()

    print("Materialized View Report generated successfully.")

    allure.attach(
        page.screenshot(full_page=True),
        name="Materialized_View_Report_Success",
        attachment_type=allure.attachment_type.PNG
    )
