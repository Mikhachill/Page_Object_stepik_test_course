from .base_page import BasePage
from .locators import LoginPageLocators

import time
import math
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not presented"
 # реализуйте проверку на корректный url адрес
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login=self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login==True, "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        reg=self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert reg==True, "Register form is not presented"

    def register_new_user(self,email,password):
        
        input_mail=self.browser.find_element(*LoginPageLocators.LOGIN_LINK_REGISTRATION_EMAIL)
        input_mail.send_keys(email)

        input_password=self.browser.find_element(*LoginPageLocators.LOGIN_LINK_REGISTRATION_PASSWORD)
        input_password.send_keys(password)

        input_password_repeat=self.browser.find_element(*LoginPageLocators.LOGIN_LINK__REGISTRATION_PASSWORD_REPEAT)
        input_password_repeat.send_keys(password)

        registration_button=self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_button.click()

        
        

    
 
