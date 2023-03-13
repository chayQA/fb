
import pytest
from pageObject.pages.base_page import BasePage
from pageObject.pages.fb_logIn_page import Login_page
from pageObject.config.config_file import ConfigData
from pageObject.config.config_xlsx import ConfigXlsxData
from pageObject.test.test_base_page import BaseTest
from pageObject.pages.fb_singUp_page import SingUppage

class TestsingUppage(BaseTest):

    def go_to_singUp_page(self):
        self.singUp_page= SingUppage(self.driver) #self.singUp_page is an object refernece calling from fb_singup_page.
        
    def test_submit_with_input(self):
        self.go_to_singUp_page()
        self.singUp_page.fill_form_with_data()
        self.singUp_page.do_click_submit()
