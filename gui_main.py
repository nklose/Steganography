# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:/steganography/main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 576)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.group_image = QtGui.QGroupBox(self.centralwidget)
        self.group_image.setGeometry(QtCore.QRect(10, 10, 1001, 291))
        self.group_image.setObjectName(_fromUtf8("group_image"))
        self.lbl_image = QtGui.QLabel(self.group_image)
        self.lbl_image.setGeometry(QtCore.QRect(180, 20, 451, 261))
        self.lbl_image.setAutoFillBackground(False)
        self.lbl_image.setFrameShape(QtGui.QFrame.Panel)
        self.lbl_image.setFrameShadow(QtGui.QFrame.Raised)
        self.lbl_image.setText(_fromUtf8(""))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setObjectName(_fromUtf8("lbl_image"))
        self.lbl_filename = QtGui.QLabel(self.group_image)
        self.lbl_filename.setGeometry(QtCore.QRect(10, 20, 161, 21))
        self.lbl_filename.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_filename.setObjectName(_fromUtf8("lbl_filename"))
        self.btn_load = QtGui.QPushButton(self.group_image)
        self.btn_load.setGeometry(QtCore.QRect(10, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_load.setFont(font)
        self.btn_load.setObjectName(_fromUtf8("btn_load"))
        self.lbl_spacing = QtGui.QLabel(self.group_image)
        self.lbl_spacing.setGeometry(QtCore.QRect(20, 150, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_spacing.setFont(font)
        self.lbl_spacing.setObjectName(_fromUtf8("lbl_spacing"))
        self.box_spacing = QtGui.QSpinBox(self.group_image)
        self.box_spacing.setGeometry(QtCore.QRect(90, 150, 71, 22))
        self.box_spacing.setMinimum(1)
        self.box_spacing.setMaximum(100)
        self.box_spacing.setProperty("value", 32)
        self.box_spacing.setObjectName(_fromUtf8("box_spacing"))
        self.radio_decode = QtGui.QRadioButton(self.group_image)
        self.radio_decode.setGeometry(QtCore.QRect(20, 120, 151, 17))
        self.radio_decode.setChecked(False)
        self.radio_decode.setObjectName(_fromUtf8("radio_decode"))
        self.radio_encode = QtGui.QRadioButton(self.group_image)
        self.radio_encode.setGeometry(QtCore.QRect(20, 90, 141, 17))
        self.radio_encode.setChecked(True)
        self.radio_encode.setObjectName(_fromUtf8("radio_encode"))
        self.verticalLayoutWidget = QtGui.QWidget(self.group_image)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(640, 20, 160, 131))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.layout_labels = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_labels.setSpacing(12)
        self.layout_labels.setObjectName(_fromUtf8("layout_labels"))
        self.lbl_height = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_height.setFont(font)
        self.lbl_height.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_height.setObjectName(_fromUtf8("lbl_height"))
        self.layout_labels.addWidget(self.lbl_height)
        self.lbl_width = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_width.setFont(font)
        self.lbl_width.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_width.setObjectName(_fromUtf8("lbl_width"))
        self.layout_labels.addWidget(self.lbl_width)
        self.lbl_format = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_format.setFont(font)
        self.lbl_format.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_format.setObjectName(_fromUtf8("lbl_format"))
        self.layout_labels.addWidget(self.lbl_format)
        self.lbl_size = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_size.setFont(font)
        self.lbl_size.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_size.setObjectName(_fromUtf8("lbl_size"))
        self.layout_labels.addWidget(self.lbl_size)
        self.lbl_max_length = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_max_length.setFont(font)
        self.lbl_max_length.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_max_length.setObjectName(_fromUtf8("lbl_max_length"))
        self.layout_labels.addWidget(self.lbl_max_length)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.group_image)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(810, 20, 181, 130))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.layout_values = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_values.setSpacing(12)
        self.layout_values.setObjectName(_fromUtf8("layout_values"))
        self.lbl_height_value = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_height_value.setFont(font)
        self.lbl_height_value.setObjectName(_fromUtf8("lbl_height_value"))
        self.layout_values.addWidget(self.lbl_height_value)
        self.lbl_width_value = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_width_value.setFont(font)
        self.lbl_width_value.setObjectName(_fromUtf8("lbl_width_value"))
        self.layout_values.addWidget(self.lbl_width_value)
        self.lbl_format_value = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_format_value.setFont(font)
        self.lbl_format_value.setObjectName(_fromUtf8("lbl_format_value"))
        self.layout_values.addWidget(self.lbl_format_value)
        self.lbl_size_value = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_size_value.setFont(font)
        self.lbl_size_value.setObjectName(_fromUtf8("lbl_size_value"))
        self.layout_values.addWidget(self.lbl_size_value)
        self.lbl_max_length_value = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_max_length_value.setFont(font)
        self.lbl_max_length_value.setObjectName(_fromUtf8("lbl_max_length_value"))
        self.layout_values.addWidget(self.lbl_max_length_value)
        self.lbl_spacing_info = QtGui.QLabel(self.group_image)
        self.lbl_spacing_info.setGeometry(QtCore.QRect(20, 180, 141, 71))
        self.lbl_spacing_info.setWordWrap(True)
        self.lbl_spacing_info.setObjectName(_fromUtf8("lbl_spacing_info"))
        self.lbl_status = QtGui.QLabel(self.group_image)
        self.lbl_status.setGeometry(QtCore.QRect(640, 160, 351, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_status.setFont(font)
        self.lbl_status.setFrameShape(QtGui.QFrame.Panel)
        self.lbl_status.setFrameShadow(QtGui.QFrame.Sunken)
        self.lbl_status.setLineWidth(2)
        self.lbl_status.setScaledContents(False)
        self.lbl_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status.setWordWrap(True)
        self.lbl_status.setIndent(-1)
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))
        self.group_message = QtGui.QGroupBox(self.centralwidget)
        self.group_message.setGeometry(QtCore.QRect(10, 310, 1001, 261))
        self.group_message.setObjectName(_fromUtf8("group_message"))
        self.text_message = QtGui.QTextEdit(self.group_message)
        self.text_message.setGeometry(QtCore.QRect(180, 20, 811, 191))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(9)
        self.text_message.setFont(font)
        self.text_message.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.text_message.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_message.setObjectName(_fromUtf8("text_message"))
        self.btn_load_text_file = QtGui.QPushButton(self.group_message)
        self.btn_load_text_file.setGeometry(QtCore.QRect(10, 22, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_load_text_file.setFont(font)
        self.btn_load_text_file.setObjectName(_fromUtf8("btn_load_text_file"))
        self.lbl_num_characters = QtGui.QLabel(self.group_message)
        self.lbl_num_characters.setGeometry(QtCore.QRect(180, 220, 811, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        self.lbl_num_characters.setFont(font)
        self.lbl_num_characters.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num_characters.setObjectName(_fromUtf8("lbl_num_characters"))
        self.lbl_message_info = QtGui.QLabel(self.group_message)
        self.lbl_message_info.setGeometry(QtCore.QRect(10, 60, 151, 91))
        self.lbl_message_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_message_info.setWordWrap(True)
        self.lbl_message_info.setObjectName(_fromUtf8("lbl_message_info"))
        self.lbl_allowed_symbols = QtGui.QLabel(self.group_message)
        self.lbl_allowed_symbols.setGeometry(QtCore.QRect(20, 140, 151, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.lbl_allowed_symbols.setFont(font)
        self.lbl_allowed_symbols.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_allowed_symbols.setWordWrap(True)
        self.lbl_allowed_symbols.setObjectName(_fromUtf8("lbl_allowed_symbols"))
        self.btn_process = QtGui.QPushButton(self.group_message)
        self.btn_process.setGeometry(QtCore.QRect(830, 220, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_process.setFont(font)
        self.btn_process.setAcceptDrops(False)
        self.btn_process.setAutoFillBackground(False)
        self.btn_process.setAutoDefault(True)
        self.btn_process.setDefault(True)
        self.btn_process.setObjectName(_fromUtf8("btn_process"))
        self.lbl_spacing_info_2 = QtGui.QLabel(self.centralwidget)
        self.lbl_spacing_info_2.setGeometry(QtCore.QRect(890, 0, 131, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(109, 109, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 109, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.lbl_spacing_info_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lbl_spacing_info_2.setFont(font)
        self.lbl_spacing_info_2.setWordWrap(True)
        self.lbl_spacing_info_2.setObjectName(_fromUtf8("lbl_spacing_info_2"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Nick\'s Image Steganography", None))
        self.group_image.setTitle(_translate("MainWindow", "Image Settings", None))
        self.lbl_filename.setText(_translate("MainWindow", "<no image selected>", None))
        self.btn_load.setText(_translate("MainWindow", "Load Image", None))
        self.lbl_spacing.setText(_translate("MainWindow", "Spacing:", None))
        self.box_spacing.setToolTip(_translate("MainWindow", "Default: 32", None))
        self.radio_decode.setText(_translate("MainWindow", "Decode Image", None))
        self.radio_encode.setText(_translate("MainWindow", "Encode Message", None))
        self.lbl_height.setText(_translate("MainWindow", "Height:", None))
        self.lbl_width.setText(_translate("MainWindow", "Width:", None))
        self.lbl_format.setText(_translate("MainWindow", "Format:", None))
        self.lbl_size.setText(_translate("MainWindow", "Size:", None))
        self.lbl_max_length.setText(_translate("MainWindow", "Max Message Length:", None))
        self.lbl_height_value.setText(_translate("MainWindow", "0 px", None))
        self.lbl_width_value.setText(_translate("MainWindow", "0 px", None))
        self.lbl_format_value.setText(_translate("MainWindow", "NONE", None))
        self.lbl_size_value.setText(_translate("MainWindow", "0 bytes", None))
        self.lbl_max_length_value.setText(_translate("MainWindow", "0 characters", None))
        self.lbl_spacing_info.setText(_translate("MainWindow", "This value selects how many pixels are skipped for every encoded pixel. Lower values will affect the image more.", None))
        self.lbl_status.setText(_translate("MainWindow", "This mode allows you to select an image file and enter a message below. When you are finished, click Process.", None))
        self.group_message.setTitle(_translate("MainWindow", "Message", None))
        self.btn_load_text_file.setText(_translate("MainWindow", "Load Text File", None))
        self.lbl_num_characters.setText(_translate("MainWindow", "0 / 0 characters", None))
        self.lbl_message_info.setText(_translate("MainWindow", "Enter the message you would like to encode into the box. Whitespace characters will be converted into spaces. English letters, numbers, and spaces are supported, plus the following characters:                ", None))
        self.lbl_allowed_symbols.setText(_translate("MainWindow", "!\"#$%&\'()\\              *+-,/:;<=>         ?@[]^_`{|}~", None))
        self.btn_process.setText(_translate("MainWindow", "Process", None))
        self.lbl_spacing_info_2.setText(_translate("MainWindow", "Copyright © 2015 Nick Klose", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

