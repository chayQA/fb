from pageObject.pages.base_page import BasePage
from pageObject.config.config_file import ConfigData
from pageObject.config.config_xlsx import ConfigXlsxData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SingUppage(BasePage):

    FIRST_NAME_INPUT =(By.XPATH, "//input[@name='firstname']")
    SURNAME_INPUT =(By.XPATH, '//input[@type="text"]')
    EMAIL_ADDRESS_INPUT =(By.CSS_SELECTOR,'#u_0_g_M3')
    NEW_PASSWORD_INPUT =(By.CSS_SELECTOR, '#password_step_input')
    SINGUP_INPUT=(By.XPATH,'//button[@type="submit"]')
    DOB_DAY_INPUT =(By.XPATH,"//select[@name='birthday_day']")
    DOB_MONTH_INPUT= (By.XPATH,"//select[@name='birthday_month']")
    DOB_YEAR_INPUT =(By.XPATH,"//select[@name='birthday_year']")
    GENDER_INPUT =(By.XPATH,'//input[@value="2"]')



 

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(ConfigData.FB_LOGIN_PAGE)

    def fill_form_with_data(self):
        self.do_send_keys(self.FIRST_NAME_INPUT,"venkatchaitanya")
        self.do_send_keys(self.SURNAME_INPUT,"puli")
        self.do_send_keys(self.EMAIL_ADDRESS_INPUT,"chaitanya@gmail.com")
        
    def do_click_submit(self):
        self.do_click(self.SINGUP_INPUT)
