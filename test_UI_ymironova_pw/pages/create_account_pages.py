from test_UI_ymironova_pw.pages.base_pages import BasePage
from faker import Faker
from test_UI_ymironova_pw.pages.locators import create_account_locators as loc
from playwright.sync_api import expect


class CreateAccount(BasePage):
    page_url = "/customer/account/create/"

    def fill_form(self, same_password=True):
        fake = Faker()
        first_name_field = self.find_id(loc.first_name_loc)
        first_name = fake.first_name()
        first_name_field.fill(first_name)
        last_name_field = self.find_id(loc.last_name_loc)
        last_name = fake.last_name()
        last_name_field.fill(last_name)
        self.page.evaluate("window.scrollTo(0, 500)")
        email_field = self.find_id(loc.email_loc)
        email = fake.email()
        email_field.fill(email)
        password_field = self.find_id(loc.password_loc)
        password = fake.password()
        password_field.fill(password)
        confirm_password_field = self.find_id(loc.confirm_password_loc)
        if same_password:
            confirm_password_field.fill(password)
            button = self.find(loc.create_button_loc)
            button.click()
            return first_name, last_name, email
        else:
            confirm_password_field.fill(fake.password())
            button = self.find(loc.create_button_loc)
            button.click()

    def check_registering_message(self, text):
        greeting_message = self.find(loc.greet_message_loc).nth(0)
        expect(greeting_message).to_have_text(text)

    def check_account_data(self, first_name, last_name, email):
        actual_text = self.find(loc.check_information_loc).text_content().strip()
        name_email = [line.strip() for line in actual_text.splitlines()]
        actual_name = name_email[0]
        actual_email = name_email[1]
        assert f"{first_name} {last_name}" == actual_name
        assert email == actual_email

    def check_error_different_password(self, text):
        error_different_password = self.find(loc.error_different_password_loc)
        expect(error_different_password).to_have_text(text)

    def submit_empty_form(self):
        self.page.evaluate("window.scrollTo(0, 500)")
        button = self.find(loc.create_button_loc)
        button.click()

    def check_required_field_error(self, text):
        expect(self.find_id(loc.error_empty_first_name_loc)).to_have_text(text)
        expect(self.find_id(loc.error_empty_last_name_loc)).to_have_text(text)
        expect(self.find_id(loc.error_empty_email_loc)).to_have_text(text)
        expect(self.find_id(loc.error_empty_password_loc)).to_have_text(text)
        expect(self.find_id(loc.error_empty_confirm_password_loc)).to_have_text(text)
