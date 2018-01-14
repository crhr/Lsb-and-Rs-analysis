# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
#from PyQt4.Qt import QMessageBox, QCoreApplication, QFileDialog, SLOT, QPixmap,\
#    QImage
from PyQt4.Qt import *
import sys
from PyQt4.QtCore import Qt
from signal import signal
import lsbencode
import lsbdecode
import rsmain
from PIL import Image
import numpy
from numpy import double

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(634, 390)
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setFixedSize(MainWindow.width(),MainWindow.height())
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 351))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(40, 10, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 10, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 290, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 290, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 161, 20))
        #self.lineEdit.setReadOnly()
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 10, 161, 20))
        #self.lineEdit_2.setReadOnly()
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 51, 250, 220))
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(340, 51, 250, 220))
        self.label_2.setFrameShape(QtGui.QFrame.Box)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 290, 241, 20))
        #self.lineEdit_3.setReadOnly()
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 280, 280))
        self.label_3.setFrameShape(QtGui.QFrame.Box)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 50, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(380, 130, 75, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 80, 201, 20))
        #self.lineEdit_4.setReadOnly()
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(380, 200, 71, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(450, 200, 113, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(380, 160, 201, 20))
        #self.lineEdit_6.setReadOnly()
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(430, 250, 75, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(40, 20, 280, 280))
        self.label_5.setFrameShape(QtGui.QFrame.Box)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(360, 50, 111, 23))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(480, 50, 75, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.lineEdit_7 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(350, 80, 231, 20))
        #self.lineEdit_7.setReadOnly()
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.pushButton_9 = QtGui.QPushButton(self.tab_3)
        self.pushButton_9.setGeometry(QtCore.QRect(410, 120, 75, 23))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        
        self.label_7 = QtGui.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(410, 160, 101, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        
        self.progressBar = QtGui.QProgressBar(self.tab_3)
        self.progressBar.setGeometry(QtCore.QRect(410, 200, 131, 41))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        
        
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        
        
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
#         self.action_2 = QtGui.QAction(MainWindow)
#         self.action_2.setObjectName(_fromUtf8("action_2"))
        self.menu.addAction(self.action)
#         self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())
        self.tabWidget.setCurrentIndex(2)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.centralwidget.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'),self.selectfile)
        #self.action_2.triggered.connect(quit)
        self.centralwidget.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.selectimage1)
        self.centralwidget.connect(self.pushButton_3,QtCore.SIGNAL('clicked()'),self.saveimage)
        self.centralwidget.connect(self.pushButton_6,QtCore.SIGNAL('clicked()'),self.savefile)
        self.centralwidget.connect(self.pushButton_5,QtCore.SIGNAL('clicked()'),self.selectimage2)
        self.centralwidget.connect(self.pushButton_8,QtCore.SIGNAL('clicked()'),self.selectimage3)
        self.centralwidget.connect(self.pushButton_4,QtCore.SIGNAL('clicked()'),self.run1)
        self.centralwidget.connect(self.pushButton_7,QtCore.SIGNAL('clicked()'),self.run2)
        self.centralwidget.connect(self.pushButton_9,QtCore.SIGNAL('clicked()'),self.analyse)
        self.action.triggered.connect(self.onAbout)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "LSB&RS", None))
        #.....
        self.pushButton.setText(_translate("MainWindow", "选择图片", None))
        
        self.pushButton_2.setText(_translate("MainWindow", "选择文件", None))
        
        self.pushButton_3.setText(_translate("MainWindow", "保存", None))
        
        self.pushButton_4.setText(_translate("MainWindow", "运行", None))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "隐写", None))
        
        self.pushButton_5.setText(_translate("MainWindow", "选择图片", None))
        
        self.pushButton_6.setText(_translate("MainWindow", "保存路径", None))
        
        self.label_4.setText(_translate("MainWindow", "输入提取码", None))
        
        self.pushButton_7.setText(_translate("MainWindow", "运行", None))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "提取", None))
        
        self.label_6.setText(_translate("MainWindow", "选择需要分析的图片", None))
        
        self.pushButton_8.setText(_translate("MainWindow", "选择图片", None))
        
        self.pushButton_9.setText(_translate("MainWindow", "分析", None))
        
        self.label_7.setText(_translate("MainWindow", "该图片的嵌入率为", None))
        #....
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "分析", None))
        #....
        self.menu.setTitle(_translate("MainWindow", "菜单", None))
        #....
        self.action.setText(_translate("MainWindow", "关于", None))

        #self.action_2.setText(_translate("MainWindow", "退出", None))
        
    def selectfile(self):
        file_path = QFileDialog.getOpenFileName()
        self.lineEdit_2.setText(file_path)
        
        
#///////////////////////////////        
    def selectimage1(self):
        image_path1 = QFileDialog.getOpenFileName(self.pushButton,"select a BMP image","C:\Users\Administrator\Desktop","BMP files(*.bmp)")
        self.lineEdit.setText(image_path1)
        x = self.label.width()
        y = self.label.height()
        image = QImage(image_path1)
        x = double(x)
        y = double(y)
        if image.width() >= image.height():
            tmp = image.width() / x
        else:
            tmp = image.height() / y
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setPixmap(QPixmap.fromImage(image).scaled(image.size()/tmp))
        filesize = double(image.width()*image.height()*3/8)/1000
        mes ="this image can encrypt the filesize is %dKB"%(filesize)
        self.statusbar.showMessage(mes)
        
    def selectimage2(self):
        image_path2 = QFileDialog.getOpenFileName(self.pushButton_5,"select a BMP image","C:\Users\Administrator\Desktop","BMP files(*.bmp)")
        self.lineEdit_4.setText(image_path2)
        x = self.label_3.width()
        y = self.label_3.height()
        image = QImage(image_path2)
        x = double(x)
        y = double(y)
        if image.width() >= image.height():
            tmp = image.width() / x
        else:
            tmp = image.height() / y
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setPixmap(QPixmap.fromImage(image).scaled(image.size()/tmp))
    def selectimage3(self):
        image_path3 = QFileDialog.getOpenFileName(self.pushButton_8,"select a BMP image","C:\Users\Administrator\Desktop","BMP files(*.bmp)")
        self.lineEdit_7.setText(image_path3)
        x = self.label_5.width()
        y = self.label_5.height()
        image = QImage(image_path3)
        x = double(x)
        y = double(y)
        if image.width() >= image.height():
            tmp = image.width() / x
        else:
            tmp = image.height() / y
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setPixmap(QPixmap.fromImage(image).scaled(image.size()/tmp))
        
#///////////////////////////////////////////        
    def onAbout(self):
        QMessageBox.about(self.menubar,"About","This is an about LSB&RS sofeware")
        
    def saveimage(self):
        save_image = QFileDialog.getSaveFileName(self.pushButton_3,'save the BMP image' , '' , '(*.bmp)')
        self.lineEdit_3.setText(save_image)
        
    def savefile(self):
        save_file = QFileDialog.getSaveFileName(self.pushButton_6,'save the file' , '' , 'All files(*.*)')
        self.lineEdit_6.setText(save_file)
#//////////////////////////////////////////////        
    def run1(self):             #隐写
        str1 = self.lineEdit.text()
        str2 = self.lineEdit_2.text()
        str3 = self.lineEdit_3.text()
        str1 = str(str1)
        str2 = str(str2)
        str3 = str(str3)
        flag = lsbencode.func(str1,str2,str3)
        if flag == 0:
            #print "too big"
            QMessageBox.about(self.pushButton_4,"LSB","this file is too big")
        else:
            x = self.label_2.width()
            y = self.label_2.height()
            image = QImage(str3)
            x = double(x)
            y = double(y)
            if image.width() >= image.height():
                tmp = image.width() / x
            else:
                tmp = image.height() / y
            self.label_2.setAlignment(Qt.AlignCenter)
            self.label_2.setPixmap(QPixmap.fromImage(image).scaled(image.size()/tmp))
            QMessageBox.about(self.pushButton_4,"succeed!","the key is %d"%(flag/8))
        
    def run2(self):              #提取
        str1 = self.lineEdit_4.text()
        str2 = self.lineEdit_6.text()
        lenth = self.lineEdit_5.text()
        str1 = str(str1)
        str2 = str(str2)
        lenth = int(lenth)
        lsbdecode.func(lenth, str1, str2)
        QMessageBox.about(self.pushButton_7,"LSB","Running successful!")
        
    def analyse(self):          #分析
        str1 = self.lineEdit_7.text()
        str1 = str(str1)
        res = rsmain.rsmain(str1)*100
        if res < 1:
            self.progressBar.setValue(0)
        else:
			if res >= 100:
				self.progressBar.setValue(100)
			else:
				self.progressBar.setValue(res)