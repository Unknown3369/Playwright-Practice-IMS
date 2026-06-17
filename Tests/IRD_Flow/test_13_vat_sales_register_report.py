import pytest

from Pages.Login import login
from Pages.Reports.Vat_sales_register_report import VatSalesRegisterReportPage


def test_vat_sales_register_report(page):

    login_page = login(page)

    login_page.perform_login(
        "Testuser", "Test@1234"
    )
    print("Logged into IMS")

    vat_sales_report = VatSalesRegisterReportPage(page)
    vat_sales_report.generate_vat_sales_register_report()
    print("VAT Sales Register Report generated successfully.")