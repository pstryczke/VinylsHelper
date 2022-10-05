import csv
from typing import List, Iterable

def save_csv(file: str, data: List[list]):
    with open(file, 'w', encoding="utf8", newline='') as stream:
        writer = csv.writer(stream, delimiter=';')
        for row in data:
            # row_data = []
            # for column in range(columns):
            #     try:
            #         item = self.table_widget_edit.item(row, column)
            #     except Exception as e:
            #         print(repr(e))
            #         item = None
            #     if item is not None:
            #         row_data.append(item.text())
            #     else:
            #         row_data.append('')
            writer.writerow(row)

def load_csv(file: str) -> Iterable:
    with open(file, 'r', encoding="utf8") as stream:
        # self.table_widget_edit.setRowCount(0)
        return csv.reader(stream, delimiter=';')
        # for row_data in reader:
        #     self.table_widget_edit.scrollToBottom()
        #     row = self.table_widget_edit.rowCount()
        #     self.table_widget_edit.insertRow(row)
        #     self.table_widget_edit.setColumnCount(len(row_data))
        #     for column, data in enumerate(row_data):
        #         item = QTableWidgetItem(data)
        #         self.table_widget_edit.setItem(row, column, item)
        # self.current_row_count = self.table_widget_edit.rowCount()