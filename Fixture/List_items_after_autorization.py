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

    # проведение оплаты случайного урока/теста, без проверки безопасности
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
    def Test_security_items(self,TEXT,Promo_for_payment,Phone,Sms_code):
        driver = self.app.driver
        number_tests_before_security = 0 # кол-во неоплаченных ТТ/тестов
        number_tests_after_security = 0  # кол-во оплаченных ТТ/тестов
        number_of_security = 0  #кол-во проверок безопасности
        for i in range(0, len(driver.find_elements_by_class_name('subject-card'))):   # цикл для предметов
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
            Items[i].click()  # нажимаем на предмет по порядку
            number_tests = self.Secutity_objects(TEXT,Promo_for_payment,Phone,Sms_code)  # функция, которая нажимает на уроки/тесты по порядку
            number_tests_before_security = number_tests_before_security + number_tests[0]
            number_tests_after_security = number_tests_after_security + number_tests[1]
            number_of_security = number_of_security + number_tests[2]
            Button_courses = driver.find_element_by_partial_link_text('курсы')  # кнопка "<- курсы"
            Button_courses.click()  # после нажатия возвращает на список предметов
        return number_tests_before_security, number_tests_after_security, number_of_security

    # выбор предмета по порядку с выполенением заданий теста/ТТ и сохранением результатов
    def Test_saving_test_results(self,TEXT):
        driver = self.app.driver
        test_result = 0
        saved_test_result = 0
        for i in range(0, len(driver.find_elements_by_class_name('subject-card'))):   # цикл для предметов
            Items = driver.find_elements_by_class_name('subject-card')  # кнопка списка предметов
            Items[i].click()  # нажимаем на предмет по порядку
            self.Test_passing_objects(TEXT)


    # выбор тестов/ТТ по порядку
    def List_of_paid_and_free_objects(self,TEXT):
        driver = self.app.driver
        Text_sub = driver.find_element_by_tag_name('h1').text  # название предмета
        kTest = 0   # Кол-во всех разработанных уроков/тестов на странице
        nTest = 0   # Кол-во уроков/тестов с доступ после оплаты
        for i in range(4, len(driver.find_elements_by_class_name('info'))):  # длина уроков/тестов
            Buttons_objects = driver.find_elements_by_class_name(
                'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
            Text_buttons_objects = Buttons_objects[i].text  # название теста/урока
            Lesson_or_test = Text_buttons_objects.split()
            if TEXT == Lesson_or_test[0] and TEXT == "ТЕСТ":
                Buttons_objects[i].click()
                kTest = kTest + 1
                if len(driver.find_elements_by_id('testPurchaseBtn')) != 0:
                    if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                        nTest = nTest + 1
                        Button_close = driver.find_elements_by_class_name('icon_close')[5]  # кнопка "Х"
                        Button_close.click()
                elif len(driver.find_elements_by_css_selector('p.not-found__title')) != 0:
                    if driver.find_element_by_css_selector('p.not-found__title').text == 'Проверка безопасности':
                        nTest = nTest + 1
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
                        kTest = kTest + 1
                        if len(driver.find_elements_by_id('testPurchaseBtn')) != 0:
                            if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                                nTest = nTest + 1
                                driver.back()
                                Buttons_objects = driver.find_elements_by_class_name('info')
                                Buttons_objects[i].click()
                        elif len(driver.find_elements_by_css_selector('p.not-found__title')) != 0:
                            if driver.find_element_by_css_selector(
                                    'p.not-found__title').text == 'Проверка безопасности':
                                nTest = nTest + 1
                                driver.back()
                        else:
                            print("Ошибка в доступе")
                            print("Предмет:", Text_sub)
                            print(Text_buttons_objects)
                    Button_back = driver.find_element_by_css_selector('span.icon.icon_back')  # кнопка <- АДУКАР
                    Button_back.click()
            else:
                pass
        return kTest,nTest

       # оплата тестов/ТТ по порядку
    def Payment_objects(self,TEXT,Promo_for_payment):
        driver = self.app.driver
        kTest = 0   # Кол-во всех разработанных уроков/тестов на странице
        nTest = 0   # Кол-во уроков/тестов с доступ после оплаты
        for i in range(4, len(driver.find_elements_by_class_name('info'))): # длина уроков/тестов
            Buttons_objects = driver.find_elements_by_class_name(
                'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
            Text_buttons_objects = Buttons_objects[i].text  # название теста/урока
            Lesson_or_test = Text_buttons_objects.split()
            if TEXT == Lesson_or_test[0] and TEXT == "ТЕСТ":
                Text_sub = driver.find_element_by_tag_name('h1').text  # название предмета
                Buttons_objects[i].click()
                kTest = kTest + 1
                if len(driver.find_elements_by_id('testPurchaseBtn')) != 0:
                    if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                        Button_payment = driver.find_element_by_id('testPurchaseBtn')  # кнопка "Перейти к оплате"
                        Button_payment.click()
                        window_after = driver.window_handles[1]
                        driver.switch_to.window(window_after)
                        payment_state = self.Test_payment(Promo_for_payment)
                        if payment_state == "оплачено":
                            nTest = nTest + 1
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
                        nTest = nTest + 1
                        driver.back()
                    else:
                        print("Ошибка в проверке безопасности")
                        print("Предмет:", Text_sub)
                        print(Text_buttons_objects)
                else:
                    print("Ошибка в доступе при оплате")
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
                        kTest = kTest + 1
                        if len(driver.find_elements_by_id('testPurchaseBtn')) != 0:
                            if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                                link_name = driver.find_element_by_id('testPurchaseBtn').get_attribute(
                                    "href")  # ссылка на оплату
                                driver.execute_script("window.open('','_blank');") # создание пустой ссылки
                                driver.switch_to.window(driver.window_handles[1]) # переход на пустую ссылку
                                driver.get(link_name)  # запуск ссылки с оплатой в новой вкладке
                                payment_state = self.Test_payment(Promo_for_payment)
                                if payment_state == "оплачено":
                                    nTest = nTest + 1
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
                                nTest = nTest + 1
                                driver.back()
                            else:
                                print("Ошибка в проверке безопасности")
                                print("Предмет:", Text_sub)
                                print(Text_buttons_objects)
                        else:
                            print("Ошибка в доступе при оплате")
                            print("Предмет:", Text_sub)
                            print(Text_buttons_objects)
                    Button_back = driver.find_element_by_css_selector('span.icon.icon_back')  # кнопка <- АДУКАР
                    Button_back.click()
            else:
                pass
        return kTest,nTest

    # прохождение проверки безопасности для тестов/ТТ по порядку
    def Secutity_objects(self,TEXT,Promo_for_payment,Phone,Sms_code):
        driver = self.app.driver
        kTest = 0  # Кол-во всех разработанных уроков/тестов на странице
        nTest = 0  # Кол-во уроков/тестов с доступ после оплаты
        security_state = 0  # Кол-во проверок безопасности
        for i in range(4, len(driver.find_elements_by_class_name('info'))):  # длина уроков/тестов
            Buttons_objects = driver.find_elements_by_class_name(
                'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
            Text_buttons_objects = Buttons_objects[i].text  # название теста/урока
            Lesson_or_test = Text_buttons_objects.split()
            if TEXT == Lesson_or_test[0] and TEXT == "ТЕСТ":
                Text_sub = driver.find_element_by_tag_name('h1').text  # название предмета
                Buttons_objects[i].click()
                kTest = kTest + 1
                if len(driver.find_elements_by_id('testPurchaseBtn')) != 0: # для раздела "перейти к оплате"
                    if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                        Button_payment = driver.find_element_by_id('testPurchaseBtn')  # кнопка "Перейти к оплате"
                        Button_payment.click()
                        window_after = driver.window_handles[1]
                        driver.switch_to.window(window_after)
                        payment_state = self.Test_payment(Promo_for_payment)
                        if payment_state == "оплачено":
                            Buttons_objects = driver.find_elements_by_class_name('info')
                            Buttons_objects[i].click()
                            if len(driver.find_elements_by_css_selector('p.not-found__title'))!= 0:
                                if driver.find_element_by_css_selector('p.not-found__title').text == 'Проверка безопасности':
                                    security_state = self.Test_security(Phone, Sms_code)
                                    if security_state != 0:
                                        nTest = nTest + 1
                                        driver.back()
                            else:
                                if len(driver.find_elements_by_css_selector("div.inner")) != 0:
                                    nTest = nTest + 1
                                    driver.back()
                        else:
                            print("Пройти проверку безопасности без оплаты нет возможности")
                            print("Статус оплаты", payment_state)
                            print("Предмет:", Text_sub)
                            print(Text_buttons_objects)
                elif len(driver.find_elements_by_css_selector('p.not-found__title')) != 0:  # для раздела проверка безопасности
                    if driver.find_element_by_css_selector('p.not-found__title').text == 'Проверка безопасности':
                        security_state = self.Test_security(Phone,Sms_code)
                        if security_state != 0:
                            nTest = nTest + 1
                            driver.back()
                elif len(driver.find_elements_by_css_selector("div.inner")) != 0:
                        nTest = nTest + 1
                        driver.back()
                else:
                    print("Ошибка в доступе при прохождении проверки безопасности")
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
                        kTest = kTest + 1
                        if len(driver.find_elements_by_id('testPurchaseBtn')) != 0:  # Перейти к оплате
                            if driver.find_element_by_id('testPurchaseBtn').text == "Перейти к оплате":
                                link_name = driver.find_element_by_id('testPurchaseBtn').get_attribute(
                                    "href")  # ссылка на оплату
                                driver.execute_script("window.open('','_blank');")  # создание пустой ссылки
                                driver.switch_to.window(driver.window_handles[1])  # переход на пустую ссылку
                                driver.get(link_name)  # запуск ссылки с оплатой в новой вкладке
                                payment_state = self.Test_payment(Promo_for_payment)
                                if payment_state == "оплачено":
                                    Button_TT = driver.find_elements_by_class_name('test-button')  # ТТ1/ТТ2
                                    Button_TT[j].click()
                                    if len(driver.find_elements_by_css_selector('p.not-found__title')) != 0:
                                        if driver.find_element_by_css_selector(
                                                'p.not-found__title').text == 'Проверка безопасности':
                                            security_state = self.Test_security(Phone, Sms_code)
                                            if security_state != 0:
                                                nTest = nTest + 1
                                                driver.back()
                                    else:
                                        if len(driver.find_elements_by_css_selector("div.inner")) != 0:
                                            nTest = nTest + 1
                                            driver.back()
                                else:
                                    print("Пройти проверку безопасности без оплаты нет возможности")
                                    print("Статус оплаты", payment_state)
                                    print("Предмет:", Text_sub)
                                    print(Text_buttons_objects)
                        elif len(driver.find_elements_by_css_selector('p.not-found__title')) != 0: # Проверка безопасности
                            if driver.find_element_by_css_selector('p.not-found__title').text == 'Проверка безопасности':
                                security_state = self.Test_security(Phone, Sms_code)
                                if security_state != 0:
                                    nTest = nTest + 1
                                    driver.back()
                        elif len(driver.find_elements_by_css_selector("div.inner")) != 0:
                            nTest = nTest + 1
                            driver.back()
                        else:
                            print("Ошибка в доступе при прохождении проверки безопасности")
                            print("Предмет:", Text_sub)
                            print(Text_buttons_objects)
                    Button_back = driver.find_element_by_css_selector('span.icon.icon_back')  # кнопка <- АДУКАР
                    Button_back.click()
            else:
                pass
        return kTest, nTest, security_state

    # выполнение задание в тесте/ТТ по порядку
    def Test_passing_objects(self,TEXT):
        driver = self.app.driver
        for i in range(4, len(driver.find_elements_by_class_name('info'))):  # длина уроков/тестов
            Buttons_objects = driver.find_elements_by_class_name(
                'info')  # кнопка список уроков и тестов и еще 4 кпоки, есть атрибут текст
            Text_buttons_objects = Buttons_objects[i].text  # название теста/урока
            Lesson_or_test = Text_buttons_objects.split()
            if TEXT == Lesson_or_test[0] and TEXT == "ТЕСТ":
                Buttons_objects[i].click()
                Button_start_test = driver.find_element_by_css_selector('input#btnStart.button.button_red')
                Button_start_test.click()
                self.Test_passing()
            elif TEXT == Lesson_or_test[0] and TEXT == "УРОК":
                pass
            else:
                pass

     # оплата урока/теста в одном предмете и возвращение на список предметов
    def Test_payment(self,Promo_for_payment):
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
    def Test_security(self, Phone, Sms_code):
        driver = self.app.driver
        Number_of_security = 0
        Button_phone = driver.find_element_by_name('phone')
        Button_phone.send_keys(Phone)  # ввод номера телефона
        Button_send_code = driver.find_element_by_id('btnSendCode')
        Button_send_code.click() # нажать на кнопку "Получить код"
        Button_sms_code = driver.find_element_by_name('sms_code')
        Button_sms_code.send_keys(Sms_code)  # ввод смс кода
        Button_OK = driver.find_element_by_id('btnTestCode')
        Button_OK.click()  # нажать на кнопку "ОК", после нажатия вы войдете в тест
        driver.refresh()
        driver.implicitly_wait(1)
        if len(driver.find_elements_by_css_selector("div.inner")) != 0: # список тестов
            Number_of_security = Number_of_security + 1
        return Number_of_security

    # выполнение заданий в тесте/ТТ
    def Test_passing(self):
        driver = self.app.driver
        numder_tests = 0
        if len(driver.find_elements_by_class_name('number')) <= 17:
            for i in range(0, len(driver.find_elements_by_class_name('number'))):
                Job_numbers = driver.find_elements_by_class_name('number')
                Text_job_numbers = Job_numbers[i].text
                Letter_number = list(Text_job_numbers)
                Letter = Letter_number[0]
                print("**:"+Letter)
                Job_numbers[i].click()
                if Letter == 'A':
                    print("tyta")
                    self.List_of_response_options()
                elif Letter == 'B':
                    entry_field = driver.find_element_by_css_selector("input.input.input_large")
                    entry_field.send_keys("А1Б2В3Г4")
                    Button_answer = driver.find_element_by_id('btnSaveAnswer')
                    Button_answer.click()
                else:
                    pass
                print("zdesa")
        else:
            for j in range(0, 17):
                Job_numbers = driver.find_elements_by_class_name('number')
                Text_job_numbers = Job_numbers[j].text
                Letter_number = list(Text_job_numbers)
                Letter = Letter_number[0]
                print("##:"+Letter)
                Job_numbers[j].click()
                if Letter == 'A':
                    print("#####tyta")
                    self.List_of_response_options()
                elif Letter == 'B':
                    entry_field = driver.find_element_by_css_selector("input.input.input_large")
                    entry_field.send_keys("А1Б2В3Г4")
                    Button_answer = driver.find_element_by_id('btnSaveAnswer')
                    Button_answer.click()
                else:
                    pass
            print("####zdesa")
            driver.implicitly_wait(3)
            Button_close = driver.find_elements_by_class_name('close')[4]
            Button_close.click()
            for q in range(18,len(driver.find_elements_by_class_name('number'))):
                Job_numbers = driver.find_elements_by_class_name('number')
                Text_job_numbers = Job_numbers[q].text
                Letter_number = list(Text_job_numbers)
                Letter = Letter_number[0]
                print("&&&&&:" + Letter)
                Job_numbers[q].click()
                if Letter == 'A':
                    print("&&&&&&tyta")
                    self.List_of_response_options()
                elif Letter == 'B':
                    entry_field = driver.find_element_by_css_selector("input.input.input_large")
                    entry_field.send_keys("А1Б2В3Г4")
                    Button_answer = driver.find_element_by_id('btnSaveAnswer')
                    Button_answer.click()
                else:
                    pass
                print("&&&&&&zdesa")
        Test_result = driver.find_element_by_css_selector('span.test-result')
        print("da-da",Test_result.text)


    # Выбор варианта ответа
    def List_of_response_options(self):
        driver = self.app.driver
        Answer_options = []
        Button_answer_options = driver.find_elements_by_tag_name('label')
        Lenght_button_answer_options = len(Button_answer_options)
        for q in range(2, Lenght_button_answer_options):
            Answer_options.append(Button_answer_options[q])
        Random_answer_options = choice(Answer_options)
        driver.implicitly_wait(1)
        Random_answer_options.click()  # нажимаем на случайный вариант ответа
        Button_answer = driver.find_element_by_id('btnSaveAnswer')
        Button_answer.click()

