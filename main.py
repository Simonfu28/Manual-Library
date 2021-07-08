import os
import sys
import glob
import PyQt5
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from configparser import ConfigParser

config = ConfigParser()
config.read('config.cfg')
path = config.get("Settings", 'systempath')
filename = ""


# ManualLib.ui import
class ManualLib(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ManualLib, self).__init__(parent)   # call inherited class
        uic.loadUi('ManualLib.ui', self)    # Loads .ui file
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        buttonBox = QtWidgets.QDialogButtonBox(self)   # Reference Y/N button click
        buttonBox.accepted.connect(self.accept)

        self.input = self.findChild(QtWidgets.QLineEdit, 'value')    # defines input when Y/N button clicked

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')   # Links setting button
        self.button.clicked.connect(self.settings)

        self.list = self.findChild(QtWidgets.QListWidget, 'listWidget')     # Defines the list to display results
        self.list.itemDoubleClicked.connect(self.selectList)

        self.image = QtGui.QPixmap("logo.png")      # adds an logo icon in the app
        self.logo = self.findChild(QtWidgets.QLabel, 'label_2')
        self.logo.setPixmap(self.image)

        self.dialog = Settings(self)    # Initializes other windows
        self.new = New(self)
        self.result = Results(self)

        self.show()

    # displays search results
    def accept(self):
        global filename, path
        filename = self.input.text()
        s = path+"*"+filename+"*\\"
        self.list.clear()
        self.list.addItem("*** Add New ***")

        for files in glob.glob(s, recursive=True):
            a = files.replace(path, "")
            self.list.addItem(a)

    # what to do when entry is double clicked
    def selectList(self):
        global filename
        t = self.list.currentItem().text()
        filename = t
        if t != "*** Add New ***":
            self.result.show()
            self.result.display()
        else:
            self.new.show()

    # opens settings window
    def settings(self):
        self.dialog.show()


# New.ui import
class New(QtWidgets.QDialog):
    def __init__(self, parent=ManualLib):
        super(New, self).__init__()
        uic.loadUi('New.ui', self)

        buttonBox = QtWidgets.QDialogButtonBox()
        buttonBox.accepted.connect(self.accept)

        self.Input = self.findChild(QtWidgets.QLineEdit, 'input')
        self.location = self.findChild(QtWidgets.QLineEdit, 'location')

        self.yes = self.findChild(QtWidgets.QRadioButton, 'location_yes')
        self.yes.toggled.connect(self.activeInput)

    # creates new directory
    def accept(self):
        if self.Input.text() != '':
            s = path + self.Input.text()
            try:
                mkDir(s)

                if self.yes.isChecked() is True:
                    t = self.location.text()
                    newTag(t, s)
                else:
                    t = "digital"
                    newTag(t, s)
            except FileNotFoundError:
                warn('File cannot be changed: File not found')
            except PermissionError:
                warn('File cannot be changed: File is being used by another process')

            self.Input.clear()
            self.location.clear()
            self.close()

    # activates physical location input bar
    def activeInput(self):
        if self.yes.isChecked() is True:
            self.location.setEnabled(True)
        else:
            self.location.setEnabled(False)


# Results.ui import
class Results(QtWidgets.QDialog):
    def __init__(self, parent=ManualLib):
        super(Results, self).__init__()
        uic.loadUi('Results.ui', self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        buttonBox = QtWidgets.QDialogButtonBox()
        buttonBox.accepted.connect(self.accept)

        self.input = self.findChild(QtWidgets.QLineEdit, 'input')
        self.location = self.findChild(QtWidgets.QLineEdit, 'location')

        self.results = self.findChild(QtWidgets.QLabel, 'label_4')

        self.modify = self.findChild(QtWidgets.QPushButton, 'modify')
        self.modify.clicked.connect(self.save)

        self.change = self.findChild(QtWidgets.QRadioButton, 'radioButton')
        self.change.toggled.connect(self.activateChange)

        self.yes = self.findChild(QtWidgets.QRadioButton, 'location_yes')
        self.no = self.findChild(QtWidgets.QRadioButton, 'location_no')
        self.yes.toggled.connect(self.activeInput)

    # displays the locations and folder of the manuals
    def display(self):
        try:
            t = path+filename+"tag.txt"
            s = readLocation(t)
            if s == "digital":
                # print("s")
                t = filename
                self.results.setText("Digital Manuals Only")
                dirOpen(t)
            else:
                self.results.setText("Physical Manual Exists at: " + s)
                t = filename
                dirOpen(t)
        except FileNotFoundError:
            warn('Cannot open file: File not found')
        finally:
            self.change.setChecked(False)
            self.no.setChecked(True)

    # enables making changes to the equipment
    def activateChange(self):
        if self.change.isChecked() is True:
            self.input.setEnabled(True)
            self.yes.setEnabled(True)
            self.no.setEnabled(True)
            self.modify.setEnabled(True)
            self.input.setPlaceholderText(filename)
        else:
            self.input.setEnabled(False)
            self.yes.setEnabled(False)
            self.no.setEnabled(False)
            self.modify.setEnabled(False)

    # activates physical location input bar
    def activeInput(self):
        if self.yes.isChecked() is True:
            self.location.setEnabled(True)
        else:
            self.location.setEnabled(False)

    def save(self):
        n = self.input.text()
        n = path + n
        c = path + filename
        try:
            if n != '':
                rename(c, n)
            s = n + "\\tag.txt"
            if self.yes.isChecked() is True:
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
            self.input.clear()
            self.location.clear()

        self.close()


# Settings.ui import
class Settings(QtWidgets.QDialog):
    def __init__(self, parent=ManualLib):
        super(Settings, self).__init__()
        uic.loadUi('Settings.ui', self)

        self.changePath = self.findChild(QtWidgets.QToolButton, "toolButton")
        #self.changePath.clicked.connect(self.open)

    #def open(self):
        #open("config.cfg", "r")


# opens directory for existing equipment
def dirOpen(file):
    if file == "*** Add New ***":
        return True
    else:
        s = path + file
        # print(s)
        os.startfile(s)
        tagPath = s + "\\tag.txt"
        if os.path.isfile(tagPath) is False:
            # print(tagPath)
            with open(tagPath, 'w') as file:
                file.write("digital")
        return False


# makes a new directory for new equipment
def mkDir(file):
    s = file
    os.mkdir(s)
    os.startfile(s)


# creates a new location tag for new equipment
def newTag(data, file):
    tagPath = file + "\\tag.txt"
    if os.path.isfile(tagPath) is False:
        # print(tagPath, data)
        with open(tagPath, 'w') as file:
            file.write(data)
        return False
    else:
        return True


# reads location tag for equipment
def readLocation(location):
    # print(location)
    if os.path.isfile(location) is True:
        f = open(location, "r")
        v = f.read()
        f.close()
        return v
    else:
        return "i"


# renames directory
def rename(current, new):
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ManualLib()
    app.exec_()


if __name__ == "__main__":
    main()

