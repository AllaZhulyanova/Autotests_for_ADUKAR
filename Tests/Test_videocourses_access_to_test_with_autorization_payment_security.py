
# доступ к тестам с авторизацией, оплатой, проверкой безопасности не доработан

def test_opening_test_with_authorization_without_payment (app):
    app.Session.Log_in(Login = "ev.point11@mail.ru", Password = "6QFvkM7gh0")  # вход в ЛК
    app.Button_menu.Test_Button_Videocourses() # кнопка "Видеокурсы"
    app.List_items_after_autorization.List_of_paid_items_with_security(TEXT="ТЕСТ")
    result = app.List_items_after_autorization.All_subject_after_payment(TEXT='ТЕСТ')
    total_number_tests = result[0]
    total_number_tests_with_access = result[1]
    app.Session.Log_out()  # выход из ЛК
    assert total_number_tests == total_number_tests_with_access
    print ("После успешного выполнения теста создать нового пользователя АДУКАР")
    print('заменить логин и пароль в тесте Test_videocourses_access_to_tests_with_authorization_without_payment_and_security.py')