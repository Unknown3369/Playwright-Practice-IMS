from Pages.reprint_invoice import Reprint_invoice
from Pages.Login import login

def test_reprint_invoice(page, config_data):
    username = config_data["username"]
    password = config_data["password"]

    login_page = login(page)
    login_page.perform_login(username, password)
    reprint_invoice = Reprint_invoice(page)
    reprint_invoice.reprint_invoice()

