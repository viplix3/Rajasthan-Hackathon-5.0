#!/usr/bin/python3.6
import sys,os,shutil
import time
import threading
# import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize    

class TrafficUi(QMainWindow):    
    def __init__(self):
        QMainWindow.__init__(self)
        naming = "no file selected"    
        self.setMinimumSize(QSize(800, 481))    
        self.setWindowTitle("Traffic Management") 
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)

        oImage = QImage("ewe.png")
        sImage = oImage.scaled(QSize(1300,481))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        run_btn = QPushButton('RUN',self)
        run_btn.resize(100,40)
        run_btn.move(10,200)
        t2 = threading.Thread(target=self.ssd)
        t2.start()
        time.sleep(5)
        run_btn.clicked.connect(self.runMethod)

        

    def gui(self):
        #time.sleep(10)
        os.system('python work2.py')


    def ssd(self):
        os.system('python ssd_script.py')

    def runMethod(self):
        t1 = threading.Thread(target=self.gui)
        t1.start()
        # t2 = threading.Thread(target=self.ssd)
        # t2.start()
        return
        
        
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainwin = TrafficUi()
    mainwin.show()
    sys.exit(app.exec_())
