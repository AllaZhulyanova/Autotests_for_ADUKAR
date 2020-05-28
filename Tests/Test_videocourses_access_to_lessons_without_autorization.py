

# Доступ к уроку без авторизации

def test_opening_lesson_without_authorization (app):
    app.Button_menu.Test_Button_Videocourses() # кнопка "Видеокурсы"
    result = app.List_items_before_autorization.Test_list_of_all_items(TEXT='УРОК') # нажимает на тесты в предмете по порядку
    total_number_tests = result[0]
    total_number_tests_with_access = result[1]
    assert total_number_tests == total_number_tests_with_access