
from selenium import webdriver
from Fixture.Session import SessionHelper
from Fixture.List_items_after_autorization import AfterAutorizationHelper
from Fixture.List_items_before_autorization import BeforeAutorizationHelper
from Fixture.Button_menu import ButtonMenuHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.Session = SessionHelper(self)
        self.List_items_after_autorization = AfterAutorizationHelper(self)
        self.List_items_before_autorization = BeforeAutorizationHelper(self)
        self.Button_menu = ButtonMenuHelper(self)
        self.base_url = base_url


    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

# открытие домашней страницы
    def Open_home_page(self):
        driver = self.driver
        driver.get(self.base_url)

# Закрытие окна браузера
    def destroy(self):
        self.driver.quit()