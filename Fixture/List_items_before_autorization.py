
class BeforeAutorizationHelper:
    def __init__(self,app):
        self.app = app

    # выбор предмета по порядку, возвращает кол-во уроков/тестов
    def Test_list_of_all_items(self, TEXT):
        driver = self.app.driver
        Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        lenght_Items = len(Items)
        number_all_tests = 0 # общее кол-во тестов по всем предметам
        number_all_tests_access = 0  # общее кол-во тестов по всем предметам, которые имеют доступ
        for i in range(0, lenght_Items):
            Items[i].click()  # нажимаем на предмет по порядку
            Lenght_Objects = len(driver.find_elements_by_class_name(
                'subject-number')) # длина списка уроков и тестов, нет атрибута текст
            if Lenght_Objects != 0:
                number_tests = self.Test_list_of_tests_and_lessons(TEXT)   # функция выбор теста по порядку
                number_all_tests = number_all_tests + number_tests[0]
                number_all_tests_access = number_all_tests_access + number_tests[1]
                Button_courses = driver.find_element_by_partial_link_text('курсы')  # кнопка "<- курсы"
                Button_courses.click()  # после нажатия возвращает на список предметов
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
            lenght_Items = len(Items)
        return number_all_tests, number_all_tests_access

    # выбор предмета по порядку для ТТ, возвращает кол-во ТТ
    def Test_list_of_all_items_for_TT (self, TEXT):
        driver = self.app.driver
        Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        lenght_Items = len(Items)
        number_all_tests = 0 # общее кол-во тестов по всем предметам
        number_all_tests_access = 0  # общее кол-во тестов по всем предметам, которые имеют доступ
        for i in range(0, lenght_Items):
            Items[i].click()  # нажимаем на предмет по порядку
            Buttons = driver.find_elements_by_class_name(
                'subject-number')  # список уроков и тестов, нет атрибута текст
            Lenght_Objects = len(Buttons)
            if Lenght_Objects != 0:
                number_tests = self.Test_list_of_TT(TEXT)   # функция выбор теста по порядку
                number_all_tests = number_all_tests + number_tests[0]
                number_all_tests_access = number_all_tests_access + number_tests[1]
                Button_courses = driver.find_element_by_partial_link_text('курсы')  # кнопка "<- курсы"
                Button_courses.click()  # после нажатия возвращает на список предметов
                driver.implicitly_wait(1)
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        return number_all_tests, number_all_tests_access

    # доступ к уроку/тесту, возвращает кол-во уроков/тестов в предмете
    def Test_list_of_tests_and_lessons(self,TEXT):
        driver = self.app.driver
        Text_sub = driver.find_element_by_tag_name('h1').text  # название предмета на списке тестов/уроков
        Lenght_buttons_objects = len(driver.find_elements_by_class_name('info'))
        k = 0   # Кол-во всех разработанных уроков/тестов на странице
        n = 0   # Кол-во всех доступных уроков/тестов на странице
        for i in range(4, Lenght_buttons_objects):
            Buttons_objects = driver.find_elements_by_class_name('info') # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
            Text_buttons_objects = Buttons_objects[i].text
            Lesson_or_test = Text_buttons_objects.split()
            if TEXT == Lesson_or_test[0] and TEXT == "ТЕСТ":
                Buttons_objects[i].click()
                k = k + 1
                message = self.Test_messаge()  #функция, которая возварщает текст "Зарегистрируйся и тренируйся без ограничений!"
                if message == "Зарегистрируйся и тренируйся без ограничений!":
                    n = n + 1
                    Button_close = driver.find_elements_by_class_name('icon_close')[4]  # кнопка "Х"
                    Button_close.click()
                else:
                    print("Ошибка в доступе к тесту")
                    print("Предмет:", Text_sub)
                    print(Text_buttons_objects)
            elif TEXT == Lesson_or_test[0] and TEXT == "УРОК":
                Buttons_objects[i].click()
                driver.implicitly_wait(1)
                if len(driver.find_elements_by_class_name('test-button')) != 0 or len(driver.find_element_by_tag_name('iframe').get_attribute("src")) != 0:
                    k = k + 1
                    if len(driver.find_elements_by_class_name('test-button')) != 0 and len(driver.find_element_by_tag_name('iframe').get_attribute("src")) != 0:
                        n = n + 1
                        Button_back = driver.find_element_by_class_name('icon_back')  # кнопка <- АДУКАР
                        Button_back.click()
                    else:
                        print("Ошибка в доступе к уроку")
                        print("Предмет:", Text_sub)
                        print(Text_buttons_objects)
            else:
                pass
            Lenght_buttons_objects = len(driver.find_elements_by_class_name('info'))
        return k, n

    # доступ к ТТ1/ТТ2
    def Test_list_of_TT(self, TEXT):
        driver = self.app.driver
        Buttons_objects = driver.find_elements_by_class_name(
            'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
        Lenght_buttons_objects = len(Buttons_objects)
        kTT = 0   # Кол-во всех разработанных тренировочных тестов в уроках
        nTT = 0   # Кол-во всех доступных тренировочных тестов в уроках
        for i in range(4, Lenght_buttons_objects):
            Text_sub = driver.find_element_by_tag_name('h1').text  # название предмета на списке тестов/уроков
            Text_buttons_objects = Buttons_objects[i].text
            Lesson_or_test = Text_buttons_objects.split()
            if Lesson_or_test[0] == 'УРОК':
                Buttons_objects[i].click()
                driver.implicitly_wait(1)
                if len(driver.find_elements_by_class_name('test-button')) != 0 and len(driver.find_element_by_tag_name('iframe').get_attribute("src")):
                    Button_TT = driver.find_elements_by_class_name('test-button')  # ТТ1/ТТ2
                    Lenght_buttons_TT = len(Button_TT)
                    for j in range(0, Lenght_buttons_TT):
                        Button_TT[j].click()
                        kTT = kTT + 1
                        message = self.Test_messаge()  # функция, которая возварщает текст "Зарегистрируйся и тренируйся без ограничений!"
                        if message == "Зарегистрируйся и тренируйся без ограничений!":
                            nTT = nTT + 1
                            driver.back()
                            Buttons_objects = driver.find_elements_by_class_name('info')  # кнопка список уроков
                            Buttons_objects[i].click()
                        else:
                            print("Ошибка в доступе")
                            print("Предмет:", Text_sub)
                            print(Text_buttons_objects)
                            print(Button_TT[j].text)
                        Button_TT = driver.find_elements_by_class_name('test-button')
                        Lenght_buttons_TT = len(Button_TT)
                    Button_back = driver.find_element_by_class_name('icon_back')  # кнопка <- АДУКАР
                    Button_back.click()
            Buttons_objects = driver.find_elements_by_class_name('info')  # кнопка список уроков/тестов и еще 4 кнопки
            Lenght_buttons_objects = len(Buttons_objects)
        return kTT, nTT

    # возвращение сообщения "Зарегистрируйся и тренируйся без ограничений!"
    def Test_messаge(self):
        driver = self.app.driver
        alert = driver.find_elements_by_tag_name('h2')[-2]
        alert_text = alert.text
        return alert_text



