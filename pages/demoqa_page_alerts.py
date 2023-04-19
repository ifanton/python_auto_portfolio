from components.components import WebElement
from pages.base_page import BasePage


class AlertsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.btn_alert = WebElement(driver, locator='#alertButton')
        self.btn_5sec_alert = WebElement(driver, locator='#timerAlertButton')
        self.btn_alert_confirm = WebElement(driver, locator='#confirmButton')
        self.btn_alert_prompt = WebElement(driver, locator='#promtButton')
        self.text_selection_result = WebElement(driver, locator='#confirmResult')
        self.text_prompt_result = WebElement(driver, locator='#promptResult')
