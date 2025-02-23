import allure
from base.base_test import BaseTest

class TestInventoryPage(BaseTest):

    @allure.feature("Inventory Functionality")
    def test_product_name(self, login):
        product_name = self.inventory_page.verify_product_name()
        assert product_name == "Sauce Labs Fleece Jacket", \
            f"Product name is not correct, got - '{product_name}'"

    @allure.feature("Inventory Functionality")
    def test_add_to_cart(self, login):
        product_quantity = self.inventory_page.add_product_to_cart()
        assert product_quantity == "1", \
            f"Product name is not correct, got - '{product_quantity}'"

    @allure.feature("Inventory Functionality")
    def test_remove_from_cart(self, login):
        self.inventory_page.add_product_to_cart()
        product_quantity = self.inventory_page.remove_product_from_cart()
        assert product_quantity is None, \
            f"Product quantity is not correct, got - '{product_quantity}'"
