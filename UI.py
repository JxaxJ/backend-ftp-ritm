from PyQt5 import QtCore, QtGui, QtWidgets
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

    def add_fucnt(self):
        self.refresh_btn.clicked.connect(self.refresh)

    def refresh(self):
        ftp = FTP(key.FTP)
        ftp.login(key.Login, key.password)

        self.Temporary_array = []
        self.files = ftp.nlst()

        for i in range(len(self.files)):
            if len(self.files[i].split('.')) > 1:
                current_directory = ftp.pwd()
                self.Temporary_array.append(f"[{current_directory}]/{self.files[i]}")

            else:
                ftp.cwd(self.files[i])
                self.Temporary_array.append(f"[FOLDER] /{self.files[i]}")
                ftp.cwd('../')

        print(self.Temporary_array)
        ftp.quit()

        for i in self.Temporary_array:
            self.dirs_widget.addItem(i)


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