from PyQt5 import QtWidgets
from frontend import myui
from backend import my_code
import sys


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)
        self.setWindowTitle('Comment Scrap')
        self.start()

    def start(self):
        form = QtWidgets.QWidget()
        ui = myui()
        ui.setupUi(form)
        my_code(ui, self)
        self.setCentralWidget(form)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    win = MyWindow()
    win.show()

    sys.exit(app.exec_())
