# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 60, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.aSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.aSpinBox.setGeometry(QtCore.QRect(50, 60, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aSpinBox.setFont(font)
        self.aSpinBox.setProperty("value", 1.0)
        self.aSpinBox.setObjectName("aSpinBox")
        self.bSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.bSpinBox.setGeometry(QtCore.QRect(320, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bSpinBox.setFont(font)
        self.bSpinBox.setProperty("value", 10.0)
        self.bSpinBox.setObjectName("bSpinBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 110, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lyambdaSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lyambdaSpinBox.setGeometry(QtCore.QRect(60, 145, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lyambdaSpinBox.setFont(font)
        self.lyambdaSpinBox.setProperty("value", 2.0)
        self.lyambdaSpinBox.setObjectName("lyambdaSpinBox")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 200, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(16, 271, 217, 48))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(16, 234, 217, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.methodComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.methodComboBox.setGeometry(QtCore.QRect(240, 320, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.methodComboBox.setFont(font)
        self.methodComboBox.setObjectName("methodComboBox")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(16, 326, 217, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_deltat = QtWidgets.QLabel(self.centralwidget)
        self.label_deltat.setGeometry(QtCore.QRect(16, 364, 217, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_deltat.setFont(font)
        self.label_deltat.setObjectName("label_deltat")
        self.tasksSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.tasksSpinBox.setGeometry(QtCore.QRect(240, 240, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tasksSpinBox.setFont(font)
        self.tasksSpinBox.setMaximum(100000)
        self.tasksSpinBox.setProperty("value", 1000)
        self.tasksSpinBox.setObjectName("tasksSpinBox")
        self.repeatSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.repeatSpinBox.setGeometry(QtCore.QRect(240, 280, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.repeatSpinBox.setFont(font)
        self.repeatSpinBox.setMaximum(100)
        self.repeatSpinBox.setObjectName("repeatSpinBox")
        self.stepSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.stepSpinBox.setGeometry(QtCore.QRect(240, 370, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stepSpinBox.setFont(font)
        self.stepSpinBox.setProperty("value", 0.01)
        self.stepSpinBox.setObjectName("stepSpinBox")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 630, 244, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 465, 244, 48))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 575, 244, 48))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 520, 244, 48))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 425, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.resTasksLabel = QtWidgets.QLabel(self.centralwidget)
        self.resTasksLabel.setGeometry(QtCore.QRect(260, 470, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.resTasksLabel.setFont(font)
        self.resTasksLabel.setObjectName("resTasksLabel")
        self.repeatTasksLabel = QtWidgets.QLabel(self.centralwidget)
        self.repeatTasksLabel.setGeometry(QtCore.QRect(260, 530, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.repeatTasksLabel.setFont(font)
        self.repeatTasksLabel.setObjectName("repeatTasksLabel")
        self.maxLenLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxLenLabel.setGeometry(QtCore.QRect(260, 575, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maxLenLabel.setFont(font)
        self.maxLenLabel.setObjectName("maxLenLabel")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(260, 630, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(100, 680, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startBtn.setFont(font)
        self.startBtn.setObjectName("startBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.methodComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Параметры генератора"))
        self.label_2.setText(_translate("MainWindow", "a"))
        self.label_3.setText(_translate("MainWindow", "b"))
        self.label_4.setText(_translate("MainWindow", "Параметры процессора"))
        self.label_5.setText(_translate("MainWindow", "λ"))
        self.label_6.setText(_translate("MainWindow", "Свойства системы"))
        self.label_8.setText(_translate("MainWindow", "Вероятность повторной\n"
"обработки заявки"))
        self.label_9.setText(_translate("MainWindow", "Количество заявок"))
        self.methodComboBox.setItemText(0, _translate("MainWindow", "Событийный"))
        self.methodComboBox.setItemText(1, _translate("MainWindow", "Пошаговый"))
        self.label_10.setText(_translate("MainWindow", "Метод моделирования"))
        self.label_deltat.setText(_translate("MainWindow", "Шаг"))
        self.label_11.setText(_translate("MainWindow", "Время работы"))
        self.label_12.setText(_translate("MainWindow", "Количество обработанных\n"
"заявок"))
        self.label_13.setText(_translate("MainWindow", "Максимальная длина\n"
"очереди"))
        self.label_14.setText(_translate("MainWindow", "Количество повторно\n"
"обработанных заявок"))
        self.label_7.setText(_translate("MainWindow", "Результаты"))
        self.resTasksLabel.setText(_translate("MainWindow", "0"))
        self.repeatTasksLabel.setText(_translate("MainWindow", "0"))
        self.maxLenLabel.setText(_translate("MainWindow", "0"))
        self.timeLabel.setText(_translate("MainWindow", "0"))
        self.startBtn.setText(_translate("MainWindow", "Промоделировать"))
