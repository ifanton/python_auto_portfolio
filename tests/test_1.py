from selenium.webdriver import Keys

from pages.demoqa_page_main import DemoQa
from pages.demoqa_page_elements import ElementsPage
from pages.demoqa_page_form import FormPage

import time
import allure


@allure.title('registration_form')
@allure.description('Проверка функционала регистрационной формы')
@allure.story('Заполнение регистрационной формы - позитивная')
@allure.severity(allure.severity_level.NORMAL)
def test_form_filling(browser):
    demoqa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    form_page = FormPage(browser)

    demoqa_page.visit()
    demoqa_page.btn_elements.click_force()
    assert demoqa_page.get_url() == 'https://demoqa.com/elements'
    time.sleep(1)
    elements_page.btn_sidebar_first.click()
    time.sleep(1)
    elements_page.btn_sidebar_second.click()
    time.sleep(1)
    elements_page.btn_sidebar_second_practice_form.click()
    assert elements_page.get_url() == 'https://demoqa.com/automation-practice-form'
    assert form_page.icon.exist()
    assert form_page.header.get_text() == 'Practice Form'
    assert form_page.first_Name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.first_Name.get_dom_attribute('type') == 'text'
    assert form_page.first_Name.get_dom_attribute('id') == 'firstName'
    form_page.first_Name.send_keys('Anton')
    # time.sleep(1)
    assert form_page.last_Name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.last_Name.get_dom_attribute('type') == 'text'
    assert form_page.last_Name.get_dom_attribute('id') == 'lastName'
    form_page.last_Name.send_keys('Panteleev')
    # time.sleep(1)
    assert form_page.email.get_dom_attribute('placeholder') == 'name@example.com'
    assert form_page.email.get_dom_attribute('type') == 'text'
    assert form_page.email.get_dom_attribute('id') == 'userEmail'
    assert form_page.email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    form_page.email.send_keys('mail@email.com')
    # time.sleep(1)
    form_page.gender_other.click()
    form_page.gender_female.click()
    form_page.gender_male.click()
    # time.sleep(1)
    assert form_page.mobile.get_dom_attribute('placeholder') == 'Mobile Number'
    assert form_page.mobile.get_dom_attribute('type') == 'text'
    assert form_page.mobile.get_dom_attribute('id') == 'userNumber'
    assert form_page.mobile.get_dom_attribute('pattern') == '\d*'
    assert form_page.mobile.get_dom_attribute('minlength') == '10'
    assert form_page.mobile.get_dom_attribute('maxlength') == '10'
    form_page.mobile.send_keys('1234567890')
    # time.sleep(1)
    assert form_page.birthday.get_dom_attribute('type') == 'text'
    assert form_page.birthday.get_dom_attribute('id') == 'dateOfBirthInput'
    form_page.birthday.click()
    form_page.birthday.send_keys(Keys.SHIFT + Keys.HOME)
    form_page.birthday.send_keys('27 May 1703')
    form_page.birthday.send_keys(Keys.ENTER)
    # time.sleep(1)
    assert form_page.subject.get_dom_attribute('type') == 'text'
    assert form_page.subject.get_dom_attribute('id') == 'subjectsInput'
    form_page.subject.send_keys('M')
    form_page.subject.send_keys(Keys.ENTER)
    form_page.subject.send_keys('A')
    form_page.subject.send_keys(Keys.ENTER)
    form_page.subject.send_keys('A')
    form_page.subject.send_keys(Keys.ENTER)
    form_page.subject.send_keys('So')
    form_page.subject.send_keys(Keys.ENTER)
    form_page.subject.send_keys('En')
    form_page.subject.send_keys(Keys.ENTER)
    # time.sleep(1)
    assert form_page.subject_clear.exist()
    form_page.subject_clear.click()
    form_page.subject.send_keys('M')
    form_page.subject.send_keys(Keys.ENTER)
    # time.sleep(1)
    form_page.hobbies_sports.click_force()
    form_page.hobbies_reading.click_force()
    form_page.hobbies_music.click_force()
    # time.sleep(1)
    assert form_page.btn_upload_photo.exist()
    assert form_page.btn_upload_photo.get_dom_attribute('type') == 'file'
    assert form_page.btn_upload_photo.get_dom_attribute('id') == 'uploadPicture'
    form_page.current_address.scroll_to_element()
    assert form_page.current_address.get_dom_attribute('placeholder') == 'Current Address'
    assert form_page.current_address.get_dom_attribute('id') == 'currentAddress'
    form_page.current_address.send_keys('Delhi, India')
    # time.sleep(1)
    form_page.state.click_force()
    form_page.state.send_keys(Keys.ARROW_DOWN)
    form_page.state.send_keys(Keys.ENTER)
    # time.sleep(1)
    form_page.city.click_force()
    form_page.city.send_keys(Keys.ARROW_DOWN)
    form_page.city.send_keys(Keys.ENTER)
    # time.sleep(1)
    form_page.btn_submit.click_force()
    assert form_page.modal_dialog.exist()
    assert form_page.modal_dialog_header.get_text() == 'Thanks for submitting the form'
    assert form_page.modal_dialog_name.get_text() == 'Anton Panteleev'
    assert form_page.modal_dialog_email.get_text() == 'mail@email.com'
    assert form_page.modal_dialog_gender.get_text() == 'Male'
    assert form_page.modal_dialog_mobile.get_text() == '1234567890'
    assert form_page.modal_dialog_birthday.get_text() == '27 May,1703'
    assert form_page.modal_dialog_subjects.get_text() == 'Maths'
    assert form_page.modal_dialog_hobbies.get_text() == 'Sports, Reading, Music'
    assert form_page.modal_dialog_picture.get_text() == ''
    assert form_page.modal_dialog_address.get_text() == 'Delhi, India'
    assert form_page.modal_dialog_state_and_city.get_text() == 'NCR Delhi'
    assert form_page.form.get_dom_attribute('class') == 'was-validated'
    # time.sleep(5)
    form_page.btn_close_modal.click_force()
    assert not form_page.modal_dialog.exist()
    # time.sleep(1)
