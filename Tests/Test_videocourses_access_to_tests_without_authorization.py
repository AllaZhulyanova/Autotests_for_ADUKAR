

# Доступ к тесту без авторизации

def test_opening_test_without_authorization (app):
    app.Button_menu.Test_Button_Videocourses() # кнопка "Видеокурсы"
    result = app.List_items_without_payments.Test_list_of_all_items() # нажимает на тесты в предмете по порядку
    total_number_tests = result[0]
    total_number_tests_with_access = result[1]
    assert total_number_tests == total_number_tests_with_access


