from components.components import WebElement
from pages.base_page import BasePage


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.btn_sidebar_first = WebElement(driver, locator='div:nth-child(1) > span > div')
        self.btn_sidebar_second = WebElement(driver, locator='div:nth-child(2) > span > div')
        self.btn_sidebar_second_practice_form = WebElement(driver, locator='div:nth-child(1) > div > ul > li')
