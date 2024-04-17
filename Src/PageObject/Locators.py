from selenium.webdriver.common.by import By


class HomePageLocators:
    # Home Dashboard Page
    HEADER = (By.CSS_SELECTOR, "div[class*='header']")
    TITLE = (By.CSS_SELECTOR, "div[class*='topic-block-title']")
    SLIDER = (By.CSS_SELECTOR, "div[id='nivo-slider']")
    NEWS_LIST = (By.CSS_SELECTOR, "div[class='news-list-homepage']")
    POLL = (By.CSS_SELECTOR, "div[class='home-page-polls']")
    FOOTER = (By.CSS_SELECTOR, "div[class='footer']")

    REG_BUTTON = (By.CSS_SELECTOR, "a[class='ico-register']")

    @staticmethod
    def get_gender_locator(gender):
        return (By.CSS_SELECTOR, f"span[class='{gender.lower()}']")

    FIRST_NAME = (By.CSS_SELECTOR, "input[id='FirstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='LastName']")
    DOB_DAY = (By.CSS_SELECTOR, "select[name='DateOfBirthDay']")
    DOB_MONTH = (By.CSS_SELECTOR, "select[name='DateOfBirthMonth']")
    DOB_YEAR = (By.CSS_SELECTOR, "select[name='DateOfBirthYear']")
    EMAIL = (By.CSS_SELECTOR, "input[id='Email']")
    COMPANY_NAME = (By.CSS_SELECTOR, "input[id='Company']")
    NEWSLETTER = (By.CSS_SELECTOR, "input[id='Newsletter']")
    PASSWORD = (By.CSS_SELECTOR, "input[id='Password']")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[id='ConfirmPassword']")
    CONFIRM_REGISTRATION = (By.CSS_SELECTOR, "button[id='register-button']")
    SUCCESS_MSG = (By.CSS_SELECTOR, "div[class='result']")


class OrderPageLocators:
    # SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Sign in ']")
    ELECTRONICS_BUTTON = (By.XPATH, "//a[@href='/electronics']")
    CELLPHONE_BUTTON = (By.XPATH, "//a[@href='/cell-phones']")

    NOKIA_PHONE_BUTTON = (By.XPATH, "//a[@href='/nokia-lumia-1020']")
    ITEM_QUANTITY = (By.CSS_SELECTOR, "input[id*='product_enteredQuantity']")
    ADD_TO_CART = (By.CSS_SELECTOR, "button[id*='add-to-cart-button")
    LOADING_ICON = (By.CSS_SELECTOR, "div[class='ajax-loading-block-window']")
    VIEW_CART_BUTTON = (By.XPATH, "//a[@href='/cart']")
    ACCEPT_CHECKBOX = (By.CSS_SELECTOR, "input[id='termsofservice']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[id='checkout']")
    CHECKOUT_GUEST_BUTTON = (By.CSS_SELECTOR, "button[class*='checkout-as-guest-button']")

    # Billing Details Section
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='BillingNewAddress_FirstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='BillingNewAddress_LastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='BillingNewAddress_Email']")
    COMPANY = (By.CSS_SELECTOR, "input[id='BillingNewAddress_Company']")
    STATE_LOADING = (By.CSS_SELECTOR, "span[id='states-loading-progress']")
    COUNTRY = (By.CSS_SELECTOR, "select[id='BillingNewAddress_CountryId']")
    STATE = (By.CSS_SELECTOR, "select[id='BillingNewAddress_StateProvinceId']")
    CITY = (By.CSS_SELECTOR, "input[id='BillingNewAddress_City']")
    ADDRESS_ONE = (By.CSS_SELECTOR, "input[id='BillingNewAddress_Address1']")
    ADDRESS_TWO = (By.CSS_SELECTOR, "input[id='BillingNewAddress_Address2']")
    ZIP_CODE = (By.CSS_SELECTOR, "input[id='BillingNewAddress_ZipPostalCode']")
    PHONE_NUMBER = (By.CSS_SELECTOR, "input[id='BillingNewAddress_PhoneNumber']")
    FAX_NUMBER = (By.CSS_SELECTOR, "input[id='BillingNewAddress_FaxNumber']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[name='save']")
    BILLING_LOADING_WAIT_TEXT = (By.CSS_SELECTOR, "span[id='billing-please-wait']")

    # Shipping Method Section
    NEXT_DAY_AIR_OPTION = (By.CSS_SELECTOR, "input[id='shippingoption_1']")
    CONTINUE_SHIPPING_BUTTON = (By.CSS_SELECTOR, "button[class*='shipping-method-next-step-button']")
    SHIPPING_LOADING_WAIT_TEXT = (By.CSS_SELECTOR, "span[id='shipping-method-please-wait']")

    # Payment Method Section
    CREDIT_CARD_OPTION = (By.CSS_SELECTOR, "input[id='paymentmethod_1']")
    CONTINUE_PAYMENT_OPTION = (By.CSS_SELECTOR, "button[class*='payment-method-next-step-button']")
    PAYMENT_LOADING_WAIT_TEXT = (By.CSS_SELECTOR, "span[id='payment-method-please-wait']")

    # Payment Information Section
    CARDHOLDER_NAME = (By.CSS_SELECTOR, "input[id='CardholderName']")
    CARDHOLDER_CARD_NUMBER = (By.CSS_SELECTOR, "input[id='CardNumber']")
    EXP_MONTH = (By.CSS_SELECTOR, "select[id='ExpireMonth']")
    EXP_YEAR = (By.CSS_SELECTOR, "select[id='ExpireYear']")
    CARD_CODE = (By.CSS_SELECTOR, "input[id='CardCode']")
    CONTINUE_PAYMENT_SUBMIT = (By.CSS_SELECTOR, "button[class*='payment-info-next-step-button']")
    PAYMENT_CONFIRM_WAIT_TEXT = (By.CSS_SELECTOR, "span[id='payment-info-please-wait']")

    FINAL_CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[class*='confirm-order-next-step-button']")
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'order-completed')]/div/strong")



