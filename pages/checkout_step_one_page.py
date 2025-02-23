import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CheckOutStepOnePage(BasePage):

    PAGE_URL = Links.CHECKOUT_STEP_ONE_PAGE
    FIRST_NAME = ("xpath","//input[@name='firstName']")
    LAST_NAME = ("xpath", "//input[@name='lastName']")
    ZIP_POSTAL_CODE = ("xpath", "//input[@name='postalCode']")
    ERROR_MESSAGE = ("xpath", "//div[@class='error-message-container error']")
    CANCEL_BUTTON = ("xpath", "//button[@class='btn btn_secondary back btn_medium cart_cancel_link']")
    CONTINUE_BUTTON = ("xpath", "//input[@class='submit-button btn btn_primary cart_button btn_action']")

    @allure.step("Enter First Name")
    def enter_first_name(self):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME)).send_keys("Test First Name")

    @allure.step("Enter Last Name")
    def enter_last_name(self):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME)).send_keys("Test Last Name")

    @allure.step("Enter Zip/Postal Code")
    def enter_zip_postal_code(self):
        self.wait.until(EC.element_to_be_clickable(self.ZIP_POSTAL_CODE)).send_keys("12345")

    @allure.step("Click Continue button")
    def click_continue_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    @allure.step("Click Cancel button")
    def click_cancel_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCEL_BUTTON)).click()

    @allure.step("Verify error message")
    def verify_error_message(self):
        error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return error_element.text