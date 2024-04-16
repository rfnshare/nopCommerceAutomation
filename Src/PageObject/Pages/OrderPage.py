import time

from Src.PageObject.Pages.BasePage import BasePage
from Src.PageObject.Locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = OrderPageLocators

    def login(self):
        self.click(*self.locator.SIGN_IN_BUTTON)
        time.sleep(5)
        return self.find_element(*self.locator.NAVBAR).text
