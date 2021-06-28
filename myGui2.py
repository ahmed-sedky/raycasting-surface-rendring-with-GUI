# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myGui2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(53, 160, 661, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.surfaceRendring = QtWidgets.QPushButton(self.centralwidget)
        self.surfaceRendring.setGeometry(QtCore.QRect(150, 110, 511, 28))
        self.surfaceRendring.setObjectName("surfaceRendring")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 210, 733, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.raycasting = QtWidgets.QPushButton(self.centralwidget)
        self.raycasting.setGeometry(QtCore.QRect(140, 250, 521, 28))
        self.raycasting.setObjectName("raycasting")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(53, 350, 671, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.green = QtWidgets.QSlider(self.centralwidget)
        self.green.setGeometry(QtCore.QRect(620, 440, 22, 84))
        self.green.setOrientation(QtCore.Qt.Vertical)
        self.green.setObjectName("green")
        self.blue = QtWidgets.QSlider(self.centralwidget)
        self.blue.setGeometry(QtCore.QRect(680, 440, 22, 84))
        self.blue.setOrientation(QtCore.Qt.Vertical)
        self.blue.setObjectName("blue")
        self.Red = QtWidgets.QSlider(self.centralwidget)
        self.Red.setGeometry(QtCore.QRect(550, 440, 22, 84))
        self.Red.setOrientation(QtCore.Qt.Vertical)
        self.Red.setObjectName("Red")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 320, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 420, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 420, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(680, 420, 55, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 26))
        self.menubar.setObjectName("menubar")
        self.menuopen_DICOM = QtWidgets.QMenu(self.menubar)
        self.menuopen_DICOM.setObjectName("menuopen_DICOM")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_DICOM = QtWidgets.QAction(MainWindow)
        self.open_DICOM.setObjectName("open_DICOM")
        self.menuopen_DICOM.addAction(self.open_DICOM)
        self.menubar.addAction(self.menuopen_DICOM.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.surfaceRendring.setText(_translate("MainWindow", "Surface Rendring"))
        self.raycasting.setText(_translate("MainWindow", "RayCasting Rendring"))
        self.label.setText(_translate("MainWindow", "Opacity"))
        self.label_2.setText(_translate("MainWindow", "Red"))
        self.label_3.setText(_translate("MainWindow", "Green"))
        self.label_4.setText(_translate("MainWindow", "Blue"))
        self.menuopen_DICOM.setTitle(_translate("MainWindow", "File"))
        self.open_DICOM.setText(_translate("MainWindow", "open DICOM"))

