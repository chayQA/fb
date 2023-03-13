import pytest
from pageObject.test.test_base_page import BaseTest
from pageObject.pages.fb_singUp_page import SingUppage


class Testloginpage(BaseTest):
    def go_to_the_logIn_page(self):
        self