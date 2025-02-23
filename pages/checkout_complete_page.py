import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CheckOutCompletePage(BasePage):

    PAGE_URL = Links.CHECKOUT_COMPLETE_PAGE
    CHECKOUT_COMPLETE_IMAGE = ("xpath", "//img[@class='pony_express']")
    CHECKOUT_COMPLETE_HEADER = ("xpath", "//h2[@class='complete-header']")
    CHECKOUT_COMPLETE_SUB_HEADER = ("xpath", "//div[@class ='complete-text']")
    BACK_HOME_BUTTON = ("xpath", "//button[@id='back-to-products']")

    def __init__(self, driver, inventory_page):
        super().__init__(driver)
        self.inventory_page = inventory_page

    @allure.step("Verify checkout_complete_image")
    def verify_checkout_complete_image(self):
        self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_COMPLETE_IMAGE))

    @allure.step("Verify checkout_complete_header")
    def verify_checkout_complete_header(self):
        header = self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_COMPLETE_HEADER))
        return header.text

    @allure.step("Verify checkout_complete_sub_header")
    def verify_checkout_complete_sub_header(self):
        sub_header = self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_COMPLETE_SUB_HEADER))
        return sub_header.text

    @allure.step("Navigate to home page")
    def navigate_to_home_page(self):
        self.wait.until(EC.visibility_of_element_located(self.BACK_HOME_BUTTON)).click()


