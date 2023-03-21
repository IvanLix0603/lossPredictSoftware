from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import sys
from read_lscpu import preprocess
from applicatedNN.manager import launchPredict
from tests.manager import launchTests
from learning_model.manager import launchLearnig
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QSplashScreen
import time


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("source/main.ui", self)
        self.show()
        self.buttonPredict.clicked.connect(self.predict_loss)
        self.buttonTest.clicked.connect(self.testing_machine)
        self.buttonLearn.clicked.connect(self.learning_nn)
        self.exit.clicked.connect(app.quit)
        self.clean.clicked.connect(self.cleaning)
        for i in [self.picLoss1,self.picLoss2, self.picLoss3, self.picLoss4, self.learningError, self.testError]:
            pixmap = QPixmap('source/clean_plot.png')
            i.setPixmap(pixmap)


    def cleaning(self):
        self.test_1p.setChecked(False)
        self.test_2p.setChecked(False)
        self.test_3p.setChecked(False)
        self.test_4p.setChecked(False)
        self.btn_25elp.setChecked(False)
        self.btn_50elp.setChecked(False)
        self.btn_100elp.setChecked(False)
        self.btn_150elp.setChecked(False)
        self.btn_200elp.setChecked(False)
        self.btn_300elp.setChecked(False)
        self.btn_500elp.setChecked(False)
        self.btn_1000elp.setChecked(False)
        self.btn_1200elp.setChecked(False)
        self.check_threadsp.setChecked(False)
        self.check_optimization_o1p.setChecked(False)
        self.check_optimization_o2p.setChecked(False)
        self.outputPredict.setText("")


        self.test_1t.setChecked(False)
        self.test_2t.setChecked(False)
        self.test_3t.setChecked(False)
        self.test_4t.setChecked(False)
        self.btn_25elt.setChecked(False)
        self.btn_50elt.setChecked(False)
        self.btn_100elt.setChecked(False)
        self.btn_150elt.setChecked(False)
        self.btn_200elt.setChecked(False)
        self.btn_300elt.setChecked(False)
        self.btn_500elt.setChecked(False)
        self.btn_1000elt.setChecked(False)
        self.btn_1200elt.setChecked(False)
        
        self.numEpochs.setText("")
        self.learningRate.setText("")
        self.batchSize.setText("")

        for i in [self.picLoss1,self.picLoss2, self.picLoss3, self.picLoss4, self.learningError, self.testError]:
            pixmap = QPixmap('source/clean_plot.png')
            i.setPixmap(pixmap)

        
    def predict_loss(self):
        data = preprocess()
        predict_loss = launchPredict() 
        test = []
        elements = []
        if self.test_1p.isChecked():
            test.append(1.0)
        if self.test_2p.isChecked():
            test.append(2.0)
        if self.test_3p.isChecked():
           test.append(3.0)
        if self.test_4p.isChecked():
            test.append(4.0)
        if self.btn_25elp.isChecked():
            elements.append(25.0)
        if self.btn_50elp.isChecked():
            elements.append(50.0)
        if self.btn_100elp.isChecked():
            elements.append(100.0)
        if self.btn_150elp.isChecked():
            elements.append(150.0)
        if self.btn_200elp.isChecked():
            elements.append(200.0)
        if self.btn_300elp.isChecked():
            elements.append(300.0)
        if self.btn_500elp.isChecked():
            elements.append(500.0)
        if self.btn_1000elp.isChecked():
            elements.append(1000.0)
        if self.btn_1200elp.isChecked():
            elements.append(1200.0)
        flag = int(self.check_threadsp.isChecked())
        data["test"] = test[0]
        data["elements"] = elements[0]
        data["O1"] = int(self.check_optimization_o1p.isChecked())
        data["O2"] = int(self.check_optimization_o2p.isChecked())
        data["threads"] = flag
        result = predict_loss.predict(data)
        self.outputPredict.setText(result)
        

    def testing_machine(self):
        tests = []
        elements = []
        pics = [False, False, False, False]
        if self.test_1t.isChecked():
            tests.append(1)
            pics[0] = True
        if self.test_2t.isChecked():
            tests.append(2)
            pics[1] = True
        if self.test_3t.isChecked():
            tests.append(3)
            pics[2] = True
        if self.test_4t.isChecked():
            tests.append(4)
            pics[3] = True
        if self.btn_25elt.isChecked():
            elements.append(25)
        if self.btn_50elt.isChecked():
            elements.append(50)
        if self.btn_100elt.isChecked():
            elements.append(100)
        if self.btn_150elt.isChecked():
            elements.append(150)
        if self.btn_200elt.isChecked():
            elements.append(200)
        if self.btn_300elt.isChecked():
            elements.append(300)
        if self.btn_500elt.isChecked():
            elements.append(500)
        if self.btn_1000elt.isChecked():
            elements.append(1000)
        if self.btn_1200elt.isChecked():
            elements.append(1200)
        launchTests(tests, elements)
        ####
        if pics[0] == True: 
            pixmap = QPixmap('tests/visual/Отображение результатов 1 теста')
            self.picLoss1.setPixmap(pixmap)
        ####
        if pics[1] == True: 
            pixmap = QPixmap('tests/visual/Отображение результатов 2 теста')
            self.picLoss2.setPixmap(pixmap)
        ####
        if pics[2] == True: 
            pixmap = QPixmap('tests/visual/Отображение результатов 3 теста')
            self.picLoss3.setPixmap(pixmap)
        ####
        if pics[3] == True: 
            pixmap = QPixmap('tests/visual/Отображение результатов 4 теста')
            self.picLoss4.setPixmap(pixmap)
        
        
    def learning_nn(self):
        num_epochs = self.numEpochs.text()
        learning_rate = self.learningRate.text()
        batch_size = self.batchSize.text()
        launch_learn = launchLearnig(num_epochs, learning_rate, batch_size) #is it correct?
        pixmap = QPixmap('learning_model/Ошибки при обучении')
        self.learningError.setPixmap(pixmap)
        pixmap = QPixmap('learning_model/Ошибки при тестировании')
        self.testError.setPixmap(pixmap)




if __name__ =="__main__":
    app = QApplication(sys.argv)
    
    splash = QSplashScreen(QPixmap('source/wall2.png'))
    splash.showMessage('Загрузка данных...', Qt.AlignHCenter | Qt.AlignBottom, Qt.yellow)
    splash.show()

    if sys.platform == 'win64':
        app.processEvents()
    else:
        QTimer.singleShot(500, app.quit)
        app.exec()

    time.sleep(3)

    window = MainWindow()
    splash.finish(window)
    app.exec_()
