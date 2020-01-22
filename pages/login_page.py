from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url=self.browser.get_current_url(*LoginPageLocators.LOGIN_URL)
        
        assert "login" is url, "Login link is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login=self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login, "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        login=self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert login, "Register form is not presented"
