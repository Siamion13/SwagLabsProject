import allure
import pytest

from base.base_test import BaseTest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

class TestCheckOutCompletePage(BaseTest):

    @allure.feature("Check Out Complete Functionality")
    @pytest.mark.smoke
    def test_order_is_complete(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        self.cart_page.go_to_checkout_page()
        self.checkout_step_one_page.enter_first_name()
        self.checkout_step_one_page.enter_last_name()
        self.checkout_step_one_page.enter_zip_postal_code()
        self.checkout_step_one_page.click_continue_button()
        self.checkout_step_two_page.click_continue_button()
        self.checkout_complete_page.verify_checkout_complete_image()
        header_text = self.checkout_complete_page.verify_checkout_complete_header()
        assert header_text == "Thank you for your order!", \
            f"Header is different, got - '{header_text}'"
        sub_header_text = self.checkout_complete_page.verify_checkout_complete_sub_header()
        assert sub_header_text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!", \
            f"Sub header is different, got - '{sub_header_text}'"
        self.checkout_complete_page.take_screenshot("Thank you for your order!")
        self.checkout_complete_page.navigate_to_home_page()
        inventory_page.is_opened()

