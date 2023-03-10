import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from ftplib import FTP
import key


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(746, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.dirs_widget = QtWidgets.QListWidget(self.centralwidget)
        self.dirs_widget.setObjectName("dirs_widget")
        self.gridLayout.addWidget(self.dirs_widget, 0, 0, 1, 1)
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setObjectName("refresh_btn")
        self.gridLayout.addWidget(self.refresh_btn, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_fucnt()
        self.dirs = []
        self.files = []

    def add_fucnt(self):
        self.refresh_btn.clicked.connect(self.refresh)

    def refresh(self):
        self.dirs_widget.clear()
        self.dirs = []
        self.files = []

        t = threading.Thread(target=self.get_files_and_dirs, args=('',))
        t.start()

    def get_files_and_dirs(self, path):
        try:
            self.ftp = FTP(key.FTP)
            self.ftp.login(key.Login, key.password)

            self.ftp.cwd(path)
            items = self.ftp.nlst()

            for item in items:
                if "." not in item:  # if item is a folder (no extension)
                    self.dirs.append(os.path.join(path, item))
                    self.dirs_widget.addItem(f"[FOLDER] {os.path.join(path, item)}")
                    self.get_files_and_dirs(os.path.join(path, item))
                else:  # if item is a file
                    self.files.append(os.path.join(path, item))
                    self.dirs_widget.addItem(f"[FILES] {os.path.join(path, item)}")

            self.ftp.cwd("..")  # go back up one level in the remote folder hierarchy
            self.ftp.quit()
        except:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.dirs_widget.isSortingEnabled()
        self.dirs_widget.setSortingEnabled(False)
        self.dirs_widget.setSortingEnabled(__sortingEnabled)
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())