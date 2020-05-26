


class PaidHelper:
    def __init__(self,app):
        self.app = app

    # выбор предмета по порядку
    def List_items(self):
        driver = self.app.driver
        driver.implicitly_wait(1)
        Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        for i in range(0, 2):              # цикл для платных предметов
            Items[i].click()  # нажимаем на предмет по порядку
            Buttons = driver.find_elements_by_class_name(
                'subject-number')  # список уроков и тестов, нет атрибута текст
            Lenght_Objects = len(Buttons)
            if Lenght_Objects != 0:
                Sub = driver.find_element_by_tag_name('h1')
                print("#############################################")
                print('Предмет:', Sub.text)  # печатает название предмета
                self.List_of_paid_objects()  # функция, которая нажимает на тесты по порядку
                Button_courses = driver.find_element_by_partial_link_text('курсы')  # кнопка "<- курсы"
                Button_courses.click()  # после нажатия возвращает на список предметов
                driver.implicitly_wait(1)
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        Lenght_Items = len(Items)
        for i in range(2, Lenght_Items):    # цикл для бесплатных предметов
            Items[i].click()  # нажимаем на предмет по порядку
            Buttons = driver.find_elements_by_class_name(
                'subject-number')  # список уроков и тестов, нет атрибута текст
            Lenght_Objects = len(Buttons)
            if Lenght_Objects != 0:
                self.List_of_free_objects()  # функция, которая нажимает на тесты по порядку
                Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[
                    1]  # кнопка "Видеокурсы"
                Button_video_courses.click()  # после нажатия возвращает на список предметов
                driver.implicitly_wait(1)
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
            Lenght_Items = len(Items)

    # выбор тестов по порядку для платных тестов
    def List_of_paid_objects(self):
        driver = self.app.driver
        Buttons_objects = driver.find_elements_by_class_name(
            'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
        Lenght_buttons_objects = len(Buttons_objects)
        for i in range(5, Lenght_buttons_objects):
            Text_buttons_objects = Buttons_objects[i].text
            Lesson_or_test = Text_buttons_objects.split()
            if Lesson_or_test[0] == 'ТЕСТ':
                print(Text_buttons_objects)  # печатает название теста
                Buttons_objects[i].click()
                Button_close = driver.find_elements_by_class_name('icon_close')[5]  # кнопка "Х"
                Button_close.click()
            Buttons_objects = driver.find_elements_by_class_name(
                'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
            Lenght_buttons_objects = len(Buttons_objects)

    # выбор тестов по порядку для бесплатных тестов: английский, биология
    def List_of_free_objects(self):
        driver = self.app.driver
        Sub = driver.find_element_by_tag_name('h1')
        Text_sub = Sub.text
        print('#############################################')
        print('Предмет:', Text_sub)  # печатает название предмета
        Buttons_objects = driver.find_elements_by_class_name(
            'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
        Lenght_buttons_objects = len(Buttons_objects)
        for i in range(5, Lenght_buttons_objects):
            Text_buttons_objects = Buttons_objects[i].text
            Lesson_or_test = Text_buttons_objects.split()
            if Lesson_or_test[0] == 'ТЕСТ':
                print(Text_buttons_objects)  # печатает название теста
                Buttons_objects[i].click()
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
