from random import choice

class AfterAutorizationHelper:
    def __init__(self,app):
        self.app = app

    # выбор предмета по порядку с проверкой доступка к уроку/TT без оплаты, без проверки безопасности
    def List_items(self,TEXT):
        driver = self.app.driver
        number_all_paid_tests = 0 # общее кол-во платных тестов по всем предметам
        number_all_paid_tests_with_access = 0  # общее кол-во платных тестов по всем предметам с доступом
        number_all_free_tests = 0 # общее кол-во беслпатных тестов по всем предметам
        number_all_free_tests_with_access = 0  # общее кол-во бесплатных тестов по всем предметам с доступ
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

    # проведение оплаты случайного урока/теста, но без проверки безопасности в платных предметах: Русс, Бел яз
    def List_of_paid_items(self,TEXT):
        driver = self.app.driver
        number_all_tests_before_payment = 0 # общее кол-во ТТ/тестов
        number_all_tests_after_payment = 0  # общее кол-во оплаченных ТТ/тестов
        for i in range(0, 2):    # цикл для платных предметов
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
            Items[i].click()  # нажимаем на предмет по порядку
            Text_sub = driver.find_element_by_tag_name('h1').text  # название предмета
            if len(driver.find_elements_by_class_name('subject-number')) != 0: # кол-во уроков/тестов
                self.Random_object(TEXT)  # выбор случайного урока/теста
                self.Payment()  # оплата
                driver.implicitly_wait(1)
                Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[1]
                Button_video_courses.click()  # после нажатия возвращает на список предметов
                for j in range(0, 2):
                    Items = driver.find_elements_by_class_name('subject-card')
                    if Text_sub == Items[j].text:
                        Subject = Items[j]
                Items[i] = Subject
        #result = self.All_subject_after_payment(TEXT)
        #number_all_tests_after_payment = result[0]
        #number_all_tests_after_payment_with_access = result[1]
        #return number_all_tests_after_payment, number_all_tests_after_payment_with_access

    # перебор всех предметов по порядку после оплаты
    def All_subject_after_payment(self, TEXT):
        driver = self.app.driver
        number_all_tests = 0  # кол-во всех уроков/тестов
        number_all_tests_with_access = 0  # кол-во оплаченных уроков/тестов
        Lenght_Items = len(driver.find_elements_by_class_name('subject-card'))
        for j in range(0, Lenght_Items):  # цикл для бесплатных предметов
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
            Items[j].click()  # нажимаем на предмет по порядку
            Lenght_Objects = len(driver.find_elements_by_class_name('subject-number'))
            if Lenght_Objects != 0:
                number_tests = self.List_of_free_objects(TEXT)  # функция, которая нажимает на уроки/тесты по порядку
                number_all_tests = number_all_tests + number_tests[0]
                number_all_tests_with_access = number_all_tests_with_access + number_tests[1]
                Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[1]
                Button_video_courses.click()  # после нажатия возвращает на список предметов
            Lenght_Items = len(driver.find_elements_by_class_name('subject-card'))
        return number_all_tests, number_all_tests_with_access

    # выбор предмета по порядку с проведением оплаты и проверки безопасности ТТ/теста
    def List_of_paid_items_with_security(self,TEXT):
        driver = self.app.driver
        number_all_tests_after_security = 0 # общее кол-во разработанных ТТ/тестов
        number_all_tests_after_security_with_access = 0  # общее кол-во оплаченных ТТ/тестов
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


    # выбор тестов/ТТ по порядку для платных предметов: русский, белорусский
    def List_of_paid_objects(self,TEXT):
        driver = self.app.driver
        Text_sub = driver.find_element_by_tag_name('h1').text  # название предмета
        kPaid = 0   # Кол-во всех разработанных уроков/тестов на странице
        nPaid = 0   # Кол-во уроков/тестов с доступ после оплаты
        Lenght_buttons_objects = len(driver.find_elements_by_class_name('info'))
        for i in range(4, Lenght_buttons_objects):
            Buttons_objects = driver.find_elements_by_class_name(
                'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
            Text_buttons_objects = Buttons_objects[i].text  # название теста/урока
            Lesson_or_test = Text_buttons_objects.split()
            if TEXT == Lesson_or_test[0] and TEXT == "ТЕСТ":
                Buttons_objects[i].click()
                kPaid = kPaid + 1
                if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                    nPaid = nPaid + 1
                    Button_close = driver.find_elements_by_class_name('icon_close')[5]  # кнопка "Х"
                    Button_close.click()
                else:
                    print("Ошибка в доступе")
                    print("Предмет:", Text_sub)
                    print(Text_buttons_objects)
            elif TEXT == Lesson_or_test[0] and TEXT == "УРОК":
                Buttons_objects[i].click()
                driver.implicitly_wait(1)
                if len(driver.find_elements_by_class_name('test-button')) != 0 and len(
                        driver.find_element_by_tag_name('iframe').get_attribute("src")):
                    Lenght_buttons_TT = len(driver.find_elements_by_class_name('test-button'))
                    for j in range(0, Lenght_buttons_TT):
                        Button_TT = driver.find_elements_by_class_name('test-button')  # ТТ1/ТТ2
                        Button_TT[j].click()
                        kPaid = kPaid + 1
                        if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                            nPaid = nPaid + 1
                            driver.back()
                            Buttons_objects = driver.find_elements_by_class_name('info')
                            Buttons_objects[i].click()
                        else:
                            print("Ошибка в доступе")
                            print("Предмет:", Text_sub)
                            print(Text_buttons_objects)
                            print(Button_TT[j].text)
                        Lenght_buttons_TT = len(driver.find_elements_by_class_name('test-button'))
                    Button_back = driver.find_element_by_class_name('icon_back')  # кнопка <- АДУКАР
                    Button_back.click()
            else:
                pass
            Lenght_buttons_objects = len(driver.find_elements_by_class_name('info'))
        return kPaid,nPaid

    # выбор уроков/ТТ по порядку для бесплатных предметов: английский, биология
    def List_of_free_objects(self,TEXT):
        driver = self.app.driver
        Text_sub = driver.find_element_by_tag_name('h1').text  # название предмета
        kFree = 0   # Кол-во всех разработанных уроков/тестов на странице
        nFree = 0   # Кол-во уроков/тестов для которых есть доступ после оплаты
        Lenght_buttons_objects = len(driver.find_elements_by_class_name('info'))
        for i in range(4, Lenght_buttons_objects):
            Buttons_objects = driver.find_elements_by_class_name('info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
            Text_buttons_objects = Buttons_objects[i].text
            Lesson_or_test = Text_buttons_objects.split()
            if TEXT == Lesson_or_test[0] and TEXT == 'ТЕСТ':
                Buttons_objects[i].click()
                kFree = kFree + 1
                if driver.find_element_by_css_selector('p.not-found__title').text == 'Проверка безопасности':
                    nFree = nFree + 1
                    driver.back()
                else:
                    print("Ошибка в доступе")
                    print("Предмет", Text_sub)
                    print(Text_buttons_objects)
            elif TEXT == Lesson_or_test[0] and TEXT == 'УРОК':
                Buttons_objects[i].click()
                driver.implicitly_wait(1)
                if len(driver.find_elements_by_class_name('test-button')) != 0 and len(
                        driver.find_element_by_tag_name('iframe').get_attribute("src")):
                    Lenght_buttons_TT = len(driver.find_elements_by_class_name('test-button'))
                    for j in range(0, Lenght_buttons_TT):
                        Button_TT = driver.find_elements_by_class_name('test-button')  # ТТ1/ТТ2
                        Button_TT[j].click()
                        kFree = kFree + 1
                        if driver.find_element_by_css_selector('p.not-found__title').text == 'Проверка безопасности':
                            nFree = nFree + 1
                            driver.back()
                        else:
                            print("Ошибка в доступе")
                            print("Предмет:", Text_sub)
                            print(Text_buttons_objects)
                        Lenght_buttons_TT = len(driver.find_elements_by_class_name('test-button'))
                    Button_back = driver.find_element_by_class_name('icon_back')  # кнопка <- АДУКАР
                    Button_back.click()
            else:
                pass
            Lenght_buttons_objects = len(driver.find_elements_by_class_name('info'))
        return kFree,nFree


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


    # выбор случайного теста/TT
    def Random_object(self, TEXT):
        driver = self.app.driver
        List_tests = []
        List_lessons = []
        List_TT = []
        num_TT = 0
        Lenght_buttons_objects = len(driver.find_elements_by_class_name('info'))
        for i in range(4, Lenght_buttons_objects):
            Buttons_objects = driver.find_elements_by_class_name('info')  # список уроков и тестов и еще 4 кпоки
            Text_buttons_objects = Buttons_objects[i].text  # название теста/урока
            Lesson_or_test = Text_buttons_objects.split()
            if TEXT == Lesson_or_test[0] and TEXT == "ТЕСТ":
                Buttons_objects[i].click()
                if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                    List_tests.append(Buttons_objects[i])
                    Button_close = driver.find_elements_by_class_name('icon_close')[5]  # кнопка "Х"
                    Button_close.click()
            elif TEXT == Lesson_or_test[0] and TEXT == "УРОК":
                Buttons_objects[i].click()
                driver.implicitly_wait(1)
                if len(driver.find_elements_by_class_name('test-button')) != 0 and len(
                        driver.find_element_by_tag_name('iframe').get_attribute("src")) != 0:
                    Lenght_buttons_TT = len(driver.find_elements_by_class_name('test-button'))
                    for j in range(0, Lenght_buttons_TT):
                        Button_TT = driver.find_elements_by_class_name('test-button')  # ТТ1/ТТ2
                        Button_TT[j].click()
                        if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                            num_TT = num_TT + 1
                            driver.back()
                            Buttons_objects = driver.find_elements_by_class_name('info')
                            Buttons_objects[i].click()
                        Lenght_buttons_TT = len(driver.find_elements_by_class_name('test-button'))
                    if len(driver.find_elements_by_class_name('test-button')) == num_TT:
                        List_lessons.append(Buttons_objects[i])
                    Button_back = driver.find_element_by_class_name('icon_back')  # кнопка <- АДУКАР
                    Button_back.click()
            else:
                pass
            Lenght_buttons_objects = len(driver.find_elements_by_class_name('info'))
        driver.implicitly_wait(1)
        if TEXT == 'ТЕСТ':
            Object_selection = choice(List_tests)
            driver.implicitly_wait(2)
            print(';;;;;',Object_selection.text)
            Object_selection.click()
        else:
            Object_selection = choice(List_lessons)
            driver.implicitly_wait(1)
            Object_selection.click()
            Lenght_buttons_TT = len(driver.find_elements_by_class_name('test-button'))
            for q in range(0, Lenght_buttons_TT):
                Button_TT = driver.find_elements_by_class_name('test-button')  # ТТ1/ТТ2
                List_TT.append(Button_TT[q])
            TT_selection = choice(List_TT)
            TT_selection.click()

     # оплата случайного урока/теста в одном предмете и возвращение на список предметов
    def Payment(self):
        driver = self.app.driver
        Button_payment = driver.find_element_by_id('testPurchaseBtn') # кнопка "Перейти к оплате"
        Button_payment.click()
        driver.close()
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
        Button_promocode = driver.find_elements_by_class_name('input')[0]
        Button_promocode.send_keys('Gsudjcjp3') # ввод промокода
        Button_apply = driver.find_element_by_id('applyPromocode')
        Button_apply.click()  # оплатить

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