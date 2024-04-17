from Resources.GeneralUtils import generate_email


class PlaceOrderData:
    ITEM_QUANTITY = 2

    # Billing Data
    FIRST_NAME = "John"
    LAST_NAME = "Doe"
    EMAIL = generate_email()
    COMPANY = "Test Company A"
    COUNTRY = "161"  # Bangladesh
    CITY = "Dhaka"
    ADDRESS_ONE = "Test Address One"
    ADDRESS_TWO = "Test Address Two"
    ZIP = "1234"
    PHONE = "01111111111"
    FAX = "12345"

    # Payment Information
    CARDHOLDER_NAME = "JOHN DOE"
    CARD_NUMBER = '4242 4242 4242 4242'
    EXP_MONTH = '10'
    EXP_YEAR = '2027'
    CARD_CODE = '783'

    ORDER_SUCCESS_MSG = "Your order has been successfully processed!"
