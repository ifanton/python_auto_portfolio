import time

import allure

from pages.demoqa_page_droppable import DroppablePage
from selenium.webdriver import ActionChains  # импорт библиотеки для выполнения low level interactions


@allure.title('drag_n_drop')
@allure.description('Проверка функционала drag`n`drop')
@allure.story('Различные варианты взаимодействия drag`n`drop элементов')
@allure.severity(allure.severity_level.NORMAL)
def test_drag_n_drop(browser):
    droppable_page = DroppablePage(browser)
    action_chains = ActionChains(browser)   # создание объекта для выполнения действия drag`n`drop

    droppable_page.visit()
    assert droppable_page.page_header.get_text() == 'Droppable'
    assert droppable_page.droppable_element.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    action_chains.drag_and_drop(
        droppable_page.draggable_element.find_element(),  # element
        droppable_page.droppable_element.find_element()   # target
    ).perform()
    assert droppable_page.droppable_element.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    assert droppable_page.droppable_element.get_text() == 'Dropped!'
    action_chains.drag_and_drop_by_offset(droppable_page.draggable_element.find_element(), -150, 0).perform()
    assert droppable_page.droppable_element.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    time.sleep(2)
    droppable_page.page_tab_accept.click()
    assert droppable_page.accept_droppable_element.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    action_chains.drag_and_drop(
        droppable_page.not_acceptable_element.find_element(),
        droppable_page.accept_droppable_element.find_element()
    ).perform()
    assert droppable_page.accept_droppable_element.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    assert not droppable_page.accept_droppable_element.get_text() == 'Dropped!'
    action_chains.drag_and_drop_by_offset(droppable_page.not_acceptable_element.find_element(), -150, 0).perform()
    time.sleep(1)
    action_chains.drag_and_drop(
        droppable_page.acceptable_element.find_element(),
        droppable_page.accept_droppable_element.find_element()
    ).perform()
    assert droppable_page.accept_droppable_element.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    assert droppable_page.accept_droppable_element.get_text() == 'Dropped!'
    time.sleep(2)
    droppable_page.page_tab_prevent.click()
    assert droppable_page.not_greedy_drop_box_inner.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    assert droppable_page.not_greedy_drop_box_outer.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    assert droppable_page.greedy_drop_box_inner.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    assert droppable_page.greedy_drop_box_outer.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    time.sleep(2)
    action_chains.drag_and_drop(
         droppable_page.drag_box.find_element(),
         droppable_page.not_greedy_drop_box_inner.find_element()
    ).perform()
    assert droppable_page.not_greedy_drop_box_inner.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    assert droppable_page.not_greedy_drop_box_outer.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    time.sleep(2)
    action_chains.drag_and_drop(
         droppable_page.drag_box.find_element(),
         droppable_page.greedy_drop_box_inner.find_element()
    ).perform()
    assert droppable_page.greedy_drop_box_inner.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    assert droppable_page.greedy_drop_box_outer.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    time.sleep(2)
    droppable_page.page_tab_revert.click()
    assert droppable_page.revert_droppable_element.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    action_chains.drag_and_drop(
        droppable_page.revertable_element.find_element(),
        droppable_page.revert_droppable_element.find_element()
    ).perform()
    time.sleep(2)
    action_chains.drag_and_drop(
        droppable_page.not_revertable_element.find_element(),
        droppable_page.revert_droppable_element.find_element()
    ).perform()
    assert droppable_page.revertable_element.get_dom_attribute('style') == 'position: relative; left: 0px; top: 0px;'
    assert droppable_page.not_revertable_element.get_dom_attribute('style') == 'position: relative; left: 200px; top: -17px;'
    time.sleep(2)
