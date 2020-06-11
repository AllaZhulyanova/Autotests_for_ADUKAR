from random import choice

class AfterAutorizationHelper:
    def __init__(self,app):
        self.app = app

    # выбор предмета по порядку с проверкой доступка к уроку/TT без оплаты, без проверки безопасности
    def List_items(self,TEXT):
        driver = self.app.driver
        All_tests = 0  # общее число тестов по всем предметам
        All_tests_with_access = 0  # доступ к общему числу тестов по всем предметам
        for i in range(0, len(driver.find_elements_by_class_name('subject-card'))): # цикл для предметов
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
            Items[i].click()  # нажимаем на предмет по порядку
            Buttons = driver.find_elements_by_class_name(
                'subject-number')  # список уроков и тестов, нет атрибута текст
            if len(Buttons) != 0:
                number_tests = self.List_of_paid_and_free_objects(TEXT)  # функция, которая нажимает на уроки/тесты по порядку
                All_tests = All_tests + number_tests[0]
                All_tests_with_access = All_tests_with_access + number_tests [1]
                Button_courses = driver.find_element_by_partial_link_text('курсы')  # кнопка "<- курсы"
                Button_courses.click()  # после нажатия возвращает на список предметов
        return All_tests, All_tests_with_access

    # проведение оплаты случайного урока/теста, но без проверки безопасности в платных предметах: Русс, Бел яз
    def Test_paid_items(self,TEXT,Promo_for_payment):
        driver = self.app.driver
        number_tests_before_payment = 0 # кол-во неоплаченных ТТ/тестов
        number_tests_after_payment = 0  # кол-во оплаченных ТТ/тестов
        for i in range(0, len(driver.find_elements_by_class_name('subject-card'))):   # цикл для предметов
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
            Items[i].click()  # нажимаем на предмет по порядку
            number_tests = self.Payment_objects(TEXT,Promo_for_payment)  # функция, которая нажимает на уроки/тесты по порядку
            number_tests_before_payment = number_tests_before_payment + number_tests[0]
            number_tests_after_payment = number_tests_after_payment + number_tests[1]
            Button_courses = driver.find_element_by_partial_link_text('курсы')  # кнопка "<- курсы"
            Button_courses.click()  # после нажатия возвращает на список предметов
        return number_tests_before_payment, number_tests_after_payment


    # выбор предмета по порядку с проведением оплаты и проверки безопасности ТТ/теста
    def List_of_paid_items_with_security(self,TEXT):
        driver = self.app.driver
        number_all_tests_after_security = 0 # общее кол-во разработанных ТТ/тестов
        number_all_tests_after_security_with_access = 0  # общее кол-во оплаченных ТТ/тестов
        #Selected_sub = self.Random_subject()
        #if Selected_sub == driver.find_elements_by_class_name('subject-card')[0] or Selected_sub == driver.find_elements_by_class_name('subject-card')[1]:  # сравнивает выбранную кнопку с Русс яз/Белор яз (там тесты и уроки платные)
        #    Selected_sub.click()
        #    self.Random_object(TEXT)
        #    self.Payment()
        #    self.Security()
        #    Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[1]
        #    Button_video_courses.click()  # после нажатия возвращает на список предметов
        #else:    # сравнивает выбранную кнопку с Англ яз/Биология (там тесты и уроки бесплатные)
        #    Selected_sub.click()
        #    self.Random_object(TEXT)
        #    self.Security()
        #    Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[1]
        #    Button_video_courses.click()  # после нажатия возвращает на список предметов
        #result = self.All_subject_after_payment(TEXT)
        #number_all_tests_after_security = result[0]
        #number_all_tests_after_security_with_access[1]
        #return number_all_tests_after_security, number_all_tests_after_security_with_access


    # выбор тестов/ТТ по порядку
    def List_of_paid_and_free_objects(self,TEXT):
        driver = self.app.driver
        Text_sub = driver.find_element_by_tag_name('h1').text  # название предмета
        kPaid = 0   # Кол-во всех разработанных уроков/тестов на странице
        nPaid = 0   # Кол-во уроков/тестов с доступ после оплаты
        for i in range(4, len(driver.find_elements_by_class_name('info'))):  # длина уроков/тестов
            Buttons_objects = driver.find_elements_by_class_name(
                'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
            Text_buttons_objects = Buttons_objects[i].text  # название теста/урока
            Lesson_or_test = Text_buttons_objects.split()
            if TEXT == Lesson_or_test[0] and TEXT == "ТЕСТ":
                Buttons_objects[i].click()
                kPaid = kPaid + 1
                if len(driver.find_elements_by_id('testPurchaseBtn')) != 0:
                    if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                        nPaid = nPaid + 1
                        Button_close = driver.find_elements_by_class_name('icon_close')[5]  # кнопка "Х"
                        Button_close.click()
                elif len(driver.find_elements_by_css_selector('p.not-found__title')) != 0:
                    if driver.find_element_by_css_selector('p.not-found__title').text == 'Проверка безопасности':
                        nPaid = nPaid + 1
                        driver.back()
                else:
                    print("Ошибка в доступе")
                    print("Предмет:", Text_sub)
                    print(Text_buttons_objects)
            elif TEXT == Lesson_or_test[0] and TEXT == "УРОК":
                Buttons_objects[i].click()
                driver.implicitly_wait(1)
                if len(driver.find_elements_by_class_name('test-button')) != 0 and len(
                        driver.find_element_by_tag_name('iframe').get_attribute("src")): # убеждаемся, что урок разработан
                    for j in range(0, len(driver.find_elements_by_class_name('test-button'))): # проходим по ТТ
                        Button_TT = driver.find_elements_by_class_name('test-button')  # ТТ1/ТТ2
                        Button_TT[j].click()
                        kPaid = kPaid + 1
                        if len(driver.find_elements_by_id('testPurchaseBtn')) != 0:
                            if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                                nPaid = nPaid + 1
                                driver.back()
                                Buttons_objects = driver.find_elements_by_class_name('info')
                                Buttons_objects[i].click()
                        elif len(driver.find_elements_by_css_selector('p.not-found__title')) != 0:
                            if driver.find_element_by_css_selector(
                                    'p.not-found__title').text == 'Проверка безопасности':
                                nPaid = nPaid + 1
                                driver.back()
                        else:
                            print("Ошибка в доступе")
                            print("Предмет:", Text_sub)
                            print(Text_buttons_objects)
                    Button_back = driver.find_element_by_css_selector('span.icon.icon_back')  # кнопка <- АДУКАР
                    Button_back.click()
            else:
                pass
        return kPaid,nPaid

       # оплата тестов/ТТ по порядку
    def Payment_objects(self,TEXT,Promo_for_payment):
        driver = self.app.driver
        kPaid = 0   # Кол-во всех разработанных уроков/тестов на странице
        nPaid = 0   # Кол-во уроков/тестов с доступ после оплаты
        for i in range(4, len(driver.find_elements_by_class_name('info'))): # длина уроков/тестов
            Buttons_objects = driver.find_elements_by_class_name(
                'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
            Text_buttons_objects = Buttons_objects[i].text  # название теста/урока
            Lesson_or_test = Text_buttons_objects.split()
            if TEXT == Lesson_or_test[0] and TEXT == "ТЕСТ":
                Text_sub = driver.find_element_by_tag_name('h1').text  # название предмета
                Buttons_objects[i].click()
                kPaid = kPaid + 1
                if len(driver.find_elements_by_id('testPurchaseBtn')) != 0:
                    if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                        Button_payment = driver.find_element_by_id('testPurchaseBtn')  # кнопка "Перейти к оплате"
                        Button_payment.click()
                        window_after = driver.window_handles[1]
                        driver.switch_to.window(window_after)
                        payment_state = self.Payment(Promo_for_payment)
                        if payment_state == "оплачено":
                            nPaid = nPaid + 1
                        else:
                            print("Статус оплаты",payment_state)
                            print("Предмет:", Text_sub)
                            print(Text_buttons_objects)
                    else:
                        print("Ошибка при оплате")
                        print("Предмет:", Text_sub)
                        print(Text_buttons_objects)
                elif len(driver.find_elements_by_css_selector('p.not-found__title')) != 0:
                    if driver.find_element_by_css_selector('p.not-found__title').text == 'Проверка безопасности':
                        nPaid = nPaid + 1
                        driver.back()
                    else:
                        print("Ошибка в проверке безопасности")
                        print("Предмет:", Text_sub)
                        print(Text_buttons_objects)
                else:
                    print("Ошибка в доступе")
                    print("Предмет:", Text_sub)
                    print(Text_buttons_objects)
            elif TEXT == Lesson_or_test[0] and TEXT == "УРОК":
                Buttons_objects[i].click()
                driver.implicitly_wait(1)
                if len(driver.find_elements_by_class_name('test-button')) != 0 and len(
                        driver.find_element_by_tag_name('iframe').get_attribute("src")):
                    for j in range(0, len(driver.find_elements_by_class_name('test-button'))):
                        Button_TT = driver.find_elements_by_class_name('test-button')  # ТТ1/ТТ2
                        Button_TT[j].click()
                        kPaid = kPaid + 1
                        if len(driver.find_elements_by_id('testPurchaseBtn')) != 0:
                            if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                                link_name = driver.find_element_by_id('testPurchaseBtn').get_attribute(
                                    "href")  # ссылка на оплату
                                driver.execute_script("window.open('','_blank');") # создание пустой ссылки
                                driver.switch_to.window(driver.window_handles[1]) # переход на пустую ссылку
                                driver.get(link_name)  # запуск ссылки с оплатой в новой вкладке
                                payment_state = self.Payment(Promo_for_payment)
                                if payment_state == "оплачено":
                                    nPaid = nPaid + 1
                                else:
                                    print("Статус оплаты", payment_state)
                                    print("Предмет:", Text_sub)
                                    print(Text_buttons_objects)
                            else:
                                print("Ошибка при оплате")
                                print("Предмет:", Text_sub)
                                print(Text_buttons_objects)
                        elif len(driver.find_elements_by_css_selector('p.not-found__title')) != 0:
                            if driver.find_element_by_css_selector(
                                    'p.not-found__title').text == 'Проверка безопасности':
                                nPaid = nPaid + 1
                                driver.back()
                            else:
                                print("Ошибка в проверке безопасности")
                                print("Предмет:", Text_sub)
                                print(Text_buttons_objects)
                        else:
                            print("Ошибка в доступе")
                            print("Предмет:", Text_sub)
                            print(Text_buttons_objects)
                    Button_back = driver.find_element_by_css_selector('span.icon.icon_back')  # кнопка <- АДУКАР
                    Button_back.click()
            else:
                pass
        return kPaid,nPaid


     # оплата урока/теста в одном предмете и возвращение на список предметов
    def Payment(self,Promo_for_payment):
        driver = self.app.driver
        window_before = driver.window_handles[0]
        Button_promocode = driver.find_elements_by_class_name('input')[0]
        Button_promocode.send_keys(Promo_for_payment) # ввод промокода
        Button_apply = driver.find_element_by_id('applyPromocode')
        Button_apply.click()  # оплатить
        driver.refresh()
        Button_status = driver.find_elements_by_css_selector('span.number')[2]
        Button_status_text = Button_status.text
        driver.close()
        driver.switch_to.window(window_before)
        driver.refresh()
        return Button_status_text

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