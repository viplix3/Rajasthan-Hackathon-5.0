#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:27:37 2018

@author: ujjwal
"""

import time,threading
import sys,os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QFont
from PyQt5.QtCore import QSize    


class TrafficUi(QMainWindow):    
    def __init__(self):
        QMainWindow.__init__(self)
        naming = "no file selected"    
        self.setMinimumSize(QSize(1015, 1000))    
        self.setWindowTitle("Traffic Management") 
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)

        oImage = QImage("b.png")
        sImage = oImage.scaled(QSize(1015,1000))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        newfont = QFont('Roboto', 12, QFont.Bold)
        self.setPalette(palette)

        self.run_btn = QPushButton('Start',self)
        self.run_btn.resize(100,40)
        self.run_btn.move(10,10)
        self.run_btn.clicked.connect(self.runMethod)        

        self.east_label = QLabel("east",self)
        self.east_label.resize(200,40)
        self.east_label.move(780,380)
        self.east_label.setFont(newfont)
        
        self.south_label = QLabel("south",self)
        self.south_label.resize(200,40)
        self.south_label.move(400,825)
        self.south_label.setFont(newfont)

        self.west_label = QLabel("west",self)
        self.west_label.resize(200,40)
        self.west_label.move(160,380)
        self.west_label.setFont(newfont)
        
        self.north_label = QLabel("north",self)
        self.north_label.resize(200,40)
        self.north_label.move(400,175)
        self.north_label.setFont(newfont)

        self.east_density = QLabel("low",self)
        self.east_density.resize(200,40)
        self.east_density.move(780,600)
        self.east_density.setFont(newfont)
        self.east_density.setStyleSheet('color : white;')
        
        self.south_density = QLabel("low",self)
        self.south_density.resize(200,40)
        self.south_density.move(600,825)
        self.south_density.setFont(newfont)
        self.south_density.setStyleSheet('color : white;')

        self.west_density = QLabel("low",self)
        self.west_density.resize(200,40)
        self.west_density.move(160,600)
        self.west_density.setFont(newfont)
        self.west_density.setStyleSheet('color : white;')
        
        self.north_density = QLabel("low",self)
        self.north_density.resize(200,40)
        self.north_density.move(600,175)
        self.north_density.setFont(newfont)
        self.north_density.setStyleSheet('color : white;')


        self.traffic_h = QLabel(self)
        self.traffic_h_pixmap = QPixmap('traffic_lamp2.png')
        self.traffic_h_pixmap = self.traffic_h_pixmap.scaled(150,60)
        self.traffic_h.setPixmap(self.traffic_h_pixmap)
        self.traffic_h.resize(150,60)
        self.traffic_h.move(425,780)
        self.traffic_h.hide()
        self.traffic_h.setStyleSheet('border-style: solid; border-width: 0px 3px 0px 3px; border-color: white;')

        self.traffic_h2 = QLabel(self)
        self.traffic_h2_pixmap = QPixmap('traffic_lamp2.png')
        self.traffic_h2_pixmap = self.traffic_h2_pixmap.scaled(150,60)
        self.traffic_h2.setPixmap(self.traffic_h2_pixmap)
        self.traffic_h2.resize(150,60)
        self.traffic_h2.move(425,160)
        self.traffic_h2.hide()
        self.traffic_h2.setStyleSheet('border-style: solid; border-width: 0px 3px 0px 3px; border-color: white;')

        self.traffic_v = QLabel(self)
        self.traffic_v_pixmap = QPixmap('traffic_lamp.png')
        self.traffic_v_pixmap = self.traffic_v_pixmap.scaled(60,150)
        self.traffic_v.setPixmap(self.traffic_v_pixmap)
        self.traffic_v.resize(60,150)
        self.traffic_v.move(780,425)
        self.traffic_v.hide()
        self.traffic_v.setStyleSheet('border-style: solid; border-width: 3px 0px 3px 0px; border-color: white;')

        self.traffic_v2 = QLabel(self)
        self.traffic_v2_pixmap = QPixmap('traffic_lamp.png')
        self.traffic_v2_pixmap = self.traffic_v2_pixmap.scaled(60,150)
        self.traffic_v2.setPixmap(self.traffic_v2_pixmap)
        self.traffic_v2.resize(60,150)
        self.traffic_v2.move(160,425)
        self.traffic_v2.hide()
        self.traffic_v2.setStyleSheet('border-style: solid; border-width: 3px 0px 3px 0px; border-color: white;')
        
        self.red_label = QLabel(self)
        self.red_pixmap = QPixmap('red.png')
        self.red_pixmap = self.red_pixmap.scaled(50,50)
        self.red_label.setPixmap(self.red_pixmap)
        self.red_label.resize(50,50)
        self.red_label.move(785, 428)

        self.red_label2 = QLabel(self)
        self.red_pixmap2 = QPixmap('red.png')
        self.red_pixmap2 = self.red_pixmap2.scaled(50,50)
        self.red_label2.setPixmap(self.red_pixmap2)
        self.red_label2.resize(50,50)
        self.red_label2.move(431, 785)

        self.red_label3 = QLabel(self)
        self.red_pixmap3 = QPixmap('red.png')
        self.red_pixmap3 = self.red_pixmap3.scaled(50,50)
        self.red_label3.setPixmap(self.red_pixmap3)
        self.red_label3.resize(50,50)
        self.red_label3.move(166, 428)

        self.red_label4 = QLabel(self)
        self.red_pixmap4 = QPixmap('red.png')
        self.red_pixmap4 = self.red_pixmap4.scaled(50,50)
        self.red_label4.setPixmap(self.red_pixmap4)
        self.red_label4.resize(50,50)
        self.red_label4.move(431, 166)

        self.yellow_label = QLabel(self)
        self.yellow_pixmap = QPixmap('yellow.png')
        self.yellow_pixmap = self.yellow_pixmap.scaled(50,50)
        self.yellow_label.setPixmap(self.yellow_pixmap)
        self.yellow_label.resize(50,50)
        self.yellow_label.move(785, 475)

        self.yellow_label2 = QLabel(self)
        self.yellow_pixmap2 = QPixmap('yellow.png')
        self.yellow_pixmap2 = self.yellow_pixmap2.scaled(50,50)
        self.yellow_label2.setPixmap(self.yellow_pixmap2)
        self.yellow_label2.resize(50,50)
        self.yellow_label2.move(478, 785)

        self.yellow_label3 = QLabel(self)
        self.yellow_pixmap3 = QPixmap('yellow.png')
        self.yellow_pixmap3 = self.yellow_pixmap3.scaled(50,50)
        self.yellow_label3.setPixmap(self.yellow_pixmap3)
        self.yellow_label3.resize(50,50)
        self.yellow_label3.move(166, 475)

        self.yellow_label4 = QLabel(self)
        self.yellow_pixmap4 = QPixmap('yellow.png')
        self.yellow_pixmap4 = self.yellow_pixmap4.scaled(50,50)
        self.yellow_label4.setPixmap(self.yellow_pixmap4)
        self.yellow_label4.resize(50,50)
        self.yellow_label4.move(478, 166)

        self.green_label = QLabel(self)
        self.green_pixmap = QPixmap('green.png')
        self.green_pixmap = self.green_pixmap.scaled(50,50)
        self.green_label.setPixmap(self.green_pixmap)
        self.green_label.resize(50,50)
        self.green_label.move(785, 522)

        self.green_label2 = QLabel(self)
        self.green_pixmap2 = QPixmap('green.png')
        self.green_pixmap2 = self.green_pixmap2.scaled(50,50)
        self.green_label2.setPixmap(self.green_pixmap2)
        self.green_label2.resize(50,50)
        self.green_label2.move(525, 785)

        self.green_label3 = QLabel(self)
        self.green_pixmap3 = QPixmap('green.png')
        self.green_pixmap3 = self.green_pixmap3.scaled(50,50)
        self.green_label3.setPixmap(self.green_pixmap3)
        self.green_label3.resize(50,50)
        self.green_label3.move(166, 522)

        self.green_label4 = QLabel(self)
        self.green_pixmap4 = QPixmap('green.png')
        self.green_pixmap4 = self.green_pixmap4.scaled(50,50)
        self.green_label4.setPixmap(self.green_pixmap4)
        self.green_label4.resize(50,50)
        self.green_label4.move(525, 166)

        self.east_road = QLabel(self)
        self.east_road_pixmap = QPixmap('./Test/images/east.png')
        self.east_road_pixmap = self.east_road_pixmap.scaled(150,150)
        self.east_road.setPixmap(self.east_road_pixmap)
        self.east_road.resize(150,150)
        self.east_road.move(10,-250)
        self.east_road.setStyleSheet('border-style: solid; border-width: 3px; border-color: white;')
                

        self.east_road_bbox = QLabel(self)
        self.east_road_bbox_pixmap = QPixmap('./Test/images/east_bbox.png')
        self.east_road_bbox_pixmap = self.east_road_bbox_pixmap.scaled(150,150)
        self.east_road_bbox.setPixmap(self.east_road_bbox_pixmap)
        self.east_road_bbox.resize(150,150)
        self.east_road_bbox.move(10,-250)
        self.east_road_bbox.setStyleSheet('border-style: solid; border-width: 3px; border-color: white;')
                

        self.south_road = QLabel(self)
        self.south_road_pixmap = QPixmap('./Test/images/south.png')
        self.south_road_pixmap = self.south_road_pixmap.scaled(150,150)
        self.south_road.setPixmap(self.south_road_pixmap)
        self.south_road.resize(150,150)
        self.south_road.move(10,-250)
        self.south_road.setStyleSheet('border-style: solid; border-width: 3px; border-color: white;')
                
        self.south_road_bbox = QLabel(self)
        self.south_road_bbox_pixmap = QPixmap('./Test/images/south_bbox.png')
        self.south_road_bbox_pixmap = self.south_road_bbox_pixmap.scaled(150,150)
        self.south_road_bbox.setPixmap(self.south_road_bbox_pixmap)
        self.south_road_bbox.resize(150,150)
        self.south_road_bbox.move(10,-250)
        self.south_road_bbox.setStyleSheet('border-style: solid; border-width: 3px; border-color: white;')
                
        self.west_road = QLabel(self)
        self.west_road_pixmap = QPixmap('./Test/images/west.png')
        self.west_road_pixmap = self.west_road_pixmap.scaled(150,150)
        self.west_road.setPixmap(self.west_road_pixmap)
        self.west_road.resize(150,150)
        self.west_road.move(10,-250)
        self.west_road.setStyleSheet('border-style: solid; border-width: 3px; border-color: white;')
                
        self.west_road_bbox = QLabel(self)
        self.west_road_bbox_pixmap = QPixmap('./Test/images/west_bbox.png')
        self.west_road_bbox_pixmap = self.west_road_bbox_pixmap.scaled(150,150)
        self.west_road_bbox.setPixmap(self.west_road_bbox_pixmap)
        self.west_road_bbox.resize(150,150)
        self.west_road_bbox.move(10,-250)
        self.west_road_bbox.setStyleSheet('border-style: solid; border-width: 3px; border-color: white;')
                
        self.north_road = QLabel(self)
        self.north_road_pixmap = QPixmap('./Test/images/north.png')
        self.north_road_pixmap = self.north_road_pixmap.scaled(150,150)
        self.north_road.setPixmap(self.north_road_pixmap)
        self.north_road.resize(150,150)
        self.north_road.move(10,-250)
        self.north_road.setStyleSheet('border-style: solid; border-width: 3px; border-color: white;')
                
        self.north_road_bbox = QLabel(self)
        self.north_road_bbox_pixmap = QPixmap('./Test/images/north_bbox.png')
        self.north_road_bbox_pixmap = self.north_road_bbox_pixmap.scaled(150,150)
        self.north_road_bbox.setPixmap(self.north_road_bbox_pixmap)
        self.north_road_bbox.resize(150,150)
        self.north_road_bbox.move(10,-250)
        self.north_road_bbox.setStyleSheet('border-style: solid; border-width: 3px; border-color: white;')
                


    def runMethod(self):

        t2 = threading.Thread(target=self.print_images)
        t2.start()
        self.runMethod_()



    def runMethod_(self):

        self.run_btn.hide()
        QApplication.processEvents()
        
        self.east = 30
        self.south = 60
        self.west = 90
        self.north = 120
        self.cur = "east"

        self.east_status ="low"
        self.south_status = "low"
        self.west_status = "low"
        self.north_status = "low"

        self.traffic_v2.show()
        self.traffic_v.show()
        self.traffic_h.show()
        self.traffic_h2.show()

        while(True):
                if self.cur == "east":
                    self.east_label.setText(str(self.east))
                    self.south_label.setText(str(self.south-30))
                    self.west_label.setText(str(self.west-30))
                    self.north_label.setText(str(self.north-30))
                if self.cur == "south":
                    self.east_label.setText(str(self.east-30))
                    self.south_label.setText(str(self.south))
                    self.west_label.setText(str(self.west-30))
                    self.north_label.setText(str(self.north-30))
                if self.cur == "west":
                    self.east_label.setText(str(self.east-30))
                    self.south_label.setText(str(self.south-30))
                    self.west_label.setText(str(self.west))
                    self.north_label.setText(str(self.north-30))
                if self.cur == "north":
                    self.east_label.setText(str(self.east-30))
                    self.south_label.setText(str(self.south-30))
                    self.west_label.setText(str(self.west-30))
                    self.north_label.setText(str(self.north))
                QApplication.processEvents()
                self.file = open('val.txt','r+')
                self.cont = self.file.read();
                self.cont = self.cont[1:-2]
                self.cont = self.cont.replace(',','')
                self.east_st,self.south_st,self.west_st,self.north_st = self.cont.split(' ')

                
                print(self.east_st,self.south_st,self.west_st,self.north_st)
                
                if float(self.east_st) >40:
                    self.east_status = "High"
                elif float(self.east_st) >30:
                    self.east_status = "Mod"
                else:
                    self.east_status = "low"

                if float(self.south_st) >40:
                    self.south_status = "High"
                elif float(self.south_st) >30:
                    self.south_status = "Mod"
                else:
                    self.south_status = "low"

                if float(self.west_st) >40:
                    self.west_status = "High"
                elif float(self.west_st) >30:
                    self.west_status = "Mod"
                else:
                    self.west_status = "low"

                if float(self.north_st) >40:
                    self.north_status = "High"
                elif float(self.north_st) >30:
                    self.north_status = "Mod"
                else:
                    self.north_status = "low"
                 
                print(self.east_status,self.south_status,self.west_status,self.north_status)
                
                time.sleep(0.9)
                
                self.east -=1
                self.south -=1
                self.west -=1
                self.north -=1
                if self.east==0:
                        self.east = 120
                        self.south = 30
                        self.west = 60
                        self.north = 90
                        self.cur="south"
                if self.south==0:
                        self.east = 90
                        self.south = 120
                        self.west = 30
                        self.north = 60
                        self.cur = "west"
                if self.west==0:
                        self.east = 60
                        self.south = 90
                        self.west = 120
                        self.north = 30
                        self.cur = "north"
                if self.north==0:
                        self.east = 30
                        self.south = 60
                        self.west = 90
                        self.north = 120
                        self.cur = "east"

                if self.east>35:
                    self.east_label.setStyleSheet('color: red')
                    self.red_label.show()
                    self.yellow_label.hide()
                    self.green_label.hide()
                elif self.east>30:
                    self.east_label.setStyleSheet('color: yellow')
                    self.red_label.hide()
                    self.yellow_label.show()
                    self.green_label.hide()
                else:
                    self.east_label.setStyleSheet('color: green')
                    self.red_label.hide()
                    self.yellow_label.hide()
                    self.green_label.show()

                if self.south>35:
                    self.south_label.setStyleSheet('color: red')
                    self.red_label2.show()
                    self.yellow_label2.hide()
                    self.green_label2.hide()
                elif self.south>30:
                    self.south_label.setStyleSheet('color: yellow')
                    self.red_label2.hide()
                    self.yellow_label2.show()
                    self.green_label2.hide()
                else:
                    self.south_label.setStyleSheet('color: green')
                    self.red_label2.hide()
                    self.yellow_label2.hide()
                    self.green_label2.show()

                if self.west>35:
                    self.west_label.setStyleSheet('color: red')
                    self.red_label3.show()
                    self.yellow_label3.hide()
                    self.green_label3.hide()
                elif self.west>30:
                    self.west_label.setStyleSheet('color: yellow')
                    self.red_label3.hide()
                    self.yellow_label3.show()
                    self.green_label3.hide()
                else:
                    self.west_label.setStyleSheet('color: green')
                    self.red_label3.hide()
                    self.yellow_label3.hide()
                    self.green_label3.show()

                if self.north>35:
                    self.north_label.setStyleSheet('color: red')
                    self.red_label4.show()
                    self.yellow_label4.hide()
                    self.green_label4.hide()
                elif self.north>30:
                    self.north_label.setStyleSheet('color: yellow')
                    self.red_label4.hide()
                    self.yellow_label4.show()
                    self.green_label4.hide()
                else:
                    self.north_label.setStyleSheet('color: green')
                    self.red_label4.hide()
                    self.yellow_label4.hide()
                    self.green_label4.show()

                

                if self.east_status == "High":
                        if self.cur != "east":
                                if (self.cur == "west" and self.west>10) and self.west_status != 'High':
                                        self.east = 70
                                        self.south = 100
                                        self.west = 10
                                        self.north = 40
                                elif (self.cur == "north" and self.north>10) and self.north_status != 'High':
                                        self.east = 40
                                        self.south = 70
                                        self.west = 100
                                        self.north = 10
                                elif (self.cur == "south" and self.south>10) and self.south_status != 'High':
                                        self.east = 100
                                        self.south = 10
                                        self.west = 40
                                        self.north = 70
                        #self.east_status = "low"
                elif self.south_status == "High":
                        if self.cur != "south":
                                if (self.cur == "west" and self.west>10) and self.west_status != 'High':
                                        self.east = 70
                                        self.south = 100
                                        self.west = 10
                                        self.north = 40
                                elif (self.cur == "north" and self.north>10) and self.north_status != 'High':
                                        self.east = 40
                                        self.south = 70
                                        self.west = 100
                                        self.north = 10
                                elif (self.cur == "east" and self.east>10) and self.east_status != 'High':
                                        self.east = 10
                                        self.south = 40
                                        self.west = 70
                                        self.north = 100
                        #self.south_status = "low"
                elif self.west_status == "High":
                        if self.cur != "west":
                                if (self.cur == "east" and self.east>10) and self.east_status != 'High':
                                        self.east = 10
                                        self.south = 40
                                        self.west = 70
                                        self.north = 100
                                elif (self.cur == "south" and self.south>10) and self.south_status != 'High':
                                        self.east = 100
                                        self.south = 10
                                        self.west = 40
                                        self.north = 70
                                elif (self.cur == "north" and self.north>10) and self.north_status != 'High':
                                        self.east = 40
                                        self.south = 70
                                        self.west = 100
                                        self.north = 10
                        #self.west_status = "low"
                elif self.north_status == "High":
                        if self.cur != "north":
                                if (self.cur == "east" and self.east>10) and self.east_status != 'High':
                                        self.east = 10
                                        self.south = 40
                                        self.west = 70
                                        self.north = 100
                                elif (self.cur == "south" and self.south>10) and self.south_status != 'High':
                                        self.east = 100
                                        self.south = 10
                                        self.west = 40
                                        self.north = 70
                                elif (self.cur == "west" and self.west>10) and self.west_status != 'High':
                                        self.east = 70
                                        self.south = 100
                                        self.west = 10
                                        self.north = 40
                        #self.north_status = "low"

                elif self.east_status == "Mod":
                        if self.cur != "east":
                                if (self.cur == "west" and self.west>15) and self.west_status == 'low':
                                        self.east = 75
                                        self.south = 105
                                        self.west = 15
                                        self.north = 45
                                elif (self.cur == "north" and self.north>15) and self.north_status == 'low':
                                        self.east = 45
                                        self.south = 75
                                        self.west = 105
                                        self.north = 15
                                elif (self.cur == "south" and self.south>15) and self.south_status == 'low':
                                        self.east = 105
                                        self.south = 15
                                        self.west = 45
                                        self.north = 75
                        #self.east_status = "low"
                elif self.south_status == "Mod":
                        if self.cur != "south":
                                if (self.cur == "west" and self.west>15) and self.west_status == 'low':
                                        self.east = 75
                                        self.south = 105
                                        self.west = 15
                                        self.north = 45
                                elif (self.cur == "north" and self.north>15) and self.north_status == 'low':
                                        self.east = 45
                                        self.south = 75
                                        self.west = 105
                                        self.north = 15
                                elif (self.cur == "east" and self.east>15) and self.east_status == 'low':
                                        self.east = 15
                                        self.south = 45
                                        self.west = 75
                                        self.north = 105
                        #self.south_status = "low"
                elif self.west_status == "Mod":
                        if self.cur != "west":
                                if (self.cur == "east" and self.east>15) and self.east_status == 'low':
                                        self.east = 15
                                        self.south = 45
                                        self.west = 75
                                        self.north = 105
                                elif (self.cur == "south" and self.south>15) and self.south_status == 'low':
                                        self.east = 105
                                        self.south = 15
                                        self.west = 45
                                        self.north = 75
                                elif (self.cur == "north" and self.north>15) and self.north_status == 'low':
                                        self.east = 45
                                        self.south = 75
                                        self.west = 105
                                        self.north = 15
                        #self.west_status = "low"
                elif self.north_status == "Mod":
                        if self.cur != "north":
                                if (self.cur == "east" and self.east>15) and self.east_status == 'low':
                                        self.east = 15
                                        self.south = 45
                                        self.west = 75
                                        self.north = 105
                                elif (self.cur == "south" and self.south>15) and self.south_status == 'low':
                                        self.east = 105
                                        self.south = 15
                                        self.west = 45
                                        self.north = 75
                                elif (self.cur == "west" and self.west>15) and self.west_status == 'low':
                                        self.east = 75
                                        self.south = 105
                                        self.west = 15
                                        self.north = 45
                        #self.north_status = "low"
                self.east_density.setText(self.east_status)
                self.south_density.setText(self.south_status)
                self.west_density.setText(self.west_status)
                self.north_density.setText(self.north_status)

                print(self.east,self.south,self.west,self.north)
                
                print(self.east_status,self.south_status,self.west_status,self.north_status)
                


    def print_images(self):

        while True:
            self.east_road_pixmap = QPixmap('./Test/images/east.png')
            if not self.east_road_pixmap.isNull():
                self.east_road_pixmap = self.east_road_pixmap.scaled(150,150)
                self.east_road.setPixmap(self.east_road_pixmap)
                self.east_road.resize(150,150)
                self.east_road.move(630,425)
                
            self.east_road_bbox_pixmap = QPixmap('./Test/images/east_bbox.png')
            if not self.east_road_bbox_pixmap.isNull():
                self.east_road_bbox_pixmap = self.east_road_bbox_pixmap.scaled(150,150)
                self.east_road_bbox.setPixmap(self.east_road_bbox_pixmap)
                self.east_road_bbox.resize(150,150)
                self.east_road_bbox.move(840,425)

            self.south_road_pixmap = QPixmap('./Test/images/south.png')
            if not self.south_road_pixmap.isNull():
                self.south_road_pixmap = self.south_road_pixmap.scaled(150,150)
                self.south_road.setPixmap(self.south_road_pixmap)
                self.south_road.resize(150,150)
                self.south_road.move(425,630)

            self.south_road_bbox_pixmap = QPixmap('./Test/images/south_bbox.png')
            if not self.south_road_bbox_pixmap.isNull():
                self.south_road_bbox_pixmap = self.south_road_bbox_pixmap.scaled(150,150)
                self.south_road_bbox.setPixmap(self.south_road_bbox_pixmap)
                self.south_road_bbox.move(425,840)

            self.west_road_pixmap = QPixmap('./Test/images/west.png')
            if not self.west_road_pixmap.isNull():
                self.west_road_pixmap = self.west_road_pixmap.scaled(150,150)
                self.west_road.setPixmap(self.west_road_pixmap)
                self.west_road.move(220,425)

            self.west_road_bbox_pixmap = QPixmap('./Test/images/west_bbox.png')
            if not self.west_road_bbox_pixmap.isNull():
                self.west_road_bbox_pixmap = self.west_road_bbox_pixmap.scaled(150,150)
                self.west_road_bbox.setPixmap(self.west_road_bbox_pixmap)
                self.west_road_bbox.move(10,425)

            self.north_road_pixmap = QPixmap('./Test/images/north.png')
            if not self.north_road_pixmap.isNull():
                self.north_road_pixmap = self.north_road_pixmap.scaled(150,150)
                self.north_road.setPixmap(self.north_road_pixmap)
                self.north_road.resize(150,150)
                self.north_road.move(425,220)

            self.north_road_bbox_pixmap = QPixmap('./Test/images/north_bbox.png')
            if not self.north_road_bbox_pixmap.isNull():
                self.north_road_bbox_pixmap = self.north_road_bbox_pixmap.scaled(150,150)
                self.north_road_bbox.setPixmap(self.north_road_bbox_pixmap)
                self.north_road_bbox.resize(150,150)
                self.north_road_bbox.move(425,10)

            time.sleep(0.3)




if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mainwin = TrafficUi()
    mainwin.show()
    sys.exit(app.exec_())


