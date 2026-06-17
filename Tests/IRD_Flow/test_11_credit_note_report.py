import pytest

from Pages.Login import login
from Pages.Reports.Credit_note_report import CreditNoteBookReportPage


def test_generate_credit_note_book_report(page):

    login_page = login(page)

    login_page.perform_login(
        "Testuser", "Test@1234")

    print("Logged into IMS")

    credit_report_page = CreditNoteBookReportPage(page)
    credit_report_page.generate_credit_note_book_report()

    print("Credit Note Book Report generated successfully.")
