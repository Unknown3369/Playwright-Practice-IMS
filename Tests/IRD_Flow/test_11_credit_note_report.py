import pytest

from Pages.Login import login
from Pages.Reports.Credit_note_report import CreditNoteBookReportPage


def test_generate_credit_note_book_report(page,config_data):
   username = config_data["username"]
   password = config_data["password"]
   
   login_page = login(page)
   credit_report_page = CreditNoteBookReportPage(page)
   login_page.perform_login(username, password)

   print("Logged into IMS")

   credit_report_page.generate_credit_note_book_report()

   print("Credit Note Book Report generated successfully.")
