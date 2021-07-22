from PyQt5 import QtWidgets, QtCore
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
from configparser import ConfigParser
import files_rc
import glob
import os
import sys
import getpass
import datetime

config = ConfigParser()
config.read('config.cfg')
path = config.get("Settings", 'systempath')
filename = ""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
        # endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
                                 "QToolTip {\n"
                                 "	color: #ffffff;\n"
                                 "	background-color: rgba(27, 29, 35, 160);\n"
                                 "	border: 1px solid rgb(40, 40, 40);\n"
                                 "	border-radius: 2px;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
                                         "color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
                                      "QLineEdit {\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(27, 29, 35);\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "	border: 2px solid rgb(91, 101, 124);\n"
                                      "}\n"
                                      "\n"
                                      "/* SCROLL BARS */\n"
                                      "QScrollBar:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    height: 14px;\n"
                                      "    margin: 0px 21px 0 21px;\n"
                                      "	border-radius: 0px;\n"
                                      "}\n"
                                      "QScrollBar::handle:horizontal {\n"
                                      "    background: rgb(85, 170, 255);\n"
                                      "    min-width: 25px;\n"
                                      "	border-radius: 7px\n"
                                      "}\n"
                                      "QScrollBar::add-line:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "    width: 20px;\n"
                                      "	border-top-right-radius: 7px;\n"
                                      "    border-bottom-right-radius: 7px;\n"
                                      "    subcontrol-position: right;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::sub-line:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "    width: 20px;\n"
                                      ""
                                      "	border-top-left-radius: 7px;\n"
                                      "    border-bottom-left-radius: 7px;\n"
                                      "    subcontrol-position: left;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
                                      "{\n"
                                      "     background: none;\n"
                                      "}\n"
                                      "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                      "{\n"
                                      "     background: none;\n"
                                      "}\n"
                                      " QScrollBar:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    width: 14px;\n"
                                      "    margin: 21px 0 21px 0;\n"
                                      "	border-radius: 0px;\n"
                                      " }\n"
                                      " QScrollBar::handle:vertical {	\n"
                                      "	background: rgb(85, 170, 255);\n"
                                      "    min-height: 25px;\n"
                                      "	border-radius: 7px\n"
                                      " }\n"
                                      " QScrollBar::add-line:vertical {\n"
                                      "     border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "     height: 20px;\n"
                                      "	border-bottom-left-radius: 7px;\n"
                                      "    border-bottom-right-radius: 7px;\n"
                                      "     subcontrol-position: bottom;\n"
                                      "     subcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::sub-line:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(55, 63"
                                      ", 77);\n"
                                      "     height: 20px;\n"
                                      "	border-top-left-radius: 7px;\n"
                                      "    border-top-right-radius: 7px;\n"
                                      "     subcontrol-position: top;\n"
                                      "     subcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      "/* CHECKBOX */\n"
                                      "QCheckBox::indicator {\n"
                                      "    border: 3px solid rgb(52, 59, 72);\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius: 10px;\n"
                                      "    background: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QCheckBox::indicator:hover {\n"
                                      "    border: 3px solid rgb(58, 66, 81);\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "    background: 3px solid rgb(52, 59, 72);\n"
                                      "	border: 3px solid rgb(52, 59, 72);	\n"
                                      "	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
                                      "}\n"
                                      "\n"
                                      "/* RADIO BUTTON */\n"
                                      "QRadioButton::indicator {\n"
                                      "    border: 3px solid rgb(52, 59, 72);\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius"
                                      ": 10px;\n"
                                      "    background: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QRadioButton::indicator:hover {\n"
                                      "    border: 3px solid rgb(58, 66, 81);\n"
                                      "}\n"
                                      "QRadioButton::indicator:checked {\n"
                                      "    background: 3px solid rgb(94, 106, 130);\n"
                                      "	border: 3px solid rgb(52, 59, 72);	\n"
                                      "}\n"
                                      "\n"
                                      "/* COMBOBOX */\n"
                                      "QComboBox{\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(27, 29, 35);\n"
                                      "	padding: 5px;\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QComboBox::drop-down {\n"
                                      "	subcontrol-origin: padding;\n"
                                      "	subcontrol-position: top right;\n"
                                      "	width: 25px; \n"
                                      "	border-left-width: 3px;\n"
                                      "	border-left-color: rgba(39, 44, 54, 150);\n"
                                      "	border-left-style: solid;\n"
                                      "	border-top-right-radius: 3px;\n"
                                      "	border-bottom-right-radius: 3px;	\n"
                                      "	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
                                      "	background-position: center;\n"
                                      "	background-repeat: no-reperat;\n"
                                      " }\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "	color: rgb("
                                      "85, 170, 255);	\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	padding: 10px;\n"
                                      "	selection-background-color: rgb(39, 44, 54);\n"
                                      "}\n"
                                      "\n"
                                      "/* SLIDERS */\n"
                                      "QSlider::groove:horizontal {\n"
                                      "    border-radius: 9px;\n"
                                      "    height: 18px;\n"
                                      "	margin: 0px;\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QSlider::groove:horizontal:hover {\n"
                                      "	background-color: rgb(55, 62, 76);\n"
                                      "}\n"
                                      "QSlider::handle:horizontal {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "    border: none;\n"
                                      "    height: 18px;\n"
                                      "    width: 18px;\n"
                                      "    margin: 0px;\n"
                                      "	border-radius: 9px;\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:hover {\n"
                                      "    background-color: rgb(105, 180, 255);\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:pressed {\n"
                                      "    background-color: rgb(65, 130, 195);\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::groove:vertical {\n"
                                      "    border-radius: 9px;\n"
                                      "    width: 18px;\n"
                                      "    margin: 0px;\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QSlider::groove:vertical:hover {\n"
                                      "	background-color: rgb(55, 62, 76);\n"
                                      "}\n"
                                      "QSlider::handle:verti"
                                      "cal {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "	border: none;\n"
                                      "    height: 18px;\n"
                                      "    width: 18px;\n"
                                      "    margin: 0px;\n"
                                      "	border-radius: 9px;\n"
                                      "}\n"
                                      "QSlider::handle:vertical:hover {\n"
                                      "    background-color: rgb(105, 180, 255);\n"
                                      "}\n"
                                      "QSlider::handle:vertical:pressed {\n"
                                      "    background-color: rgb(65, 130, 195);\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
                                           "	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                           "	background-position: center;\n"
                                           "	background-repeat: no-reperat;\n"
                                           "	border: none;\n"
                                           "	background-color: rgb(27, 29, 35);\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "	background-color: rgb(33, 37, 43);\n"
                                           "}\n"
                                           "QPushButton:pressed {	\n"
                                           "	background-color: rgb(85, 170, 255);\n"
                                           "}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)

        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
                                              "background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
                                              "background-position: center;\n"
                                              "background-repeat: no-repeat;\n"
                                              "")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
                                               "")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)

        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
                                        "	border: none;\n"
                                        "	background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "	background-color: rgb(85, 170, 255);\n"
                                        "}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
                                                "	border: none;\n"
                                                "	background-color: transparent;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "	background-color: rgb(52, 59, 72);\n"
                                                "}\n"
                                                "QPushButton:pressed {	\n"
                                                "	background-color: rgb(85, 170, 255);\n"
                                                "}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
                                     "	border: none;\n"
                                     "	background-color: transparent;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "	background-color: rgb(52, 59, 72);\n"
                                     "}\n"
                                     "QPushButton:pressed {	\n"
                                     "	background-color: rgb(85, 170, 255);\n"
                                     "}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)

        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 11))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)

        self.verticalLayout_2.addWidget(self.frame_top_info)

        self.horizontalLayout_3.addWidget(self.frame_top_right)

        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
                                           "	border-radius: 30px;\n"
                                           "	background-color: rgb(44, 49, 60);\n"
                                           "	border: 5px solid rgb(39, 44, 54);\n"
                                           "	background-position: center;\n"
                                           "	background-repeat: no-repeat;\n"
                                           "}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")

        ################################# SEARCH PAGE #################################
        self.searchWidget = QWidget()
        self.searchWidget.setObjectName(u"searchWidget")
        self.searchWidget_verticalLayout = QVBoxLayout(self.searchWidget)
        self.searchWidget_verticalLayout.setObjectName(u"searchWidget_verticalLayout")

        self.frame_searchBox = QFrame(self.searchWidget)
        self.frame_searchBox.setObjectName(u"frame_searchBox")
        self.frame_searchBox.setStyleSheet(u"border-radius: 5px;")
        self.frame_searchBox.setFrameShape(QFrame.StyledPanel)
        self.frame_searchBox.setFrameShadow(QFrame.Raised)
        self.searchBox_verticalLayout = QVBoxLayout(self.frame_searchBox)
        self.searchBox_verticalLayout.setSpacing(0)
        self.searchBox_verticalLayout.setObjectName(u"searchBox_verticalLayout")
        self.searchBox_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_searchBoxContents = QFrame(self.frame_searchBox)
        self.frame_searchBoxContents.setObjectName(u"frame_searchBoxContents")
        self.frame_searchBoxContents.setMinimumSize(QSize(0, 110))
        self.frame_searchBoxContents.setMaximumSize(QSize(16777215, 110))
        self.frame_searchBoxContents.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
                                                   "border-radius: 5px;\n"
                                                   "")
        self.frame_searchBoxContents.setFrameShape(QFrame.NoFrame)
        self.frame_searchBoxContents.setFrameShadow(QFrame.Raised)
        self.searchBoxContents_verticalLayout = QVBoxLayout(self.frame_searchBoxContents)
        self.searchBoxContents_verticalLayout.setSpacing(0)
        self.searchBoxContents_verticalLayout.setObjectName(u"searchBoxContents_verticalLayout")
        self.searchBoxContents_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_searchBoxTitle = QFrame(self.frame_searchBoxContents)
        self.frame_searchBoxTitle.setObjectName(u"frame_title_wid_1")
        self.frame_searchBoxTitle.setMaximumSize(QSize(16777215, 35))
        self.frame_searchBoxTitle.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_searchBoxTitle.setFrameShape(QFrame.StyledPanel)
        self.frame_searchBoxTitle.setFrameShadow(QFrame.Raised)
        self.searchBoxTitle_verticalLayout = QVBoxLayout(self.frame_searchBoxTitle)
        self.searchBoxTitle_verticalLayout.setObjectName(u"searchBoxTitle_verticalLayout")
        self.searchLabel = QLabel(self.frame_searchBoxTitle)
        self.searchLabel.setObjectName(u"searchLabel")
        self.searchLabel.setFont(font1)
        self.searchLabel.setStyleSheet(u"")

        self.searchBoxTitle_verticalLayout.addWidget(self.searchLabel)

        self.searchBoxContents_verticalLayout.addWidget(self.frame_searchBoxTitle)

        self.frame_content_wid_1 = QFrame(self.frame_searchBoxContents)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.searchInput = QLineEdit(self.frame_content_wid_1)
        self.searchInput.setObjectName(u"searchInput")
        self.searchInput.setMinimumSize(QSize(0, 30))
        self.searchInput.setStyleSheet(u"QLineEdit {\n"
                                       "	background-color: rgb(27, 29, 35);\n"
                                       "	border-radius: 5px;\n"
                                       "	border: 2px solid rgb(27, 29, 35);\n"
                                       "	padding-left: 10px;\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "	border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "	border: 2px solid rgb(91, 101, 124);\n"
                                       "}")

        self.gridLayout.addWidget(self.searchInput, 0, 0, 1, 1)

        self.searchGo = QPushButton(self.frame_content_wid_1)
        self.searchGo.setObjectName(u"searchGo")
        self.searchGo.setMinimumSize(QSize(150, 30))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)
        self.searchGo.setFont(font8)
        self.searchGo.setStyleSheet(u"QPushButton {\n"
                                    "	border: 2px solid rgb(52, 59, 72);\n"
                                    "	border-radius: 5px;	\n"
                                    "	background-color: rgb(52, 59, 72);\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(57, 65, 80);\n"
                                    "	border: 2px solid rgb(61, 70, 86);\n"
                                    "}\n"
                                    "QPushButton:pressed {	\n"
                                    "	background-color: rgb(35, 40, 49);\n"
                                    "	border: 2px solid rgb(43, 50, 61);\n"
                                    "}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchGo.setIcon(icon3)

        self.gridLayout.addWidget(self.searchGo, 0, 1, 1, 1)
        self.searchGo.clicked.connect(self.searchClick)

        self.searchExample = QLabel(self.frame_content_wid_1)
        self.searchExample.setObjectName(u"searchExample")
        self.searchExample.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.searchExample.setLineWidth(1)
        self.searchExample.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.searchExample, 1, 0, 1, 2)

        self.horizontalLayout_9.addLayout(self.gridLayout)

        self.searchBoxContents_verticalLayout.addWidget(self.frame_content_wid_1)

        self.searchBox_verticalLayout.addWidget(self.frame_searchBoxContents)

        self.searchWidget_verticalLayout.addWidget(self.frame_searchBox)

        self.frame_searchResults = QFrame(self.searchWidget)
        self.frame_searchResults.setObjectName(u"frame_searchResults")
        self.frame_searchResults.setMinimumSize(QSize(16777215, 400))
        self.frame_searchResults.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                               "border-radius: 5px;")
        self.frame_searchResults.setFrameShape(QFrame.StyledPanel)
        self.frame_searchResults.setFrameShadow(QFrame.Raised)
        self.results_verticalLayout = QVBoxLayout(self.frame_searchResults)
        self.results_verticalLayout.setObjectName(u"results_verticalLayout")

        self.frame_resultTitle = QFrame(self.frame_searchResults)
        self.frame_resultTitle.setObjectName(u"frame_resultTitle")
        self.frame_resultTitle.setMinimumSize(QSize(16777215, 35))
        self.frame_resultTitle.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                             "border-radius: 5px;\n"
                                             "")
        self.frame_resultTitle.setFrameShape(QFrame.NoFrame)
        self.frame_resultTitle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_resultsTitle = QVBoxLayout(self.frame_resultTitle)
        self.verticalLayout_resultsTitle.setObjectName(u"verticalLayout_resultsTitle")

        self.resultsLabel = QLabel(self.frame_resultTitle)
        self.resultsLabel.setObjectName(u"resultsLabel")
        self.resultsLabel.setFont(font1)
        self.resultsLabel.setStyleSheet(u"")

        self.verticalLayout_resultsTitle.addWidget(self.resultsLabel)
        self.results_verticalLayout.addWidget(self.frame_resultTitle)

        self.frame_resultList = QFrame(self.frame_searchResults)
        self.frame_resultList.setObjectName(u"frame_resultList")
        self.resultList_verticalLayout = QVBoxLayout(self.frame_resultList)
        self.resultList_verticalLayout.setObjectName(u"resultList_verticalLayout")

        self.resultList = QListWidget(self.frame_resultList)
        self.resultList.setObjectName(u"resultList")
        self.resultList.setMinimumSize(QSize(200, 200))
        self.resultList.setStyleSheet(u"QListWidget {\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	padding: 10px;\n"
                                      "}\n"
                                      "QListWidget:hover {\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QListWidget:focus {\n"
                                      "	border: 2px solid rgb(91, 101, 124);\n"
                                      "}")
        self.resultList.itemDoubleClicked.connect(self.selectResult)

        self.resultList_verticalLayout.addWidget(self.resultList)
        self.results_verticalLayout.addWidget(self.frame_resultList)

        self.searchWidget_verticalLayout.addWidget(self.frame_searchResults)
        ################################# END #################################


        ################################# RESULTS DISPLAY #################################
        self.displayWidget = QWidget()
        self.displayWidget.setObjectName(u"displayWidget")
        self.displayWidget_verticalLayout = QVBoxLayout(self.displayWidget)
        self.displayWidget_verticalLayout.setObjectName(u"displayWidget_verticalLayout")

        self.frame_displayTitle = QFrame(self.displayWidget)
        self.frame_displayTitle.setObjectName(u"frame_displayTitle")
        self.frame_displayTitle.setMaximumSize(QSize(900, 35))
        self.frame_displayTitle.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                                   "border-radius: 5px;\n"
                                                   "")
        self.displayTitle_verticalLayout = QVBoxLayout(self.frame_displayTitle)
        self.displayTitle_verticalLayout.setObjectName(u"displayTitle_verticalLayout")
        self.displayTitle = QLabel(self.frame_displayTitle)
        self.displayTitle.setObjectName(u"displayTitle")
        self.displayTitle.setFont(font1)
        self.displayTitle.setStyleSheet(u"")

        self.displayTitle_verticalLayout.addWidget(self.displayTitle)

        self.frame_displayResults = QFrame(self.displayWidget)
        self.frame_displayResults.setObjectName(u"frame_displayResults")
        self.frame_displayResults.setMaximumSize(QSize(900, 700))
        self.frame_displayResults.setFrameShape(QFrame.NoFrame)
        self.frame_displayResults.setFrameShadow(QFrame.Raised)
        self.frame_displayResults.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                              "border-radius: 5px;\n"
                                              "")
        self.displayResults_gridLayout = QGridLayout(self.frame_displayResults)
        self.displayResults_gridLayout.setObjectName(u"displayResults_gridLayout")

        self.frame_displayLocation = QFrame(self.frame_displayResults)
        self.frame_displayLocation.setObjectName(u"frame_displayLocation")
        self.frame_displayLocation.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                                "border-radius: 5px;\n"
                                                "")
        self.displayLocation_verticalLayout = QVBoxLayout(self.frame_displayLocation)
        self.displayLocation_verticalLayout.setObjectName(u"displayLocation_verticalLayout")
        self.displayLocation = QLabel(self.frame_displayLocation)
        self.displayLocation.setObjectName(u"displayLocation")
        self.displayLocation.setFont(font1)
        self.displayLocation.setStyleSheet(u"")

        self.displayLink = QCommandLinkButton(self.frame_displayLocation)
        self.displayLink.setObjectName(u"displayLink")
        self.displayLink.setStyleSheet(u"QCommandLinkButton {	\n"
                                       "	color: rgb(85, 170, 255);\n"
                                       "	border-radius: 5px;\n"
                                       "	padding: 5px;\n"
                                       "}\n"
                                       "QCommandLinkButton:hover {	\n"
                                       "	color: rgb(210, 210, 210);\n"
                                       "	background-color: rgb(44, 49, 60);\n"
                                       "}\n"
                                       "QCommandLinkButton:pressed {	\n"
                                       "	color: rgb(210, 210, 210);\n"
                                       "	background-color: rgb(52, 58, 71);\n"
                                       "}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.displayLink.setIcon(icon4)
        self.displayLink.setMaximumSize(QSize(160, 85))
        self.displayLink.clicked.connect(self.openDir)

        self.displayLocation_verticalLayout.addWidget(self.displayLocation)
        self.displayLocation_verticalLayout.addWidget(self.displayLink)

        self.frame_checkout = QFrame(self.frame_displayResults)
        self.frame_checkout.setObjectName(u"frame_checkout")
        self.frame_checkout.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                          "	border-radius: 5px;\n")
        self.frame_checkout.setMaximumSize(QSize(430, 400))
        self.checkout_grid = QGridLayout(self.frame_checkout)
        self.checkout_grid.setObjectName(u"checkout_grid")
        self.checkout_available = QLabel(self.frame_checkout)
        self.checkout_available.setObjectName(u"checkout_available")
        self.checkout_available.setFont(font1)
        self.checkout_available.setStyleSheet(u"")
        self.checkout = QCommandLinkButton(self.frame_checkout)
        self.checkout.setObjectName(u"checkout")
        self.checkout.setStyleSheet(u"QCommandLinkButton {	\n"
                                    "	color: rgb(85, 170, 255);\n"
                                    "	border-radius: 5px;\n"
                                    "	padding: 5px;\n"
                                    "}\n"
                                    "QCommandLinkButton:hover {	\n"
                                    "	color: rgb(210, 210, 210);\n"
                                    "	background-color: rgb(44, 49, 60);\n"
                                    "}\n"
                                    "QCommandLinkButton:disabled {	\n"
                                    "	color: rgb(211,211,211);\n"
                                    "}\n"
                                    "QCommandLinkButton:pressed {	\n"
                                    "	color: rgb(210, 210, 210);\n"
                                    "	background-color: rgb(52, 58, 71);\n"
                                    "}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-cloud-upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkout.setIcon(icon5)
        self.checkout.setMaximumSize(QSize(100, 50))
        self.checkout.setEnabled(False)
        self.Return = QCommandLinkButton(self.frame_checkout)
        self.Return.setObjectName(u"Return")
        self.Return.setStyleSheet(u"QCommandLinkButton {	\n"
                                  "	color: rgb(85, 170, 255);\n"
                                  "	border-radius: 5px;\n"
                                  "	padding: 5px;\n"
                                  "}\n"
                                  "QCommandLinkButton:hover {	\n"
                                  "	color: rgb(210, 210, 210);\n"
                                  "	background-color: rgb(44, 49, 60);\n"
                                  "}\n"
                                  "QCommandLinkButton:disabled {	\n"
                                  "	color: rgb(211,211,211);\n"
                                  "}\n"
                                  "QCommandLinkButton:pressed {	\n"
                                  "	color: rgb(210, 210, 210);\n"
                                  "	background-color: rgb(52, 58, 71);\n"
                                  "}")
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-cloud-download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Return.setIcon(icon6)
        self.Return.setMaximumSize(QSize(100, 50))
        self.Return.setEnabled(False)
        self.checkout.clicked.connect(self.checkoutManual)
        self.Return.clicked.connect(self.returnManual)

        self.checkout_grid.addWidget(self.checkout_available, 0, 0, 1, 1, alignmnet=Qt.AlignLeft)
        self.checkout_grid.addWidget(self.checkout, 1, 1, 1, 1, alignment=Qt.AlignRight)
        self.checkout_grid.addWidget(self.Return, 1, 0, 1, 1, alignment=Qt.AlignLeft)

        self.displayResults_gridLayout.addWidget(self.frame_displayLocation, 0, 0)
        self.displayResults_gridLayout.addWidget(self.frame_checkout, 0, 1)

        self.frame_edit = QFrame(self.displayWidget)
        self.frame_edit.setObjectName(u"frame_edit")
        self.frame_edit.setMinimumSize(QSize(110, 270))
        self.frame_edit.setMaximumSize(QSize(900, 270))
        self.frame_edit.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                                 "border-radius: 5px;\n"
                                                 "")
        self.edit_verticalLayout = QVBoxLayout(self.frame_edit)
        self.edit_verticalLayout.setObjectName(u"edit_verticalLayout")

        self.editEnable = QRadioButton(self.frame_edit)
        self.editEnable.setObjectName(u"editEnable")
        self.editEnable.setStyleSheet(u"")
        self.editEnable.setAutoExclusive(False)
        self.editEnable.toggled.connect(self.activateChange)

        self.location_gridLayout = QGridLayout()
        self.location_gridLayout.setObjectName(u"location_gridLayout")

        self.nameEdit = QLineEdit()
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setMinimumSize(QSize(500, 35))
        self.nameEdit.setMaximumSize(QSize(500, 35))
        self.nameEdit.setStyleSheet(u"QLineEdit {\n"
                                    "	background-color: rgb(27, 29, 35);\n"
                                    "	border-radius: 5px;\n"
                                    "	border: 2px solid rgb(27, 29, 35);\n"
                                    "	padding-left: 10px;\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "	border: 2px solid rgb(64, 71, 88);\n"
                                    "}\n"
                                    "QLineEdit:disabled {\n"
                                    "	background-color: rgb(44, 49, 60);\n"
                                    "   border: 2px solid rgb(44, 49, 60);\n"
                                    "}\n"
                                    "QLineEdit:focus {\n"
                                    "	border: 2px solid rgb(91, 101, 124);\n"
                                    "}")
        self.nameEdit.setEnabled(False)

        self.physicalLocation = QLabel()
        self.physicalLocation.setObjectName(u"physicalLocation")
        self.physicalLocation.setFont(font3)


        self.location_yes = QRadioButton()
        self.location_yes.setObjectName(u"location_yes")
        self.location_yes.setEnabled(False)
        self.location_no = QRadioButton()
        self.location_no.setObjectName(u"location_no")
        self.location_no.setEnabled(False)
        self.location_yes.toggled.connect(self.activeInput)

        self.location = QLineEdit()
        self.location.setObjectName(u"location")
        self.location.setMinimumSize(QSize(350, 35))
        self.location.setMaximumSize(QSize(350, 35))
        self.location.setStyleSheet(u"QLineEdit {\n"
                                    "	background-color: rgb(27, 29, 35);\n"
                                    "	border-radius: 5px;\n"
                                    "	border: 2px solid rgb(27, 29, 35);\n"
                                    "	padding-left: 10px;\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "	border: 2px solid rgb(64, 71, 88);\n"
                                    "}\n"
                                    "QLineEdit:disabled {\n"
                                    "	background-color: rgb(44, 49, 60);\n"
                                    "   border: 2px solid rgb(44, 49, 60);\n"
                                    "}\n"
                                    "QLineEdit:focus {\n"
                                    "	border: 2px solid rgb(91, 101, 124);\n"
                                    "}")
        self.location.setEnabled(False)

        self.edit_button = QPushButton()
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setMinimumSize(QSize(150, 30))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)
        self.edit_button.setFont(font8)
        self.edit_button.setStyleSheet(u"QPushButton {\n"
                                    "	border: 2px solid rgb(52, 59, 72);\n"
                                    "	border-radius: 5px;	\n"
                                    "	background-color: rgb(27, 29, 35);\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(57, 65, 80);\n"
                                    "	border: 2px solid rgb(61, 70, 86);\n"
                                    "}\n"
                                    "QPushButton:disabled {\n"
                                    "	background-color: rgb(44, 49, 60);\n"
                                    "   border: 2px solid rgb(44, 49, 60);\n"
                                    "}\n"
                                    "QPushButton:pressed {	\n"
                                    "	background-color: rgb(35, 40, 49);\n"
                                    "	border: 2px solid rgb(43, 50, 61);\n"
                                    "}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_button.setIcon(icon5)
        self.edit_button.setEnabled(False)
        self.edit_button.clicked.connect(self.save)


        self.location_gridLayout.addWidget(self.nameEdit, 0, 0, 1, 1, alignment=Qt.AlignLeft)
        self.location_gridLayout.addWidget(self.physicalLocation, 1, 0, 1, 1, alignment=Qt.AlignLeft)
        self.location_gridLayout.addWidget(self.location_yes, 2, 0, 1 , 1, alignment=Qt.AlignLeft)
        self.location_gridLayout.addWidget(self.location_no, 2, 1, 1, 1, alignment=Qt.AlignLeft)
        self.location_gridLayout.addWidget(self.location, 3, 0, 1, 1, alignment=Qt.AlignLeft)
        self.location_gridLayout.addWidget(self.edit_button, 4, 1, 1, 1, alignment=Qt.AlignRight)


        self.edit_verticalLayout.addWidget(self.editEnable)
        self.edit_verticalLayout.addSpacing(35)
        self.edit_verticalLayout.addLayout(self.location_gridLayout)
        self.edit_verticalLayout.addSpacing(5)

        self.displayWidget_verticalLayout.addWidget(self.frame_displayTitle)
        self.displayWidget_verticalLayout.addWidget(self.frame_displayResults)
        self.displayWidget_verticalLayout.addWidget(self.frame_edit)
        ################################# END #################################


        ################################# ADD NEW #################################
        self.newWidget = QWidget()
        self.newWidget.setObjectName(u"newWidget")
        self.newWidget_verticalLayout = QVBoxLayout(self.newWidget)
        self.newWidget_verticalLayout.setObjectName(u"newWidget_verticalLayout")

        self.frame_newTitle = QFrame(self.newWidget)
        self.frame_newTitle.setObjectName(u"newTitle")
        self.frame_newTitle.setMinimumSize(QSize(110, 40))
        self.frame_newTitle.setMaximumSize(QSize(900, 60))
        self.frame_newTitle.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                                 "border-radius: 5px;\n"
                                                 "")
        self.newTitle_verticalLayout = QVBoxLayout(self.frame_newTitle)
        self.newTitle_verticalLayout.setObjectName(u"newTitle_verticalLayout")
        self.newTitle = QLabel(self.frame_newTitle)
        self.newTitle.setObjectName(u"newTitle")
        self.newTitle.setFont(font1)
        self.newTitle.setStyleSheet(u"")
        self.newTitle_verticalLayout.addWidget(self.newTitle)

        self.frame_newEdit = QFrame()
        self.frame_newEdit.setObjectName(u"newEdit")
        self.frame_newEdit.setMinimumSize(QSize(110, 100))
        self.frame_newEdit.setMaximumSize(QSize(900, 250))
        self.frame_newEdit.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                                 "border-radius: 5px;\n"
                                                 "")
        self.newEdit_grid = QGridLayout(self.frame_newEdit)
        self.newEdit_grid.setObjectName(u"newEdit_grid")

        self.newEquipment = QLineEdit(self.frame_newEdit)
        self.newEquipment.setObjectName(u"newEquipment")
        self.newEquipment.setMinimumSize(QSize(300, 35))
        self.newEquipment.setMaximumSize(QSize(300, 35))
        self.newEquipment.setStyleSheet(u"QLineEdit {\n"
                                    "	background-color: rgb(27, 29, 35);\n"
                                    "	border-radius: 5px;\n"
                                    "	border: 2px solid rgb(27, 29, 35);\n"
                                    "	padding-left: 10px;\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "	border: 2px solid rgb(64, 71, 88);\n"
                                    "}\n"
                                    "QLineEdit:focus {\n"
                                    "	border: 2px solid rgb(91, 101, 124);\n"
                                    "}")

        self.newCopy = QLabel(self.frame_newEdit)
        self.newCopy.setObjectName(u"newCopy")
        self.newCopy.setFont(font3)
        self.newCopy_yes = QRadioButton(self.frame_newEdit)
        self.newCopy_yes.setObjectName(u"newCopy_yes")
        self.newCopy_no = QRadioButton(self.frame_newEdit)
        self.newCopy_no.setObjectName(u"newCopy_no")
        self.newCopy_yes.toggled.connect(self.activenewInput)
        self.newCopy_no.toggled.connect(self.activenewInput)
        self.newLocationGroup = QButtonGroup()

        self.newLocation = QLineEdit(self.frame_newEdit)
        self.newLocation.setObjectName(u"newLocation")
        self.newLocation.setMinimumSize(QSize(300, 35))
        self.newLocation.setMaximumSize(QSize(300, 35))
        self.newLocation.setStyleSheet(u"QLineEdit {\n"
                                    "	background-color: rgb(27, 29, 35);\n"
                                    "	border-radius: 5px;\n"
                                    "	border: 2px solid rgb(27, 29, 35);\n"
                                    "	padding-left: 10px;\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "	border: 2px solid rgb(64, 71, 88);\n"
                                    "}\n"
                                    "QLineEdit:disabled {\n"
                                    "	background-color: rgb(44, 49, 60);\n"
                                    "   border: 2px solid rgb(44, 49, 60);\n"
                                    "}\n"
                                    "QLineEdit:focus {\n"
                                    "	border: 2px solid rgb(91, 101, 124);\n"
                                    "}")
        self.newLocation.setEnabled(False)
        self.newEditConfirm_HLayout = QHBoxLayout()
        self.newEditConfirm_HLayout.setObjectName(u"newEditConfirm_HLayout")
        self.newEdit_confirmY = QPushButton()
        self.newEdit_confirmY.setObjectName(u"newEdit_confirmY")
        self.newEdit_confirmY.setFixedSize(QSize(120, 35))
        self.newEdit_confirmY.setStyleSheet(u"QPushButton {\n"
                                       "	border: 2px solid rgb(52, 59, 72);\n"
                                       "	border-radius: 5px;	\n"
                                       "	background-color: rgb(27, 29, 35);\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "	background-color: rgb(57, 65, 80);\n"
                                       "	border: 2px solid rgb(61, 70, 86);\n"
                                       "}\n"
                                       "QPushButton:pressed {	\n"
                                       "	background-color: rgb(35, 40, 49);\n"
                                       "	border: 2px solid rgb(43, 50, 61);\n"
                                       "}")
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newEdit_confirmY.setIcon(icon8)
        self.newEdit_confirmN = QPushButton()
        self.newEdit_confirmN.setObjectName(u"newEdit_confirmN")
        self.newEdit_confirmN.setFixedSize(QSize(120, 35))
        self.newEdit_confirmN.setStyleSheet(u"QPushButton {\n"
                                            "	border: 2px solid rgb(52, 59, 72);\n"
                                            "	border-radius: 5px;	\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "	background-color: rgb(57, 65, 80);\n"
                                            "	border: 2px solid rgb(61, 70, 86);\n"
                                            "}\n"
                                            "QPushButton:pressed {	\n"
                                            "	background-color: rgb(35, 40, 49);\n"
                                            "	border: 2px solid rgb(43, 50, 61);\n"
                                            "}")
        icon9 = QIcon()
        icon9.addFile(u":/20x20/icons/20x20/cil-trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newEdit_confirmN.setIcon(icon9)
        self.newEdit_confirmO = QPushButton()
        self.newEdit_confirmO.setObjectName(u"newEdit_confirmO")
        self.newEdit_confirmO.setFixedSize(QSize(120, 35))
        self.newEdit_confirmO.setStyleSheet(u"QPushButton {\n"
                                            "	border: 2px solid rgb(52, 59, 72);\n"
                                            "	border-radius: 5px;	\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "	background-color: rgb(57, 65, 80);\n"
                                            "	border: 2px solid rgb(61, 70, 86);\n"
                                            "}\n"
                                            "QPushButton:pressed {	\n"
                                            "	background-color: rgb(35, 40, 49);\n"
                                            "	border: 2px solid rgb(43, 50, 61);\n"
                                            "}")
        icon10 = QIcon()
        icon10.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newEdit_confirmO.setIcon(icon10)

        self.newEdit_confirmY.clicked.connect(self.newSave)
        self.newEdit_confirmO.clicked.connect(self.newSaveOpen)
        self.newEdit_confirmN.clicked.connect(self.newDiscard)


        self.newEditConfirm_HLayout.addWidget(self.newEdit_confirmY)
        self.newEditConfirm_HLayout.addWidget(self.newEdit_confirmO)
        self.newEditConfirm_HLayout.addWidget(self.newEdit_confirmN)

        self.newEdit_grid.setVerticalSpacing(15)
        self.newEdit_grid.setRowMinimumHeight(0, 60)
        self.newEdit_grid.addWidget(self.newEquipment, 0, 0, 1, 1, alignment=Qt.AlignLeft)
        self.newEdit_grid.addWidget(self.newCopy, 1, 0, 1, 1, alignment=Qt.AlignLeft)
        self.newEdit_grid.addWidget(self.newCopy_yes, 2, 0, 1, 1, alignment=Qt.AlignLeft)
        self.newEdit_grid.addWidget(self.newCopy_no, 2, 0, 1, 1, alignment=Qt.AlignCenter)
        self.newEdit_grid.addWidget(self.newLocation, 3, 0, 1, 1, alignment=Qt.AlignLeft)
        self.newEdit_grid.addLayout(self.newEditConfirm_HLayout, 4, 1, 1, 1, alignment=Qt.AlignRight)

        self.newWidget_verticalLayout.addSpacing(80)
        self.newWidget_verticalLayout.addWidget(self.frame_newTitle)
        self.newWidget_verticalLayout.addWidget(self.frame_newEdit)
        self.newWidget_verticalLayout.addSpacing(100)
        ################################# END #################################


        ################################# USER #################################
        self.userWidget = QWidget()
        self.userWidget.setObjectName(u"userWidget")
        self.userWidget_verticalLayout = QVBoxLayout(self.userWidget)
        self.userWidget_verticalLayout.setObjectName(u"userWidget_verticalLayout")

        self.frame_userTitle = QFrame()
        self.frame_userTitle.setObjectName(u"frame_userTitle")
        self.frame_userTitle.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                                 "border-radius: 5px;\n"
                                                 "")
        self.userTitle_HLayout = QHBoxLayout(self.frame_userTitle)
        self.userTitle_HLayout.setObjectName(u"userTitle_HLayout")

        self.user_icon = QLabel(self.frame_userTitle)
        self.user_icon.setObjectName(u"user_icon")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.user_icon.sizePolicy().hasHeightForWidth())
        self.user_icon.setSizePolicy(sizePolicy5)
        self.user_icon.setMinimumSize(QSize(70, 70))
        self.user_icon.setMaximumSize(QSize(70, 70))
        self.user_icon.setStyleSheet(u"QLabel {\n"
                                           "	border-radius: 35px;\n"
                                           "	background-color: rgb(44, 49, 60);\n"
                                           "	border: 5px solid rgb(27, 29, 35);\n"
                                           "	background-position: center;\n"
                                           "	background-repeat: no-repeat;\n"
                                           "}")
        icon11 = QPixmap(u":/20x20/icons/20x20/cil-user.png")
        self.user_icon.setPixmap(icon11)
        self.user_icon.setAlignment(Qt.AlignCenter)

        self.user_name = QLabel(self.frame_userTitle)
        self.user_icon.setObjectName(u"user_name")
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(20)
        self.user_name.setFont(font9)
        self.user_name.setStyleSheet(u"")

        self.userTitle_HLayout.addWidget(self.user_icon)
        self.userTitle_HLayout.addSpacing(15)
        self.userTitle_HLayout.addWidget(self.user_name)

        self.frame_userCheckedout = QFrame()
        self.frame_userCheckedout.setObjectName(u"frame_userCheckedout")
        self.frame_userCheckedout.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                                 "border-radius: 5px;\n"
                                                 "")
        self.userCheckout_Grid = QGridLayout(self.frame_userCheckedout)
        self.userCheckout_Grid.setObjectName(u"frame_userCheckedout")


        self.userWidget_verticalLayout.addWidget(self.frame_userTitle)


        ################################# END #################################


        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
        # endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
        # endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
        # endif

        self.stackedWidget.addWidget(self.searchWidget)
        self.stackedWidget.addWidget(self.displayWidget)
        self.stackedWidget.addWidget(self.newWidget)
        self.stackedWidget.addWidget(self.userWidget)
        self.verticalLayout_9.addWidget(self.stackedWidget)

        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)

        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
                                           "	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
                                           "	background-position: center;\n"
                                           "	background-repeat: no-repeat;\n"
                                           "}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)

        self.verticalLayout_4.addWidget(self.frame_grip)

        self.horizontalLayout_2.addWidget(self.frame_content_right)

        self.verticalLayout.addWidget(self.frame_center)

        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)



        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        # if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))

        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v2.1.0", None))

        self.searchLabel.setText(QCoreApplication.translate("MainWindow", "Manual Search", None))
        self.searchInput.setPlaceholderText(QCoreApplication.translate("MainWindow", "Equipment Name or Keyword", None))
        self.searchExample.setText(QCoreApplication.translate("MainWindow", "Ex: Atlas Copco Compresser", None))
        self.searchGo.setText(QCoreApplication.translate("MainWindow", "  Search", None))

        self.resultsLabel.setText(QCoreApplication.translate("MainWindow", "Results", None))

        self.displayTitle.setText(QCoreApplication.translate("MainWindow", "Search Results", None))
        self.displayLink.setText(QCoreApplication.translate("MainWindow", u"Open Directory", None))
        self.displayLink.setDescription(QCoreApplication.translate("MainWindow", u"Opens digital manuals\n(if exists)", None))
        self.checkout.setText(QCoreApplication.translate("MainWindow", u"Checkout", None))
        self.Return.setText(QCoreApplication.translate("MainWindow", u"Return", None))

        self.editEnable.setText(QCoreApplication.translate("MainWindow", u"Modify Equipment", None))
        self.nameEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Equipment Name", None))
        self.physicalLocation.setText(QCoreApplication.translate("MainWindow", u"Physical Copy?", None))
        self.location_yes.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.location_no.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.location.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Manual Location", None))
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))

        self.newTitle.setText(QCoreApplication.translate('MainWindow', "Add New Manual", None))
        self.newEquipment.setPlaceholderText(QCoreApplication.translate('MainWindow', "New Equipment Name", None))
        self.newCopy.setText(QCoreApplication.translate('MainWindow', "Physical Copy?", None))
        self.newCopy_yes.setText(QCoreApplication.translate('MainWindow', "Yes", None))
        self.newCopy_no.setText(QCoreApplication.translate('MainWindow', "No", None))
        self.newLocation.setPlaceholderText(QCoreApplication.translate("MainWindow", "Location", None))
        self.newEdit_confirmY.setText(QCoreApplication.translate("MainWindow", "Save", None))
        self.newEdit_confirmO.setText(QCoreApplication.translate("MainWindow", "Save and Open", None))
        self.newEdit_confirmN.setText(QCoreApplication.translate("MainWindow", "Discard", None))

        c = getpass.getuser()
        self.user_name.setText(QCoreApplication.translate("MainWindow", c, None))


    # retranslateUi

    def searchClick(self):  # displays search results
        global filename, path
        filename = self.searchInput.text()
        s = path + "*" + filename + "*\\"
        self.resultList.clear()
        self.resultList.addItem("*** Add New ***")

        for files in glob.glob(s, recursive=True):
            a = files.replace(path, "")
            self.resultList.addItem(a)

    def display(self):  # displays the locations and folder of the manuals
        try:
            t = path + filename + "tag.txt"
            s = readLocation(t)
            self.displayTitle.setText("Search Results (" + filename + "):")
            if s == "digital":
                # print("s")
                t = filename
                self.displayLocation.setText("Digital Manuals Only")
            else:
                self.displayLocation.setText("Physical copy at: " + s)
                t = filename
        except FileNotFoundError:
            warn('Cannot open file: File not found')
        # finally:
        # self.change.setChecked(False)
        # self.no.setChecked(True)

    def selectResult(self):  # what to do when entry is double clicked
        global filename
        t = self.resultList.currentItem().text()
        filename = t
        self.editEnable.setChecked(False)
        if t != "*** Add New ***":
            self.stackedWidget.setCurrentIndex(1)
            self.display()
            try:
                self.checked_out()
            except:
                warn("Unknown Error (checkout.txt)")
        else:
            self.stackedWidget.setCurrentIndex(2)

    def newResult(self, info):  # prints the new equipment on the results screen after saving
        global filename
        try:
            t = info
            filename = t
            self.display()
        except:
            warn("UnknownError (new result)")
        try:
            self.checked_out()
        except:
            warn("Unknown Error (checkout.txt)")

    def openDir(self):  # opens directory of the manual
        try:
            if self.searchInput.text() != "":
                t = path + filename + "tag.txt"
                s = readLocation(t)
                t = filename
                dirOpen(t, False)
            else:
                t = filename
                dirOpen(t, True)
        except FileNotFoundError:
            warn('Cannot open file: File not found')

    def checked_out(self):  # checks if the manual has been checked out
        t = path + filename + "checkout.txt"
        if os.path.isfile(t) is False:
            f = open(t, "w")
            f.write("available,0")
            f.close()
        f = open(t, "r")
        v = f.read()
        f.close()
        v = v.split(",")
        if v[0] == "available" or "":
            self.checkout.setEnabled(True)
            self.Return.setEnabled(False)
            self.checkout_available.setText("Manual is available")
        else:
            self.checkout.setEnabled(False)
            self.Return.setEnabled(True)
            c = "Checked out by " + v[0] + " on " + v[1]
            self.checkout_available.setText(c)

    def checkoutManual(self): # checks the manual out
        try:
            username = getpass.getuser()
        except:
            warn("Unknown Error (user)")
            username = ""
        try:
            ct = datetime.datetime.now().date()
            ct = str(ct)
        except:
            warn("Unknown Error (time)")
        try:
            t = path + filename + "checkout.txt"
            checkout(username, ct, t)
            self.checkout.setEnabled(False)
            self.Return.setEnabled(True)
            c = "Checked out by " + username + " on " + ct
            self.checkout_available.setText(c)
        except:
            warn("Unknown Error (checkout)")    # s

    def returnManual(self):     # returns the manual
        try:
            t = path + filename + "checkout.txt"
            checkout("available", "", t)
            self.checkout.setEnabled(True)
            self.Return.setEnabled(False)
            self.checkout_available.setText("Manual is available")
        except:
            warn("Unknown Error (checkout)")

    def activateChange(self):   # enables making changes to the equipment
        if self.editEnable.isChecked() is True:
            self.nameEdit.setEnabled(True)
            self.location_yes.setEnabled(True)
            self.location_no.setEnabled(True)
            self.edit_button.setEnabled(True)
            self.activeInput()
        else:
            self.nameEdit.setEnabled(False)
            self.location_yes.setEnabled(False)
            self.location_no.setEnabled(False)
            self.edit_button.setEnabled(False)
            self.location.setEnabled(False)

    def activeInput(self):   # activates physical location input bar in modify equipment tab
        if self.location_yes.isChecked() is True:
            self.location.setEnabled(True)
        else:
            self.location.setEnabled(False)

    def activenewInput(self):  # activates physical location input bar in new tab
        if self.newCopy_yes.isChecked() is True:
            self.newLocation.setEnabled(True)
        else:
            self.newLocation.setEnabled(False)

    def save(self): # saves the changes to the equipment
        n = self.nameEdit.text()
        n = path + n
        c = path + filename
        try:
            if n != '':
                rename(c, n)
            s = n + "\\tag.txt"
            if self.location_yes.isChecked() is True:
                os.remove(s)
                t = self.location.text()
                newTag(t, n)
            else:
                os.remove(s)
                t = "digital"
                newTag(t, n)
        except FileNotFoundError:
            warn('File cannot be changed: File not found')
        except PermissionError:
            warn('File cannot be changed: File is being used by another process')
        finally:
            self.nameEdit.clear()
            self.location.clear()

    def newSave(self):    # creates new equipment directory
        s = path + self.newEquipment.text()
        info = self.newEquipment.text()
        info = info+"\\"
        try:
            mkDir(s, False)
            if self.newCopy_yes.isChecked() is True:
                t = self.newLocation.text()
                newTag(t, s)
            else:
                t = "digital"
                newTag(t, s)
            self.newResult(info)
            self.newEquipment.clear()
            self.newLocation.clear()
        except FileNotFoundError:
            warn('File cannot be changed: File not found')
        except PermissionError:
            warn('File cannot be changed: File is being used by another process')
        except FileExistsError:
            warn('File cannot be changed: File already exists')

    def newSaveOpen(self):    # creates new equipment directory and opens it
        s = path + self.newEquipment.text()
        info = self.newEquipment.text()
        info = info+"\\"
        try:
            mkDir(s, True)
            if self.newCopy_yes.isChecked() is True:
                t = self.newLocation.text()
                newTag(t, s)
            else:
                t = "digital"
                newTag(t, s)
            self.newResult(info)
            self.newEquipment.clear()
            self.newLocation.clear()
        except FileNotFoundError:
            warn('File cannot be changed: File not found')
        except PermissionError:
            warn('File cannot be changed: File is being used by another process')
        except FileExistsError:
            warn('File cannot be changed: File already exists')

    def newDiscard(self):   # discards entry on new equipment tab
        self.newEquipment.clear()
        self.newLocation.clear()






############################# FUNCTIONS #############################
def dirOpen(file, state):  # opens directory for existing equipment
    if file == "*** Add New ***":
        return True
    else:
        s = path + file
        # print(s)
        os.startfile(s)
        tagPath = s + "\\tag.txt"
        if os.path.isfile(tagPath) and state is False:
            # print(tagPath)
            with open(tagPath, 'w') as file:
                file.write("digital")
        return False


def mkDir(file, open):  # makes a new directory for new equipment
    s = file
    os.mkdir(s)
    if open is True:
        os.startfile(s)


def newTag(data, file):  # creates a new location tag for new equipment
    tagPath = file + "\\tag.txt"
    if os.path.isfile(tagPath) is False:
        # print(tagPath, data)
        with open(tagPath, 'w') as file:
            file.write(data)
        return False
    else:
        return True


def checkout(username, time, file):   # edits a checkout tag file
    f = open(file, "w")
    v = username + "," + time
    f.write(v)
    f.close()


def readLocation(location):  # reads location tag for equipment
    # print(location)
    if os.path.isfile(location) is True:
        f = open(location, "r")
        v = f.read()
        f.close()
        return v
    else:
        return "i"


def rename(current, new):  # renames directory
    os.rename(current, new)
    os.startfile(new)


def warn(str):
    msg = QtWidgets.QMessageBox()
    msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText(str)
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
    msg.exec_()
############################# END #############################
