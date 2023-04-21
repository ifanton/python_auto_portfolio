import time

import allure

from pages.demoqa_page_newtab import BrowserTabPage


@allure.title('new_browser_tab')
@allure.description('Проверка действий с вкладками браузера')
@allure.story('Проверка открытия новой вкладки, переходов между вкладками')
@allure.severity(allure.severity_level.NORMAL)
def test_new_browser_tab(browser):
    browser_tab_page = BrowserTabPage(browser)

    browser_tab_page.visit()
    browser.maximize_window()
    assert len(browser.window_handles) == 1

    browser_tab_page.btn_new_tab.click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)
    assert browser.current_url == 'https://demoqa.com/sample'
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[0])
    assert browser_tab_page.equal_url()
    time.sleep(1)

    browser_tab_page.btn_new_tab.click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[2])
    time.sleep(1)
    assert len(browser.window_handles) == 3
    browser.switch_to.window(browser.window_handles[2])
    browser.close()
    time.sleep(1)

    browser.switch_to.window(browser.window_handles[1])
    browser.close()
    time.sleep(1)

    browser.switch_to.window(browser.window_handles[0])
    browser.set_window_size(1000, 1000)
    time.sleep(2)
