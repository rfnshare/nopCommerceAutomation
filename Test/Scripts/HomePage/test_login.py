import allure
import pytest
from Src.PageObject.Pages.OrderPage import OrderPage
from Src.TestBase.WebDriverSetup import WebDriverSetup


@allure.title("Login Test")
@allure.description("Checking Login Function")
class TestLoginPage(WebDriverSetup):
    @pytest.mark.smoke
    def test_01_login(self):
        log = self.get_logger()
        pass

