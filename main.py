# pyuic6 C:\Users\mrpst\PycharmProjects\VinylsHelper\img\VinylsHelper.ui -o gui.py
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication

from gui import Ui_main_window


class MyWindow(QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def run_main():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    run_main()
