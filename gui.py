# Form implementation generated from reading ui file 'C:\Users\mrpst\PycharmProjects\VinylsHelper\img\VinylsHelper.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1040, 925)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QtCore.QSize(1040, 925))
        main_window.setMaximumSize(QtCore.QSize(1040, 925))
        main_window.setBaseSize(QtCore.QSize(1030, 905))
        self.central_widget = QtWidgets.QWidget(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.central_widget.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.central_widget.setObjectName("central_widget")
        self.tabWidget = QtWidgets.QTabWidget(self.central_widget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1041, 921))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.line_10 = QtWidgets.QFrame(self.tab)
        self.line_10.setGeometry(QtCore.QRect(450, 280, 571, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_10.setObjectName("line_10")
        self.frame_info_2 = QtWidgets.QFrame(self.tab)
        self.frame_info_2.setGeometry(QtCore.QRect(450, 10, 581, 281))
        self.frame_info_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_info_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_info_2.setObjectName("frame_info_2")
        self.line_2 = QtWidgets.QFrame(self.frame_info_2)
        self.line_2.setGeometry(QtCore.QRect(390, 60, 20, 181))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_11 = QtWidgets.QFrame(self.frame_info_2)
        self.line_11.setGeometry(QtCore.QRect(190, 150, 20, 91))
        self.line_11.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_11.setObjectName("line_11")
        self.widget_3 = QtWidgets.QWidget(self.frame_info_2)
        self.widget_3.setGeometry(QtCore.QRect(10, 90, 380, 30))
        self.widget_3.setObjectName("widget_3")
        self.label_year_4 = QtWidgets.QLabel(self.widget_3)
        self.label_year_4.setGeometry(QtCore.QRect(0, 5, 31, 16))
        self.label_year_4.setObjectName("label_year_4")
        self.title_input_edit = QtWidgets.QLineEdit(self.widget_3)
        self.title_input_edit.setEnabled(True)
        self.title_input_edit.setGeometry(QtCore.QRect(70, 5, 310, 20))
        self.title_input_edit.setObjectName("title_input_edit")
        self.widget_13 = QtWidgets.QWidget(self.frame_info_2)
        self.widget_13.setGeometry(QtCore.QRect(10, 120, 380, 30))
        self.widget_13.setObjectName("widget_13")
        self.label_year_11 = QtWidgets.QLabel(self.widget_13)
        self.label_year_11.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_11.setObjectName("label_year_11")
        self.artist_input_edit = QtWidgets.QLineEdit(self.widget_13)
        self.artist_input_edit.setEnabled(True)
        self.artist_input_edit.setGeometry(QtCore.QRect(70, 5, 310, 20))
        self.artist_input_edit.setObjectName("artist_input_edit")
        self.widget_14 = QtWidgets.QWidget(self.frame_info_2)
        self.widget_14.setGeometry(QtCore.QRect(10, 150, 180, 30))
        self.widget_14.setObjectName("widget_14")
        self.label_year_12 = QtWidgets.QLabel(self.widget_14)
        self.label_year_12.setGeometry(QtCore.QRect(0, 5, 31, 16))
        self.label_year_12.setObjectName("label_year_12")
        self.year_input_edit = QtWidgets.QLineEdit(self.widget_14)
        self.year_input_edit.setEnabled(True)
        self.year_input_edit.setGeometry(QtCore.QRect(70, 5, 110, 20))
        self.year_input_edit.setObjectName("year_input_edit")
        self.widget_15 = QtWidgets.QWidget(self.frame_info_2)
        self.widget_15.setGeometry(QtCore.QRect(10, 180, 180, 30))
        self.widget_15.setObjectName("widget_15")
        self.label_year_16 = QtWidgets.QLabel(self.widget_15)
        self.label_year_16.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_16.setObjectName("label_year_16")
        self.category_input_edit = QtWidgets.QLineEdit(self.widget_15)
        self.category_input_edit.setEnabled(True)
        self.category_input_edit.setGeometry(QtCore.QRect(70, 5, 110, 20))
        self.category_input_edit.setObjectName("category_input_edit")
        self.widget_16 = QtWidgets.QWidget(self.frame_info_2)
        self.widget_16.setGeometry(QtCore.QRect(10, 210, 180, 30))
        self.widget_16.setObjectName("widget_16")
        self.label_year_17 = QtWidgets.QLabel(self.widget_16)
        self.label_year_17.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_17.setObjectName("label_year_17")
        self.records_input_edit = QtWidgets.QLineEdit(self.widget_16)
        self.records_input_edit.setEnabled(True)
        self.records_input_edit.setGeometry(QtCore.QRect(70, 5, 110, 20))
        self.records_input_edit.setObjectName("records_input_edit")
        self.widget_17 = QtWidgets.QWidget(self.frame_info_2)
        self.widget_17.setGeometry(QtCore.QRect(210, 150, 180, 30))
        self.widget_17.setObjectName("widget_17")
        self.label_year_18 = QtWidgets.QLabel(self.widget_17)
        self.label_year_18.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_18.setObjectName("label_year_18")
        self.vinyl_input_edit = QtWidgets.QLineEdit(self.widget_17)
        self.vinyl_input_edit.setEnabled(True)
        self.vinyl_input_edit.setGeometry(QtCore.QRect(70, 5, 110, 20))
        self.vinyl_input_edit.setObjectName("vinyl_input_edit")
        self.widget_18 = QtWidgets.QWidget(self.frame_info_2)
        self.widget_18.setGeometry(QtCore.QRect(210, 180, 180, 30))
        self.widget_18.setObjectName("widget_18")
        self.label_year_19 = QtWidgets.QLabel(self.widget_18)
        self.label_year_19.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_19.setObjectName("label_year_19")
        self.cover_input_edit = QtWidgets.QLineEdit(self.widget_18)
        self.cover_input_edit.setEnabled(True)
        self.cover_input_edit.setGeometry(QtCore.QRect(70, 5, 110, 20))
        self.cover_input_edit.setObjectName("cover_input_edit")
        self.widget_19 = QtWidgets.QWidget(self.frame_info_2)
        self.widget_19.setGeometry(QtCore.QRect(210, 210, 180, 30))
        self.widget_19.setObjectName("widget_19")
        self.price_input_edit = QtWidgets.QLineEdit(self.widget_19)
        self.price_input_edit.setEnabled(True)
        self.price_input_edit.setGeometry(QtCore.QRect(70, 5, 110, 20))
        self.price_input_edit.setObjectName("price_input_edit")
        self.label_year_20 = QtWidgets.QLabel(self.widget_19)
        self.label_year_20.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_20.setObjectName("label_year_20")
        self.widget_20 = QtWidgets.QWidget(self.frame_info_2)
        self.widget_20.setGeometry(QtCore.QRect(10, 240, 561, 30))
        self.widget_20.setObjectName("widget_20")
        self.label_year_21 = QtWidgets.QLabel(self.widget_20)
        self.label_year_21.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_21.setObjectName("label_year_21")
        self.information_input_edit = QtWidgets.QLineEdit(self.widget_20)
        self.information_input_edit.setEnabled(True)
        self.information_input_edit.setGeometry(QtCore.QRect(70, 5, 491, 20))
        self.information_input_edit.setObjectName("information_input_edit")
        self.widget_21 = QtWidgets.QWidget(self.frame_info_2)
        self.widget_21.setGeometry(QtCore.QRect(10, 60, 381, 30))
        self.widget_21.setObjectName("widget_21")
        self.label_year_22 = QtWidgets.QLabel(self.widget_21)
        self.label_year_22.setGeometry(QtCore.QRect(0, 5, 51, 16))
        self.label_year_22.setObjectName("label_year_22")
        self.number_input_edit = QtWidgets.QLineEdit(self.widget_21)
        self.number_input_edit.setEnabled(True)
        self.number_input_edit.setGeometry(QtCore.QRect(70, 5, 221, 20))
        self.number_input_edit.setObjectName("number_input_edit")
        self.scrap_button = QtWidgets.QPushButton(self.widget_21)
        self.scrap_button.setGeometry(QtCore.QRect(292, 4, 90, 22))
        self.scrap_button.setObjectName("scrap_button")
        self.label_4 = QtWidgets.QLabel(self.frame_info_2)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line_14 = QtWidgets.QFrame(self.frame_info_2)
        self.line_14.setGeometry(QtCore.QRect(410, 230, 161, 20))
        self.line_14.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_14.setObjectName("line_14")
        self.image_add_label_2 = QtWidgets.QLabel(self.frame_info_2)
        self.image_add_label_2.setGeometry(QtCore.QRect(540, 180, 30, 30))
        self.image_add_label_2.setText("")
        self.image_add_label_2.setObjectName("image_add_label_2")
        self.offer_add_label_2 = QtWidgets.QLabel(self.frame_info_2)
        self.offer_add_label_2.setGeometry(QtCore.QRect(540, 210, 30, 30))
        self.offer_add_label_2.setText("")
        self.offer_add_label_2.setObjectName("offer_add_label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_info_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(410, 159, 160, 75))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edit_vinyl_single_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.edit_vinyl_single_button.setObjectName("edit_vinyl_single_button")
        self.horizontalLayout.addWidget(self.edit_vinyl_single_button)
        self.edit_vinyl_all_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.edit_vinyl_all_button.setObjectName("edit_vinyl_all_button")
        self.horizontalLayout.addWidget(self.edit_vinyl_all_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edit_vinyl_from_number_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.edit_vinyl_from_number_button.setObjectName("edit_vinyl_from_number_button")
        self.horizontalLayout_2.addWidget(self.edit_vinyl_from_number_button)
        self.edit_vinyl_from_number_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_vinyl_from_number_line.setObjectName("edit_vinyl_from_number_line")
        self.horizontalLayout_2.addWidget(self.edit_vinyl_from_number_line)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_info_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(410, 60, 160, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_vinyl_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.add_vinyl_button.setObjectName("add_vinyl_button")
        self.verticalLayout_2.addWidget(self.add_vinyl_button)
        self.save_vinyl_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.save_vinyl_button.setObjectName("save_vinyl_button")
        self.verticalLayout_2.addWidget(self.save_vinyl_button)
        self.delete_vinyl_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.delete_vinyl_button.setObjectName("delete_vinyl_button")
        self.verticalLayout_2.addWidget(self.delete_vinyl_button)
        self.line_12 = QtWidgets.QFrame(self.frame_info_2)
        self.line_12.setGeometry(QtCore.QRect(410, 140, 160, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_12.setObjectName("line_12")
        self.table_widget_edit = QtWidgets.QTableWidget(self.tab)
        self.table_widget_edit.setGeometry(QtCore.QRect(10, 350, 1011, 541))
        self.table_widget_edit.setObjectName("table_widget_edit")
        self.table_widget_edit.setColumnCount(10)
        self.table_widget_edit.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_edit.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_edit.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_edit.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_edit.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_edit.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_edit.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_edit.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_edit.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_edit.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_edit.setHorizontalHeaderItem(9, item)
        self.line_15 = QtWidgets.QFrame(self.tab)
        self.line_15.setGeometry(QtCore.QRect(10, 330, 1011, 20))
        self.line_15.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_15.setObjectName("line_15")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(453, 300, 561, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.layout_buttons_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.layout_buttons_2.setContentsMargins(0, 0, 0, 0)
        self.layout_buttons_2.setSpacing(6)
        self.layout_buttons_2.setObjectName("layout_buttons_2")
        self.previous_image_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.previous_image_button.setObjectName("previous_image_button")
        self.layout_buttons_2.addWidget(self.previous_image_button)
        self.next_image_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.next_image_button.setObjectName("next_image_button")
        self.layout_buttons_2.addWidget(self.next_image_button)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.layout_buttons_2.addItem(spacerItem)
        self.load_images_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.load_images_button.setObjectName("load_images_button")
        self.layout_buttons_2.addWidget(self.load_images_button)
        self.load_json_button_edit = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.load_json_button_edit.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.load_json_button_edit.setObjectName("load_json_button_edit")
        self.layout_buttons_2.addWidget(self.load_json_button_edit)
        self.save_json_button_edit = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.save_json_button_edit.setObjectName("save_json_button_edit")
        self.layout_buttons_2.addWidget(self.save_json_button_edit)
        self.vinyl_image_label_edit = QtWidgets.QLabel(self.tab)
        self.vinyl_image_label_edit.setGeometry(QtCore.QRect(10, 10, 428, 321))
        self.vinyl_image_label_edit.setText("")
        self.vinyl_image_label_edit.setScaledContents(True)
        self.vinyl_image_label_edit.setObjectName("vinyl_image_label_edit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_info = QtWidgets.QFrame(self.tab_2)
        self.frame_info.setGeometry(QtCore.QRect(450, 10, 581, 281))
        self.frame_info.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_info.setObjectName("frame_info")
        self.line = QtWidgets.QFrame(self.frame_info)
        self.line.setGeometry(QtCore.QRect(390, 60, 20, 181))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_4 = QtWidgets.QFrame(self.frame_info)
        self.line_4.setGeometry(QtCore.QRect(190, 150, 20, 91))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.widget = QtWidgets.QWidget(self.frame_info)
        self.widget.setGeometry(QtCore.QRect(10, 90, 380, 30))
        self.widget.setObjectName("widget")
        self.label_year_2 = QtWidgets.QLabel(self.widget)
        self.label_year_2.setGeometry(QtCore.QRect(0, 5, 31, 16))
        self.label_year_2.setObjectName("label_year_2")
        self.title_input = QtWidgets.QLineEdit(self.widget)
        self.title_input.setEnabled(False)
        self.title_input.setGeometry(QtCore.QRect(70, 5, 310, 20))
        self.title_input.setObjectName("title_input")
        self.widget_2 = QtWidgets.QWidget(self.frame_info)
        self.widget_2.setGeometry(QtCore.QRect(10, 120, 380, 30))
        self.widget_2.setObjectName("widget_2")
        self.label_year_3 = QtWidgets.QLabel(self.widget_2)
        self.label_year_3.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_3.setObjectName("label_year_3")
        self.artist_input = QtWidgets.QLineEdit(self.widget_2)
        self.artist_input.setEnabled(False)
        self.artist_input.setGeometry(QtCore.QRect(70, 5, 310, 20))
        self.artist_input.setObjectName("artist_input")
        self.widget_4 = QtWidgets.QWidget(self.frame_info)
        self.widget_4.setGeometry(QtCore.QRect(10, 150, 180, 30))
        self.widget_4.setObjectName("widget_4")
        self.label_year_5 = QtWidgets.QLabel(self.widget_4)
        self.label_year_5.setGeometry(QtCore.QRect(0, 5, 31, 16))
        self.label_year_5.setObjectName("label_year_5")
        self.year_input = QtWidgets.QLineEdit(self.widget_4)
        self.year_input.setEnabled(False)
        self.year_input.setGeometry(QtCore.QRect(70, 5, 110, 20))
        self.year_input.setObjectName("year_input")
        self.widget_5 = QtWidgets.QWidget(self.frame_info)
        self.widget_5.setGeometry(QtCore.QRect(10, 180, 180, 30))
        self.widget_5.setObjectName("widget_5")
        self.label_year_6 = QtWidgets.QLabel(self.widget_5)
        self.label_year_6.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_6.setObjectName("label_year_6")
        self.category_input = QtWidgets.QLineEdit(self.widget_5)
        self.category_input.setEnabled(False)
        self.category_input.setGeometry(QtCore.QRect(70, 5, 110, 20))
        self.category_input.setObjectName("category_input")
        self.widget_6 = QtWidgets.QWidget(self.frame_info)
        self.widget_6.setGeometry(QtCore.QRect(10, 210, 180, 30))
        self.widget_6.setObjectName("widget_6")
        self.label_year_7 = QtWidgets.QLabel(self.widget_6)
        self.label_year_7.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_7.setObjectName("label_year_7")
        self.records_input = QtWidgets.QLineEdit(self.widget_6)
        self.records_input.setEnabled(False)
        self.records_input.setGeometry(QtCore.QRect(70, 5, 110, 20))
        self.records_input.setObjectName("records_input")
        self.widget_7 = QtWidgets.QWidget(self.frame_info)
        self.widget_7.setGeometry(QtCore.QRect(210, 150, 180, 30))
        self.widget_7.setObjectName("widget_7")
        self.label_year_8 = QtWidgets.QLabel(self.widget_7)
        self.label_year_8.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_8.setObjectName("label_year_8")
        self.vinyl_input = QtWidgets.QLineEdit(self.widget_7)
        self.vinyl_input.setEnabled(False)
        self.vinyl_input.setGeometry(QtCore.QRect(70, 5, 110, 20))
        self.vinyl_input.setObjectName("vinyl_input")
        self.widget_8 = QtWidgets.QWidget(self.frame_info)
        self.widget_8.setGeometry(QtCore.QRect(210, 180, 180, 30))
        self.widget_8.setObjectName("widget_8")
        self.label_year_10 = QtWidgets.QLabel(self.widget_8)
        self.label_year_10.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_10.setObjectName("label_year_10")
        self.cover_input = QtWidgets.QLineEdit(self.widget_8)
        self.cover_input.setEnabled(False)
        self.cover_input.setGeometry(QtCore.QRect(70, 5, 110, 20))
        self.cover_input.setObjectName("cover_input")
        self.widget_9 = QtWidgets.QWidget(self.frame_info)
        self.widget_9.setGeometry(QtCore.QRect(210, 210, 180, 30))
        self.widget_9.setObjectName("widget_9")
        self.price_input = QtWidgets.QLineEdit(self.widget_9)
        self.price_input.setEnabled(False)
        self.price_input.setGeometry(QtCore.QRect(70, 5, 110, 20))
        self.price_input.setObjectName("price_input")
        self.label_year_15 = QtWidgets.QLabel(self.widget_9)
        self.label_year_15.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_15.setObjectName("label_year_15")
        self.widget_10 = QtWidgets.QWidget(self.frame_info)
        self.widget_10.setGeometry(QtCore.QRect(10, 240, 561, 30))
        self.widget_10.setObjectName("widget_10")
        self.label_year_13 = QtWidgets.QLabel(self.widget_10)
        self.label_year_13.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_year_13.setObjectName("label_year_13")
        self.information_input = QtWidgets.QLineEdit(self.widget_10)
        self.information_input.setEnabled(False)
        self.information_input.setGeometry(QtCore.QRect(70, 5, 491, 20))
        self.information_input.setObjectName("information_input")
        self.widget_11 = QtWidgets.QWidget(self.frame_info)
        self.widget_11.setGeometry(QtCore.QRect(10, 60, 180, 30))
        self.widget_11.setObjectName("widget_11")
        self.label_year_14 = QtWidgets.QLabel(self.widget_11)
        self.label_year_14.setGeometry(QtCore.QRect(0, 5, 51, 16))
        self.label_year_14.setObjectName("label_year_14")
        self.number_input = QtWidgets.QLineEdit(self.widget_11)
        self.number_input.setEnabled(False)
        self.number_input.setGeometry(QtCore.QRect(70, 5, 110, 20))
        self.number_input.setObjectName("number_input")
        self.label = QtWidgets.QLabel(self.frame_info)
        self.label.setGeometry(QtCore.QRect(10, 0, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.public_vinyl_button = QtWidgets.QPushButton(self.frame_info)
        self.public_vinyl_button.setGeometry(QtCore.QRect(410, 60, 161, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.public_vinyl_button.setFont(font)
        self.public_vinyl_button.setObjectName("public_vinyl_button")
        self.widget_12 = QtWidgets.QWidget(self.frame_info)
        self.widget_12.setGeometry(QtCore.QRect(410, 210, 161, 30))
        self.widget_12.setObjectName("widget_12")
        self.label_year_9 = QtWidgets.QLabel(self.widget_12)
        self.label_year_9.setGeometry(QtCore.QRect(0, 5, 151, 16))
        self.label_year_9.setObjectName("label_year_9")
        self.letter_input = QtWidgets.QLineEdit(self.widget_12)
        self.letter_input.setEnabled(True)
        self.letter_input.setGeometry(QtCore.QRect(100, 5, 61, 20))
        self.letter_input.setObjectName("letter_input")
        self.vinyl_image_label = QtWidgets.QLabel(self.tab_2)
        self.vinyl_image_label.setGeometry(QtCore.QRect(10, 10, 428, 321))
        self.vinyl_image_label.setText("")
        self.vinyl_image_label.setScaledContents(True)
        self.vinyl_image_label.setObjectName("vinyl_image_label")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(453, 300, 561, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.layout_buttons = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.layout_buttons.setContentsMargins(0, 0, 0, 0)
        self.layout_buttons.setObjectName("layout_buttons")
        self.load_json_button_post = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.load_json_button_post.setObjectName("load_json_button_post")
        self.layout_buttons.addWidget(self.load_json_button_post)
        self.layout_buttons.setStretch(0, 200)
        self.plain_text_input = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plain_text_input.setGeometry(QtCore.QRect(10, 700, 1011, 191))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.plain_text_input.setFont(font)
        self.plain_text_input.setPlainText("")
        self.plain_text_input.setObjectName("plain_text_input")
        self.line_7 = QtWidgets.QFrame(self.tab_2)
        self.line_7.setGeometry(QtCore.QRect(10, 330, 1011, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.table_widget = QtWidgets.QTableWidget(self.tab_2)
        self.table_widget.setGeometry(QtCore.QRect(10, 350, 1011, 341))
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(10)
        self.table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(9, item)
        self.line_5 = QtWidgets.QFrame(self.tab_2)
        self.line_5.setGeometry(QtCore.QRect(450, 280, 571, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.tabWidget.addTab(self.tab_2, "")
        main_window.setCentralWidget(self.central_widget)

        self.retranslateUi(main_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Wystawiacz Allegro"))
        self.label_year_4.setText(_translate("main_window", "Tytuł"))
        self.label_year_11.setText(_translate("main_window", "Wykonawca"))
        self.label_year_12.setText(_translate("main_window", "Rok"))
        self.label_year_16.setText(_translate("main_window", "Kategoria"))
        self.label_year_17.setText(_translate("main_window", "Wytwórnia"))
        self.label_year_18.setText(_translate("main_window", "Stan winyl"))
        self.label_year_19.setText(_translate("main_window", "Stan okładka"))
        self.label_year_20.setText(_translate("main_window", "Cena"))
        self.label_year_21.setText(_translate("main_window", "Informacje"))
        self.label_year_22.setText(_translate("main_window", "Link"))
        self.scrap_button.setText(_translate("main_window", "Pobierz Dane"))
        self.label_4.setText(_translate("main_window", "OBECNIE EDYTOWANE"))
        self.label_5.setText(_translate("main_window", "Edytuj płytę"))
        self.edit_vinyl_single_button.setText(_translate("main_window", "Pojedynczo"))
        self.edit_vinyl_all_button.setText(_translate("main_window", "Wszystkie"))
        self.edit_vinyl_from_number_button.setText(_translate("main_window", "Od numeru"))
        self.add_vinyl_button.setText(_translate("main_window", "Dodaj płytę"))
        self.save_vinyl_button.setText(_translate("main_window", "Zapisz edycję"))
        self.delete_vinyl_button.setText(_translate("main_window", "Usuń Płytę"))
        item = self.table_widget_edit.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "Wykonawca"))
        item = self.table_widget_edit.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "Tytuł"))
        item = self.table_widget_edit.horizontalHeaderItem(2)
        item.setText(_translate("main_window", "Rok"))
        item = self.table_widget_edit.horizontalHeaderItem(3)
        item.setText(_translate("main_window", "Kategoria"))
        item = self.table_widget_edit.horizontalHeaderItem(4)
        item.setText(_translate("main_window", "Wytwórnia"))
        item = self.table_widget_edit.horizontalHeaderItem(5)
        item.setText(_translate("main_window", "Stan winyl"))
        item = self.table_widget_edit.horizontalHeaderItem(6)
        item.setText(_translate("main_window", "Stan okładka"))
        item = self.table_widget_edit.horizontalHeaderItem(7)
        item.setText(_translate("main_window", "Informacje"))
        item = self.table_widget_edit.horizontalHeaderItem(8)
        item.setText(_translate("main_window", "Cena"))
        item = self.table_widget_edit.horizontalHeaderItem(9)
        item.setText(_translate("main_window", "Zdjęcie"))
        self.previous_image_button.setText(_translate("main_window", " Poprzednie zdjęcie "))
        self.next_image_button.setText(_translate("main_window", " Kolejne zdjęcie "))
        self.load_images_button.setText(_translate("main_window", " Wczytaj zdjęcia "))
        self.load_json_button_edit.setText(_translate("main_window", " Wczytaj Listę "))
        self.save_json_button_edit.setText(_translate("main_window", " Zapisz Listę "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("main_window", "Opisywanie plyt"))
        self.label_year_2.setText(_translate("main_window", "Tytuł"))
        self.label_year_3.setText(_translate("main_window", "Wykonawca"))
        self.label_year_5.setText(_translate("main_window", "Rok"))
        self.label_year_6.setText(_translate("main_window", "Kategoria"))
        self.label_year_7.setText(_translate("main_window", "Wytwórnia"))
        self.label_year_8.setText(_translate("main_window", "Stan winyl"))
        self.label_year_10.setText(_translate("main_window", "Stan okładka"))
        self.label_year_15.setText(_translate("main_window", "Cena"))
        self.label_year_13.setText(_translate("main_window", "Informacje"))
        self.label_year_14.setText(_translate("main_window", "Numer"))
        self.label.setText(_translate("main_window", "OBECNA PŁYTA DO WYSTAWIENIA"))
        self.public_vinyl_button.setText(_translate("main_window", "Wystaw płytę"))
        self.label_year_9.setText(_translate("main_window", "Litera początkowa:"))
        self.load_json_button_post.setText(_translate("main_window", " Wczytaj Listę "))
        item = self.table_widget.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "Wykonawca"))
        item = self.table_widget.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "Tytuł"))
        item = self.table_widget.horizontalHeaderItem(2)
        item.setText(_translate("main_window", "Rok"))
        item = self.table_widget.horizontalHeaderItem(3)
        item.setText(_translate("main_window", "Kategoria"))
        item = self.table_widget.horizontalHeaderItem(4)
        item.setText(_translate("main_window", "Wytwórnia"))
        item = self.table_widget.horizontalHeaderItem(5)
        item.setText(_translate("main_window", "Stan winyl"))
        item = self.table_widget.horizontalHeaderItem(6)
        item.setText(_translate("main_window", "Stan okładka"))
        item = self.table_widget.horizontalHeaderItem(7)
        item.setText(_translate("main_window", "Informacje"))
        item = self.table_widget.horizontalHeaderItem(8)
        item.setText(_translate("main_window", "Cena"))
        item = self.table_widget.horizontalHeaderItem(9)
        item.setText(_translate("main_window", "Wystawiono?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("main_window", "Wystawianie plyt"))
