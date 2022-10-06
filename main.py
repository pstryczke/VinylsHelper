# pyuic6 C:\Users\mrpst\PycharmProjects\VinylsHelper\img\VinylsHelper.ui -o gui.py
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QAbstractItemView

from events import EventHandlerEdit
from gui import Ui_main_window


class MyWindow(QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.event = EventHandlerEdit(self)
        self.initialize_events()

    def initialize_events(self):
        # self.scrap_button.clicked.connect(self.get_info_from_url)
        self.table_widget_edit.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.previous_image_button.clicked.connect(self.event.clicked_previous_button)
        self.next_image_button.clicked.connect(self.event.clicked_next_button)
        self.load_images_button.clicked.connect(self.event.load_images)
        self.table_widget_edit.clicked.connect(self.event.clicked_table_row)
        self.add_vinyl_button.clicked.connect(self.event.add_vinyl)
        self.save_vinyl_button.clicked.connect(self.event.save_edited_record)
        self.delete_vinyl_button.clicked.connect(self.event.delete_vinyl_dialog)
        self.edit_vinyl_all_button.clicked.connect(self.event.edit_multiple_records)
        self.edit_vinyl_single_button.clicked.connect(self.event.edit_record)
        self.edit_vinyl_from_number_button.clicked.connect(self.event.edit_from_number)
        self.load_csv_button_edit.clicked.connect(self.event.load_csv)
        self.save_csv_button_edit.clicked.connect(self.event.save_csv)
        self.save_vinyl_button.setEnabled(self.event.edit_flag)


def run_main():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    run_main()
