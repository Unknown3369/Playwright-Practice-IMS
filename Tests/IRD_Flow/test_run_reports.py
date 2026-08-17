from Pages.Login import login
from Tests.IRD_Flow.test_09_materialized_report import (
    test_materialized_view_report as run_materialized_view_report
)
from Tests.IRD_Flow.test_11_credit_note_report import (
    test_generate_credit_note_book_report as run_generate_credit_note_book_report
)
from Tests.IRD_Flow.test_15_debit_note_report import (
    test_generate_debit_note_book_report as run_generate_debit_note_book_report
)
from Tests.IRD_Flow.test_11_vat_sales_register_report import (
    test_vat_sales_register_report as run_vat_sales_register_report
)
from Tests.IRD_Flow.test_16_vat_purchase_report import (
    test_vat_purchase_register_report as run_vat_purchase_register_report
)
from Tests.IRD_Flow.test_17_stock_summary_report import (
    test_stock_summary_report as run_stock_summary_report
)
import time

def close_active_modal(page):

    modal = page.locator(
        "div.modal.fade.in.show[role='dialog'][aria-modal='true']"
    )

    if modal.count() == 0:
        return

    if not modal.first.is_visible():
        return

    print("Active modal detected. Attempting to close it...")

    # Try OK
    ok_button = modal.get_by_role(
        "button",
        name="OK"
    ).first

    if ok_button.count() > 0 and ok_button.is_visible():
        ok_button.click()
        modal.wait_for(state="hidden", timeout=5000)
        return

    # Try Close
    close_button = modal.locator(
        "button.close, "
        "button[aria-label='Close'], "
        ".close"
    ).first

    if close_button.count() > 0 and close_button.is_visible():
        close_button.click()
        modal.wait_for(state="hidden", timeout=5000)

def materialized_view_report(page, config_data):
    run_materialized_view_report(page, config_data)
    print("Completed Test Materialized View Report")

def credit_note_report(page, config_data):
    run_generate_credit_note_book_report(page, config_data)
    print("Completed Test Generate Credit Note Book Report")

def debit_note_report(page, config_data):
    run_generate_debit_note_book_report(page, config_data)
    print("Completed Test Generate Debit Note Book Report")

def vat_sales_report(page,config_data):
    run_vat_sales_register_report(page, config_data)
    print("Completed Test VAT Sales Register Report")

def vat_purchase_report(page,config_data):
    run_vat_purchase_register_report(page, config_data)
    print("Completed Test VAT Purchase Register Report")

def stock_summary_report(page,config_data):
    run_stock_summary_report(page, config_data)
    print("Completed Test Stock Summary Report")

def test_print_all_final_reports(page, config_data):
    username = config_data["username"]
    password = config_data["password"]

#----------------------------------------------------------------------------------
    login_page = login(page)

    try:
        login_page.perform_login(username, password)
    except Exception as e:
        print("Logged into IMS", e)


    close_active_modal(page)
    materialized_view_report(page, config_data)

#----------------------------------------------------------------------------------
    close_active_modal(page)
    credit_note_report(page, config_data)

#----------------------------------------------------------------------------------
    close_active_modal(page)
    debit_note_report(page, config_data)

#----------------------------------------------------------------------------------
    close_active_modal(page)
    vat_sales_report(page, config_data)

#----------------------------------------------------------------------------------
    close_active_modal(page)
    vat_purchase_report(page, config_data)

#----------------------------------------------------------------------------------
    close_active_modal(page)
    stock_summary_report(page,config_data)
    time.sleep(5)
