import time

import allure
import pytest
from Src.PageObject.Pages.HomePage import HomePage
from Src.PageObject.Pages.OrderPage import OrderPage
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Test.TestData.HomePageData import HomePageData
from Test.TestData.PlaceOrderData import PlaceOrderData


@allure.title("Place Order Test")
@allure.description("User should be able to successfully place order as a guest user")
class TestPlaceOrder(WebDriverSetup):
    @pytest.mark.smoke
    def test_place_order(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        url = home_page.get_url()
        log.info(f"URL {url} is loaded")  # User go to the NopCommerce Home page
        order_page = OrderPage(self.driver)

        order_page.go_to_cellphone_page()  # User click "Cell phones" option from "Electronics" category
        order_page.go_to_product_page_details()  # User click on the "Nokia Lumia 1020" for product details
        order_page.set_product_quantity()  # User set the quantity number 2 in the quantity field
        order_page.adding_product_into_cart()  # User click on the "ADD TO CART" button
        order_page.got_to_shipping_cart()  # User go to the shipping cart page
        order_page.accept_terms_and_click_checkout()  # User accept terms conditions and click checkout button
        order_page.click_checkout_as_guest()  # User click checkout as guest button
        order_page.enter_billing_details_and_continue()  # User input all the billing details and click continue
        order_page.select_shipping_method_and_continue()  # User select shipping method "Next Day Air" and click continue
        order_page.select_payment_method_and_continue()  # User select payment method "Credit Card" and click continue
        order_page.enter_card_information()  # User select "Visa" card and input card information
        order_page.click_confirm_and_place_the_order()  # User click confirm button to place the order
        assert PlaceOrderData.ORDER_SUCCESS_MSG == order_page.verify_order_message()  # Verify that the order place message "Your order has been successfully processed!" is displayed
        log.info(
            f"Verified that user successfully place order as a guest user")
