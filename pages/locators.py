from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")
    
    
class ProductPageLocators():
    BASKET_BUTTON=(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, "div.alertinner ")
    BASKET_BUTTON=((By.CSS_SELECTOR, "button[value='Add to basket']"))
    
    #LOGIN_LINK_REGISTRATION_EMAIL = (By.CSS_SELECTOR, ".form-control#id_registration-email")
    #LOGIN_LINK_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, ".form-control#id_registration-password1")
    #LOGIN_LINK__REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, ".form-control#id_registration-password2")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    
