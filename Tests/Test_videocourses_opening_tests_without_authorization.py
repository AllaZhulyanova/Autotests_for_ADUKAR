

# Доступ к тесту без авторизации

def test_opening_test_without_authorization (app):
    app.Button_menu.Test_Button_Videocourses() # кнопка "Видеокурсы"
    app.List_items_without_payments.Test_list_items() # выбор случайного предмета