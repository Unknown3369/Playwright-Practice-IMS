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


    materialized_view_report(page, config_data)

#----------------------------------------------------------------------------------
    credit_note_report(page, config_data)

#----------------------------------------------------------------------------------
    debit_note_report(page, config_data)

#----------------------------------------------------------------------------------
    vat_sales_report(page, config_data)

#----------------------------------------------------------------------------------
    vat_purchase_report(page, config_data)

#----------------------------------------------------------------------------------
    stock_summary_report(page,config_data)
    time.sleep(5)
