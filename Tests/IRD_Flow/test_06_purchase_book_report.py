import time
import os

from Pages.Login import login
from Pages.Reports.Purchase_book_report import PurchaseBookReport

def test_purchase_book_report(page,config_data):
    username = config_data["username"]
    password = config_data["password"]

    try:
        login_page = login(page)
        login_page.perform_login(username, password)
    except:
        print("already logged in")
    purchase_report = PurchaseBookReport(page)

    purchase_report.open_purchase_book_report()

    time.sleep(8)
