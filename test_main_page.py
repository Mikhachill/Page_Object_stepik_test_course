from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      #cd открываем страницу
    page.go_to_login_page()
    login_page=LoginPage(browser, browser.current_url) # если комментить эту строку то надо править main_page.py
    #что бы работал первый подход к переходу между страницами
    login_page.should_be_login_page() #выполняем метод страницы - переходим на страницу логина
  

    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


##Гость открывает главную страницу 
##Переходит в корзину по кнопке в шапке сайта
##Ожидаем, что в корзине нет товаров
##Ожидаем, что есть текст о том что корзина пуста
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/"
    page=BasketPage(browser,link)
    page.open()
    page.should_be_clickable_header_basket_button()
    page.should_not_to_be_present_goods_inside_basket()
    page.should_be_basket_empty_message()
    
    
