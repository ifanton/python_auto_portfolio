import allure
import time
from pages.demoqa_page_alerts import AlertsPage


@allure.title('alerts')
@allure.description('Проверка функционала всплывающих сообщений')
@allure.story('Действия с всплывающими сообщениями - позитивная')
@allure.severity(allure.severity_level.NORMAL)
def test_alerts(browser):
    alerts_page = AlertsPage(browser)

    alerts_page.visit()
    assert not alerts_page.alert()
    alerts_page.btn_alert.click()
    assert alerts_page.alert()
    assert alerts_page.alert().text == 'You clicked a button'
    time.sleep(1)
    alerts_page.alert().accept()
    assert not alerts_page.alert()
    time.sleep(2)
    alerts_page.btn_alert_confirm.click()
    time.sleep(1)
    assert alerts_page.alert()
    alerts_page.alert().dismiss()
    assert not alerts_page.alert()
    assert alerts_page.text_selection_result.get_text() == 'You selected Cancel'
    alerts_page.btn_alert_confirm.click()
    time.sleep(1)
    alerts_page.alert().accept()
    assert not alerts_page.alert()
    assert alerts_page.text_selection_result.get_text() == 'You selected Ok'
    time.sleep(2)
    alerts_page.btn_alert_prompt.click()
    time.sleep(1)
    assert alerts_page.alert()
    alerts_page.alert().send_keys('Anton')
    time.sleep(1)
    alerts_page.alert().accept()
    assert alerts_page.text_prompt_result.get_text() == 'You entered Anton'
    time.sleep(2)
