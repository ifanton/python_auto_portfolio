import time

import allure
from selenium.webdriver import Keys

from pages.demoqa_page_webtable import WebtablePage


@allure.title('web_table')
@allure.description('Проверка функционала таблиц')
@allure.story('Добавление, изменение и удаление записей в таблице - позитивный')
@allure.severity(allure.severity_level.NORMAL)
def test_webtable(browser):
    webtable_page = WebtablePage(browser)

    webtable_page.visit()
    webtable_page.table_size_selector.scroll_to_element()
    webtable_page.table_size_selector.click_force()
    webtable_page.table_size_selector.send_keys(Keys.ARROW_UP)
    webtable_page.table_size_selector.send_keys(Keys.ENTER)
    webtable_page.table_nav_btn_previous.click()
    webtable_page.table_nav_btn_next.click()
    assert webtable_page.table_nav_page_index.get_dom_attribute('value') == '1'
    assert webtable_page.table_nav_btn_previous.get_dom_attribute('disabled')
    assert webtable_page.table_nav_btn_next.get_dom_attribute('disabled')
    time.sleep(1)
    webtable_page.btn_add.click()
    assert webtable_page.modal_window.visible()
    webtable_page.modal_window_btn_submit.click()
    assert webtable_page.modal_window_user_form.get_dom_attribute('class') == 'was-validated'
    time.sleep(1)
    webtable_page.modal_window_btn_close.click()
    time.sleep(1)
    for i in range(1, 4):
        webtable_page.btn_add.click()
        webtable_page.modal_window_first_name.send_keys('Anton')
        webtable_page.modal_window_last_name.send_keys('Panteleev')
        webtable_page.modal_window_email.send_keys('email@email.com')
        webtable_page.modal_window_age.send_keys('37')
        webtable_page.modal_window_salary.send_keys('100000')
        webtable_page.modal_window_department.send_keys('QA')
        webtable_page.modal_window_btn_submit.click()
        time.sleep(1)
    assert not webtable_page.modal_window.exist()
    assert webtable_page.table_nav_page_counter.get_text() == '2'
    assert not webtable_page.table_nav_btn_next.get_dom_attribute('disabled')
    webtable_page.table_nav_btn_next.click()
    time.sleep(1)
    assert webtable_page.table_nav_page_index.get_dom_attribute('value') == '2'
    webtable_page.table_nav_btn_previous.click()
    time.sleep(1)
    assert webtable_page.table_nav_page_index.get_dom_attribute('value') == '1'
    assert not webtable_page.table_no_elements.exist()
    while webtable_page.table_bin.exist():
        webtable_page.table_bin.click_force()
        time.sleep(1)
    assert webtable_page.table_no_elements.visible()
    time.sleep(3)
