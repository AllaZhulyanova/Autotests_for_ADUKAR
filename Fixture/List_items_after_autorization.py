from random import choice

class AfterAutorizationHelper:
    def __init__(self,app):
        self.app = app

    # выбор предмета по порядку с проверкой доступка к уроку/тесту без оплаты, проверки безопасности
    def List_items(self,TEXT):
        driver = self.app.driver
        number_all_paid_tests = 0 # общее кол-во платных тестов по всем предметам
        number_all_paid_tests_with_access = 0  # общее кол-во платных тестов по всем предметам, которые имеют доступ
        number_all_free_tests = 0 # общее кол-во беслпатных тестов по всем предметам
        number_all_free_tests_with_access = 0  # общее кол-во обеплатных тестов по всем предметам, которые имеют доступ
        All_tests = 0  # общее число тестов по всем предметам
        All_tests_with_access = 0  # доступ к общему числу тестов по всем предметам
        Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        for i in range(0, 2):              # цикл для платных предметов
            Items[i].click()  # нажимаем на предмет по порядку
            Buttons = driver.find_elements_by_class_name(
                'subject-number')  # список уроков и тестов, нет атрибута текст
            Lenght_Objects = len(Buttons)
            if Lenght_Objects != 0:
                number_paid_tests = self.List_of_paid_objects(TEXT)  # функция, которая нажимает на уроки/тесты по порядку
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
                number_free_tests = self.List_of_free_objects(TEXT)  # функция, которая нажимает на уроки/тесты по порядку
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

    # выбор предмета по порядку с проверкой доступка к уроку/тесту с проведением оплаты, но без проверки безопасности
    def List_of_paid_items(self,TEXT):
        driver = self.app.driver
        number_all_tests_after_payment = 0 # общее кол-во тестов по всем предметам
        number_all_tests_after_payment_with_access = 0  # общее кол-во тестов по всем предметам, которые имеют доступ
        Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        for i in range(0, 2):              # цикл для платных предметов
            Items[i].click()  # нажимаем на предмет по порядку
            Buttons = driver.find_elements_by_class_name(
                'subject-number')  # список уроков и тестов, нет атрибута текст
            Lenght_Objects = len(Buttons)
            if Lenght_Objects != 0:
                self.Random_object(TEXT)  # выбор случайного урока/теста
                self.Payment()  # оплата
                Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[
                    1]  # кнопка "Видеокурсы"
                Button_video_courses.click()  # после нажатия возвращает на список предметов
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        #result = self.All_subject_after_payment(TEXT)
        #number_all_tests_after_payment = result[0]
        #number_all_tests_after_payment_with_access = result[1]
        #return number_all_tests_after_payment, number_all_tests_after_payment_with_access

    # выбор предмета по порядку с проверкой доступка к уроку/тесту с проведением оплаты и проверки безопасности
    def List_of_paid_items_with_security(self,TEXT):
        driver = self.app.driver
        number_all_tests_after_security = 0 # общее кол-во разработанных ТТ/тестов по всем предметам
        number_all_tests_after_security_with_access = 0  # общее кол-во ТТ/тестов по всем предметам, которые имеют доступ
        Selected_sub = self.Random_subject()
        if Selected_sub == driver.find_elements_by_class_name('subject-card')[0] or Selected_sub == driver.find_elements_by_class_name('subject-card')[1]:  # сравнивает выбранную кнопку с Русс яз/Белор яз (там тесты и уроки платные)
            Selected_sub.click()
            self.Random_object(TEXT)
            self.Payment()
            self.Security()
            Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[1]
            Button_video_courses.click()  # после нажатия возвращает на список предметов
        else:    # сравнивает выбранную кнопку с Англ яз/Биология (там тесты и уроки бесплатные)
            Selected_sub.click()
            self.Random_object(TEXT)
            self.Security()
            Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[1]
            Button_video_courses.click()  # после нажатия возвращает на список предметов
        #result = self.All_subject_after_payment(TEXT)
        #number_all_tests_after_security = result[0]
        #number_all_tests_after_security_with_access[1]
        #return number_all_tests_after_security, number_all_tests_after_security_with_access


    # выбор уроков/тестов по порядку для платных тестов
    def List_of_paid_objects(self,TEXT):
        driver = self.app.driver
        Sub = driver.find_element_by_tag_name('h1')
        Text_sub = Sub.text  # название предмета
        kPaid = 0   # Кол-во всех разработанных уроков/тестов на странице
        nPaid = 0   # Кол-во уроков/тестов для которых есть доступ после оплаты
        Buttons_objects = driver.find_elements_by_class_name(
            'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
        Lenght_buttons_objects = len(Buttons_objects)
        for i in range(4, Lenght_buttons_objects):
            Text_buttons_objects = Buttons_objects[i].text  # название теста/урока
            Lesson_or_test = Text_buttons_objects.split()
            if Lesson_or_test[0] == "ТЕСТ":
                Buttons_objects[i].click()
                kPaid = kPaid + 1
                Text_button = driver.find_element_by_id('testPurchaseBtn').text
                if Text_button != "Перейти к оплате":
                    print("Ошибка в доступе")
                    print("Предмет:",Text_sub)
                    print(Text_buttons_objects)
                else:
                    nPaid = nPaid + 1
                Button_close = driver.find_elements_by_class_name('icon_close')[5]  # кнопка "Х"
                Button_close.click()
            if Lesson_or_test[0] == "УРОК":
                Buttons_objects[i].click()
                if len(driver.find_elements_by_class_name('test-button')) != 0:
                    kPaid = kPaid + 1
                    Link_name = driver.find_element_by_tag_name('iframe').get_attribute("src") # ссылка на видеоурок
                    Button_TT = driver.find_elements_by_class_name('test-button')  # ТТ1/ТТ2
                    if len(Link_name) == 0 and len(Button_TT) == 0:
                        print("Ошибка в доступе")
                        print("Предмет:", Text_sub)
                        print(Text_buttons_objects)
                    else:
                        nPaid = nPaid + 1
                        self.Videocourse_subject()
                            #Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[1]
                            #Button_video_courses.click()  # после нажатия возвращает на список предметов
                            #if i < Lenght_buttons_objects:
                             #   All_subjects = driver.find_elements_by_class_name('subject-card')
                             #   Lenght_all_subjects = len(All_subjects)
                             #   for j in range(0, Lenght_all_subjects):
                             #       if Text_sub == All_subjects[j].text:
                             #           Button_sub = All_subjects[j]
                             #   Button_sub.click()
            Buttons_objects = driver.find_elements_by_class_name(
                'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
            Lenght_buttons_objects = len(Buttons_objects)
        return kPaid,nPaid

    # выбор тестов по порядку для бесплатных уроков/тестов: английский, биология
    def List_of_free_objects(self,TEXT):
        driver = self.app.driver
        Sub = driver.find_element_by_tag_name('h1')
        Text_sub = Sub.text  # название предмета
        kFree = 0   # Кол-во всех разработанных уроков/тестов на странице
        nFree = 0   # Кол-во уроков/тестов для которых есть доступ после оплаты
        Buttons_objects = driver.find_elements_by_class_name(
            'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
        Lenght_buttons_objects = len(Buttons_objects)
        for i in range(4, Lenght_buttons_objects):
            Text_buttons_objects = Buttons_objects[i].text
            Lesson_or_test = Text_buttons_objects.split()
            if Lesson_or_test[0] == TEXT:
                Buttons_objects[i].click()
                if Lesson_or_test[0] == "ТЕСТ":
                    kFree = kFree + 1
                    Text = driver.find_element_by_css_selector('p.not-found__title').text
                    if Text != 'Проверка безопасности':
                        print("Ошибка в доступе")
                        print("Предмет",Text_sub)
                        print(Text_buttons_objects)
                    else:
                        nFree = nFree + 1
                    self.Videocourse_subject()
                    #Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[1]
                    #Button_video_courses.click()  # после нажатия возвращает на список предметов
                    #if i < Lenght_buttons_objects:
                    #    All_subjects = driver.find_elements_by_class_name('subject-card')
                    #    Lenght_all_subjects = len(All_subjects)
                    #    for n in range(0,Lenght_all_subjects):
                    #        if Text_sub == All_subjects[n].text:
                    #            Button_sub = All_subjects[n]
                    #    Button_sub.click()
                if Lesson_or_test[0] == "УРОК":
                    if len(driver.find_elements_by_class_name('test-button')) != 0:
                        kFree = kFree + 1
                        Link_name = driver.find_element_by_tag_name('iframe').get_attribute("src") # ссылка на видеоурок
                        Button_TT = driver.find_elements_by_class_name('test-button')  # ТТ1/ТТ2
                        if len(Link_name) == 0 and len(Button_TT) == 0:
                            print("Предмет:", Text_sub)
                            print(Text_buttons_objects)
                        else:
                            nFree = nFree + 1
                            self.Videocourse_subject()
                            #Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[1]
                            #Button_video_courses.click()  # после нажатия возвращает на список предметов
                            #if i < Lenght_buttons_objects:
                             #   All_subjects = driver.find_elements_by_class_name('subject-card')
                             #   Lenght_all_subjects = len(All_subjects)
                             #   for j in range(0, Lenght_all_subjects):
                             #       if Text_sub == All_subjects[j].text:
                             #           Button_sub = All_subjects[j]
                              #  Button_sub.click()
            Buttons_objects = driver.find_elements_by_class_name('info')
            Lenght_buttons_objects = len(Buttons_objects)
        return kFree,nFree

    # перебор всех предметов по порядку после оплаты
    def All_subject_after_payment(self, TEXT):
        driver = self.app.driver
        number_all_tests = 0
        number_all_tests_with_access = 0
        Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        Lenght_Items = len(Items)
        for j in range(0, Lenght_Items):  # цикл для бесплатных предметов
            Items[j].click()  # нажимаем на предмет по порядку
            Buttons = driver.find_elements_by_class_name('subject-number')  # список уроков и тестов
            Lenght_Objects = len(Buttons)
            if Lenght_Objects != 0:
                number_tests = self.List_of_free_objects(TEXT)  # функция, которая нажимает на уроки/тесты по порядку
                number_all_tests = number_all_tests + number_tests[0]
                number_all_tests_with_access = number_all_tests_with_access + number_tests[1]
                Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[1]
                Button_video_courses.click()  # после нажатия возвращает на список предметов
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
            Lenght_Items = len(Items)
        return number_all_tests, number_all_tests_with_access



    # Выбор случайного предмета
    def Random_subject(self):
        driver = self.app.driver
        List_subject = [] # текстовый список предметов
        Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
        Lenght_Items = len(Items)
        for i in range(0, Lenght_Items): # цикл для всех предметов
            Items[i].click()  # нажимаем на предмет по порядку
            Buttons = driver.find_elements_by_class_name('subject-number')  # список уроков и тестов
            Lenght_Objects = len(Buttons)
            if Lenght_Objects != 0:
                Sub = driver.find_element_by_tag_name('h1')
                Text_sub = Sub.text  # название предмета
                List_subject.append(Text_sub)  # список предметов
                Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[1]
                Button_video_courses.click()  # после нажатия возвращает на список предметов
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
            Lenght_Items = len(Items)
        Subject_selection = choice(List_subject)  # выбрали случайный предмет
        for j in range(0, Lenght_Items):  # цикл для прохожения всех предметов по порядку
            if Subject_selection == Items[j].text:
                return Items[j]


    # выбор случайного урока/теста
    def Random_object(self, TEXT):
        driver = self.app.driver
        Objects = []
        Sub = driver.find_element_by_tag_name('h1')
        Text_sub = Sub.text  # название предмета
        Buttons_objects = driver.find_elements_by_class_name('info')  # список уроков и тестов и еще 4 кпоки, есть атрибут текст
        Lenght_buttons_objects = len(Buttons_objects)
        for i in range(4, Lenght_buttons_objects):
            Text_buttons_objects = Buttons_objects[i].text  # название теста/урока
            Lesson_or_test = Text_buttons_objects.split()
            if Lesson_or_test[0] == "ТЕСТ":
                Buttons_objects[i].click()
                if len(driver.find_element_by_id('testPurchaseBtn').text) != 0:
                    Objects.append(Buttons_objects[i])
                    Button_close = driver.find_elements_by_class_name('icon_close')[5]  # кнопка "Х"
                    Button_close.click()
                    self.Videocourse_subject()
                if len(driver.find_element_by_css_selector('p.not-found__title')) != 0:
                    self.Videocourse_subject()
            if Lesson_or_test[0] == "УРОК":
                Buttons_objects[i].click()
                if len(driver.find_elements_by_class_name('test-button')) != 0:
                    self.Videocourse_subject()
            Buttons_objects = driver.find_elements_by_class_name('info')
            Lenght_buttons_objects = len(Buttons_objects)
        Object_selection = choice(Objects)
        Object_selection.click()

    # нажимает видеокурсы-предмет
    def Videocourse_subject(self):
        driver = self.app.driver
        Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[1]
        Button_video_courses.click()  # после нажатия возвращает на список предметов
        if i < Lenght_buttons_objects:
            All_subjects = driver.find_elements_by_class_name('subject-card')
            Lenght_all_subjects = len(All_subjects)
            for j in range(0, Lenght_all_subjects):
                if Text_sub == All_subjects[j].text:
                    Button_sub = All_subjects[j]
            Button_sub.click()

    # оплата случайного урока/теста в одном предмете и возвращение на список предметов
    def Payment(self):
        driver = self.app.driver
        Button_payment = driver.find_element_by_id('testPurchaseBtn') # кнопка "Перейти к оплате"
        Button_payment.click()
        driver.close()
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
        Button_promocode = driver.find_elements_by_class_name('input')[0]
        Button_promocode.send_keys('Gsudjcjp3')
        Button_apply = driver.find_element_by_id('applyPromocode')
        Button_apply.click()

    # прохождение проверки безопасности для урока/теста и возвращение на список предметов
    def Security(self):
        driver = self.app.driver
        Button_phone = driver.find_element_by_name('phone')
        Button_phone.send_keys("79001234567")  # ввод номера телефона
        Button_send_code = driver.find_element_by_id('btnSendCode')
        Button_send_code.click()
        Button_sms_code = driver.find_element_by_name('sms_code')
        Button_sms_code.send_keys('554306')  # ввод смс кода
        Button_OK = driver.find_element_by_id('btnTestCode')
        Button_OK.click()  # после нажатия вы войдете в тест

