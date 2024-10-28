from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.ta.ta_landing_window import Ui_TaLandingWindow
from ui.ta.ta_goToActiveCourse_logic import TAGoToActiveCourseLogic
# from ui.ta.ta_view_courses_logic import TAViewCoursesLogic
# from ui.ta.ta_change_password_logic import TAChangePasswordLogic


class TALandingLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()
        self.ui = Ui_TaLandingWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window

        self.ui.pushButton.clicked.connect(self.go_to_active_course)
        # self.ui.pushButton_2.clicked.connect(self.view_courses)
        # self.ui.pushButton_3.clicked.connect(self.change_password)
        self.ui.pushButton_5.clicked.connect(self.handle_back)


    def go_to_active_course(self):
        self.ui_goToActiveCourse = TAGoToActiveCourseLogic(self)
        self.ui_goToActiveCourse.show()
        self.close()

    # def view_courses(self):
    #     self.ui_viewCourses = TAViewCoursesLogic(self)
    #     self.ui_viewCourses.show()
    #     self.close()    

    # def change_password(self):
    #     self.ui_changePassword = TAChangePasswordLogic(self)
    #     self.ui_changePassword.show()  
    #     self.close()

    def handle_back(self):
        self.previous_window.show()
        self.close()
