# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homedGtpWW.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Home(object):
    def setupUi(self, Home):
        if Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(679, 400)
        self.centralwidget = QWidget(Home)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.shadow = QFrame(self.centralwidget)
        self.shadow.setObjectName(u"shadow")
        self.shadow.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(45, 48, 55);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.shadow.setFrameShape(QFrame.StyledPanel)
        self.shadow.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.shadow)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 10, 661, 181))
        font = QFont()
        font.setFamily(u"Casta")
        font.setPointSize(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: #E7B18E;")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.btn_pre = QPushButton(self.shadow)
        self.btn_pre.setObjectName(u"btn_pre")
        self.btn_pre.setGeometry(QRect(80, 220, 181, 51))
        font1 = QFont()
        font1.setFamily(u"Gramatika-Medium")
        font1.setPointSize(10)
        self.btn_pre.setFont(font1)
        self.btn_pre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pre.setStyleSheet(u"background-color: #E7B18E;\n"
"border: 1px solid #E7B18E; \n"
"border-radius: 20px;")
        self.btn_detect = QPushButton(self.shadow)
        self.btn_detect.setObjectName(u"btn_detect")
        self.btn_detect.setGeometry(QRect(400, 220, 181, 51))
        self.btn_detect.setFont(font1)
        self.btn_detect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_detect.setStyleSheet(u"background-color: #E7B18E;\n"
"border: 1px solid #E7B18E; \n"
"border-radius: 20px;")
        self.btn_minimize = QPushButton(self.shadow)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(590, 10, 18, 18))
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet(u"background: #FFBD44;\n"
"border-radius: 9%;")
        self.btn_gtw = QPushButton(self.shadow)
        self.btn_gtw.setObjectName(u"btn_gtw")
        self.btn_gtw.setGeometry(QRect(620, 10, 18, 18))
        self.btn_gtw.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gtw.setStyleSheet(u"background: #00CA4E;\n"
"border-radius: 9%;")
        self.btn_close = QPushButton(self.shadow)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(560, 10, 18, 18))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet(u"background: #FF605C;\n"
"border-radius: 9%;")
        self.label_credits = QLabel(self.shadow)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(10, 340, 191, 31))
        self.label_credits.setFont(font1)
        self.label_credits.setStyleSheet(u"color: rgb(110, 117, 134);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.shadow)

        Home.setCentralWidget(self.centralwidget)

        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("Home", u"<html><head/><body><p>Home</p></body></html>", None))
        self.btn_pre.setText(QCoreApplication.translate("Home", u"Coming Soon", None))
        self.btn_detect.setText(QCoreApplication.translate("Home", u"Query-Document Similarity", None))
        self.btn_minimize.setText("")
        self.btn_gtw.setText("")
        self.btn_close.setText("")
        self.label_credits.setText(QCoreApplication.translate("Home", u"Final project by : Naufal Mufid F", None))
    # retranslateUi

