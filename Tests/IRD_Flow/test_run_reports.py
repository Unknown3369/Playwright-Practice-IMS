from Pages.Login import login
from Pages.Reports.Materialized_View import MaterializedViewReportPage
from Pages.Reports.Credit_note_report import CreditNoteBookReportPage
from Pages.Reports.Debit_note_report import DebitNoteBookReportPage
from Pages.Reports.Vat_sales_register_report import VatSalesRegisterReportPage
from Pages.Reports.Vat_purchase_register_report import VatPurchaseRegisterReportPage
from Pages.Reports.Stock_summary_report import StockSummaryReport
import time


def test_print_all_final_reports(page, config_data):
    username = config_data["username"]
    password = config_data["password"]

#----------------------------------------------------------------------------------
    login_page = login(page)
    materialized_view_report_page = MaterializedViewReportPage(page)

    try:
        login_page.perform_login(username, password)
    except:
        print("Logged into IMS")

    materialized_view_report_page.generate_materialized_view_report()
    materialized_view_report_page.download_materialized_view_report()
    print("Materialized View Report generated successfully.")
    time.sleep(2)

#----------------------------------------------------------------------------------
    credit_report_page = CreditNoteBookReportPage(page)
    credit_report_page.generate_credit_note_book_report()
    credit_report_page.download_credit_note_report()
    print("Credit Note Book Report generated successfully.")
    time.sleep(2)

#----------------------------------------------------------------------------------
    debit_report_page = DebitNoteBookReportPage(page)
    debit_report_page.generate_debit_note_book_report()
    debit_report_page.download_debit_note_report()
    print("Debit Note Book Report generated successfully.")
    time.sleep(2)

#----------------------------------------------------------------------------------
    vat_sales_report = VatSalesRegisterReportPage(page)
    vat_sales_report.generate_vat_sales_register_report()
    vat_sales_report.download_vat_sales_report()
    print("VAT Sales Register Report generated successfully.")
    time.sleep(2)

#----------------------------------------------------------------------------------
    vat_purchase_report = VatPurchaseRegisterReportPage(page)
    vat_purchase_report.generate_vat_purchase_register_report()
    vat_purchase_report.download_vat_purchase_report()
    print("Vat Purchase Register Report generated successfully.") 
    time.sleep(2) 

#----------------------------------------------------------------------------------
    stock_report = StockSummaryReport(page)
    stock_report.open_stock_summary_report()
    stock_report.run_report()
    stock_report.download_stock_summary_report()

    print("Stock Summary Report generated successfully.")
    time.sleep(2)
