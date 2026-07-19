from Tests.IRD_Flow.test_01_Login import (
    test_login_to_ims as run_login_to_ims
)

from Tests.IRD_Flow.test_02_add_product_group import (
    test_add_product_group_master as run_add_product_group_master
)

from Tests.IRD_Flow.test_04_add_customer import (
    test_add_customer as run_add_customer
)

from Tests.IRD_Flow.test_04_add_vendor import (
    test_create_vendor as run_create_vendor
)

from Tests.IRD_Flow.test_03_add_prod import (
    test_add_prod as run_add_prod
)

from Tests.IRD_Flow.test_05_purchase_invoice import (
    test_purchase_invoice as run_purchase_invoice
)

from Tests.IRD_Flow.test_06_purchase_book_report import (
    test_purchase_book_report as run_purchase_book_report
)

from Tests.IRD_Flow.test_07_abbv_invoice import (
    test_abbv_invoice as run_abbv_invoice
)

from Tests.IRD_Flow.test_07_sales_invoice import (
    test_sales_invoice as run_sales_invoice
)

from Tests.IRD_Flow.test_08_sales_book_report import (
    test_sales_book_report as run_sales_book_report
)

from Tests.IRD_Flow.test_09_materialized_report import (
    test_materialized_view_report as run_materialized_view_report
)

from Tests.IRD_Flow.test_10_credit_note import (
    test_generate_credit_note as run_generate_credit_note
)

from Tests.IRD_Flow.test_11_credit_note_report import (
    test_generate_credit_note_book_report as run_generate_credit_note_book_report
)

from Tests.IRD_Flow.test_11_vat_sales_register_report import (
    test_vat_sales_register_report as run_vat_sales_register_report
)

from Tests.IRD_Flow.test_14_debit_note import (
    test_debit_note as run_debit_note
)

from Tests.IRD_Flow.test_15_debit_note_report import (
    test_generate_debit_note_book_report as run_generate_debit_note_book_report
)

from Tests.IRD_Flow.test_16_vat_purchase_report import (
    test_vat_purchase_register_report as run_vat_purchase_register_report
)

from Tests.IRD_Flow.test_17_stock_summary_report import (
    test_stock_summary_report as run_stock_summary_report
)

from Tests.IRD_Flow.test_18_transaction_activity_report import (
    test_transaction_activity_report as run_transaction_activity_report
)

from Tests.IRD_Flow.test_reprint_sales_invoice import (
    test_reprint_invoice as run_reprint_invoice
)

from Tests.IRD_Flow.test_reprint_credit_note import (
    test_reprint_credit_note as run_reprint_credit_note
)

from Tests.IRD_Flow.test_run_reports import (
    test_print_all_final_reports as run_print_all_final_reports
)

from Tests.IRD_Flow.printpreview import close_print_preview

import os
import time
SKIP_TESTS = os.getenv("SKIP_TESTS", "").split(",")

def run_test(test_function, page, config_data, test_name):
    if test_name not in SKIP_TESTS:
        try:
            test_function(page, config_data)
            print(f"Completed {test_name}")

        except Exception as e:
            print(f"\n FAILED: {test_name}")
            print(f"Error: {e}")
            print("Stopping remaining tests...")
            raise

def sales_book_report(page, config_data):
    if "test_sales_book_report" not in SKIP_TESTS:
        run_sales_book_report(page, config_data)
        print("Completed Test Sales Book Report")

def purchase_book_report(page, config_data):
    if "test_purchase_book_report" not in SKIP_TESTS:
        run_purchase_book_report(page, config_data)
        print("Completed Test Purchase Book Report")

def vat_purchase_report(page,config_data):
    if "test_vat_purchase_register_report" not in SKIP_TESTS:
        run_vat_purchase_register_report(page, config_data)
        print("Completed Test VAT Purchase Register Report")

def debit_note_report(page, config_data):
    if "test_generate_debit_note_book_report" not in SKIP_TESTS:
        run_generate_debit_note_book_report(page, config_data)
        print("Completed Test Generate Debit Note Book Report")

def credit_note_report(page, config_data):
    if "test_generate_credit_note_book_report" not in SKIP_TESTS:
        run_generate_credit_note_book_report(page, config_data)
        print("Completed Test Generate Credit Note Book Report")

def vat_sales_report(page,config_data):
    if "test_vat_sales_register_report" not in SKIP_TESTS:
        run_vat_sales_register_report(page, config_data)
        print("Completed Test VAT Sales Register Report")

def materialized_view_report(page, config_data):
    if "test_materialized_view_report" not in SKIP_TESTS:
        run_materialized_view_report(page, config_data)
        print("Completed Test Materialized View Report")

def stock_summary_report(page,config_data):
    if "test_stock_summary_report" not in SKIP_TESTS:
        run_stock_summary_report(page, config_data)
        print("Completed Test Stock Summary Report")

def transaction_activity_report(page, config_data):
    if "test_transaction_activity_report" not in SKIP_TESTS:
        run_transaction_activity_report(page, config_data)
        print("Completed Test Transaction Activity Report")

def test_ird_flow(page, config_data):

    if "test_login_to_ims" not in SKIP_TESTS:
        run_login_to_ims(page, config_data)
        print("Completed Test Login")

#---------------------------Add Product/Customer/Vendor/Product_Group------------------
    if "test_add_product_group_master" not in SKIP_TESTS:
        run_add_product_group_master(page, config_data)
        print("Completed Test Add Product Group")
    if "test_add_customer" not in SKIP_TESTS:
        run_add_customer(page, config_data)
        print("Completed Test Add Customer")
    if "test_create_vendor" not in SKIP_TESTS:
        run_create_vendor(page, config_data)                
        print("Completed Test Add Vendor")
    if "test_add_prod" not in SKIP_TESTS:
        run_add_prod(page, config_data)
        print("Completed Test Add Product")

# #----------------------------Purchase Invoice------------------------------------------
#     if "test_purchase_invoice" not in SKIP_TESTS:
#         run_purchase_invoice(page, config_data)
#         print("Completed Test Generate Purchase invoice")

#----------------------------Purchase Invoice/Print Preview---------------------------------------------
    if "test_purchase_invoice" not in SKIP_TESTS:
        run_purchase_invoice(page, config_data)
        print("Completed Test Generate Purchase invoice")
        time.sleep(15)
        close_print_preview()
        page.bring_to_front()
        time.sleep(1)

#----------------------------Purchase Book Report--------------------------------------
    purchase_book_report(page, config_data)

#----------------------------Abbv Invoice/ Sales Bill----------------------------------
    try:
        if "test_abbv_invoice" not in SKIP_TESTS:
            run_abbv_invoice(page, config_data)
            print("Completed Test Generate Abbreviated Invoice")
            time.sleep(20)
            try:
                close_print_preview()
                page.bring_to_front()
                time.sleep(1)
            except:
                print('Print Preview Not Found')
    except:
        print('Abbv Invoice/ Sales Bill Not Found')

#----------------------------Sales Invoice---------------------------------------------
    try:
        if "test_sales_invoice" not in SKIP_TESTS:
            run_sales_invoice(page, config_data)
            print("Completed Test Generate Sales Invoice")
            time.sleep(20)
            close_print_preview()
            page.bring_to_front()
            time.sleep(1)
    except:
        print('Sales Invoice Not Found')

    if "test_reprint_sales_invoice" not in SKIP_TESTS:
        for i in range (1):
            run_reprint_invoice(page, config_data)
            print("Completed Test Reprint Invoice")
            time.sleep(20)
            try:
                close_print_preview()
                page.bring_to_front()
                time.sleep(1)
            except:
                print('Print Preview Not Found')
#----------------------------Sales Book Report-----------------------------------------
    sales_book_report(page, config_data)

#-----------------------------VAT Sales register Report--------------------------------
    vat_sales_report(page, config_data)

#----------------------------Materialized View Report----------------------------------
    materialized_view_report(page, config_data)

#----------------------------Credit Note-----------------------------------------------
    if "test_generate_credit_note" not in SKIP_TESTS:
        run_generate_credit_note(page, config_data)
        print("Completed Test Generate Credit Note")
        time.sleep(15)
        try:
            close_print_preview()
            page.bring_to_front()
            time.sleep(1)
        except:
            print('Print Preview Not Found')
    if "test_reprint_credit_note" not in SKIP_TESTS:
        for i in range (3):
            run_reprint_credit_note(page, config_data)
            print("Completed Test Reprint Credit Note")
            time.sleep(15)
            try:
                close_print_preview()
                page.bring_to_front()
                time.sleep(1)
            except:
                print('Print Preview Not Found')

#-----------------------------Credit Note Book Report----------------------------------
    credit_note_report(page, config_data)

#-----------------------------VAT Purchase register Report-----------------------------
    vat_purchase_report(page, config_data)

#-----------------------------Debit Note-----------------------------------------------
    if "test_debit_note" not in SKIP_TESTS:
        run_debit_note(page, config_data)
        print("Completed Test Generate Debit Note")
        try:
            close_print_preview()
            page.bring_to_front()
            time.sleep(1)
        except:
            print('Print Preview Not Found')
#-----------------------------Debit Note Book Report-----------------------------------
    debit_note_report(page, config_data)

#-----------------------------Stock Summary Report-------------------------------------
    stock_summary_report(page,config_data)

#-----------------------------Reprint Reports------------------------------------------
    if "test_print_all_final_reports" not in SKIP_TESTS:
        run_print_all_final_reports(page, config_data)
        print("Completed Test Print All Final Reports")

#-----------------------------Transacction Activity Report-----------------------------
    transaction_activity_report(page, config_data)

    page.wait_for_timeout(1000)
    print("test passed")

