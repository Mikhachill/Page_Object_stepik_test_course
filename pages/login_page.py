from .base_page import BasePage
from .locators import LoginPageLocators


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
