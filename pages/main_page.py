from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
import time
#from .login_page import LoginPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
   
##Как вы уже знаете, метод __init__ вызывается при создании объекта.
##Конструктор выше с ключевым словом super на самом деле только
##вызывает конструктор класса предка и передает
##ему все те аргументы, которые мы передали в конструктор MainPage.

#равносильная запись
        #class MainPage(BasePage):
   # pass
