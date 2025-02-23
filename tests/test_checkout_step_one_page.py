import allure
from base.base_test import BaseTest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

class TestCheckOutStepOnePage(BaseTest):

    @allure.feature("Check Out Step One Functionality")
    def test_correct_information(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        cart_page.go_to_checkout_page()
        self.checkout_step_one_page.enter_first_name()
        self.checkout_step_one_page.enter_last_name()
        self.checkout_step_one_page.enter_zip_postal_code()
        self.checkout_step_one_page.click_continue_button()
        self.checkout_step_two_page.is_opened()

    @allure.feature("Check Out Step One Functionality")
    def test_no_information(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        cart_page.go_to_checkout_page()
        self.checkout_step_one_page.click_continue_button()
        error_text = self.checkout_step_one_page.verify_error_message()
        assert error_text == "Error: First Name is required", \
            f"Error message is not correct, got - '{error_text}'"

    @allure.feature("Check Out Step One Functionality")
    def test_no_last_name_and_zip_code(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        cart_page.go_to_checkout_page()
        self.checkout_step_one_page.enter_first_name()
        self.checkout_step_one_page.click_continue_button()
        error_text = self.checkout_step_one_page.verify_error_message()
        assert error_text == "Error: Last Name is required", \
            f"Error message is not correct, got - '{error_text}'"

    @allure.feature("Check Out Step One Functionality")
    def test_no_zip_code(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        cart_page.go_to_checkout_page()
        self.checkout_step_one_page.enter_first_name()
        self.checkout_step_one_page.enter_last_name()
        self.checkout_step_one_page.click_continue_button()
        error_text = self.checkout_step_one_page.verify_error_message()
        assert error_text == "Error: Postal Code is required", \
            f"Error message is not correct, got - '{error_text}'"

    @allure.feature("Check Out Step One Functionality")
    def test_cancel_checkout(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        cart_page.go_to_checkout_page()
        self.checkout_step_one_page.click_cancel_button()
        cart_page.is_opened()