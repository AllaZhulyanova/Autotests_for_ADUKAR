

class ButtonMenuHelper:
    def __init__(self,app):
        self.app = app


    # кнопка "Видеокурсы"
    def Test_Button_Videocourses(self):
        driver = self.app.driver
        #driver.implicitly_wait(1)
        element = driver.find_elements_by_class_name('masthead-menu__item_third')[1]  # кнопка "Видеокурсы"
        button_video_courses = element.text  # выдает текст "Видеокурсы" и количество уроков
        text_button_video_courses = button_video_courses.split()
        text_video_courses = text_button_video_courses[0]
        print(text_video_courses)  # печатает текст "Видеокурсы"
        element.click()