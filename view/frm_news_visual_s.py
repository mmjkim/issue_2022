from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import pandas as pd

import common.config.apiinfo as apifp
from common.config.filepassclass import FilePathClass


class Ui_news_collect_win(object):
    def setupUi(self, news_collect_win):
        news_collect_win.setObjectName("news_collect_win")
        news_collect_win.resize(1024, 768)
        news_collect_win.setMaximumSize(QtCore.QSize(1024, 768))
        self.centralwidget = QtWidgets.QWidget(news_collect_win)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1004, 95))
        self.groupBox.setObjectName("groupBox")
        self.rad_type_1 = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_1.setGeometry(QtCore.QRect(40, 41, 86, 20))
        self.rad_type_1.setObjectName("rad_type_1")
        self.rad_type_2 = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_2.setGeometry(QtCore.QRect(141, 41, 86, 21))
        self.rad_type_2.setObjectName("rad_type_2")
        self.rad_type_3 = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_3.setGeometry(QtCore.QRect(243, 41, 86, 21))
        self.rad_type_3.setObjectName("rad_type_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(621, 46, 20, 17))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(376, 44, 78, 16))
        self.label.setObjectName("label")
        self.sel_yy_end = QtWidgets.QComboBox(self.groupBox)
        self.sel_yy_end.setGeometry(QtCore.QRect(639, 41, 71, 23))
        self.sel_yy_end.setObjectName("sel_yy_end")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_mm_start = QtWidgets.QComboBox(self.groupBox)
        self.sel_mm_start.setGeometry(QtCore.QRect(543, 41, 71, 23))
        self.sel_mm_start.setObjectName("sel_mm_start")
        self.sel_mm_start.addItem("")
        self.sel_mm_start.addItem("")
        self.sel_mm_start.addItem("")
        self.sel_mm_start.addItem("")
        self.sel_mm_start.addItem("")
        self.sel_mm_start.addItem("")
        self.sel_mm_start.addItem("")
        self.sel_mm_start.addItem("")
        self.sel_mm_start.addItem("")
        self.sel_mm_start.addItem("")
        self.sel_mm_start.addItem("")
        self.sel_mm_start.addItem("")
        self.btn_show = QtWidgets.QPushButton(self.groupBox)
        self.btn_show.setGeometry(QtCore.QRect(810, 39, 110, 28))
        self.btn_show.setObjectName("btn_show")
        self.sel_yy_start = QtWidgets.QComboBox(self.groupBox)
        self.sel_yy_start.setGeometry(QtCore.QRect(460, 41, 71, 22))
        self.sel_yy_start.setObjectName("sel_yy_start")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_mm_end = QtWidgets.QComboBox(self.groupBox)
        self.sel_mm_end.setGeometry(QtCore.QRect(721, 41, 71, 23))
        self.sel_mm_end.setObjectName("sel_mm_end")
        self.sel_mm_end.addItem("")
        self.sel_mm_end.addItem("")
        self.sel_mm_end.addItem("")
        self.sel_mm_end.addItem("")
        self.sel_mm_end.addItem("")
        self.sel_mm_end.addItem("")
        self.sel_mm_end.addItem("")
        self.sel_mm_end.addItem("")
        self.sel_mm_end.addItem("")
        self.sel_mm_end.addItem("")
        self.sel_mm_end.addItem("")
        self.sel_mm_end.addItem("")
        self.graphWidget = pg.PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(23, 120, 981, 621))
        self.graphWidget.setObjectName("graphWidget")
        news_collect_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(news_collect_win)
        QtCore.QMetaObject.connectSlotsByName(news_collect_win)

        self.btn_show.clicked.connect(self.get_graph)


    def get_graph(self):
        file_path = FilePathClass()

        if self.rad_type_1.isChecked():
            dataPath = apifp.NEWS_DATA_PATH_POLITICS
            part = '정치'
        elif self.rad_type_2.isChecked():
            dataPath = apifp.NEWS_DATA_PATH_ECONOMY
            part = '경제'
        elif self.rad_type_3.isChecked():
            dataPath = apifp.NEWS_DATA_PATH_SOCIETY
            part = '사회'

        news = pd.read_csv("{0}{1}\\1차마트_{2}.csv".format(file_path.get_raw_use_path(), dataPath, part))


        # # news = pd.read_csv("D:/issue_2022/data/02_분석데이터/뉴스_경제/1차마트_경제.csv")
        news_pivot = news.pivot(index='keyword', columns='stdym', values='freq')
        news_pivot = news_pivot.sort_values(news_pivot.columns[-1:][0], ascending=False)

        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setBackground('w')
        self.graphWidget.addLegend()

        self.graphWidget.plot(news_pivot.head(5).columns.values, news_pivot.head(5).values[0],
                              pen=pg.mkPen(width=2, color='r'), name=news_pivot.index.values[0])
        self.graphWidget.plot(news_pivot.head(5).columns.values, news_pivot.head(5).values[1],
                              pen=pg.mkPen(width=2, color='b'), name=news_pivot.index.values[1])

        self.graphWidget.show()


    def retranslateUi(self, news_collect_win):
        _translate = QtCore.QCoreApplication.translate
        news_collect_win.setWindowTitle(_translate("news_collect_win", "MainWindow"))
        self.groupBox.setTitle(_translate("news_collect_win", " [ 뉴스 ] "))
        self.rad_type_1.setText(_translate("news_collect_win", "정치"))
        self.rad_type_2.setText(_translate("news_collect_win", "사회"))
        self.rad_type_3.setText(_translate("news_collect_win", "경제"))
        self.label_2.setText(_translate("news_collect_win", "~"))
        self.label.setText(_translate("news_collect_win", "기간 선택:"))
        self.sel_yy_end.setItemText(0, _translate("news_collect_win", "2022"))
        self.sel_yy_end.setItemText(1, _translate("news_collect_win", "2021"))
        self.sel_yy_end.setItemText(2, _translate("news_collect_win", "2020"))
        self.sel_yy_end.setItemText(3, _translate("news_collect_win", "2019"))
        self.sel_yy_end.setItemText(4, _translate("news_collect_win", "2018"))
        self.sel_yy_end.setItemText(5, _translate("news_collect_win", "2017"))
        self.sel_mm_start.setItemText(0, _translate("news_collect_win", "01"))
        self.sel_mm_start.setItemText(1, _translate("news_collect_win", "02"))
        self.sel_mm_start.setItemText(2, _translate("news_collect_win", "03"))
        self.sel_mm_start.setItemText(3, _translate("news_collect_win", "04"))
        self.sel_mm_start.setItemText(4, _translate("news_collect_win", "05"))
        self.sel_mm_start.setItemText(5, _translate("news_collect_win", "06"))
        self.sel_mm_start.setItemText(6, _translate("news_collect_win", "07"))
        self.sel_mm_start.setItemText(7, _translate("news_collect_win", "08"))
        self.sel_mm_start.setItemText(8, _translate("news_collect_win", "09"))
        self.sel_mm_start.setItemText(9, _translate("news_collect_win", "10"))
        self.sel_mm_start.setItemText(10, _translate("news_collect_win", "11"))
        self.sel_mm_start.setItemText(11, _translate("news_collect_win", "12"))
        self.btn_show.setText(_translate("news_collect_win", "그래프 출력"))
        self.sel_yy_start.setItemText(0, _translate("news_collect_win", "2022"))
        self.sel_yy_start.setItemText(1, _translate("news_collect_win", "2021"))
        self.sel_yy_start.setItemText(2, _translate("news_collect_win", "2020"))
        self.sel_yy_start.setItemText(3, _translate("news_collect_win", "2019"))
        self.sel_yy_start.setItemText(4, _translate("news_collect_win", "2018"))
        self.sel_yy_start.setItemText(5, _translate("news_collect_win", "2017"))
        self.sel_mm_end.setItemText(0, _translate("news_collect_win", "01"))
        self.sel_mm_end.setItemText(1, _translate("news_collect_win", "02"))
        self.sel_mm_end.setItemText(2, _translate("news_collect_win", "03"))
        self.sel_mm_end.setItemText(3, _translate("news_collect_win", "04"))
        self.sel_mm_end.setItemText(4, _translate("news_collect_win", "05"))
        self.sel_mm_end.setItemText(5, _translate("news_collect_win", "06"))
        self.sel_mm_end.setItemText(6, _translate("news_collect_win", "07"))
        self.sel_mm_end.setItemText(7, _translate("news_collect_win", "08"))
        self.sel_mm_end.setItemText(8, _translate("news_collect_win", "09"))
        self.sel_mm_end.setItemText(9, _translate("news_collect_win", "10"))
        self.sel_mm_end.setItemText(10, _translate("news_collect_win", "11"))
        self.sel_mm_end.setItemText(11, _translate("news_collect_win", "12"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    news_collect_win = QtWidgets.QMainWindow()
    ui = Ui_news_collect_win()
    ui.setupUi(news_collect_win)
    news_collect_win.show()
    sys.exit(app.exec_())
