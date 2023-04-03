from pages.demoqa_page_main import DemoQa
from pages.demoqa_page_elements import ElementsPage
from pages.demoqa_page_form import FormPage
import time


def form_filling(browser):

    demoqa_page = DemoQa()
    elements_page = ElementsPage()
    form_page = FormPage()

    demoqa_page.visit()
    demoqa_page.btn_elements.click_force()
    # assert browser.get_url() == 'https://demoqa.com/elements'
    # elements_page.btn_sidebar_first.click()
    # elements_page.btn_sidebar_second.click()
    # elements_page.btn_sidebar_second_practice_form.click()
    # assert browser.get_url() == 'https://demoqa.com/automation-practice-form'
