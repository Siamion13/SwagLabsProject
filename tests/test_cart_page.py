import allure
from base.base_test import BaseTest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


class TestCartPage(BaseTest):

    @allure.feature("Cart Functionality")
    def test_product_is_visible(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        assert cart_page.verify_cart_item_is_visible() is not None, "Cart item is not visible"

    @allure.feature("Cart Functionality")
    def test_product_is_removed_from_cart(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        assert cart_page.verify_product_is_removed_from_cart() is None, "Cart item is visible"

    @allure.feature("Cart Functionality")
    def test_continue_shopping_redirection(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        cart_page.click_continue_shopping_button()
        inventory_page.is_opened()
