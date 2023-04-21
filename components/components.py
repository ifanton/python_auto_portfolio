from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class WebElement:

    def __init__(self, driver, locator='', text='', locator_type='css'):
        self.driver = driver
        self.text = text
        self.locator = locator
        self.locator_type = locator_type

    def find_element(self):  # поиск элемента
        return self.driver.find_element(self.get_by_type(), self.locator)  # возвращает поиск через метод get_by_type

    def find_elements(self):  # поиск сразу нескольких элементов
        return self.driver.find_elements(self.get_by_type(), self.locator)  # возвращает поиск через метод get_by_type

    def click(self):  # клик по элементу
        self.find_element().click()

    def click_force(self):  # форс-клик сквозь все слои страницы (даже по скрытому элементу)
        self.driver.execute_script('arguments[0].click();', self.find_element())

    def check_count_elements(self, count: int):
        if len(self.find_elements()) == count:
            return True
        return False

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def equal_text(self):
        if self.get_text() == self.text:
            return True
        return False

    def visible(self):  # проверка видимости элемента на странице
        return self.find_element().is_displayed()

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + 'a')
        self.find_element().send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def get_by_type(self):  # метод для определения типа локатора
        if self.locator_type == 'id':
            return By.ID
        if self.locator_type == 'name':
            return By.NAME
        if self.locator_type == 'xpath':
            return By.XPATH
        if self.locator_type == 'css':
            return By.CSS_SELECTOR
        if self.locator_type == 'class':
            return By.CLASS_NAME
        if self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print('Locator type ' + self.locator_type + ' not correct!')
        return False

    def scroll_to_element(self):  # прокрутка страницы до элемента
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", self.find_element())

    def check_css(self, style, value=''):  # возвращает True, если у эл-та есть стиль с указанным значением
        return self.find_element().value_of_css_property(style) == value
