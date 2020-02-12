#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:40:58 2020

@author: sebastian
"""


import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel,QMessageBox,  QLineEdit, QPushButton, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot


class Example(QWidget):

    distance = 0
    def __init__(self):
        super().__init__()  
        self.width = 300
        self.height = 100
        self.initUI()
           
    def initUI(self):               
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Beam Distance')  
        
        #loading image
        label = QLabel(self)
        pixmap = QPixmap('logo-lidarit.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        
        #tex box
        self.textbox = QLineEdit(self)
        self.textbox.move(50, 270)
        self.textbox.resize(90,20)
        #push button
        self.button = QPushButton('Add distance', self)
        self.button.move(50,300)
        self.button.clicked.connect(self.distanceF)
        #push button 2 load vector of degrees the inform
        self.button = QPushButton('Load Vector BeamsDeg', self)
        self.button.move(150,300)
        self.button.clicked.connect(self.openFileNameDialog)
        #show gui interface
        self.show()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        f = open("direction.txt", "w")
        f.write(fileName)
        f.close
        if fileName:
            print(fileName)
        
    def distanceF(self):           
        textboxValue = self.textbox.text()    
        result = np.genfromtxt('vectorDg.txt', delimiter=',')
        dist = (((int(textboxValue))/np.cos(np.deg2rad(result))))
        np.savetxt('distanciafinal.txt', np.array([dist]), delimiter=',')
        #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        #self.textbox.setText("")
        #dist = (((d)/np.cos(np.deg2rad(thetaVD))))
    """    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()      
    """
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = Example()
    ex.resize(400,400)
    sys.exit(app.exec_())
    
    
    