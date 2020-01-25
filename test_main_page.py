from .pages.main_page import MainPage
from .pages.login_page import LoginPage

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




    
