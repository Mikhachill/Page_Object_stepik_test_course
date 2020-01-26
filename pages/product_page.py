from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class ProductPage(BasePage):    
        
       
    def should_not_to_be_present(self):
         assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), (
               "Message is presented, but should not be")

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), (
               "Message do not disappear, but it should be ")

    
    def should_be_in_product_page(self):
        button_basket=self.is_element_present(*ProductPageLocators.BASKET_BUTTON)
        assert button_basket==True, "Button is not presented"

    def should_be_clickable_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
     # Ждем явным ожиданием 
        button = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")))
     # нажимаем кнопку Add to basket
        button.click()
        
        time.sleep(1)
    
    def should_be_message_about_adding(self):
# Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        time.sleep(3)
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
 # Затем получаем текст элементов для проверки
        product_name = f'{self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text} has been added to your basket.'
        print(product_name)
        
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        print(message)
# Проверяем, что название товара присутствует в сообщении о добавлении

        assert product_name == message, "No product name in the message"
        
    def should_be_message_basket_total(self):
        #Проверяем что элементы присутсвуют на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")

        #Получаем текст этих элементов для проверки
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        print(message_basket_total)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print(product_price)

        #Проверяем что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price == message_basket_total, "No product price in the message"

#Проверки:
#Появилось ли сообщение о том что товар добавлен в корзину
#название товара действительно совпадает с тем товаром который добавили
#Появилось ли сообщение со стоимостью корзины
#Стоимость корзины действительно совпадает с ценой товара 
        
        
