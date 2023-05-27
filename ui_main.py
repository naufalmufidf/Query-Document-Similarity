# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainvVrPXf.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1919, 1045)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.shadow = QFrame(self.centralwidget)
        self.shadow.setObjectName(u"shadow")
        self.shadow.setEnabled(True)
        self.shadow.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(45, 48, 55);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.shadow.setFrameShape(QFrame.StyledPanel)
        self.shadow.setFrameShadow(QFrame.Raised)
        self.widget_2 = QWidget(self.shadow)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 1901, 141))
        self.widget_2.setStyleSheet(u"border-top-left-radius : 10px;\n"
"border-top-right-radius : 10px;\n"
"background-color: #E7B18E;")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(470, 30, 971, 101))
        font = QFont()
        font.setFamily(u"Casta Thin")
        font.setPointSize(68)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"color: E7B18E;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.btn_close = QPushButton(self.widget_2)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(1800, 20, 18, 18))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet(u"background: #FF605C;\n"
"border-radius: 9%;")
        self.btn_minimize = QPushButton(self.widget_2)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(1830, 20, 18, 18))
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet(u"background: #FFBD44;\n"
"border-radius: 9%;")
        self.btn_gtw = QPushButton(self.widget_2)
        self.btn_gtw.setObjectName(u"btn_gtw")
        self.btn_gtw.setGeometry(QRect(1860, 20, 18, 18))
        self.btn_gtw.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gtw.setStyleSheet(u"background: #00CA4E;\n"
"border-radius: 9%;")
        self.label_back = QLabel(self.widget_2)
        self.label_back.setObjectName(u"label_back")
        self.label_back.setGeometry(QRect(10, 30, 151, 71))
        self.label_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_back.setPixmap(QPixmap(u"Ihome.png"))
        self.label_4 = QLabel(self.shadow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 150, 141, 61))
        font1 = QFont()
        font1.setFamily(u"Gramatika-Medium")
        font1.setPointSize(24)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: #E7B18E;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.btn_preprocess = QPushButton(self.shadow)
        self.btn_preprocess.setObjectName(u"btn_preprocess")
        self.btn_preprocess.setGeometry(QRect(30, 610, 651, 51))
        font2 = QFont()
        font2.setFamily(u"Gramatika-Medium")
        font2.setPointSize(10)
        self.btn_preprocess.setFont(font2)
        self.btn_preprocess.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_preprocess.setStyleSheet(u"background-color: #E7B18E;\n"
"border: 1px solid #E7B18E; \n"
"border-radius: 20px;")
        self.btn_add = QPushButton(self.shadow)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(690, 220, 41, 41))
        self.btn_add.setFont(font2)
        self.btn_add.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add.setStyleSheet(u"background-color: #E7B18E;\n"
"border: 1px solid #E7B18E; \n"
"border-radius: 20px;")
        icon = QIcon()
        icon.addFile(u"C:/Users/lenovo/Pictures/addLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add.setIcon(icon)
        self.btn_add.setIconSize(QSize(20, 20))
        self.label_credits = QLabel(self.shadow)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(-570, 990, 771, 31))
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(110, 117, 134);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_14 = QLabel(self.shadow)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(1590, 580, 151, 16))
        font3 = QFont()
        font3.setFamily(u"Gramatika-Medium")
        font3.setPointSize(12)
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"background-color:rgb(45, 48, 55);\n"
"color: #E7B18E;")
        self.tableWidget = QTableWidget(self.shadow)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(231, 177, 142));
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 220, 651, 381))
        self.tableWidget.setStyleSheet(u"QTableWidget\n"
"{\n"
"    color: rgb(231, 177, 142);;\n"
"    border: 1px solid rgb(231, 177, 142);;\n"
"    \n"
"    gridline-color: rgb(231, 177, 142);;\n"
"}\n"
"QTableWidget::item\n"
"{\n"
"  color: rgb(231, 177, 142);\n"
"}")
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tabWidget = QTabWidget(self.shadow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(800, 260, 1071, 771))
        font4 = QFont()
        font4.setPointSize(12)
        self.tabWidget.setFont(font4)
        self.tabWidget.setStyleSheet(u"\n"
"\n"
"QTabWidget::tab-bar {\n"
"   border: 1px rgb(231, 177, 142);\n"
"   border-radius : 0px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  background: rgb(174, 138, 116);\n"
"  color: rgb(45, 48, 55);\n"
"  padding: 10px;\n"
"   border-radius : 0px;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background: rgb(231, 177, 142);\n"
"   border-radius : 0px;\n"
"  \n"
" }\n"
"\n"
"QTabWidget::pane { \n"
"   border: 1px rgb(231, 177, 142);\n"
"   background-color: rgb(45, 48, 55);\n"
"   border-radius : 0px;\n"
"}")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 1051, 571))
        self.label.setStyleSheet(u"color: #E7B18E;")
        self.label.setWordWrap(True)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.isiPreprocessing = QTabWidget(self.tab)
        self.isiPreprocessing.setObjectName(u"isiPreprocessing")
        self.isiPreprocessing.setGeometry(QRect(10, 10, 1051, 711))
        self.isiPreprocessing.setStyleSheet(u"border-radius: 0px;")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-10, 360, 351, 61))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: #E7B18E;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.tableWidget_3 = QTableWidget(self.tab_2)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(231, 177, 142));
        __qtablewidgetitem1.setForeground(brush);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(0, 90, 731, 191))
        self.tableWidget_3.setStyleSheet(u"QTableWidget\n"
"{\n"
"    color: rgb(231, 177, 142);;\n"
"    border: 1px solid rgb(231, 177, 142);\n"
"    \n"
"    gridline-color: rgb(231, 177, 142);;\n"
"}\n"
"QTableWidget::item\n"
"{\n"
"  color: rgb(231, 177, 142);\n"
"}")
        self.tableWidget_3.setFrameShape(QFrame.StyledPanel)
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(-130, 30, 351, 61))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: #E7B18E;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.tableView = QTableView(self.tab_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 420, 1071, 301))
        self.tableView.setStyleSheet(u"QTableView\n"
"{\n"
"    color: black;\n"
"    border: 1px solid rgb(231, 177, 142);\n"
"    \n"
"    gridline-color: rgb(231, 177, 142);;\n"
"}\n"
"QTableView::item\n"
"{\n"
"  color: rgb(231, 177, 142);\n"
"}\n"
"\n"
"QTableView::section {\n"
"    background-color: black;\n"
"    border: none;\n"
"}")
        self.tableView.setAlternatingRowColors(False)
        self.tabWidget.addTab(self.tab_2, "")
        self.label_7.raise_()
        self.label_6.raise_()
        self.tableWidget_3.raise_()
        self.tableView.raise_()
        self.plainTextEdit = QPlainTextEdit(self.shadow)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(800, 220, 531, 31))
        self.plainTextEdit.setFont(font2)
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(231, 177, 142);\n"
"color: rgb(45, 48, 55);\n"
"")
        self.label_5 = QLabel(self.shadow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(780, 150, 141, 61))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: #E7B18E;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.btn_calculate = QPushButton(self.shadow)
        self.btn_calculate.setObjectName(u"btn_calculate")
        self.btn_calculate.setGeometry(QRect(1350, 220, 171, 31))
        self.btn_calculate.setFont(font2)
        self.btn_calculate.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_calculate.setStyleSheet(u"background-color: #E7B18E;\n"
"border: 1px solid #E7B18E; \n"
"border-radius: 10px;")
        self.textBrowser = QTextBrowser(self.shadow)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 990, 441, 31))
        self.widget_2.raise_()
        self.label_4.raise_()
        self.btn_preprocess.raise_()
        self.btn_add.raise_()
        self.label_14.raise_()
        self.tableWidget.raise_()
        self.label_5.raise_()
        self.plainTextEdit.raise_()
        self.btn_calculate.raise_()
        self.textBrowser.raise_()
        self.tabWidget.raise_()
        self.label_credits.raise_()

        self.gridLayout.addWidget(self.shadow, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.isiPreprocessing.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Query-Document Similarity", None))
        self.btn_close.setText("")
        self.btn_minimize.setText("")
        self.btn_gtw.setText("")
        self.label_back.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Corpus", None))
        self.btn_preprocess.setText(QCoreApplication.translate("MainWindow", u"Preprocess", None))
        self.btn_add.setText("")
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Final project by : Naufal Mufid F", None))
        self.label_14.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"File(s)", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Selamat datang di aplikasi Query-Document Similairty!</span><span style=\" font-size:6pt;\">.</span></p><p><br/></p><p><span style=\" font-size:14pt;\">Tujuan dari aplikasi ini adalah untuk menghitung kemiripan antar query dengan (beberapa) dokumen lengkap dengan step preprocessing dan juga kemiripan antar dokumen pada corpus.</span><span style=\" font-size:6pt;\">.</span></p><p><br/></p><p><span style=\" font-size:14pt;\">Untuk langkah penggunaan aplikasi dapat dilihat di bawah.</span></p><p><span style=\" font-size:14pt;\">1. Klik button plus (+) untuk menambahkan dokumen ke dalam corpus.</span></p><p><span style=\" font-size:14pt;\">2. Pilih dokumen pada corpus yang akan dilakukan dikalkulasi kemiripannya dengan cara check dokumen tersebut</span></p><p><span style=\" font-size:14pt;\">3. Klik button </span><span style=\" font-size:14pt; font-weight:600;\">Preprocess</span><span style=\" font-size:14pt;\"> untuk melakukan tahapan preprocessing dan juga k"
                        "alkulasi antar dokumen pada corpus.</span></p><p><span style=\" font-size:14pt;\">- Untuk lihat tahapan preprocessing, klik tab </span><span style=\" font-size:14pt; font-weight:600;\">Preprocessing</span><span style=\" font-size:14pt;\">.</span></p><p><span style=\" font-size:14pt;\">- Untuk lihat hasil kalkulasi, klik tab </span><span style=\" font-size:14pt; font-weight:600;\">Measurement</span><span style=\" font-size:14pt;\">.</span></p><p><span style=\" font-size:14pt;\">4. Masukkan query di kolom yang telah disediakan.</span></p><p><span style=\" font-size:14pt;\">5. Klik button </span><span style=\" font-size:14pt; font-weight:600;\">Calculate</span><span style=\" font-size:14pt;\"> untuk melakukan proses kalkulasi kemiripan antara query dengan dokumen.</span></p><p><span style=\" font-size:14pt;\">- Untuk lihat hasil kalkulasi, klik tab </span><span style=\" font-size:14pt; font-weight:600;\">Measurement</span><span style=\" font-size:14pt;\">.</span></p><p><br/></p><p><span style=\" font-size:14pt;\""
                        ">Berikan saran agar aplikasi ini dapat lebih baik lagi ke depannya. Terima kasih!</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Guide", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Preprocessing", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Documents Similarity", None))
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Document", None));
        ___qtablewidgetitem2 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Similarity", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Query", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Measurement", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Query", None))
        self.btn_calculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
    # retranslateUi

