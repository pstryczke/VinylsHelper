import os
from typing import Optional, List, Iterable

from PyQt6.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox
from PyQt6.QtGui import QIcon, QImage, QPixmap
from PyQt6.QtCore import QCoreApplication, QEventLoop, Qt

from csv_handler import load_csv, save_csv
from functions import ScrappingFunctions
from gui import Ui_main_window


class EventHandlerEdit:
    def __init__(self, main_window: Ui_main_window):
        super().__init__()
        self.main_window = main_window
        self.start_directory = r'D:\PŁYTY'
        self.icon_path = '../discogs_ml/data/vinyl.ico'
        self.edit_flag = False
        self.current_image = 0
        self.images_dir = None
        self.images_list = None
        self.current_image_dir = None
        self.current_row_count = 0
        self.loop = QEventLoop()
        self.line_inputs = (
            self.main_window.artist_input_edit,
            self.main_window.title_input_edit,
            self.main_window.year_input_edit,
            self.main_window.category_input_edit,
            self.main_window.records_input_edit,
            self.main_window.vinyl_input_edit,
            self.main_window.cover_input_edit,
            self.main_window.information_input_edit,
            self.main_window.price_input_edit,
            self.main_window.image_name_input,
        )

    def add_vinyl(self) -> None:
        self.main_window.table_widget_edit.insertRow(self.current_row_count)
        for idx, line_input in enumerate(self.line_inputs):
            self.main_window.table_widget_edit.setItem(self.current_row_count, idx, QTableWidgetItem(line_input.text()))
        self.clear_input()
        self.current_row_count = self.main_window.table_widget_edit.rowCount()
        self.main_window.table_widget_edit.scrollToBottom()
        self.clicked_next_button()
        self.make_backup()

    def edit_vinyl(self, selected_row: int) -> None:
        for idx, line_input in enumerate(self.line_inputs):
            self.main_window.table_widget_edit.setItem(selected_row, idx, QTableWidgetItem(line_input.text()))
        self.clear_input()
        self.make_backup()

    def clear_input(self) -> None:
        for line_input in self.line_inputs:
            if line_input.isEnabled():
                line_input.clear()

    def check_selection(self) -> list:
        temp_list = list()
        indexes = self.main_window.table_widget_edit.selectionModel().selectedRows()
        for index in sorted(indexes):
            temp_list.append(index.row())
        temp_list.reverse()
        return temp_list

    def delete_vinyl(self) -> None:
        temp_selected = self.check_selection()
        if temp_selected:
            for selection_row in temp_selected:
                self.main_window.table_widget_edit.removeRow(selection_row)
            self.current_row_count = self.main_window.table_widget_edit.rowCount()
        else:
            self.main_window.table_widget_edit.removeRow(self.current_row_count - 1)
            self.current_row_count = self.main_window.table_widget_edit.rowCount()

    def make_backup(self):
        save_csv('backup.csv', self.parse_from_table())

    def save_csv(self):
        path = QFileDialog.getSaveFileName(self.main_window.central_widget,
                                           'Save File', self.start_directory, 'CSV(*.csv)')
        if path[0]:
            save_csv(path[0], self.parse_from_table())

    def load_csv(self):
        path = QFileDialog.getOpenFileName(self.main_window.central_widget,
                                           'Open File', self.start_directory, 'CSV(*.csv)')
        if path[0]:
            self.parse_to_table(load_csv(path[0]))

    def parse_from_table(self) -> List[list]:
        all_data = list()
        for row in range(self.main_window.table_widget_edit.rowCount()):
            row_data = list()
            for column in range(self.main_window.table_widget_edit.columnCount()):
                try:
                    item = self.main_window.table_widget_edit.item(row, column)
                    row_data.append(item.text())
                except AttributeError:
                    row_data.append('')
            all_data.append(row_data)
        return all_data

    def parse_to_table(self, reader: Iterable) -> None:
        self.main_window.table_widget_edit.setRowCount(0)
        for row_data in reader:
            self.main_window.table_widget_edit.scrollToBottom()
            row = self.main_window.table_widget_edit.rowCount()
            self.main_window.table_widget_edit.insertRow(row)
            self.main_window.table_widget_edit.setColumnCount(len(self.line_inputs))
            for column, data in enumerate(row_data):
                item = QTableWidgetItem(data)
                self.main_window.table_widget_edit.setItem(row, column, item)
            if len(row_data) < len(self.line_inputs):
                for idx in range(len(self.line_inputs) - len(row_data)):
                    item = QTableWidgetItem()
                    self.main_window.table_widget_edit.setItem(row, len(row_data) + idx, item)
        self.current_row_count = self.main_window.table_widget_edit.rowCount()

    def edit_record(self, current_row: Optional[int] = None) -> None:
        if current_row is not False:
            selected_row = current_row
        else:
            if self.check_selection():
                selected_row = self.check_selection()[0]
            else:
                information_dialog('Zaznacz płytę do edycji', 'Uwaga', icon_path=self.icon_path)
                return None
        self.edit_flag = True
        self.insert_selected_from_table(selected_row)
        self.main_window.table_widget_edit.selectRow(selected_row)
        self.change_buttons()

    def save_edited_record(self, current_row: Optional[int] = None) -> None:
        if current_row is not None:
            selected_row = current_row
        else:
            selected_row = self.check_selection()[0]
        self.edit_flag = False
        self.edit_vinyl(selected_row)
        self.change_buttons()

    def edit_multiple_records(self, from_number: Optional[int] = None) -> None:
        if self.edit_flag:
            self.edit_flag = False
            self.loop.quit()
            self.clear_input()
            self.main_window.save_vinyl_button.clicked.disconnect()
            self.main_window.save_vinyl_button.clicked.connect(self.save_edited_record)
            self.change_buttons()
        else:
            self.edit_flag = True
            self.main_window.save_vinyl_button.clicked.disconnect()
            self.main_window.save_vinyl_button.clicked.connect(self.wait_until_clicked)
            self.change_buttons()
            if from_number:
                from_number = from_number - 1
            else:
                from_number = 0
            for row in range(from_number, self.main_window.table_widget_edit.rowCount()):
                self.edit_record(row)
                self.loop.exec()
                if not self.edit_flag:
                    break
                self.save_edited_record(row)

    def edit_from_number(self) -> None:
        from_number = self.main_window.edit_vinyl_from_number_line.text()
        if from_number is not None and from_number.isnumeric():
            self.edit_multiple_records(int(from_number))
        else:
            information_dialog('Wprowadź prawidłową liczbę', 'Uwaga', icon_path=self.icon_path)

    def wait_until_clicked(self) -> None:
        self.loop.quit()

    def change_buttons(self) -> None:
        _translate = QCoreApplication.translate
        button_text = "Anuluj edycje" if self.edit_flag else "Wszystkie"
        self.main_window.add_vinyl_button.setEnabled(not self.edit_flag)
        self.main_window.delete_vinyl_button.setEnabled(not self.edit_flag)
        self.main_window.save_vinyl_button.setEnabled(self.edit_flag)
        self.main_window.edit_vinyl_all_button.setText(_translate("main_window", button_text))

    def insert_selected_from_table(self, selected_row) -> None:
        self.clear_input()
        for idx, line_input in enumerate(self.line_inputs):
            text = None
            if self.main_window.table_widget_edit.item(selected_row, idx) is not None:
                text = self.main_window.table_widget_edit.item(selected_row, idx).text()
            line_input.setText(text)

    def delete_vinyl_dialog(self) -> None:
        msg_box = QMessageBox()
        msg_box.setWindowIcon(QIcon(self.icon_path))
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setText("Czy na pewno chcesz usunąć wybrane płyty?")
        msg_box.setWindowTitle("Potwierdzenie usunięcia")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        return_value = msg_box.exec()
        if return_value == QMessageBox.StandardButton.Yes:
            self.delete_vinyl()
            
    def clicked_previous_button(self):
        self.current_image -= 1 if self.current_image > 0 else 0
        self.show_image()

    def clicked_next_button(self):
        if self.images_list:
            self.current_image += 1 if self.current_image < len(self.images_list) - 1 else 0
        self.show_image()
    
    def clicked_table_row(self):
        selected_row = self.check_selection()[0]
        if self.main_window.table_widget_edit.columnCount() == 9:
            image = self.main_window.table_widget_edit.item(selected_row, 9).text()
            self.show_image(image)
        
    def load_images(self):
        information = 'Wczytaj folder ze zdjęciami'
        path = QFileDialog.getExistingDirectory(self.main_window.central_widget, information, self.start_directory)
        if path:
            self.images_dir = path
            self.images_list = self._get_images_list()
            self._show_image()

    def _get_images_list(self):
        images_list = list()
        for file in os.listdir(self.images_dir):
            if file.split('.')[-1] in ('jpg', 'png', 'bmp'):
                images_list.append(file)
        return images_list

    def show_image(self, image_name: Optional[str] = None) -> None:
        if self.images_dir and self.images_list:
            self._show_image(image_name)
        else:
            information_dialog('Nie wybrano folderu ze zdjęciami!', 'Uwaga', icon_path=self.icon_path)

    def _show_image(self, image_name: Optional[str] = None) -> None:
        self.main_window.image_name_input.setText(self.images_list[self.current_image])
        image_name = self.images_list[self.current_image] if image_name is None else image_name
        current_image_dir = os.path.join(self.images_dir, image_name)
        image = QImage(current_image_dir)
        image = image.scaled(428, 321, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                             transformMode=Qt.TransformationMode.SmoothTransformation)
        self.main_window.vinyl_image_label_edit.setPixmap(QPixmap.fromImage(image))

    def scrap_data(self):
        url = self.main_window.url_input_edit.text()
        if not url:
            information_dialog('Wprowadź link', 'Uwaga', icon_path=self.icon_path)
        else:
            scrap = ScrappingFunctions(url)
            scrap.get_information()
            if scrap.data is not None:
                self.clear_input()
                self.main_window.artist_input_edit.setText(scrap.information_dict['artist'])
                self.main_window.title_input_edit.setText(scrap.information_dict['title'])
                self.main_window.year_input_edit.setText(scrap.information_dict['year'])
                self.main_window.category_input_edit.setText(scrap.information_dict['genre'])
                self.main_window.records_input_edit.setText(scrap.information_dict['record'])
                self.main_window.url_input_edit.clear()
            else:
                information_dialog('Wprowadzono błędny link', 'Uwaga', icon_path=self.icon_path)
                self.main_window.url_input_edit.clear()


def information_dialog(information: str, title: str, icon_path: Optional[str] = None):
    msg_box = QMessageBox()
    if icon_path:
        msg_box.setWindowIcon(QIcon(icon_path))
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setText(information)
    msg_box.setWindowTitle(title)
    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg_box.exec()
