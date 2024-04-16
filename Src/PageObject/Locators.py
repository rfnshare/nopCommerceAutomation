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
    SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Sign in ']")
    NAVBAR = (By.XPATH, "//h1")
