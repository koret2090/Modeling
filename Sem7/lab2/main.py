import sys
from PyQt5 import QtWidgets
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem,  QTableWidgetItem, QMessageBox
import design
import solvation
import stabilization
import matplotlib.pyplot as plt

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        self.is_ended = False
        self.ended_index = 0

        super().__init__()
        self.setupUi(self)  
        self.initUI()     

    def initUI(self):
        self.statesBox.valueChanged.connect(self.generateTable)
        self.table.itemChanged.connect(self.inputCheck)
        self.pushButton.clicked.connect(self.calculate)

        self.setFixedSize(988, 884)
        
    def generateTable(self, value):
        self.table.setRowCount(value + 2)
        self.table.setColumnCount(value)
        self.table.clearContents()

        horizontalLabels = ["S" + str(i) for i in range(1, value + 1)]
        self.table.setHorizontalHeaderLabels(horizontalLabels)
        
        verticalLabels = horizontalLabels.copy()
        verticalLabels.append("P")
        verticalLabels.append("T")
        self.table.setVerticalHeaderLabels(verticalLabels)

    def inputCheck(self, value):
        try:
            if value.text() != "":
                float(value.text())
        except ValueError:
            QMessageBox.warning(None, "Ошибка", "Введите число.")
            value.setText("")
        
    def getMatrixFromTable(self):
        res = []
        try:
            for i in range(self.table.rowCount() - 2):
                row = []
                for j in range(self.table.columnCount()):
                    item  = self.table.item(i, j)
                    if item and item.text() != "":
                        row.append(float(item.text()))
                    else:
                        row.append(0)                    
                res.append(row)
        except KeyError:
            print(res)
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Введите число.")
        return res    

    def generateFirstProbabilities(self, count):
        res = [0] * count
        res[0] = 1
        return res
    
    def drawGraphics(self, probabilities, stabilization_time, times, probabilities_over_time):
        plt.close()
        for i in range(len(probabilities_over_time[0])):
            plt.plot(times, [j[i] for j in probabilities_over_time])
            plt.scatter(stabilization_time[i], probabilities[i])

        plt.legend(range(len(probabilities)))
        plt.xlabel('time')
        plt.ylabel('probability')
        plt.show()

    def inputProbabilities(self, probability):
        if len(probability) == 0:
            QtWidgets.QMessageBox.critical(None, "Ошибка", "Некорректный ввод")
            return
        else:
            index = 0
            for state in probability:
                item = QTableWidgetItem()
                item.setText(str(round(state, 4)))
                self.table.setItem(self.table.rowCount() - 2, index, item)
                index += 1 
    
    def inputTimings(self, timings):
        if len(timings) == 0:
            QtWidgets.QMessageBox.critical(None, "Ошибка", "Некорректный ввод")
            return
        else:
            index = 0
            for state in timings:
                item = QTableWidgetItem()
                item.setText(str(round(state, 4)))
                self.table.setItem(self.table.rowCount() - 1, index, item)
                index += 1 

    def calculate(self):
        matrix = self.getMatrixFromTable()
        probability = solvation.solve(matrix)      
        self.inputProbabilities(probability)
                
        firstProbabilities = self.generateFirstProbabilities(len(matrix))
        stabilizationTime = stabilization.CalculateStabilizationTimings(matrix, firstProbabilities, probability) 
        
        self.inputTimings(stabilizationTime)       
        times, allProbabilities = stabilization.CalculateAllProbabilities(matrix,  firstProbabilities, 5)
        self.drawGraphics(probability, stabilizationTime, times, allProbabilities)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()