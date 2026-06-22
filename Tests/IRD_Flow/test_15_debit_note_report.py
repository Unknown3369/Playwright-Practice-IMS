import pytest

from Pages.Login import login
from Pages.Reports.Debit_note_report import DebitNoteBookReportPage

def test_generate_debit_note_book_report(page,config_data):
    username = config_data["username"]
    password = config_data["password"]

    login_page = login(page)

    login_page.perform_login(username, password)

    print("Logged into IMS")

    debit_report_page = DebitNoteBookReportPage(page)
    debit_report_page.generate_debit_note_book_report()

    print("Debit Note Book Report generated successfully.")
