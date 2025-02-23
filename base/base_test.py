import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckOutStepOnePage
from pages.checkout_step_two_page import CheckOutStepTwoPage
from pages.checkout_complete_page import CheckOutCompletePage


class BaseTest:

    data:Data

    login_page: LoginPage
    inventory_page: InventoryPage
    cart_page: CartPage
    checkout_step_one_page: CheckOutStepOnePage
    checkout_step_two_page: CheckOutStepTwoPage
    checkout_complete_page: CheckOutCompletePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.inventory_page = InventoryPage(driver)
        request.cls.cart_page = CartPage(driver, request.cls.inventory_page)
        request.cls.checkout_step_one_page = CheckOutStepOnePage(driver)
        request.cls.checkout_step_two_page = CheckOutStepTwoPage(driver, request.cls.inventory_page)
        request.cls.checkout_complete_page = CheckOutCompletePage(driver, request.cls.inventory_page)