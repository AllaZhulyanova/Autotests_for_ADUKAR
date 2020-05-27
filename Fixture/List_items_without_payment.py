
class FreeHelper:
    def __init__(self,app):
        self.app = app

    # выбор предмета по порядку, возвращает кол-во тестов
    def Test_list_of_all_items(self):
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
                number_tests = self.Test_test_list()   # функция выбор теста по порядку
                number_all_tests = number_all_tests + number_tests[0]
                number_all_tests_access = number_all_tests_access + number_tests[1]
                Button_courses = driver.find_element_by_partial_link_text('курсы')  # кнопка "<- курсы"
                Button_courses.click()  # после нажатия возвращает на список предметов
                driver.implicitly_wait(1)
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        return number_all_tests, number_all_tests_access



    # нажатие на тесты по порядку, возвращает кол-во тестов в предмете
    def Test_test_list(self):
        driver = self.app.driver
        list_tests = []
        Sub = driver.find_element_by_tag_name('h1').text
        Buttons_objects = driver.find_elements_by_class_name(
            'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
        Lenght_buttons_objects = len(driver.find_elements_by_class_name(
            'info'))
        k = 0   # Кол-во всех тестов на странице
        n = 0   # Кол-во тестов для которых есть доступ после авторизации
        for i in range(5, Lenght_buttons_objects):
            Text_buttons_objects = Buttons_objects[i].text
            Lesson_or_test = Text_buttons_objects.split()
            if Lesson_or_test[0] == 'ТЕСТ':
                k = k +1
                Buttons_objects[i].click()
                message = self.Test_messаge()  #функция, которая возварщает текст "Зарегистрируйся и тренируйся без ограничений!"
                if message != "Зарегистрируйся и тренируйся без ограничений!":
                    print("Ошибка в работе")
                    print(Text_buttons_objects)
                    print("Предмет:", Sub)
                else:
                    n = n + 1
                Button_close = driver.find_elements_by_class_name('icon_close')[4]  # кнопка "Х"
                Button_close.click()
            Buttons_objects = driver.find_elements_by_class_name(
                'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
            list_tests = [k, n]
        return list_tests


    # возвращение сообщения "Зарегистрируйся и тренируйся без ограничений!"
    def Test_messаge(self):
        driver = self.app.driver
        alert = driver.find_elements_by_tag_name('h2')[-2]
        alert_text = alert.text
        return alert_text

