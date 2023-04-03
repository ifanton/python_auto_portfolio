from pages.base_page import BasePage  # импорт класса из файла base_page.py
from components.components import WebElement


class DemoQa(BasePage):  # родительский класс BasePage из файла base_page.py

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)  # super прокидывает URL в родительский класс
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.icon = WebElement(driver, locator='#app > header > a')
        self.btn_elements = WebElement(driver, locator='#app > div > div > div.home-body > div > div:nth-child(1)')
