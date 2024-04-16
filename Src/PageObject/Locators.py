from selenium.webdriver.common.by import By


class HomePageLocators:
    # Home Dashboard Page
    HEADER = (By.CSS_SELECTOR, "div[class*='header']")
    TITLE = (By.CSS_SELECTOR, "div[class*='topic-block-title']")


class OrderPageLocators:
    SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Sign in ']")
    NAVBAR = (By.XPATH, "//h1")
