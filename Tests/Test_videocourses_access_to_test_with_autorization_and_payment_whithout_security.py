

# доступ к тестам с авторизацией и оплатой, но без проверки безопасности

def test_opening_test_with_authorization_without_payment (app):
    app.Session.Log_in(Login = "ev.point9@mail.ru", Password = "jyD5PiFfad")  # вход в ЛК
    app.Button_menu.Test_Button_Videocourses() # кнопка "Видеокурсы"
    result = app.List_items_with_payments.List_of_paid_items()
    total_number_tests = result[0]
    total_number_tests_with_access = result[1]
    app.Session.Log_out()  # выход из ЛК
    assert total_number_tests == total_number_tests_with_access
    print ("После успешного выполнения теста создать нового пользователя АДУКАР")
    print('заменить логин и пароль в тесте Test_videocourses_access_to_tests_with_authorization_without_payment_and_security.py')