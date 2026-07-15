import pytest

from Pages.Login import login
from Pages.Reports.Debit_note_report import DebitNoteBookReportPage

def test_generate_debit_note_book_report(page,config_data):
    username = config_data["username"]
    password = config_data["password"]

    try:
        login_page = login(page)
        login_page.perform_login(username, password)
    except:
        print('Already Logged In')

    debit_report_page = DebitNoteBookReportPage(page)
    debit_report_page.generate_debit_note_book_report()
    debit_report_page.download_debit_note_report()

    print("Debit Note Book Report generated successfully.")
