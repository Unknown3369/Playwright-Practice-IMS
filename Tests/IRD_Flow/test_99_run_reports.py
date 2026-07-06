
from Tests.IRD_Flow.test_06_purchase_book_report import test_purchase_book_report
from Tests.IRD_Flow.test_08_sales_book_report import test_sales_book_report
from Tests.IRD_Flow.test_09_materialized_report import test_materialized_view_report
from Tests.IRD_Flow.test_11_credit_note_report import test_generate_credit_note_book_report
from Tests.IRD_Flow.test_13_vat_sales_register_report import test_vat_sales_register_report
from Tests.IRD_Flow.test_15_debit_note_report import test_generate_debit_note_book_report
from Tests.IRD_Flow.test_16_vat_purchase_report import test_vat_purchase_register_report
from Tests.IRD_Flow.test_17_stock_summary_report import test_stock_summary_report
from Tests.IRD_Flow.test_18_transaction_activity_report import test_transaction_activity_report


import os
SKIP_TESTS = os.getenv("SKIP_TESTS", "").split(",")

def sales_book_report(page, config_data):
    if "test_sales_book_report" not in SKIP_TESTS:
        test_sales_book_report(page, config_data)
        print("Completed Test Sales Book Report")

def purchase_book_report(page, config_data):
    if "test_purchase_book_report" not in SKIP_TESTS:
        test_purchase_book_report(page, config_data)
        print("Completed Test Purchase Book Report")

def vat_purchase_report(page,config_data):
    if "test_vat_purchase_register_report" not in SKIP_TESTS:
        test_vat_purchase_register_report(page, config_data)
        print("Completed Test VAT Purchase Register Report")

def debit_note_report(page, config_data):
    if "test_generate_debit_note_book_report" not in SKIP_TESTS:
        test_generate_debit_note_book_report(page, config_data)
        print("Completed Test Generate Debit Note Book Report")

def credit_note_report(page, config_data):
    if "test_generate_credit_note_book_report" not in SKIP_TESTS:
        test_generate_credit_note_book_report(page, config_data)
        print("Completed Test Generate Credit Note Book Report")

def vat_sales_report(page,config_data):
    if "test_vat_sales_register_report" not in SKIP_TESTS:
        test_vat_sales_register_report(page, config_data)
        print("Completed Test VAT Sales Register Report")

def materialized_view_report(page, config_data):
    if "test_materialized_view_report" not in SKIP_TESTS:
        test_materialized_view_report(page, config_data)
        print("Completed Test Materialized View Report")

def stock_summary_report(page,config_data):
    if "test_stock_summary_report" not in SKIP_TESTS:
        test_stock_summary_report(page, config_data)
        print("Completed Test Stock Summary Report")

def transaction_activity_report(page, config_data):
    if "test_transaction_activity_report" not in SKIP_TESTS:
        test_transaction_activity_report(page, config_data)
        print("Completed Test Transaction Activity Report")

def test_ird_flow(page, config_data):

#----------------------------Purchase Book Report-------------------------------------
    purchase_book_report(page, config_data)

#----------------------------Sales Book Report------------------------------------------
    sales_book_report(page, config_data)

#-----------------------------Credit Note Book Report------------------------------------
    credit_note_report(page, config_data)

#-----------------------------Materialized Report----------------------------------------
    materialized_view_report(page, config_data)
    
#-----------------------------VAT Sales register Report---------------------------------
    vat_sales_report(page, config_data)

#-----------------------------Debit Note Book Report-----------------------------------
    debit_note_report(page, config_data)

#-----------------------------VAT Purchase register Report-----------------------------
    vat_purchase_report(page, config_data)

#-----------------------------Stock Summary Report-------------------------------------
    stock_summary_report(page,config_data)

#-----------------------------Transacction Activity Report-----------------------------
    transaction_activity_report(page, config_data)

    page.wait_for_timeout(1000)
    print("test passed")