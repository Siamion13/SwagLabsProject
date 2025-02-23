import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):

    PAGE_URL = Links.INVENTORY_PAGE
    FLEECE_JACKET = ("xpath","// div[text() = 'Sauce Labs Fleece Jacket']")
    ADD_TO_CART_FLEECE_JACKET = ("xpath", "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")
    SHOPPING_CART = ("xpath", "//span[@class='shopping_cart_badge']")
    SHOPPING_CART_LINK = ("xpath", "//a[@class='shopping_cart_link']")

    @allure.step("Verify product name")
    def verify_product_name(self):
        product_name = self.wait.until(EC.visibility_of_element_located(self.FLEECE_JACKET))
        return product_name.text

    @allure.step("Add product to cart")
    def add_product_to_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.ADD_TO_CART_FLEECE_JACKET)).click()
        product_quantity = self.wait.until(EC.visibility_of_element_located(self.SHOPPING_CART))
        return product_quantity.text

    @allure.step("Remove product from cart")
    def remove_product_from_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.REMOVE_BUTTON)).click()
        self.wait.until(EC.invisibility_of_element_located(self.SHOPPING_CART))