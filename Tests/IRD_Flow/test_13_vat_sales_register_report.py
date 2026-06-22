import pytest

from Pages.Login import login
from Pages.Reports.Vat_sales_register_report import VatSalesRegisterReportPage


def test_vat_sales_register_report(page,config_data):
    username = config_data["username"]
    password = config_data["password"]

    login_page = login(page)

    login_page.perform_login(username, password)
    print("Logged into IMS")

    vat_sales_report = VatSalesRegisterReportPage(page)
    vat_sales_report.generate_vat_sales_register_report()
    print("VAT Sales Register Report generated successfully.")