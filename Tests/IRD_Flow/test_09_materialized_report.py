import pytest

from Pages.Login import login
from Pages.Reports.Materialized_View import MaterializedViewReportPage



def test_materialized_view_report(page,config_data):
    username = config_data["username"]
    password = config_data["password"]
    
    try:
        login_page = login(page)
        login_page.perform_login(username, password)
    except:
        print('Already logged In')


    materialized_view_report = MaterializedViewReportPage(page)
    materialized_view_report.generate_materialized_view_report()
    materialized_view_report.download_materialized_view_report()

    print("Materialized View Report generated successfully.")
