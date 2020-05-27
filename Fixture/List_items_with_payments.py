
class PaidHelper:
    def __init__(self,app):
        self.app = app

    # выбор предмета по порядку
    def List_items(self):
        driver = self.app.driver
        number_all_paid_tests = 0 # общее кол-во тестов по всем предметам
        number_all_paid_tests_with_access = 0  # общее кол-во тестов по всем предметам, которые имеют доступ
        number_all_free_tests = 0 # общее кол-во тестов по всем предметам
        number_all_free_tests_with_access = 0  # общее кол-во тестов по всем предметам, которые имеют доступ
        All_tests = 0  # общее число тестов по всем предметам
        All_tests_with_access = 0  # доступ к общему числу тестов по всем предметам
        Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        for i in range(0, 2):              # цикл для платных предметов
            Items[i].click()  # нажимаем на предмет по порядку
            Buttons = driver.find_elements_by_class_name(
                'subject-number')  # список уроков и тестов, нет атрибута текст
            Lenght_Objects = len(Buttons)
            if Lenght_Objects != 0:
                number_paid_tests = self.List_of_paid_objects()  # функция, которая нажимает на тесты по порядку
                number_all_paid_tests = number_all_paid_tests + number_paid_tests[0]
                number_all_paid_tests_with_access = number_all_paid_tests_with_access + number_paid_tests [1]
                Button_courses = driver.find_element_by_partial_link_text('курсы')  # кнопка "<- курсы"
                Button_courses.click()  # после нажатия возвращает на список предметов
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        Lenght_Items = len(Items)
        for i in range(2, Lenght_Items):    # цикл для бесплатных предметов
            Items[i].click()  # нажимаем на предмет по порядку
            Buttons = driver.find_elements_by_class_name(
                'subject-number')  # список уроков и тестов, нет атрибута текст
            Lenght_Objects = len(Buttons)
            if Lenght_Objects != 0:
                number_free_tests = self.List_of_free_objects()  # функция, которая нажимает на тесты по порядку
                number_all_free_tests = number_all_free_tests + number_free_tests[0]
                number_all_free_tests_with_access = number_all_free_tests_with_access + number_free_tests[1]
                Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[
                    1]  # кнопка "Видеокурсы"
                Button_video_courses.click()  # после нажатия возвращает на список предметов
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
            Lenght_Items = len(Items)
        All_tests = number_all_paid_tests + number_all_free_tests
        All_tests_with_access = number_all_paid_tests_with_access + number_all_free_tests_with_access
        return All_tests, All_tests_with_access

    # выбор тестов по порядку для платных тестов
    def List_of_paid_objects(self):
        driver = self.app.driver
        Sub = driver.find_element_by_tag_name('h1')
        Text_sub = Sub.text  # название предмета
        kPaid = 0   # Кол-во всех тестов на странице
        nPaid = 0   # Кол-во тестов для которых есть доступ после оплаты
        Buttons_objects = driver.find_elements_by_class_name(
            'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
        Lenght_buttons_objects = len(Buttons_objects)
        for i in range(5, Lenght_buttons_objects):
            Text_buttons_objects = Buttons_objects[i].text  # название теста
            Lesson_or_test = Text_buttons_objects.split()
            if Lesson_or_test[0] == 'ТЕСТ':
                kPaid = kPaid + 1
                Buttons_objects[i].click()
                Text_button = driver.find_element_by_id('testPurchaseBtn').text
                if Text_button != "Перейти к оплате":
                    print("Предмет:",Text_sub)
                    print(Text_buttons_objects)
                else:
                    nPaid = nPaid + 1
                Button_close = driver.find_elements_by_class_name('icon_close')[5]  # кнопка "Х"
                Button_close.click()
            Buttons_objects = driver.find_elements_by_class_name(
                'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
            Lenght_buttons_objects = len(Buttons_objects)
        return kPaid,nPaid

    # выбор тестов по порядку для бесплатных тестов: английский, биология
    def List_of_free_objects(self):
        driver = self.app.driver
        Sub = driver.find_element_by_tag_name('h1')
        Text_sub = Sub.text  # название предмета
        kFree = 0   # Кол-во всех тестов на странице
        nFree = 0   # Кол-во тестов для которых есть доступ после оплаты
        Buttons_objects = driver.find_elements_by_class_name(
            'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
        Lenght_buttons_objects = len(Buttons_objects)
        for i in range(5, Lenght_buttons_objects):
            Text_buttons_objects = Buttons_objects[i].text
            Lesson_or_test = Text_buttons_objects.split()
            if Lesson_or_test[0] == 'ТЕСТ':
                kFree = kFree + 1
                Buttons_objects[i].click()
                Text = driver.find_element_by_css_selector('p.not-found__title').text
                if Text != 'Проверка безопасности':
                    print("Предмет",Text_sub)
                    print(Text_buttons_objects)
                else:
                    nFree = nFree + 1
                Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[
                    1]  # кнопка "Видеокурсы"
                Button_video_courses.click()  # после нажатия возвращает на список предметов
                if i < Lenght_buttons_objects:
                    All_subjects = driver.find_elements_by_class_name('subject-card')
                    Lenght_all_subjects = len(All_subjects)
                    for n in range(1,Lenght_all_subjects):
                        if Text_sub == All_subjects[n].text:
                            Button_sub = All_subjects[n]
                    Button_sub.click()
            Buttons_objects = driver.find_elements_by_class_name('info')
            Lenght_buttons_objects = len(Buttons_objects)
        return kFree,nFree
