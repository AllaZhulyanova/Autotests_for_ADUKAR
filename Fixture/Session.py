from selenium.webdriver.common.keys import Keys

class SessionHelper:
    def __init__(self,app):
        self.app = app



# вход в личный кабинет
    def Log_in(self, Login, Password):
        driver = self.app.driver
        element = driver.find_elements_by_class_name('icon-label')[1]  # кнопка войти
        element.click()
        driver.implicitly_wait(1)
        element = driver.find_element_by_name("email")
        element.send_keys(Login)
        element = driver.find_element_by_name("password")
        element.send_keys(Password)
        element.send_keys(Keys.RETURN)
        

# Выход из личного кабинета
    def Log_out(self):
        driver = self.app.driver
        element = driver.find_elements_by_class_name('icon-label')[1]  # кнопка "войти"
        element.click()
        driver.implicitly_wait(1)
        element = driver.find_elements_by_class_name('exit')[1]  # кнопка "выйти"
        element.click()