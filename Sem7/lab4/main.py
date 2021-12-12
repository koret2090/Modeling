import sys
from PyQt5 import QtWidgets
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem,  QTableWidgetItem, QMessageBox
import design
from models import event_model, step_model
from distributions import UniformDistribution, PoissonDistribution

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        a, b = 1, 10
        self.generator = UniformDistribution(a, b)

        lyambda = 2.0
        self.processor = PoissonDistribution(lyambda)

        self.total_tasks = 1000
        self.repeat_percentage = 0
        self.step = 0.01

        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.startBtn.clicked.connect(self.startBtnPushed)


    def startBtnPushed(self):
        a = self.aSpinBox.value()
        b = self.bSpinBox.value()
        lyambda = self.lyambdaSpinBox.value()

        self.generator = UniformDistribution(a, b)
        self.processor = PoissonDistribution(lyambda)

        self.total_tasks = self.tasksSpinBox.value()
        self.repeat_percentage = self.repeatSpinBox.value()
        self.step = self.stepSpinBox.value()
        processed_tasks, reentered_tasks, max_queue_len, t = 0, 0, 0, 0
        if self.methodComboBox.currentText() == "Событийный":
            processed_tasks, reentered_tasks, max_queue_len, t = event_model(self.generator, self.processor, self.total_tasks, self.repeat_percentage)
        else:
            processed_tasks, reentered_tasks, max_queue_len, t = step_model(self.generator, self.processor, self.total_tasks, self.repeat_percentage)

        self.resTasksLabel.setText(str(processed_tasks))
        self.repeatTasksLabel.setText(str(reentered_tasks))
        self.maxLenLabel.setText(str(max_queue_len))
        self.timeLabel.setText(str(round(t, 2)))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

    print('event_model:', event_model(generator, processor, total_tasks, repeat_percentage))
    print('step_model:', step_model(generator, processor, total_tasks, repeat_percentage, step))


if __name__ == '__main__':
    main()
