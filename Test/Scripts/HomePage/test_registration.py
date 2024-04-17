import allure
import pytest

from Resources.GeneralUtils import store_info
from Src.PageObject.Pages.HomePage import HomePage
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Test.TestData.HomePageData import HomePageData


@allure.title("Registration Test")
@allure.description("User should be able to registration new account successfully")
class TestRegistration(WebDriverSetup):
    @pytest.mark.smoke
    @pytest.mark.parametrize("test_data", HomePageData.reg_data)
    def test_registration_new_account(self, test_data):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        url = home_page.get_url()
        log.info(f"URL {url} is loaded")  # User go to the NopCommerce Home page

        home_page.click_user_registration()  # User navigate to the Registration page
        home_page.click_user_gender(test_data['type'])  # User select the <type> as gender
        home_page.set_user_name(first_name='John', last_name='Doe')  # User set first name and last name
        home_page.set_dob(test_data['dob'])  # User set <dob> as date of birth
        home_page.set_user_email(test_data['dynamicemail'])  # User set <dynamicEmail> as email
        home_page.set_user_company(test_data['companyName'])  # User set <companyName> as company details
        home_page.set_user_options(test_data['status'])  # User set Newsletter option as <status>
        home_page.set_user_password(test_data['password'])  # User set <password> as password and confirm password again
        home_page.confirm_registration()  # User click on the Register button
        assert test_data[
                   'msg'] in home_page.verify_registration()  # Verify that the new account registration message <msg> is displayed
        log.info(
            f"Verified that new account registration message {test_data['msg']} is displayed. Email: {test_data['dynamicemail']}")
        store_info("Registration", request_payload=test_data, response_payload="Success")
