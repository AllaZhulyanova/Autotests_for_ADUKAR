

# доступ к тестам с авторизацией, но без оплаты и проверки безопасности

def test_opening_test_with_authorization(app):
    app.Session.Log_in(Login = "vilas.gromov@mail.ru", Password = "rcvOn7BBrp")  # вход в ЛК
    app.Button_menu.Test_Button_Videocourses() # кнопка "Видеокурсы"
    result = app.List_items_after_autorization.List_items(TEXT='ТЕСТ')
    total_number_tests = result[0]
    total_number_tests_with_access = result[1]
    assert total_number_tests == total_number_tests_with_access
    app.Session.Log_out()    # выход из ЛК