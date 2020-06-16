
# сохранение результатов теста после прохождения
def test_opening_test_with_authorization_without_payment(app):
    app.Session.Log_in(Login = "ev.point36@mail.ru", Password = "WQm38BfoD8")  # вход в ЛК
    #app.Session.Log_in(Login = "ev.point37@mail.ru", Password = "YEN8ljewZD")  # вход в ЛК
    #app.Session.Log_in(Login = "ev.point39@mail.ru", Password = "NjugNXgbiZ")  # вход в ЛК
    # app.Session.Log_in(Login = "ev.point40@mail.ru", Password = "jyunnzajNG")  # вход в ЛК
    #app.Session.Log_in(Login = "ev.point42@mail.ru", Password = "ZIurKR2Xch")  # вход в ЛК
    #app.Session.Log_in(Login = "ev.point43@mail.ru", Password = "YX0CF5eORO")  # вход в ЛК
    #app.Session.Log_in(Login = "ev.point44@mail.ru", Password = "lgkcDTYJ86")  # вход в ЛК
    #app.Session.Log_in(Login = "ev.point49@mail.ru", Password = "qsYPVm8ny8")  # вход в ЛК
    #app.Session.Log_in(Login = "ev.point47@mail.ru", Password = "dSuSTCGywO")  # вход в ЛК
    app.Button_menu.Test_Button_Videocourses() # кнопка "Видеокурсы"
    app.List_items_after_autorization.Test_saving_test_results(TEXT="ТЕСТ")
    #finish_test_results = test_results[0]
    #saving_test_results = test_results[1]
    app.Session.Log_out()  # выход из ЛК
    #assert finish_test_results == saving_test_results
