from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

import pytest
import time

#открыть страницу регистрации
#зарегистрировать нового пользователя
#проверить, что пользователь залогинен
@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function",autouse=True)
    def setup(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user((str(time.time()) + "@fakemail.org"),('lolo12345678901'))
        page.should_be_authorized_user()
 
    def test_user_cant_see_success_message(self,browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear)"
        page=ProductPage(browser, link)
        page.open()
        page.should_not_to_be_present()

    @pytest.mark.need_review                
    def test_user_can_add_product_to_basket(self,browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
        page=ProductPage(browser,link)
        page.open()
        page.should_be_basket_button_in_product_page()
        page.should_be_clickable_basket_button()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()


#Открываем страницу товара 
#Добавляем товар в корзину 
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
@pytest.mark.xfail(reason="just fail test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page=ProductPage(browser, link)
    page.open()

    page.should_be_clickable_basket_button()
    page.should_not_to_be_present()
    
    
#Открываем страницу товара
#Добавляем товар в корзину
#Проверяем, что нет сообщения об успехе с помощью is_disappeared
@pytest.mark.xfail(reason="just fail test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page=ProductPage(browser, link)
    page.open()
    page.should_be_clickable_basket_button()  
    page.should_be_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_quest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page= ProductPage(browser,link)
    page.open()
    page.go_to_login_page()

#Открываем страницу товара 
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present 
def test_guest_cant_see_success_message(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page=ProductPage(browser, link)
    page.open()
    page.should_not_to_be_present()
    

    
xfile = 7
mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
links = [mask+str(i) for i in range(10) if i != xfile] #range10  отсекаем из проверки страницу с ошибкой генератор списка что бы создать все страницы от 0 до 9
xlink = pytest.param(mask+str(xfile), marks=pytest.mark.xfail(reason="mistake on page")) 
links.insert(xfile, xlink)

@pytest.mark.parametrize('link', links)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser,link):
    page=ProductPage(browser,link)
    page.open()
    page.should_be_basket_button_in_product_page()
    page.should_be_clickable_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

   

#Гость открывает страницу товара
#Переходит в корзину по кнопке в шапке 
#Ожидаем, что в корзине нет товаров
#Ожидаем, что есть текст о том что корзина пуста
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link ="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page =BasketPage(browser,link)
    page.open()
    page.should_be_clickable_header_basket_button()
    page.should_not_to_be_present_goods_inside_basket()
    page.should_be_basket_empty_message()




