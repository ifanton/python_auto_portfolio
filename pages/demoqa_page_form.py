from components.components import WebElement
from pages.base_page import BasePage


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

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
        self.hobbies_sports = WebElement(driver, locator='#hobbies-checkbox-1')
        self.hobbies_reading = WebElement(driver, locator='#hobbies-checkbox-2')
        self.hobbies_music = WebElement(driver, locator='#hobbies-checkbox-3')
        self.btn_upload_photo = WebElement(driver, locator='#uploadPicture')
        self.current_address = WebElement(driver, locator='#currentAddress')
        self.state = WebElement(driver, locator='#react-select-3-input')
        self.city = WebElement(driver, locator='#react-select-4-input')
        self.btn_submit = WebElement(driver, locator='#submit')
        self.modal_dialog = WebElement(driver, locator='body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, locator='#closeLargeModal')
