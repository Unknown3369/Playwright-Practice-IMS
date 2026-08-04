from playwright.sync_api import Page, expect
import time

class logout:
    def __init__(self, page: Page):
        self.page = page
        self.logout_link = "svg[data-icon='caret-down']"
        self.logout_button = "a[title='log out']"

    def perform_logout(self):
        self.page.locator(self.logout_link).click()
        self.page.locator(self.logout_button).wait_for(state="visible", timeout=10000)
        self.page.locator(self.logout_button).click()
        print('logout clicked')
        self.page.on("dialog", lambda dialog: dialog.accept())
        print('popup handled')
        time.sleep(2)
