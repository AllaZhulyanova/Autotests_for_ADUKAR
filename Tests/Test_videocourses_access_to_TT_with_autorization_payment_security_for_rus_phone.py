
# доступ к ТТ урока после авторизации, оплаты и прохождение проверки безопасности с помощью российского номера телефона

def test_opening_test_with_authorization_without_payment (app):
    app.Session.Log_in(Login = "ev.point51@mail.ru", Password = "a0BoPi0jmF")  # вход в ЛК
    app.Button_menu.Test_Button_Videocourses() # кнопка "Видеокурсы"
    result_wiht_blr_phone = app.List_items_after_autorization.Test_security_items(TEXT="УРОК",Promo_for_payment='Gsudjcjp3',Phone='+79001111111',Sms_code='554306')
    total_number_tests_for_blr_phone = result_wiht_blr_phone[0] # число тестов до проверки безопасности
    total_number_tests_with_access_for_blr_phone = result_wiht_blr_phone[1] # число тестов после проверки безопасности
    total_number_of_security = result_wiht_blr_phone[2] # кол-во проверок безопасности
    app.Session.Log_out()  # выход из ЛК
    assert total_number_tests_for_blr_phone == total_number_tests_with_access_for_blr_phone
    assert total_number_of_security == 1 # в видеокурсах новый авторизованный пользователь должен выполнить обязательно 1 раз проверку безопасности
    print("После успешного выполнения теста создать нового пользователя АДУКАР")
    print('заменить логин и пароль в тесте Test_videocourses_access_to_TT_with_authorization_payment_security_for_blr_phone.py')