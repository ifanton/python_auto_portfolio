import logging

from components.components import WebElement


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

        self.meta = WebElement(driver, locator='head > meta')

    def visit(self):  # метод перехода на страницу
        return self.driver.get(self.base_url)  # возвращает переход через .get()

    def back(self):   # метод перехода на страницу назад
        self.driver.back()

    def forward(self):   # метод перехода на страницу вперед
        self.driver.forward()

    def refresh(self):  # метод обновления страницы
        self.driver.refresh()

    def get_url(self):  # возвращает текущий URL
        return self.driver.current_url

    def get_title(self):  # возвращает название страницы (вкладки браузера)
        return self.driver.title

    def equal_url(self):  # сравнивает текущий URL с заданной строкой
        if self.get_url() == self.base_url:
            return True
        else:
            return False

    def alert(self):  # проверяет открыто окно алерта или нет, возвращает получение объекта окна
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False
