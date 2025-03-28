from playwright.sync_api import Page


def test_get_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    username = page.get_by_role('textbox', name='username')
    username.fill('tomsmith')
    password = page.get_by_role('textbox', name='password')
    password.fill('SuperSecretPassword!')
    page.get_by_role('button').click()


def test_fill_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Masha')
    page.get_by_placeholder('Last Name').fill('Ivanova')
    page.get_by_placeholder('name@example.com').fill('MashaMilasha@mail.ru')
    page.locator('[for = "gender-radio-2"]').click()
    page.get_by_role('textbox', name='Mobile Number').fill('1234567890')
    page.locator('#dateOfBirthInput').click()
    page.locator('.react-datepicker__month-select').select_option('2')
    page.locator('.react-datepicker__year-select').select_option('1998')
    page.get_by_role('option', name='Choose Tuesday, March 17th, 1998').click()
    page.locator('.subjects-auto-complete__control.css-yk16xz-control').click()
    page.locator('.subjects-auto-complete__control input[type="text"]').fill('Maths')
    page.locator('.subjects-auto-complete__menu').click()
    page.locator('[for="hobbies-checkbox-1"]').click()
    page.get_by_placeholder('Current Address').fill('Moscow, Lenina 47A')
    page.locator('#state .css-yk16xz-control .css-1hwfws3').click()
    page.locator('#react-select-3-input').fill('Uttar Pradesh')
    page.locator('.css-26l3qy-menu').click()
    page.locator('#city .css-yk16xz-control .css-1hwfws3').click()
    page.locator('#react-select-4-input').fill('Merrut')
    page.locator('.css-26l3qy-menu').click()
    page.get_by_role('button').click()
