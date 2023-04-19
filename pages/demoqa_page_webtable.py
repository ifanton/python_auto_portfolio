from components.components import WebElement
from pages.base_page import BasePage


class WebtablePage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.btn_add = WebElement(driver, locator='#addNewRecordButton')
        self.modal_window = WebElement(driver, locator='div.fade.modal.show')
        self.modal_window_user_form = WebElement(driver, locator='#userForm')
        self.modal_window_first_name = WebElement(driver, locator='#firstName')
        self.modal_window_last_name = WebElement(driver, locator='#lastName')
        self.modal_window_email = WebElement(driver, locator='#userEmail')
        self.modal_window_age = WebElement(driver, locator='#age')
        self.modal_window_salary = WebElement(driver, locator='#salary')
        self.modal_window_department = WebElement(driver, locator='#department')
        self.modal_window_btn_submit = WebElement(driver, locator='#submit')
        self.modal_window_btn_close = WebElement(driver, 'div.modal-header > button > span:nth-child(1)')
        self.table_pencil_4 = WebElement(driver, locator='#edit-record-4')
        self.table_bin_4 = WebElement(driver, locator='#delete-record-4')
        self.table_name = WebElement(driver, locator='div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.table_no_elements = WebElement(driver, locator='div.rt-noData')
        self.table_bin = WebElement(driver, locator='[title="Delete"]')
        self.table_size_selector = WebElement(driver, locator='span.select-wrap.-pageSizeOptions > select')
        self.table_nav_btn_previous = WebElement(driver, locator='div.-previous > button')
        self.table_nav_btn_next = WebElement(driver, locator='div.-next > button')
        self.table_nav_page_counter = WebElement(driver, locator='span.-pageInfo > span')
        self.table_nav_page_index = WebElement(driver, locator='input[type=number]')
        self.table_header_any = WebElement(driver, locator='div.rt-thead.-header > div > div')  # 7 столбцов
        self.table_header_firstName = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(1)')
        self.table_header_LastName = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(2)')
