from Pages.Login import login
from Pages.Reports.Transaction_activity_report import TransactionActivityReport

def test_transaction_activity_report(page,config_data):
    username = config_data["username"]
    password = config_data["password"]

    try:
        login_page = login(page)
        login_page.perform_login(username, password)
    except:
        print("Logged into IMS")

    transaction_report = TransactionActivityReport(page)
    transaction_report.open_transaction_activity_report()
    transaction_report.run_report()

    print("Transaction Activity Report generated successfully.")