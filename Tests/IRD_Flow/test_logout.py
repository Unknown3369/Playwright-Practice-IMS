import time

from Pages.Logout import logout
from Pages.Login import login

def test_logout(page, config_data):
    username = config_data["username"]
    password = config_data["password"]

    try:
        login_page = login(page)
        login_page.perform_login(username, password)
    except:
        print('already logged in')
    logout_page = logout(page)
    time.sleep(2)
    logout_page.perform_logout()
    print('loggedout sucessfully')

    time.sleep(10)