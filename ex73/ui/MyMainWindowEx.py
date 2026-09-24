from math import sqrt

from CHAPTER5.ex73.libs.my_module import solve_quadratic
from CHAPTER5.ex73.ui.MyMainWindow import Ui_MainWindow


class MyMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow #luu o nho de tai su dung, neu khong luu thi KH thao tac xong se mat luon
        self.setupSignalAndSlot()

    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_calc.clicked. connect(self.solve_quadratic)

    def solve_quadratic(self):
        try:
            a = float(self.valueALineEdit.text())
            b = float(self.valueBLineEdit.text())
            c = float(self.valueCLineEdit.text())

            result_str = solve_quadratic(a, b, c)

            self.resultLineEdit.setText(result_str)

        except ValueError:
            self.resultLineEdit.setText("Vui lòng nhập số hợp lệ!")