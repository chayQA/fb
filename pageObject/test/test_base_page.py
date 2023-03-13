import pytest
from pageObject.pages.base_page import BasePage
from pageObject.pages.fb_logIn_page import Login_page
from pageObject.config.config_file import ConfigData
from pageObject.config.config_xlsx import ConfigXlsxData
from selenium import webdriver


@pytest.mark.usefixtures('init_driver')

class BaseTest:

    @pytest.fixture(scope="function")

    def init_driver(self,request):
        options=webdriver.ChromeOptions()
        web_driver = webdriver.Chrome(executable_path=ConfigData.CHROME_DRIVER_PATH,options=options)
        request.cls.driver=web_driver #assing the class variable in fixture
        yield # generator function 
        web_driver.quit()
