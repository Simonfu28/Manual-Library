################################################################################
##
## UI FRAMEWORK BY: WANDERSON M.PIMENTA
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from configparser import ConfigParser
import getpass


config = ConfigParser()
config.read('config.cfg')
path = config.get("Settings", 'systempath')
filename = ""


# GUI FILE
from app_modules import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('ManualLib2.1')
        UIFunctions.labelTitle(self, 'ManualLib2.1')
        # UIFunctions.labelDescription(self, 'Set text')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "RESULTS", "btn_results", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "SEARCH", "btn_search", "url(:/16x16/icons/16x16/cil-magnifying-glass.png)", True)
        UIFunctions.addNewMenu(self, "ADD", "btn_add", "url(:/16x16/icons/16x16/cil-library-add.png)", True)
        UIFunctions.addNewMenu(self, "USER", "btn_user", "url(:/16x16/icons/16x16/cil-people.png)", True)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_search")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.searchWidget)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        try:
            username = getpass.getuser()
            c = username.split(".")
            initial = c[0][0] + c[1][0]
            initial = initial.upper()
            UIFunctions.userIcon(self, initial, "", True)
        except:
            UIFunctions.userIcon(self, "", "", False)
        ## ==> END ##

        ## PRINT PATH AT TOP OF WINDOW
        UIFunctions.labelPath(self, path)
        ## END

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################


        ## ==> QTableWidget RARAMETERS
        ########################################################################
        #self.ui.displayWidget.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE RESULTS
        if btnWidget.objectName() == "btn_results":
            self.ui.stackedWidget.setCurrentWidget(self.ui.displayWidget)
            UIFunctions.resetStyle(self, "btn_results")
            UIFunctions.labelPage(self, "RESULTS")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE SEARCH
        if btnWidget.objectName() == "btn_search":
            self.ui.stackedWidget.setCurrentWidget(self.ui.searchWidget)
            UIFunctions.resetStyle(self, "btn_search")
            UIFunctions.labelPage(self, "SEARCH")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE ADD
        if btnWidget.objectName() == "btn_add":
            self.ui.stackedWidget.setCurrentWidget(self.ui.newWidget)
            UIFunctions.resetStyle(self, "btn_add")
            UIFunctions.labelPage(self, "ADD")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE USER
        if btnWidget.objectName() == "btn_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.userWidget)
            UIFunctions.resetStyle(self, "btn_user")
            UIFunctions.labelPage(self, "USER")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ## EVENTS ###

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
