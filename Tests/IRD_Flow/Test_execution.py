from playwright.sync_api import sync_playwright

from Tests.IRD_Flow.test_01_Login import test_login_to_ims
from Tests.IRD_Flow.test_02_add_product_group import test_add_product_group_master
from Tests.IRD_Flow.test_03_add_prod import test_add_prod
from Tests.IRD_Flow.test_04_add_customer import test_add_customer
from Tests.IRD_Flow.test_04_add_vendor import test_create_vendor
from Tests.IRD_Flow.test_05_purchase_invoice import test_purchase_invoice
from Tests.IRD_Flow.test_06_purchase_book_report import test_purchase_book_report
from Tests.IRD_Flow.test_07_abbv_invoice import test_abbv_invoice
from Tests.IRD_Flow.test_07_sales_invoice import test_sales_invoice
from Tests.IRD_Flow.test_08_sales_book_report import test_sales_book_report
from Tests.IRD_Flow.test_09_materialized_report import test_materialized_view_report
from Tests.IRD_Flow.test_10_credit_note import test_generate_credit_note
from Tests.IRD_Flow.test_11_vat_sales_register_report import test_vat_sales_register_report
from Tests.IRD_Flow.test_14_debit_note import test_debit_note
from Tests.IRD_Flow.test_16_vat_purchase_report import test_vat_purchase_register_report


def test_ird_flow(page):
    test_login_to_ims(page)
    test_add_product_group_master(page)
    test_add_prod(page)
    test_add_customer(page)
    test_create_vendor(page)
    test_purchase_invoice(page)
    test_purchase_book_report(page)
    test_abbv_invoice(page)
    test_sales_invoice(page)
    test_sales_book_report(page)
    test_materialized_view_report(page)
    test_generate_credit_note(page)
    test_materialized_view_report(page)
    test_vat_sales_register_report(page)
    test_debit_note(page)
    test_vat_purchase_register_report(page)