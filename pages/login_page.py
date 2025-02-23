import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Links.HOST
    USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    SUBMIT_BUTTON =("xpath", "//input[@type='submit']")
    ERROR_MESSAGE =("xpath", "//div[@class='error-message-container error']")

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    @allure.step("Verify error message")
    def verify_error_message(self):
        error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return error_element.text