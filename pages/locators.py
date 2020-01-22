from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")

    
    #LOGIN_LINK_REGISTRATION_EMAIL = (By.CSS_SELECTOR, ".form-control#id_registration-email")
    #LOGIN_LINK_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, ".form-control#id_registration-password1")
    #LOGIN_LINK__REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, ".form-control#id_registration-password2")
    
    
