from selenium.webdriver.common.by import By


class HomePageLocators:
    # Home Dashboard Page
    HEADER = (By.CSS_SELECTOR, "div[class*='header']")
    TITLE = (By.CSS_SELECTOR, "div[class*='topic-block-title']")
    SLIDER = (By.CSS_SELECTOR, "div[id='nivo-slider']")
    NEWS_LIST = (By.CSS_SELECTOR, "div[class='news-list-homepage']")
    POLL = (By.CSS_SELECTOR, "div[class='home-page-polls']")
    FOOTER = (By.CSS_SELECTOR, "div[class='footer']")


class OrderPageLocators:
    SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Sign in ']")
    NAVBAR = (By.XPATH, "//h1")
