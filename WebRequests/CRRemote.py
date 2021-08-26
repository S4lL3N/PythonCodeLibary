"""
req.post("https://maker.ifttt.com/trigger/CR_RED/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn")

req.post("https://maker.ifttt.com/trigger/CR_OFF/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn")
req.post("https://maker.ifttt.com/trigger/CR_ON/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn")
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import requests as req

from gspread import *
from oauth2client.service_account import ServiceAccountCredentials
import datetime

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'CR Lights'
        self.left = 800
        self.top = 500
        self.width = 100
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
        button = QPushButton('ON', self)
        button2 = QPushButton('RED', self)
        button3 = QPushButton('OFF', self)
    

        button.setToolTip('Turns lights ON')
        button2.setToolTip('Turns lights RED')
        button3.setToolTip('Turns lights OFF')
       

        button.move(30,25)
        button2.move(30,75)
        button3.move(30,125)
        

        button.clicked.connect(self.on_click)
        button2.clicked.connect(self.on_click2)
        button3.clicked.connect(self.on_click3)
        
        
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Lights ON')
        r = req.post("https://maker.ifttt.com/trigger/CR_ON/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn") #WAN
        print(f'Status code: [{r.status_code}]')
        

    @pyqtSlot()
    def on_click2(self):
        print('RED LIGHtS ON')
        r2 = req.post("https://maker.ifttt.com/trigger/CR_RED/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn") #WAN
        print(f'Status code: [{r2.status_code}]')
        

    @pyqtSlot()
    def on_click3(self):
        print('Lights OFF')        
        r3 = req.post("https://maker.ifttt.com/trigger/CR_OFF/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn")
        print(f'Status code: [{r3.status_code}]')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())