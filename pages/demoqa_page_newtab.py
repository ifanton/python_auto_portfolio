from components.components import WebElement
from pages.base_page import BasePage


class BrowserTabPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/browser-windows'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.page_header = WebElement(driver, 'div.pattern-backgound.playgound-header')
        self.btn_new_tab = WebElement(driver, '#tabButton')
