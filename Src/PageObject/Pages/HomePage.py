from Src.PageObject.Pages.BasePage import BasePage
from Src.PageObject.Locators import HomePageLocators
from selenium.webdriver.support.ui import Select


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = HomePageLocators

    def check_home_page_elements(self):
        """
        This method checks if all the elements on the home page are visible
        :return:
        """
        tests = [self.find_element(*self.locator.HEADER),
                 self.find_element(*self.locator.SLIDER),
                 self.find_element(*self.locator.NEWS_LIST),
                 self.find_element(*self.locator.POLL),
                 self.find_element(*self.locator.FOOTER)]
        return all(tests)

    def get_title_text(self):
        return self.find_element(*self.locator.TITLE).text

    def click_user_registration(self):
        self.find_element(*self.locator.REG_BUTTON).click()

    def click_user_gender(self, gender):
        gender_locator = HomePageLocators.get_gender_locator(gender)

        # Click on the gender element
        self.find_element(*gender_locator).click()

    def set_user_name(self, first_name, last_name):
        self.find_element(*self.locator.FIRST_NAME).send_keys(first_name)
        self.find_element(*self.locator.LAST_NAME).send_keys(last_name)

    def set_dob(self, dob):
        year = str(dob.year)
        month = str(dob.month)
        day = str(dob.day)
        day_select = Select(self.find_element(*self.locator.DOB_DAY))
        day_select.select_by_value(day)

        month_select = Select(self.find_element(*self.locator.DOB_MONTH))
        month_select.select_by_value(month)

        year_select = Select(self.find_element(*self.locator.DOB_YEAR))
        year_select.select_by_value(year)

    def set_user_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def set_user_company(self, company_name):
        self.find_element(*self.locator.COMPANY_NAME).send_keys(company_name)

    def set_user_options(self, option):
        if option == 'checked':
            self.find_element(*self.locator.NEWSLETTER).click()
        else:
            pass

    def set_user_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)
        self.find_element(*self.locator.CONFIRM_PASSWORD).send_keys(password)

    def confirm_registration(self):
        self.find_element(*self.locator.CONFIRM_REGISTRATION).click()

    def verify_registration(self):
        return self.find_element(*self.locator.SUCCESS_MSG).text
