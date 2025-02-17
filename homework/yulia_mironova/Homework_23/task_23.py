from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--force-device-scale-factor=0.8")
    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.maximize_window()
    return chrome_driver


def test_one(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    data = 'something'
    text_string.send_keys(data)
    text_string.submit()
    input_string = driver.find_element(By.CLASS_NAME, 'result-text')
    print(input_string.text)


def test_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys('Masha')
    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys('Ivanova')
    email_string = driver.find_element(By.CSS_SELECTOR, '[placeholder ="name@example.com" ]')
    email_string.send_keys('MashaMilasha@mail.ru')
    gender = driver.find_element(By.CSS_SELECTOR, '[for = "gender-radio-2"]')
    gender.click()
    number = driver.find_element(By.CSS_SELECTOR, '[placeholder = "Mobile Number"]')
    number.send_keys('1234567890')
    date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth.click()
    select_month = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select')
    dropdown_month = Select(select_month)
    dropdown_month.select_by_value('8')
    select_year = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select')
    dropdown_year = Select(select_year)
    dropdown_year.select_by_value('1999')
    date = driver.find_element(By.CSS_SELECTOR, '[aria-label = "Choose Monday, September 6th, 1999"]')
    date.click()
    subject_1 = driver.find_element(By.CSS_SELECTOR, '.subjects-auto-complete__control.css-yk16xz-control')
    subject_1.click()
    subject_2 = driver.find_element(By.CSS_SELECTOR, '.subjects-auto-complete__control input[type="text"]')
    subject_2.send_keys('Maths')
    subject_ok = driver.find_element(By.CSS_SELECTOR, '.subjects-auto-complete__menu')
    subject_ok.click()
    hobby = driver.find_element(By.CSS_SELECTOR, '[for ="hobbies-checkbox-3"]')
    hobby.click()
    address = driver.find_element(By.CSS_SELECTOR, '[placeholder = "Current Address"]')
    address.send_keys('Moscow, Lenina 47A')
    state = driver.find_element(By.CSS_SELECTOR, '#state .css-yk16xz-control .css-1hwfws3')
    state.click()
    input_state = driver.find_element(By.ID, 'react-select-3-input')
    input_state.send_keys('Uttar Pradesh')
    state_ok = driver.find_element(By.CLASS_NAME, 'css-26l3qy-menu')
    state_ok.click()
    city = driver.find_element(By.CSS_SELECTOR, '#city .css-yk16xz-control .css-1hwfws3')
    city.click()
    input_city = driver.find_element(By.ID, 'react-select-4-input')
    input_city.send_keys('Merrut')
    city_ok = driver.find_element(By.CLASS_NAME, 'css-26l3qy-menu')
    city_ok.click()
    submit = driver.find_element(By.ID, 'submit')
    submit.submit()

    name_value = driver.find_element(By.XPATH, '//td [text()="Student Name"]/following-sibling::td')
    print(name_value.text)
    email_value = driver.find_element(By.XPATH, '//td [text()="Student Email"]/following-sibling::td')
    print(email_value.text)
    gender_value = driver.find_element(By.XPATH, '//td [text()="Gender"]/following-sibling::td')
    print(gender_value.text)
    mobile_value = driver.find_element(By.XPATH, '//td [text()="Mobile"]/following-sibling::td')
    print(mobile_value.text)
    birthday_value = driver.find_element(By.XPATH, '//td [text()="Date of Birth"]/following-sibling::td')
    print(birthday_value.text)
    subjects_value = driver.find_element(By.XPATH, '//td [text()="Subjects"]/following-sibling::td')
    print(subjects_value.text)
    hobby_value = driver.find_element(By.XPATH, '//td [text()="Hobbies"]/following-sibling::td')
    print(hobby_value.text)
    address_value = driver.find_element(By.XPATH, '//td [text()="Address"]/following-sibling::td')
    print(address_value.text)
    state_city_value = driver.find_element(By.XPATH, '//td [text()="State and City"]/following-sibling::td')
    print(state_city_value.text)


def test_select(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    language = driver.find_element(By.CSS_SELECTOR, 'select[name ="choose_language"]')
    select_language = Select(language)
    select_language.select_by_value('1')
    value = driver.find_element(By.CSS_SELECTOR, 'option[value ="1"]').text
    language.submit()
    assert value == driver.find_element(By.ID, 'result-text').text


def test_loading(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button = driver.find_element(By.XPATH, '//button')
    button.click()
    WebDriverWait(driver, 5).until(
        ec.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="finish"]/child::h4'),
            'Hello World!'
        )
    )
