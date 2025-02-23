import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CheckOutStepTwoPage(BasePage):

    PAGE_URL = Links.CHECKOUT_STEP_TWO_PAGE
    CANCEL_BUTTON = ("xpath", "//button[@class='btn btn_secondary back btn_medium cart_cancel_link']")
    FINISH_BUTTON = ("xpath", "//button[@class='btn btn_action btn_medium cart_button']")
    PAYMENT_INFORMATION_LABEL = ("xpath", "//div[@data-test='payment-info-label']")
    PAYMENT_INFORMATION_VALUE = ("xpath", "//div[@data-test='payment-info-value']")
    SHIPPING_INFORMATION_LABEL = ("xpath", "//div[@data-test='shipping-info-label']")
    SHIPPING_INFORMATION_VALUE = ("xpath", "//div[@data-test='shipping-info-value']")
    PRICE_TOTAL_LABEL = ("xpath", "//div[@data-test='total-info-label']")
    ITEM_TOTAL_LABEL = ("xpath", "//div[@data-test='subtotal-label']")
    TAX_LABEL = ("xpath", "//div[@data-test='tax-label']")
    TOTAL_LABEL = ("xpath","//div[@data-test='total-label']")

    def __init__(self, driver, inventory_page):
        super().__init__(driver)
        self.inventory_page = inventory_page

    @allure.step("Verify product name")
    def verify_product_name(self):
        product_name = self.wait.until(EC.visibility_of_element_located(self.inventory_page.FLEECE_JACKET))
        return product_name.text

    @allure.step("Verify payment information")
    def verify_payment_information(self):
        self.wait.until(EC.visibility_of_element_located(self.PAYMENT_INFORMATION_LABEL))
        payment_info = self.wait.until(EC.visibility_of_element_located(self.PAYMENT_INFORMATION_VALUE))
        return payment_info.text

    @allure.step("Verify shipping information")
    def verify_shipping_information(self):
        self.wait.until(EC.visibility_of_element_located(self.SHIPPING_INFORMATION_LABEL))
        shipping_info = self.wait.until(EC.visibility_of_element_located(self.SHIPPING_INFORMATION_VALUE))
        return shipping_info.text

    @allure.step("Click Cancel button")
    def click_cancel_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCEL_BUTTON)).click()

    @allure.step("Click Finish button")
    def click_continue_button(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()




