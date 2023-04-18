from components.components import WebElement
from pages.base_page import BasePage


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.icon = WebElement(driver, 'header > a > img')
        self.header = WebElement(driver, 'div.pattern-backgound.playgound-header')
        self.form = WebElement(driver, locator='#userForm')
        self.first_Name = WebElement(driver, locator='#firstName')
        self.last_Name = WebElement(driver, locator='#lastName')
        self.email = WebElement(driver, locator='#userEmail')
        self.gender_male = WebElement(driver, locator='#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)')
        self.gender_female = WebElement(driver, locator='#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(2)')
        self.gender_other = WebElement(driver, locator='#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(3)')
        self.mobile = WebElement(driver, locator='#userNumber')
        self.birthday = WebElement(driver, locator='#dateOfBirthInput')
        self.subject = WebElement(driver, locator='#subjectsInput')
        self.subject_clear = WebElement(driver, 'div.subjects-auto-complete__indicators.css-1wy0on6')
        self.hobbies_sports = WebElement(driver, locator='#hobbies-checkbox-1')
        self.hobbies_reading = WebElement(driver, locator='#hobbies-checkbox-2')
        self.hobbies_music = WebElement(driver, locator='#hobbies-checkbox-3')
        self.btn_upload_photo = WebElement(driver, locator='#uploadPicture')
        self.current_address = WebElement(driver, locator='#currentAddress')
        self.state = WebElement(driver, locator='#react-select-3-input')
        self.city = WebElement(driver, locator='#react-select-4-input')
        self.btn_submit = WebElement(driver, locator='#submit')
        self.modal_dialog = WebElement(driver, locator='body > div.fade.modal.show > div')
        self.modal_dialog_header = WebElement(driver, '#example-modal-sizes-title-lg')
        self.modal_dialog_name = WebElement(driver, 'tr:nth-child(1) > td:nth-child(2)')
        self.modal_dialog_email = WebElement(driver, 'tr:nth-child(2) > td:nth-child(2)')
        self.modal_dialog_gender = WebElement(driver, 'tr:nth-child(3) > td:nth-child(2)')
        self.modal_dialog_mobile = WebElement(driver, 'tr:nth-child(4) > td:nth-child(2)')
        self.modal_dialog_birthday = WebElement(driver, 'tr:nth-child(5) > td:nth-child(2)')
        self.modal_dialog_subjects = WebElement(driver, 'tr:nth-child(6) > td:nth-child(2)')
        self.modal_dialog_hobbies = WebElement(driver, 'tr:nth-child(7) > td:nth-child(2)')
        self.modal_dialog_picture = WebElement(driver, 'tr:nth-child(8) > td:nth-child(2)')
        self.modal_dialog_address = WebElement(driver, 'tr:nth-child(9) > td:nth-child(2)')
        self.modal_dialog_state_and_city = WebElement(driver, 'tr:nth-child(10) > td:nth-child(2)')
        self.btn_close_modal = WebElement(driver, locator='#closeLargeModal')
