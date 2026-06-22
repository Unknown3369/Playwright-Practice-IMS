
from Pages.Login import login
from Pages.Reports.Vat_purchase_register_report import VatPurchaseRegisterReportPage


def test_vat_purchase_register_report(page,config_data):
    username = config_data["username"]
    password = config_data["password"]

    login_page = login(page)
    login_page.perform_login(username, password)

    print("Logged into IMS")

    vat_purchase_report = VatPurchaseRegisterReportPage(page)
    vat_purchase_report.generate_vat_purchase_register_report()

    print("Vat Purchase Register Report generated successfully.")  
