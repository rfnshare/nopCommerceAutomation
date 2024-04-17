import time

from Src.PageObject.Pages.BasePage import BasePage
from Src.PageObject.Locators import OrderPageLocators
from Test.TestData.PlaceOrderData import PlaceOrderData
from selenium.webdriver.support.ui import Select


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = OrderPageLocators

    def go_to_cellphone_page(self):
        self.wait_till_visibility_of_element_located(10, *self.locator.ELECTRONICS_BUTTON)
        self.hover(*self.locator.ELECTRONICS_BUTTON)
        self.click(*self.locator.CELLPHONE_BUTTON)

    def go_to_product_page_details(self):
        self.wait_for_clickable_an_element(self.locator.NOKIA_PHONE_BUTTON)
        self.click(*self.locator.NOKIA_PHONE_BUTTON)

    def set_product_quantity(self):
        self.type_text(self.locator.ITEM_QUANTITY, PlaceOrderData.ITEM_QUANTITY)

    def wait_for_disappear(self, *element):
        loading = True
        while loading:
            loading = self.element_is_displayed(*element)
            time.sleep(1)
            print("Waiting....")

    def adding_product_into_cart(self):
        self.click(*self.locator.ADD_TO_CART)
        self.wait_for_disappear(*self.locator.LOADING_ICON)

    def got_to_shipping_cart(self):
        self.click(*self.locator.VIEW_CART_BUTTON)

    def accept_terms_and_click_checkout(self):
        self.wait_for_clickable_an_element(self.locator.ACCEPT_CHECKBOX)
        self.click(*self.locator.ACCEPT_CHECKBOX)
        self.click(*self.locator.CHECKOUT_BUTTON)

    def click_checkout_as_guest(self):
        self.wait_for_clickable_an_element(self.locator.CHECKOUT_GUEST_BUTTON)
        self.click(*self.locator.CHECKOUT_GUEST_BUTTON)

    def enter_billing_details_and_continue(self):
        self.wait_for_clickable_an_element(self.locator.FIRST_NAME)

        self.type_text(self.locator.FIRST_NAME, PlaceOrderData.FIRST_NAME)
        self.type_text(self.locator.LAST_NAME, PlaceOrderData.LAST_NAME)
        self.type_text(self.locator.EMAIL, PlaceOrderData.EMAIL)
        self.type_text(self.locator.COMPANY, PlaceOrderData.COMPANY)
        country_select = Select(self.find_element(*self.locator.COUNTRY))
        country_select.select_by_value(PlaceOrderData.COUNTRY)
        self.wait_for_disappear(*self.locator.STATE_LOADING)
        self.type_text(self.locator.CITY, PlaceOrderData.CITY)
        self.type_text(self.locator.ADDRESS_ONE, PlaceOrderData.ADDRESS_ONE)
        self.type_text(self.locator.ADDRESS_TWO, PlaceOrderData.ADDRESS_TWO)
        self.type_text(self.locator.ZIP_CODE, PlaceOrderData.ZIP)
        self.type_text(self.locator.PHONE_NUMBER, PlaceOrderData.PHONE)
        self.type_text(self.locator.FAX_NUMBER, PlaceOrderData.FAX)

        self.click(*self.locator.CONTINUE_BUTTON)
        self.wait_for_disappear(*self.locator.BILLING_LOADING_WAIT_TEXT)

    def select_shipping_method_and_continue(self):
        self.wait_for_clickable_an_element(self.locator.NEXT_DAY_AIR_OPTION)
        self.click(*self.locator.NEXT_DAY_AIR_OPTION)
        self.click(*self.locator.CONTINUE_SHIPPING_BUTTON)
        self.wait_for_disappear(*self.locator.SHIPPING_LOADING_WAIT_TEXT)

    def select_payment_method_and_continue(self):
        self.wait_for_clickable_an_element(self.locator.CREDIT_CARD_OPTION)
        self.click(*self.locator.CREDIT_CARD_OPTION)
        self.click(*self.locator.CONTINUE_PAYMENT_OPTION)
        self.wait_for_disappear(*self.locator.PAYMENT_LOADING_WAIT_TEXT)

    def enter_card_information(self):
        self.wait_for_clickable_an_element(self.locator.CARDHOLDER_NAME)

        self.type_text(self.locator.CARDHOLDER_NAME, PlaceOrderData.CARDHOLDER_NAME)
        self.type_text(self.locator.CARDHOLDER_CARD_NUMBER, PlaceOrderData.CARD_NUMBER)

        month_select = Select(self.find_element(*self.locator.EXP_MONTH))
        month_select.select_by_value(PlaceOrderData.EXP_MONTH)

        year_select = Select(self.find_element(*self.locator.EXP_YEAR))
        year_select.select_by_value(PlaceOrderData.EXP_YEAR)

        self.type_text(self.locator.CARD_CODE, PlaceOrderData.CARD_CODE)
        self.click(*self.locator.CONTINUE_PAYMENT_SUBMIT)
        self.wait_for_disappear(*self.locator.PAYMENT_CONFIRM_WAIT_TEXT)

    def click_confirm_and_place_the_order(self):
        self.wait_for_clickable_an_element(self.locator.FINAL_CONFIRM_BUTTON)
        self.click(*self.locator.FINAL_CONFIRM_BUTTON)

    def verify_order_message(self):
        self.wait_till_visibility_of_element_located(10, *self.locator.ORDER_SUCCESS_MESSAGE)
        return self.find_element(*self.locator.ORDER_SUCCESS_MESSAGE).text
