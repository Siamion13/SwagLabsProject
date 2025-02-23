import allure
from base.base_test import BaseTest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support import expected_conditions as EC

class TestCheckOutStepTwoPage(BaseTest):

    @allure.feature("Check Out Step Two Functionality")
    def test_product_is_visible(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        self.cart_page.go_to_checkout_page()
        self.checkout_step_one_page.enter_first_name()
        self.checkout_step_one_page.enter_last_name()
        self.checkout_step_one_page.enter_zip_postal_code()
        self.checkout_step_one_page.click_continue_button()
        product_name = self.checkout_step_two_page.verify_product_name()
        assert "Sauce Labs Fleece Jacket" in product_name, f"Error, product name is different - {product_name}"

    @allure.feature("Check Out Step Two Functionality")
    def test_check_order_information(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        self.cart_page.go_to_checkout_page()
        self.checkout_step_one_page.enter_first_name()
        self.checkout_step_one_page.enter_last_name()
        self.checkout_step_one_page.enter_zip_postal_code()
        self.checkout_step_one_page.click_continue_button()
        payment_info = self.checkout_step_two_page.verify_payment_information()
        assert "SauceCard #31337" in payment_info, f"Error, payment information is different - {payment_info}"
        shipping_info = self.checkout_step_two_page.verify_shipping_information()
        assert "Free Pony Express Delivery!" in shipping_info, f"Error, shipping information is different - {shipping_info}"

    @allure.feature("Check Out Step Two Functionality")
    def test_compare_item_price(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        cart_item_price_element = self.cart_page.wait.until(
            EC.visibility_of_element_located(self.cart_page.CART_ITEM_PRICE))
        cart_price = cart_item_price_element.text.strip()
        self.cart_page.go_to_checkout_page()
        self.checkout_step_one_page.enter_first_name()
        self.checkout_step_one_page.enter_last_name()
        self.checkout_step_one_page.enter_zip_postal_code()
        self.checkout_step_one_page.click_continue_button()
        checkout_item_price_element = self.checkout_step_two_page.wait.until(
            EC.visibility_of_element_located(self.checkout_step_two_page.ITEM_TOTAL_LABEL))
        checkout_item_price = checkout_item_price_element.text.strip()
        cart_price_value = cart_price.replace("$", "").strip()
        checkout_item_price_value = checkout_item_price.replace("Item total:","").replace("$", "").strip()
        assert float(cart_price_value) == float(checkout_item_price_value), "Error, there is a price mismatch"

    @allure.feature("Check Out Step Two Functionality")
    def test_total_price_including_tax(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        self.cart_page.go_to_checkout_page()
        self.checkout_step_one_page.enter_first_name()
        self.checkout_step_one_page.enter_last_name()
        self.checkout_step_one_page.enter_zip_postal_code()
        self.checkout_step_one_page.click_continue_button()
        checkout_item_price_element = self.checkout_step_two_page.wait.until(
            EC.visibility_of_element_located(self.checkout_step_two_page.ITEM_TOTAL_LABEL))
        checkout_item_price = checkout_item_price_element.text.strip()
        checkout_item_price_value = float(checkout_item_price.replace("Item total:", "").replace("$", "").strip())
        tax_price_element = self.checkout_step_two_page.wait.until(
            EC.visibility_of_element_located(self.checkout_step_two_page.TAX_LABEL))
        tax_price = tax_price_element.text.strip()
        tax_price_value = float(tax_price.replace("Tax:", "").replace("$", "").strip())
        total_value_element = self.checkout_step_two_page.wait.until(
            EC.visibility_of_element_located(self.checkout_step_two_page.TOTAL_LABEL))
        total_price = total_value_element.text.strip()
        total_price_value = float(total_price.replace("Total:", "").replace("$", "").strip())

        assert total_price_value == checkout_item_price_value + tax_price_value, f"Error, total value is different - {total_price_value}"

    @allure.feature("Check Out Step Two Functionality")
    def test_cancel_order(self, login):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver, inventory_page)
        cart_page.inventory_page.add_product_to_cart()
        cart_page.go_to_cart()
        self.cart_page.go_to_checkout_page()
        self.checkout_step_one_page.enter_first_name()
        self.checkout_step_one_page.enter_last_name()
        self.checkout_step_one_page.enter_zip_postal_code()
        self.checkout_step_one_page.click_continue_button()
        self.checkout_step_two_page.click_cancel_button()
        inventory_page.is_opened()




