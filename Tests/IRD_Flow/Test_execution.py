from playwright.sync_api import sync_playwright

from Tests.IRD_Flow.test_01_Login import test_login_to_ims
from Tests.IRD_Flow.test_02_add_product_group import test_add_product_group_master
from Tests.IRD_Flow.test_04_add_customer import test_add_customer
from Tests.IRD_Flow.test_04_add_vendor import test_create_vendor
from Tests.IRD_Flow.test_03_add_prod import test_add_prod
from Tests.IRD_Flow.test_05_purchase_invoice import test_purchase_invoice
from Tests.IRD_Flow.test_06_purchase_book_report import test_purchase_book_report
from Tests.IRD_Flow.test_07_abbv_invoice import test_abbv_invoice
from Tests.IRD_Flow.test_07_sales_invoice import test_sales_invoice
from Tests.IRD_Flow.test_08_sales_book_report import test_sales_book_report
from Tests.IRD_Flow.test_09_materialized_report import test_materialized_view_report
from Tests.IRD_Flow.test_10_credit_note import test_generate_credit_note
from Tests.IRD_Flow.test_11_credit_note_report import test_generate_credit_note_book_report
from Tests.IRD_Flow.test_13_vat_sales_register_report import test_vat_sales_register_report
from Tests.IRD_Flow.test_14_debit_note import test_debit_note
from Tests.IRD_Flow.test_15_debit_note_report import test_generate_debit_note_book_report
from Tests.IRD_Flow.test_16_vat_purchase_report import test_vat_purchase_register_report
from Tests.IRD_Flow.test_17_stock_summary_report import test_stock_summary_report
from Tests.IRD_Flow.test_18_transaction_activity_report import test_transaction_activity_report

import os
SKIP_TESTS = os.getenv("SKIP_TESTS", "").split(",")


def test_ird_flow(page, config_data):

    if "test_login_to_ims" not in SKIP_TESTS:
        test_login_to_ims(page, config_data)
        print("Completed Test Login")
    if "test_add_product_group_master" not in SKIP_TESTS:
        test_add_product_group_master(page)
        print("Completed Test Add Product Group")
    if "test_add_customer" not in SKIP_TESTS:
        test_add_customer(page)
        print("Completed Test Add Customer")
    if "test_create_vendor" not in SKIP_TESTS:
        test_create_vendor(page)                
        print("Completed Test Add Vendor")
    if "test_add_prod" not in SKIP_TESTS:
        test_add_prod(page)
        print("Completed Test Add Product")
    if "test_purchase_invoice" not in SKIP_TESTS:
        test_purchase_invoice(page)
        print("Completed Test Generate Purchase invoice")
    if "test_purchase_book_report" not in SKIP_TESTS:
        test_purchase_book_report(page)
        print("Completed Test Purchase Book Report")
    if "test_abbv_invoice" not in SKIP_TESTS:
        test_abbv_invoice(page)
        print("Completed Test Generate Abbreviated Invoice")
    if "test_sales_invoice" not in SKIP_TESTS:
        test_sales_invoice(page)
        print("Completed Test Generate Sales Invoice")
    if "test_sales_book_report" not in SKIP_TESTS:
        test_sales_book_report(page)
        print("Completed Test Sales Book Report")
    if "test_materialized_view_report" not in SKIP_TESTS:
        test_materialized_view_report(page)
        print("Completed Test Materialized View Report")
    if "test_generate_credit_note" not in SKIP_TESTS:
        test_generate_credit_note(page)
        print("Completed Test Generate Credit Note")
    if "test_generate_credit_note_book_report" not in SKIP_TESTS:
        test_generate_credit_note_book_report(page)
        print("Completed Test Generate Credit Note Book Report")
    if "test_materialized_view_report" not in SKIP_TESTS:
        test_materialized_view_report(page)
        print("Completed Test Materialized View Report")
    if "test_vat_sales_register_report" not in SKIP_TESTS:
        test_vat_sales_register_report(page)
        print("Completed Test VAT Sales Register Report")
    if "test_debit_note" not in SKIP_TESTS:
        test_debit_note(page)
        print("Completed Test Generate Debit Note")
    if "test_generate_debit_note_book_report" not in SKIP_TESTS:
        test_generate_debit_note_book_report(page)
        print("Completed Test Generate Debit Note Book Report")
    if "test_vat_purchase_register_report" not in SKIP_TESTS:
        test_vat_purchase_register_report(page)
        print("Completed Test VAT Purchase Register Report")
    if "test_stock_summary_report" not in SKIP_TESTS:
        test_stock_summary_report(page)
        print("Completed Test Stock Summary Report")
    if "test_transaction_activity_report" not in SKIP_TESTS:
        test_transaction_activity_report(page)
        print("Completed Test Transaction Activity Report")