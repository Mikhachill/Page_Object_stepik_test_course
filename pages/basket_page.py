from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class BasketPage(BasePage):
    def should_be_clickable_header_basket_button(self):
            button = self.browser.find_element(*BasketPageLocators.HEADER_BASKET_BUTTON)
            # Ждем явным ожиданием 
            button = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((BasketPageLocators.HEADER_BASKET_BUTTON)))
            button.click()
            time.sleep(2)

    def should_not_to_be_present_goods_inside_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_INSIDE_BASKET_INDICATOR), (
               "Product is presented, but should not be")

    def should_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), (
               "Message is not presented, but should be")
    




