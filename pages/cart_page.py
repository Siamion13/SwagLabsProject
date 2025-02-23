import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):

    PAGE_URL = Links.CART_PAGE
    CONTINUE_SHOPPING_BUTTON = ("xpath","//button[@id='continue-shopping']")
    CHECKOUT_BUTTON = ("xpath", "//button[@id='checkout']")
    CART_ITEM = ("xpath", "//div[@class='inventory_item_name']")
    CART_ITEM_PRICE = ("xpath", "//div[@class='inventory_item_price']")
    REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")


    def __init__(self, driver, inventory_page):
        super().__init__(driver)
        self.inventory_page = inventory_page

    @allure.step("Verify cart item is visible")
    def verify_cart_item_is_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.CART_ITEM))

    @allure.step("Verify product could be removed from cart")
    def verify_product_is_removed_from_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.REMOVE_BUTTON)).click()
        self.wait.until(EC.invisibility_of_element_located(self.CART_ITEM))

    @allure.step("Add product to cart from inventory page")
    def add_product_to_cart(self):
        return self.inventory_page.add_product_to_cart()

    @allure.step("Navigate to cart page")
    def go_to_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.inventory_page.SHOPPING_CART_LINK)).click()

    @allure.step("Click continue shopping button")
    def click_continue_shopping_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)).click()

    @allure.step("Navigate to checkout page")
    def go_to_checkout_page(self):
        self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_BUTTON)).click()