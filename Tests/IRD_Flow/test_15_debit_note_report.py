import pytest

from Pages.Login import login
from Pages.Reports.Debit_note_report import DebitNoteBookReportPage

def test_generate_debit_note_book_report(page):

    login_page = login(page)

    login_page.perform_login(
            "Testuser","Test@1234")

    print("Logged into IMS")

    debit_report_page = DebitNoteBookReportPage(page)
    debit_report_page.generate_debit_note_book_report()

    print("Debit Note Book Report generated successfully.")
