

class FreeHelper:
    def __init__(self,app):
        self.app = app

        # выбор предмета по порядку

    def Test_list_items(self):
        driver = self.app.driver
        driver.implicitly_wait(1)
        Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        lenght_Items = len(Items)
        for i in range(0, lenght_Items):
            Items[i].click()  # нажимаем на предмет по порядку
            Buttons = driver.find_elements_by_class_name(
                'subject-number')  # список уроков и тестов, нет атрибута текст
            Lenght_Objects = len(Buttons)
            if Lenght_Objects != 0:
                #Sub = driver.find_element_by_tag_name('h1').text   # название предмета
                self.Test_list_objects()   # функция выбор теста по порядку
                Button_courses = driver.find_element_by_partial_link_text('курсы')  # кнопка "<- курсы"
                Button_courses.click()  # после нажатия возвращает на список предметов
                driver.implicitly_wait(1)
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов

        # выбор теста по порядку

    def Test_list_objects(self):
        driver = self.app.driver
        Sub = driver.find_element_by_tag_name('h1').text
        Buttons_objects = driver.find_elements_by_class_name(
            'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
        Lenght_buttons_objects = len(driver.find_elements_by_class_name(
            'info'))
        k=0
        n=0
        for i in range(5, Lenght_buttons_objects):
            Text_buttons_objects = Buttons_objects[i].text
            Lesson_or_test = Text_buttons_objects.split()
            if Lesson_or_test[0] == 'ТЕСТ':
                n=n+1
                Buttons_objects[i].click()
                message = self.Test_messаge()  #функция, которая возварщает текст "Зарегистрируйся и тренируйся без ограничений!"
                if message != "Зарегистрируйся и тренируйся без ограничений!":
                    print ("Ошибка в работе")
                    print(Text_buttons_objects)
                    print("Предмет:", Sub)
                Button_close = driver.find_elements_by_class_name('icon_close')[4]  # кнопка "Х"
                Button_close.click()
            Buttons_objects = driver.find_elements_by_class_name(
                'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст


    # возвращение сообщения "Зарегистрируйся и тренируйся без ограничений!"
    def Test_messаge(self):
        driver = self.app.driver
        alert = driver.find_elements_by_tag_name('h2')[-2]
        alert_text = alert.text
        return alert_text