import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture()
def login(request):
    test_class = request.node.cls
    test_class.login_page.open()
    test_class.login_page.is_opened()
    test_class.login_page.enter_login(test_class.data.LOGIN)
    test_class.login_page.enter_password(test_class.data.PASSWORD)
    test_class.login_page.click_submit_button()