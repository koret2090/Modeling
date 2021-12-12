import sys
from PyQt5 import QtWidgets
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem,  QTableWidgetItem, QMessageBox
import design
from itertools import islice

COUNT = 10000

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        self.current = 10
        self.m = 2.**32
        self.a = 1664525
        self.c = 1013904223
        self.count = 1

        super().__init__()
        self.setupUi(self)
        self.initUI()    
        
        self.setFixedSize(858, 875) 

    def initUI(self):
        self.calcAlgBtn.clicked.connect(self.calcAlgBtnPushed)
        self.calcTableBtn.clicked.connect(self.calcTableBtnPushed)
        self.calcManualBtn.clicked.connect(self.calcManualBtnPushed)

    def get_number(self, low=0, high=100):
        self.current = (self.a * self.current + self.c) % self.m
        result = int(low + self.current % (high - low))
        return result


    def calcAlgBtnPushed(self):
        one_alg, two_alg, three_alg = self.alg_rand()

        for i in range(10):
            self.tableAlg.setItem(i, 0, QTableWidgetItem(str(one_alg[10*(self.count-1):10*self.count][i])))
            self.tableAlg.setItem(i, 1, QTableWidgetItem(str(two_alg[10*(self.count-1):10*self.count][i])))
            self.tableAlg.setItem(i, 2, QTableWidgetItem(str(three_alg[10*(self.count-1):10*self.count][i])))

        self.measureAlg1.clear()
        self.measureAlg2.clear()
        self.measureAlg3.clear()
        self.measureAlg1.setText(str(round(self.calc_hi(one_alg, 10000, 0, 10), 3)))
        self.measureAlg2.setText(str(round(self.calc_hi(two_alg, 10000, 10, 100), 3)))
        self.measureAlg3.setText(str(round(self.calc_hi(three_alg, 10000, 100, 1000), 3)))

        self.count += 1

    def calcTableBtnPushed(self):
        one_tbl, two_tbl, three_tbl = self.table_rand()
        #self.tableTable.clear()
        for i in range(10):
            self.tableTable.setItem(i, 0, QTableWidgetItem(str(one_tbl[:10][i])))
            self.tableTable.setItem(i, 1, QTableWidgetItem(str(two_tbl[:10][i])))
            self.tableTable.setItem(i, 2, QTableWidgetItem(str(three_tbl[:10][i])))
    
        self.measureTable1.clear()
        self.measureTable2.clear()
        self.measureTable3.clear()
        self.measureTable1.setText(str(round(self.calc_hi(one_tbl, 10000, 0, 10), 3)))
        self.measureTable2.setText(str(round(self.calc_hi(two_tbl, 10000, 10, 100), 3)))
        self.measureTable3.setText(str(round(self.calc_hi(three_tbl, 10000, 100, 1000), 3)))

        self.count += 1

    def table_rand(self):
        numbers = set()
        with open('numbers.txt') as file: 
            line_num = 0
            lines = islice(file, line_num, None)
            for l in lines:
                numbers.update(set(l.split(" ")[1:-1]))
                line_num += 1
                if len(numbers) >= 3* COUNT + 1:
                    break
            numbers.remove("") 
            numbers = list(numbers)[:3*COUNT]
        one_digit = [int(i)%10 for i in numbers[:COUNT]]
        two_digits = [int(i)%90 + 10 for i in numbers[COUNT:COUNT * 2]]
        three_digits = [int(i)%900 + 100 for i in numbers[COUNT*2:3*COUNT]]
        return one_digit, two_digits, three_digits

    def alg_rand(self):
        one_digit = [self.get_number(0, 10) for i in range(COUNT)]
        two_digits = [self.get_number(10, 100) for i in range(COUNT)]
        three_digits = [self.get_number(100, 1000) for i in range(COUNT)]
        return  one_digit, two_digits, three_digits

    def calc_hi(self, arr, n, start, end): 
        tab = [0 for i in range(start + end)]

        for i in range(n):
            tab[arr[i]] += 1
        s = 0
        
        for i in tab:
            s += i * i
        
        return s * (end-start) / n - n 
        
    def calcManualBtnPushed(self):
        nums = self.manualText.toPlainText().split()
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        
        hi = self.calc_hi(nums, len(nums), min(nums), max(nums)+1)
        self.measureManual.setText(str(round(hi, 3)))
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main() 

