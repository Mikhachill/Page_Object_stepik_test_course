from .pages.product_page import ProductPage
import pytest
import time

##xfile = 7
##mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
##links = [mask+str(i) for i in range(1) if i != xfile] #range10 # отсекаем из проверки страницу с ошибкой генератор списка что бысоздать все страницы от 0 до 9
##xlink = pytest.param(mask+str(xfile), marks=pytest.mark.xfail(reason="mistake on page")) #
##links.insert(xfile, xlink)
##
##@pytest.mark.parametrize('link', links)
##                         
##def test_quest_can_add_product_to_basket(browser,link):
##    #link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
##    page=ProductPage(browser,link)
##    page.open()
##    product_page_button=ProductPage(browser, browser.current_url)
##    product_page_button.should_be_in_product_page()
##    product_page_button.should_be_clickable_basket_button()
##    product_page_button.solve_quiz_and_get_code()
##
##    product_page_button.should_be_disappeared()
##    
##    product_page_button.should_be_message_about_adding()
##    page.should_be_message_basket_total()


#Открываем страницу товара 
#Добавляем товар в корзину 
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present   
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page=ProductPage(browser, link)
    page.open()

    page.should_be_clickable_basket_button()
    page.should_not_to_be_present()
    
    
#Открываем страницу товара 
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present 
def test_guest_cant_see_success_message(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page=ProductPage(browser, link)
    page.open()
    page.should_not_to_be_present()
    

#Открываем страницу товара
#Добавляем товар в корзину
#Проверяем, что нет сообщения об успехе с помощью is_disappeared
def test_message_disappeared_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page=ProductPage(browser, link)
    page.open()

    page.should_be_clickable_basket_button()
    
    page.should_be_disappeared()
