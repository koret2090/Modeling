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
        MainWindow.resize(858, 874)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableAlg = QtWidgets.QTableWidget(self.centralwidget)
        self.tableAlg.setGeometry(QtCore.QRect(40, 60, 351, 361))
        self.tableAlg.setObjectName("tableAlg")
        self.tableAlg.setColumnCount(3)
        self.tableAlg.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableAlg.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAlg.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAlg.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAlg.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAlg.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAlg.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAlg.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAlg.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAlg.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAlg.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAlg.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAlg.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAlg.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 10, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 480, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.calcAlgBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calcAlgBtn.setGeometry(QtCore.QRect(40, 440, 131, 28))
        self.calcAlgBtn.setObjectName("calcAlgBtn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 520, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 560, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 600, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.measureAlg1 = QtWidgets.QTextEdit(self.centralwidget)
        self.measureAlg1.setGeometry(QtCore.QRect(140, 525, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.measureAlg1.setFont(font)
        self.measureAlg1.setObjectName("measureAlg1")
        self.measureAlg2 = QtWidgets.QTextEdit(self.centralwidget)
        self.measureAlg2.setGeometry(QtCore.QRect(140, 565, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.measureAlg2.setFont(font)
        self.measureAlg2.setObjectName("measureAlg2")
        self.measureAlg3 = QtWidgets.QTextEdit(self.centralwidget)
        self.measureAlg3.setGeometry(QtCore.QRect(140, 605, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.measureAlg3.setFont(font)
        self.measureAlg3.setObjectName("measureAlg3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(470, 520, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.measureTable2 = QtWidgets.QTextEdit(self.centralwidget)
        self.measureTable2.setGeometry(QtCore.QRect(570, 565, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.measureTable2.setFont(font)
        self.measureTable2.setObjectName("measureTable2")
        self.calcTableBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calcTableBtn.setGeometry(QtCore.QRect(470, 440, 131, 28))
        self.calcTableBtn.setObjectName("calcTableBtn")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 600, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.measureTable3 = QtWidgets.QTextEdit(self.centralwidget)
        self.measureTable3.setGeometry(QtCore.QRect(570, 605, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.measureTable3.setFont(font)
        self.measureTable3.setObjectName("measureTable3")
        self.measureTable1 = QtWidgets.QTextEdit(self.centralwidget)
        self.measureTable1.setGeometry(QtCore.QRect(570, 525, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.measureTable1.setFont(font)
        self.measureTable1.setObjectName("measureTable1")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(470, 480, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(470, 560, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 665, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.manualText = QtWidgets.QTextEdit(self.centralwidget)
        self.manualText.setGeometry(QtCore.QRect(40, 715, 741, 31))
        self.manualText.setObjectName("manualText")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 805, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.calcManualBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calcManualBtn.setGeometry(QtCore.QRect(40, 765, 131, 28))
        self.calcManualBtn.setObjectName("calcManualBtn")
        self.measureManual = QtWidgets.QTextEdit(self.centralwidget)
        self.measureManual.setGeometry(QtCore.QRect(260, 810, 104, 31))
        self.measureManual.setObjectName("measureManual")
        self.tableTable = QtWidgets.QTableWidget(self.centralwidget)
        self.tableTable.setGeometry(QtCore.QRect(470, 60, 351, 361))
        self.tableTable.setObjectName("tableTable")
        self.tableTable.setColumnCount(3)
        self.tableTable.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTable.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTable.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTable.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableAlg.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableAlg.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableAlg.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableAlg.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableAlg.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableAlg.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableAlg.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableAlg.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableAlg.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableAlg.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableAlg.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "0..9"))
        item = self.tableAlg.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "10..99"))
        item = self.tableAlg.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "100..999"))
        self.label.setText(_translate("MainWindow", "Алгоритмический метод"))
        self.label_2.setText(_translate("MainWindow", "Табличный метод"))
        self.label_3.setText(_translate("MainWindow", "Мера случайности"))
        self.calcAlgBtn.setText(_translate("MainWindow", "Вычислить"))
        self.label_4.setText(_translate("MainWindow", "0..9"))
        self.label_5.setText(_translate("MainWindow", "10..99"))
        self.label_6.setText(_translate("MainWindow", "100..999"))
        self.label_7.setText(_translate("MainWindow", "0..9"))
        self.calcTableBtn.setText(_translate("MainWindow", "Вычислить"))
        self.label_8.setText(_translate("MainWindow", "100..999"))
        self.label_9.setText(_translate("MainWindow", "Мера случайности"))
        self.label_10.setText(_translate("MainWindow", "10..99"))
        self.label_11.setText(_translate("MainWindow", "Ручной ввод (через пробел)"))
        self.label_12.setText(_translate("MainWindow", "Мера случайности"))
        self.calcManualBtn.setText(_translate("MainWindow", "Вычислить"))
        item = self.tableTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableTable.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableTable.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableTable.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableTable.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "0..9"))
        item = self.tableTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "10..99"))
        item = self.tableTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "100..999"))