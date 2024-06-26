from selenium import webdriver
import allure
from selenium.webdriver.chrome.service import Service as Chrome_Service
from selenium.webdriver.edge.service import Service as Edge_Service
from selenium.webdriver.firefox.service import Service as Firefox_Service
from selenium.webdriver.ie.service import Service as IE_Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from Config.ApplicationSettings import ApplicationSettings
from Resources.ExcelUtils import read_configuration_data_from_excel


class Browser:
    web_driver = webdriver
    application_settings = ApplicationSettings()

    configuration_data = read_configuration_data_from_excel(
        application_settings.get_test_data_file_path(), sheet_name="configuration"
    )
    headless = "headless" if configuration_data["headless"] == "yes" else "headful"

    options = Options()

    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument(f"--{headless}")
    options.add_argument("--test-type")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-application-cache")
    options.add_argument("--no-sandbox")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--window-size=1280,800")

    options.experimental_options["prefs"] = {"logging.browser.enable": "false"}

    def launch_browser(self):
        """
        This method will launch the browser based on the environment type
        :return:
        """
        self.application_settings.setUp()
        browser_name = self.application_settings.get_browser_name()
        if browser_name == "chrome":
            chrome_service = Chrome_Service()
            self.web_driver = webdriver.Chrome(service=chrome_service, options=self.options
                                               )
            # self.web_driver = webdriver.Chrome(
            #     ChromeDriverManager().install(), options=self.options
            # ) Old Method
        elif browser_name == "firefox":
            firefox_service = Firefox_Service()
            self.web_driver = webdriver.Firefox(service=firefox_service)
            # self.web_driver = webdriver.Firefox(GeckoDriverManager().install()) old method
        elif browser_name == "ie":
            ie_service = IE_Service()
            self.web_driver = webdriver.Ie(service=ie_service)
            # self.web_driver = webdriver.Ie(IEDriverManager().install()) old method
        elif browser_name == "edge":
            edge_service = Edge_Service()
            self.web_driver = webdriver.Edge(service=edge_service)
            # self.web_driver = webdriver.Edge(
            #                 executable_path=EdgeChromiumDriverManager().install()
            #             ) old method

        elif browser_name == "opera":
            self.web_driver = webdriver.Opera(
                executable_path=OperaDriverManager().install(),
            )

    def get_wait(self):
        return WebDriverWait(self.web_driver, 30)

    def get_web_driver(self):
        return self.web_driver

    @allure.step("Navigate to URL")
    def go_to_url(self):
        print("Navigating to the webpage")
        self.web_driver.get(self.application_settings.get_test_url())

    def close_browser(self):
        self.web_driver.close()

    def quit_browser(self):
        self.web_driver.quit()

    def maximize_browser(self):
        self.web_driver.maximize_window()

    def accept_alert(self):
        self.web_driver.switch_to.alert.accept()
        self.web_driver.switch_to.default_content()
