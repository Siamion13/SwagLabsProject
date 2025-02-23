import allure
from base.base_test import BaseTest

class TestLoginPage(BaseTest):

    @allure.feature("Login Functionality")
    def test_correct_login(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.inventory_page.is_opened()

    @allure.feature("Login Functionality")
    def test_incorrect_login(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(self.data.INCORRECT_LOGIN)
        self.login_page.enter_password(self.data.INCORRECT_PASSWORD)
        self.login_page.click_submit_button()
        error_text = self.login_page.verify_error_message()
        assert error_text == "Epic sadface: Username and password do not match any user in this service", \
        f"Error message is not correct, got - '{error_text}'"

    @allure.feature("Login Functionality")
    def test_no_login(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        error_text = self.login_page.verify_error_message()
        assert error_text == "Epic sadface: Username is required", \
        f"Error message is not correct, got - '{error_text}'"

    @allure.feature("Login Functionality")
    def test_no_password(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.click_submit_button()
        error_text = self.login_page.verify_error_message()
        assert error_text == "Epic sadface: Password is required", \
        f"Error message is not correct, got - '{error_text}'"