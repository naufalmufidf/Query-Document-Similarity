# GUI libs
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# system libs
import shutil
import os
import sys

# main libs (calculation etc.)
import numpy as np
from matplotlib import pyplot as plt, widgets
import math
import pandas as pd
import collections
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# GUI files
from ui_loading_screen import Ui_Loading
from ui_main import Ui_MainWindow
from ui_home import Ui_Home
from ui_GUI import Ui_ComingSoon
from ui_loading_screen2 import Ui_Loading2

# extension file
import prep

# counter untuk animasi
counter = 0

# corpus folder path
corpusDir = 'D:/!kuliah/Semester 5/Data Mining/Tugas Akhir/Final Project - Kelompok 7/corpus/'


# first window shown (Menu)
class Home(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        self.ui.btn_pre.clicked.connect(self.pre)
        self.ui.btn_detect.clicked.connect(self.detect)
        self.ui.btn_close.clicked.connect(self.quit)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.shadow.setGraphicsEffect(self.shadow)

        self.show()

    @QtCore.Slot()
    def quit(self):
        for file in os.listdir(corpusDir):
            os.unlink(corpusDir + file)
        app.quit()

    def detect(self):
        det = Loading2()
        widget.addWidget(det)
        widget.setCurrentIndex(widget.currentIndex()+1)
        for file in os.listdir(corpusDir):
            os.unlink(corpusDir + file)

    def pre(self):
        det = Loading()
        widget.addWidget(det)
        widget.setCurrentIndex(widget.currentIndex()+1)
        for file in os.listdir(corpusDir):
            os.unlink(corpusDir + file)

# first option menu (no content included)


class ComingSoon(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ComingSoon()
        self.ui.setupUi(self)

        self.Image = None

        self.ui.btn_close.clicked.connect(self.quit)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.label_back.mousePressEvent = self.balik
        self.ui.label_back.mousePressEvent = MainWindow.close

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.show()

    @QtCore.Slot()
    def quit(self):
        app.quit()

    def balik(self, event):
        det = Home()
        widget.addWidget(det)
        widget.setCurrentIndex(widget.currentIndex()+1)


# model untuk menampilkan pandas dataframe pada QViewTable
class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

# second option menu (main app, similarity measurement)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_preprocess.clicked.connect(self.preprocess)
        self.ui.btn_calculate.clicked.connect(self.Tfidf)
        self.ui.btn_close.clicked.connect(self.quit)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.btn_add.clicked.connect(self.openfile)

        self.ui.label_back.mousePressEvent = self.balik
        self.ui.label_back.mousePressEvent = MainWindow.close

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.shadow.setGraphicsEffect(self.shadow)

        self.corpus = []
        self.corpus2 = {}

    # function kembali ke window home
    def balik(self, event):
        det = Home()
        widget.addWidget(det)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # function close window
    def eventFilter(self, obj, event):
        if obj is self.w and event.type() == QtCore.QEvent.Close:
            self.quit_app()
            event.ignore()
            return True
        return super(Manager, self).eventFilter(obj, event)

    # function close window
    @QtCore.Slot()
    def quit(self):
        for file in os.listdir(corpusDir):
            os.unlink(corpusDir + file)
        print('CLEAN EXIT')
        self.removeEventFilter(self)
        app.quit()

    # function membuka file (copy selected files ke corpus)
    def openfile(self):

        docPath, _ = QFileDialog.getOpenFileNames()
        for i in docPath:
            shutil.copy2(
                i, corpusDir)

        # Memasukan direktori folder
        os.chdir(corpusDir)
        data = os.listdir()
        print(data)

        # Menampilakn semua file yang ada didalam folder yang di pilih dalam bentuk table
        row = 0
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.itemClicked.connect(self.handleItemClicked)
        for file in os.listdir():
            self.item = QtWidgets.QTableWidgetItem('%s' % data[row])
            self.item.setFlags(QtCore.Qt.ItemIsUserCheckable |
                               QtCore.Qt.ItemIsEnabled)
            self.item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tableWidget.setItem(row, 0, self.item)
            row = row+1

        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

    # function check box behavio+r
    def handleItemClicked(self, item):
        cnt = 0
        cek = []
        if item.checkState() == QtCore.Qt.Checked:
            cnt += 1
            print('"%s" Checked' % item.text())
            cek.append(item.text())
            self.corpus.append(item.text())
            print(self.corpus)
            print(cek)
        else:
            print('"%s" Clicked' % item.text())
            self.corpus.remove(item.text())
            print(self.corpus)

    # function untuk preprocessing
    def preprocess(self):

        # membuat list untuk menyimpan dokumen yg akan diproses
        corpusPro = []

        # melakukan loop preprocessing untuk tiap dokumen
        for file in self.corpus:
            # apabila file berupa pdf
            if file.endswith('.pdf'):

                # ekstraksi
                view = prep.pdfview(file)
                ori = prep.pdf(file)
                ori2 = ' '.join(ori)
                df = pd.DataFrame()

                # lowercasing
                df['Original'] = ori
                df['Lower cased'] = prep.lowercase(df['Original'])
                lc = df['Lower cased'].values.tolist()
                lc = str(lc)
                print(lc)

                # punctuation removal
                df['Clean_text'] = df['Lower cased']
                df['Clean_text'] = df['Clean_text'].str.replace(
                    '[^a-zA-Z]', ' ')
                df['Clean_text'] = np.vectorize(prep.preprocess_remove)(
                    'http[\w]*', df['Clean_text'])
                df['Clean_text'] = np.vectorize(
                    prep.preprocess_remove)('@[\w]*', df['Clean_text'])
                df['Clean_text'] = df['Clean_text'].apply(
                    lambda x: ' '.join([w for w in x.split() if len(w) > 3]))
                bersih = df['Clean_text'].values.tolist()
                bersih = str(bersih)
                bersih = bersih.replace("[", '')
                bersih = bersih.replace("'", '')
                bersih = bersih.replace("]", '')
                print(bersih)
                df['Clean_text'] = bersih

                # stemming
                df['Stemmed'] = df['Clean_text'].apply(prep.stem_sentences)
                stemmed = df['Stemmed'].values.tolist()
                stemmed = str(stemmed)
                corpusPro.append(stemmed)
                print(stemmed)

                # tokenizing
                df['Final'] = prep.sw(df['Stemmed'])
                tokenize = df['Final'].values.tolist()
                tokenize = str(tokenize)
                tokenize = tokenize.split()
                print(tokenize)

                counter = collections.Counter(tokenize).most_common()

            # apabila file berupa word
            elif file.endswith('.docx'):
                # ekstraksi
                view = prep.wordview(file)
                ori = prep.word(file)
                ori2 = ' '.join(ori)
                df = pd.DataFrame()

                # lowercasing
                df['Original'] = ori
                df['Lower cased'] = prep.lowercase(df['Original'])
                lc = df['Lower cased'].values.tolist()
                lc = str(lc)

                # punctuation removal
                df['Clean_text'] = df['Lower cased']
                df['Clean_text'] = df['Clean_text'].str.replace(
                    '[^a-zA-Z]', ' ')
                df['Clean_text'] = np.vectorize(prep.preprocess_remove)(
                    'http[\w]*', df['Clean_text'])
                df['Clean_text'] = np.vectorize(
                    prep.preprocess_remove)('@[\w]*', df['Clean_text'])
                df['Clean_text'] = df['Clean_text'].apply(
                    lambda x: ' '.join([w for w in x.split() if len(w) > 3]))
                bersih = df['Clean_text'].values.tolist()
                bersih = str(bersih)
                bersih = bersih.replace("[", '')
                bersih = bersih.replace("'", '')
                bersih = bersih.replace("]", '')
                df['Clean_text'] = bersih

                # stemming
                df['Stemmed'] = df['Clean_text'].apply(prep.stem_sentences)
                stemmed = df['Stemmed'].values.tolist()
                stemmed = str(stemmed)

                # memasukkan hasil stemming dari tiap dokumen ke list corpus
                corpusPro.append(stemmed)

                df['Final'] = prep.sw(df['Stemmed'])
                tokenize = df['Final'].values.tolist()
                tokenize = str(tokenize)
                tokenize = tokenize.split()

                # menghitung frekuensi kemunculan tiap kata
                counter = collections.Counter(tokenize).most_common()

            # memasukkan tiap hasil preprocessing ke model tab untuk ditampilkan
            self.ui.isiPreprocessing.addTab(tabPreprocessing(
                str(ori2), lc, bersih, stemmed, tokenize, counter), file)

        # membuat objek dari  kelas tfidf
        tfidf = TfidfVectorizer()
        # melakukan pembobotan menggunakan tfidf terhadap apa" yg ada di list corpus
        weighted = tfidf.fit_transform(corpusPro)
        # melakukan kalkulasi kemiripan menggunakan cosine similarity
        sim = cosine_similarity(weighted)

        # membuat dataframe dari hasil perhitungan
        df_cs = pd.DataFrame(sim, index=self.corpus, columns=self.corpus)
        print(df_cs)

        # memasukkan hasil perhitungan ke QTableView
        model = TableModel(df_cs)
        self.ui.tableView.setModel(model)

        header = self.ui.tableView.horizontalHeader()

        for i in range(len(self.corpus)):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
        self.ui.tableView.verticalHeader().setMaximumWidth(160)

    # function tfif antara query dengan dokumen
    def Tfidf(self):

        # membuat list corpus untuk menyimpan dokumen yang akan diproses
        corpusPro = []

        # melakukan loop proses sejumlah dokumen masukan
        for file in self.corpus:
            x = prep.prep2(file)
            # memasukkan dokumen ke list corpus
            corpusPro.append(x)
            print(corpusPro)

        # membuat objek dari  kelas tfidf
        tfidf = TfidfVectorizer()
        # melakukan pembobotan menggunakan tfidf terhadap apa" yg ada di list corpus
        weighted = tfidf.fit_transform(corpusPro)
        sim = cosine_similarity(weighted)

        # mengambil masukan dari textedit pada GUI
        q = self.ui.plainTextEdit.toPlainText()
        # melakukan stemming pada query
        q = prep.stem_sentences(q)
        # melakukan konversi query menjadi vektor
        q = tfidf.transform([q])
        # melakukan kalkulasi kemiripan antara query dengan dokumen
        simq = cosine_similarity(q, weighted)

        # memasukkan hasil perhitungan ke table
        self.ui.tableWidget_3.setRowCount(len(corpusPro))
        self.ui.tableWidget_3.setStyleSheet(
            "font-family: Gramatika Medium; color: #E7B18E; font-size: 15px;QTableWidget{color: rgb(231, 177, 142); border: 1px solid rgb(231, 177, 142); gridline-color: rgb(231, 177, 142);} QTableWidget:: item{color: rgb(231, 177, 142);}")
        # self.ui.tableWidget_3.setVerticalScrollBar
        for i, j in enumerate(simq[0]):
            print(f"Dokumen {i+1}: {j}")
            self.ui.tableWidget_3.setItem(
                i, 0, QtWidgets.QTableWidgetItem(self.corpus[i]))
            self.ui.tableWidget_3.setItem(
                i, 1, QtWidgets.QTableWidgetItem(f"{j}"))

        header = self.ui.tableWidget_3.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)


# class model preprocessing
class tabPreprocessing(QWidget):
    def __init__(self, asli, lowercased, cleared, stemmed, tokenized, index):
        self.asli = asli
        self.lowercased = lowercased
        self.cleared = cleared
        self.stemmed = stemmed
        self.tokenized = tokenized
        self.index = index
        super().__init__()
        self.UI()

    def UI(self):
        Vbox = QVBoxLayout()
        Outer = QVBoxLayout()

        TabScroll = QScrollArea()
        TabScroll.setWidgetResizable(True)
        TabScroll.setMinimumHeight(800)
        OuterWidget = QWidget()
        Vbox.setSpacing(0)

        bacaDoc = QVBoxLayout()
        lowercasedDoc = QVBoxLayout()
        clearedDoc = QVBoxLayout()
        stemmedDoc = QVBoxLayout()
        tokenizedDoc = QVBoxLayout()
        indexedDoc = QVBoxLayout()

        bacaDoclabel = QLabel("View Document")
        bacaDoclabel.setStyleSheet(
            "font-size: 25px; font-family: Gramatika Medium; color: #E7B18E;")
        bacaDocScroll = QScrollArea()
        bacaDocScroll.setWidgetResizable(True)
        bacaDocScroll.setMinimumHeight(200)
        bacaDocWidget = QWidget()
        bacaDocWidget.setStyleSheet(
            "color: #E7B18E; border: 1px solid rgb(231, 177, 142); font-size: 15px;")
        bacaDocVbox = QVBoxLayout()
        bacaDocnew = QLabel(self.asli)
        bacaDocnew.setWordWrap(True)
        bacaDocVbox.addWidget(bacaDocnew)
        bacaDocWidget.setLayout(bacaDocVbox)
        bacaDocScroll.setWidget(bacaDocWidget)
        jumlahinput = QLabel("")

        lowercasedDoclabel = QLabel("Lower Case")
        lowercasedDoclabel.setStyleSheet(
            "font-size: 25px; font-family: Gramatika Medium; color: #E7B18E;")
        lowercasedDocScroll = QScrollArea()
        lowercasedDocScroll.setWidgetResizable(True)
        lowercasedDocScroll.setMinimumHeight(200)
        lowercasedDocWidget = QWidget()
        lowercasedDocWidget.setStyleSheet(
            "color: #E7B18E; border: 1px solid rgb(231, 177, 142); font-size: 15px;")
        lowercasedDocVbox = QVBoxLayout()
        lowercasedDocnew = QLabel(self.lowercased)
        lowercasedDocnew.setWordWrap(True)
        lowercasedDocVbox.addWidget(lowercasedDocnew)
        lowercasedDocWidget.setLayout(lowercasedDocVbox)
        lowercasedDocScroll.setWidget(lowercasedDocWidget)
        jumlahlowercasedDoc = QLabel("")

        clearedDoclabel = QLabel("Cleared Text")
        clearedDoclabel.setStyleSheet(
            "font-size: 25px; font-family: Gramatika Medium; color: #E7B18E;")
        clearedDocScroll = QScrollArea()
        clearedDocScroll.setWidgetResizable(True)
        clearedDocScroll.setMinimumHeight(200)
        clearedDocWidget = QWidget()
        clearedDocWidget.setStyleSheet(
            "color: #E7B18E; border: 1px solid rgb(231, 177, 142); font-size: 15px;")
        clearedDocVbox = QVBoxLayout()
        clearedDocnew = QLabel(self.cleared)
        clearedDocnew.setWordWrap(True)
        clearedDocVbox.addWidget(clearedDocnew)
        clearedDocWidget.setLayout(clearedDocVbox)
        clearedDocScroll.setWidget(clearedDocWidget)
        jumlahclearedDoc = QLabel("")

        stemmedDoclabel = QLabel("Stemmed")
        stemmedDoclabel.setStyleSheet(
            "font-size: 25px; font-family: Gramatika Medium; color: #E7B18E;")
        stemmedDocScroll = QScrollArea()
        stemmedDocScroll.setWidgetResizable(True)
        stemmedDocScroll.setMinimumHeight(200)
        stemmedDocWidget = QWidget()
        stemmedDocWidget.setStyleSheet(
            "color: #E7B18E; border: 1px solid rgb(231, 177, 142); font-size: 15px;")
        # stemmedDocWidget.setStyleSheet(" border: 1px solid rgb(231, 177, 142);")
        stemmedDocVbox = QVBoxLayout()
        stemmedDocnew = QLabel(self.stemmed)
        stemmedDocnew.setWordWrap(True)
        stemmedDocVbox.addWidget(stemmedDocnew)
        stemmedDocWidget.setLayout(stemmedDocVbox)
        stemmedDocScroll.setWidget(stemmedDocWidget)
        jumlahstemmedDoc = QLabel("")

        tokenizedDoclabel = QLabel("Tokenized")
        tokenizedDoclabel.setStyleSheet(
            "font-size: 25px; font-family: Gramatika Medium; color: #E7B18E;")
        tokenizedDocScroll = QScrollArea()
        tokenizedDocScroll.setWidgetResizable(True)
        tokenizedDocScroll.setMinimumHeight(210)
        tokenizedDocWidget = QWidget()
        tokenizedDocWidget.setStyleSheet("color: #E7B18E;")
        tokenizedDocVbox = QVBoxLayout()
        tokenizedDocTable = QTableWidget()
        tokenizedDocTable.setStyleSheet(
            "font-size: 15px;QTableWidget{color: rgb(231, 177, 142); border: 1px solid rgb(231, 177, 142); gridline-color: rgb(231, 177, 142);} QTableWidget:: item{color: rgb(231, 177, 142);}")
        tokenizedDocTable.setMinimumHeight(180)
        tokenizedDocTable.setRowCount(len(self.tokenized))
        tokenizedDocTable.setColumnCount(1)
        for row in range(len(self.tokenized)):
            tokenizedDocTable.setItem(
                row, 0, QTableWidgetItem(self.tokenized[row]))
        tokenizedDocTable.horizontalHeader().setStretchLastSection(True)
        tokenizedDocTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tokenizedDocVbox.addWidget(tokenizedDocTable)
        tokenizedDocWidget.setLayout(tokenizedDocVbox)
        tokenizedDocScroll.setWidget(tokenizedDocWidget)
        jumlahtokenizedDoc = QLabel("Jumlah Kata: %d" % len(self.tokenized))

        indexedDoclabel = QLabel("Indexed")
        indexedDoclabel.setStyleSheet(
            "font-size: 25px; font-family: Gramatika Medium; color: #E7B18E;")
        indexedDocScroll = QScrollArea()
        indexedDocScroll.setWidgetResizable(True)
        indexedDocScroll.setMinimumHeight(210)
        indexedDocWidget = QWidget()
        indexedDocWidget.setStyleSheet("color: #E7B18E;")
        indexedDocVbox = QVBoxLayout()
        indexedDocTable = QTableWidget()
        indexedDocTable.setStyleSheet(
            "font-size: 15px;QTableWidget{color: rgb(231, 177, 142); border: 1px solid rgb(231, 177, 142); gridline-color: rgb(231, 177, 142);} QTableWidget:: item{color: rgb(231, 177, 142);}")
        indexedDocTable.setMinimumHeight(180)
        indexedDocTable.setRowCount(len(self.index))
        indexedDocTable.setColumnCount(2)
        rowIndex = 0
        for i in self.index:
            indexedDocTable.setItem(
                rowIndex, 0, QtWidgets.QTableWidgetItem(i[0]))
            indexedDocTable.setItem(
                rowIndex, 1, QtWidgets.QTableWidgetItem("%d" % i[1]))
            rowIndex += 1
        indexedDocTable.horizontalHeader().setStretchLastSection(True)
        indexedDocTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        indexedDocVbox.addWidget(indexedDocTable)
        indexedDocWidget.setLayout(indexedDocVbox)
        indexedDocScroll.setWidget(indexedDocWidget)
        jumlahindexedDoc = QLabel("Jumlah Kata: %d" % len(self.index))

        bacaDoc.addWidget(bacaDoclabel)
        bacaDoc.addWidget(bacaDocScroll)
        bacaDoc.addWidget(jumlahinput)

        lowercasedDoc.addWidget(lowercasedDoclabel)
        lowercasedDoc.addWidget(lowercasedDocScroll)
        lowercasedDoc.addWidget(jumlahlowercasedDoc)

        clearedDoc.addWidget(clearedDoclabel)
        clearedDoc.addWidget(clearedDocScroll)
        clearedDoc.addWidget(jumlahclearedDoc)

        stemmedDoc.addWidget(stemmedDoclabel)
        stemmedDoc.addWidget(stemmedDocScroll)
        stemmedDoc.addWidget(jumlahstemmedDoc)

        tokenizedDoc.addWidget(tokenizedDoclabel)
        tokenizedDoc.addWidget(tokenizedDocScroll)
        tokenizedDoc.addWidget(jumlahtokenizedDoc)

        indexedDoc.addWidget(indexedDoclabel)
        indexedDoc.addWidget(indexedDocScroll)
        indexedDoc.addWidget(jumlahindexedDoc)

        Vbox.addLayout(bacaDoc)
        Vbox.addLayout(lowercasedDoc)
        Vbox.addLayout(clearedDoc)
        Vbox.addLayout(stemmedDoc)
        Vbox.addLayout(tokenizedDoc)
        Vbox.addLayout(indexedDoc)

        OuterWidget.setLayout(Vbox)
        TabScroll.setWidget(OuterWidget)

        Outer.addWidget(TabScroll)
        Outer.addStretch()

        self.setLayout(Outer)

# window loading


class Loading(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Loading()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.shadow.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        self.ui.label_desc.setText(
            "Nothing to see here")
        QtCore.QTimer.singleShot(
            2000, lambda: self.ui.label_desc.setText("Space for next project"))
        QtCore.QTimer.singleShot(
            3500, lambda: self.ui.label_desc.setText("Space for next project"))

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    # ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = ComingSoon()
            self.main.show()
            # self.main.show() del later

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

# window loading


class Loading2(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Loading2()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.shadow.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        self.ui.label_desc.setText(
            "Menghitung kemiripan beberapa dokumen dengan query")
        QtCore.QTimer.singleShot(
            1500, lambda: self.ui.label_desc.setText("Preparing..."))
        QtCore.QTimer.singleShot(
            2500, lambda: self.ui.label_desc.setText("Untuk arahan penggunaan baca guide terlebih dahulu."))

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    # ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()
            # self.main.show() del later

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Home()
    sys.exit(app.exec_())
window.show()
