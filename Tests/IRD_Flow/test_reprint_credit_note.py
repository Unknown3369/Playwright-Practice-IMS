import time
from Pages.invoice_reprint import invoice_reprint
from Pages.Login import login

def test_reprint_credit_note(page, config_data):
    username = config_data["username"]
    password = config_data["password"]

    try:
        login_page = login(page)
        login_page.perform_login(username, password)
    except:
        print('already logged in')
    reprint_invoice = invoice_reprint(page)
    reprint_invoice.reprint_invoice()



