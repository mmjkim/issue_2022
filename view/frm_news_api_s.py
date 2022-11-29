import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from datetime import datetime

from source.get_api_data_news import *
import common.config.apiinfo as apifp
from common.config.filepassclass import *
from source.save_anal_mart import anal_mart_news


class Ui_news_collect_win(object):
    def setupUi(self, news_collect_win):
        news_collect_win.setObjectName("news_collect_win")
        news_collect_win.resize(1024, 768)
        news_collect_win.setMaximumSize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(news_collect_win)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 110, 1004, 651))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tbl_politics = QtWidgets.QTableWidget(self.frame_2)
        self.tbl_politics.setGeometry(QtCore.QRect(10, 19, 321, 615))
        self.tbl_politics.setObjectName("tbl_politics")
        self.tbl_politics.setColumnCount(1)
        self.tbl_politics.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_politics.setHorizontalHeaderItem(0, item)
        self.tbl_politics.horizontalHeader().setStretchLastSection(True)
        self.tbl_politics.verticalHeader().setDefaultSectionSize(35)
        self.tbl_politics.setSortingEnabled(True)
        self.tbl_economy = QtWidgets.QTableWidget(self.frame_2)
        self.tbl_economy.setGeometry(QtCore.QRect(672, 19, 321, 615))
        self.tbl_economy.setObjectName("tbl_economy")
        self.tbl_economy.setColumnCount(1)
        self.tbl_economy.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_economy.setHorizontalHeaderItem(0, item)
        self.tbl_economy.horizontalHeader().setStretchLastSection(True)
        self.tbl_economy.verticalHeader().setDefaultSectionSize(35)
        self.tbl_economy.setSortingEnabled(True)
        self.tbl_social = QtWidgets.QTableWidget(self.frame_2)
        self.tbl_social.setGeometry(QtCore.QRect(341, 19, 321, 615))
        self.tbl_social.setObjectName("tbl_social")
        self.tbl_social.setColumnCount(1)
        self.tbl_social.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_social.setHorizontalHeaderItem(0, item)
        self.tbl_social.horizontalHeader().setStretchLastSection(True)
        self.tbl_social.verticalHeader().setDefaultSectionSize(35)
        self.tbl_social.setSortingEnabled(True)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1004, 103))
        self.groupBox.setObjectName("groupBox")
        self.rad_type_1 = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_1.setGeometry(QtCore.QRect(40, 30, 86, 20))
        self.rad_type_1.setObjectName("rad_type_1")
        self.rad_type_1.setChecked(True)
        self.rad_type_2 = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_2.setGeometry(QtCore.QRect(141, 30, 86, 21))
        self.rad_type_2.setObjectName("rad_type_2")
        self.rad_type_3 = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_3.setGeometry(QtCore.QRect(40, 61, 86, 21))
        self.rad_type_3.setObjectName("rad_type_3")
        self.rad_type_4 = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_4.setGeometry(QtCore.QRect(141, 61, 111, 20))
        self.rad_type_4.setObjectName("rad_type_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(531, 46, 20, 17))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(286, 44, 78, 16))
        self.label.setObjectName("label")
        self.sel_yy_end = QtWidgets.QComboBox(self.groupBox)
        self.sel_yy_end.setGeometry(QtCore.QRect(549, 41, 71, 23))
        self.sel_yy_end.setObjectName("sel_yy_end")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_mm_start = QtWidgets.QComboBox(self.groupBox)
        self.sel_mm_start.setGeometry(QtCore.QRect(453, 41, 71, 23))
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
        self.btn_sel = QtWidgets.QPushButton(self.groupBox)
        self.btn_sel.setGeometry(QtCore.QRect(720, 39, 110, 28))
        self.btn_sel.setObjectName("btn_sel")
        self.btn_mart = QtWidgets.QPushButton(self.groupBox)
        self.btn_mart.setGeometry(QtCore.QRect(842, 40, 110, 28))
        self.btn_mart.setObjectName("btn_mart")
        self.sel_yy_start = QtWidgets.QComboBox(self.groupBox)
        self.sel_yy_start.setGeometry(QtCore.QRect(370, 41, 71, 22))
        self.sel_yy_start.setObjectName("sel_yy_start")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_mm_end = QtWidgets.QComboBox(self.groupBox)
        self.sel_mm_end.setGeometry(QtCore.QRect(631, 41, 71, 23))
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
        news_collect_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(news_collect_win)
        QtCore.QMetaObject.connectSlotsByName(news_collect_win)

        self.btn_sel.clicked.connect(self.get_news)
        self.btn_mart.clicked.connect(self.save_mart)

        self.tbl_politics.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_social.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_economy.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tbl_politics.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")
        self.tbl_social.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")
        self.tbl_economy.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.show_folders()


    def save_mart(self):
        if self.rad_type_1.isChecked():
            anal_mart_news('정치')
        elif self.rad_type_2.isChecked():
            anal_mart_news('사회')
        elif self.rad_type_3.isChecked():
            anal_mart_news('경제')
        elif self.rad_type_4.isChecked():
            anal_mart_news('정치')
            anal_mart_news('사회')
            anal_mart_news('경제')


    def show_folders(self):
        file_path = FilePathClass()

        pathPolitics = file_path.get_raw_collect_path() + apifp.NEWS_DATA_PATH_POLITICS
        pathSocial = file_path.get_raw_collect_path() + apifp.NEWS_DATA_PATH_SOCIETY
        pathEconomy = file_path.get_raw_collect_path() + apifp.NEWS_DATA_PATH_ECONOMY

        if file_path.is_path_exist_check(pathPolitics) is False:
            file_path.make_path(pathPolitics)
        if file_path.is_path_exist_check(pathSocial) is False:
            file_path.make_path(pathSocial)
        if file_path.is_path_exist_check(pathEconomy) is False:
            file_path.make_path(pathEconomy)

        folderPolitics = os.listdir(pathPolitics)
        folderSocial = os.listdir(pathSocial)
        folderEconomy = os.listdir(pathEconomy)

        politics_list = []
        social_list = []
        economy_list = []

        for i in range(0, len(folderPolitics)):
            if folderPolitics[i][-3:] == 'csv':
                politics_list.append(folderPolitics[i])
        for i in range(0, len(folderSocial)):
            if folderSocial[i][-3:] == 'csv':
                social_list.append(folderSocial[i])
        for i in range(0, len(folderEconomy)):
            if folderEconomy[i][-3:] == 'csv':
                economy_list.append(folderEconomy[i])

        self.tbl_politics.setRowCount(len(politics_list))
        self.tbl_social.setRowCount(len(social_list))
        self.tbl_economy.setRowCount(len(economy_list))

        for j in range(0, len(politics_list)):
            self.tbl_politics.setItem(j, 0, QTableWidgetItem(politics_list[j]))
        for j in range(0, len(social_list)):
            self.tbl_social.setItem(j, 0, QTableWidgetItem(social_list[j]))
        for j in range(0, len(economy_list)):
            self.tbl_economy.setItem(j, 0, QTableWidgetItem(economy_list[j]))

        self.tbl_economy.cellClicked.connect(self.get_value)


    def get_value(self, row, column):
        item = self.tbl_economy.item(row, column).text()
        print(item)


    def get_news(self):
        global part
        s_yy_start = self.sel_yy_start.currentText()
        s_mm_start = self.sel_mm_start.currentText()
        s_yy_end = self.sel_yy_end.currentText()
        s_mm_end = self.sel_mm_end.currentText()

        if self.rad_type_1.isChecked():
            part = '정치'
        elif self.rad_type_2.isChecked():
            part = '사회'
        elif self.rad_type_3.isChecked():
            part = '경제'
        elif self.rad_type_4.isChecked():
            part = '전체'

        get_news_data(part, s_yy_start+s_mm_start, s_yy_end+s_mm_end)

        self.show_folders()


    def retranslateUi(self, news_collect_win):
        _translate = QtCore.QCoreApplication.translate
        news_collect_win.setWindowTitle(_translate("news_collect_win", "뉴스 데이터 수집"))
        item = self.tbl_politics.horizontalHeaderItem(0)
        item.setText(_translate("news_collect_win", "정치"))
        item = self.tbl_social.horizontalHeaderItem(0)
        item.setText(_translate("news_collect_win", "사회"))
        item = self.tbl_economy.horizontalHeaderItem(0)
        item.setText(_translate("news_collect_win", "경제"))
        self.groupBox.setTitle(_translate("news_collect_win", " [ 뉴스 ] "))
        self.rad_type_1.setText(_translate("news_collect_win", "정치"))
        self.rad_type_2.setText(_translate("news_collect_win", "사회"))
        self.rad_type_3.setText(_translate("news_collect_win", "경제"))
        self.rad_type_4.setText(_translate("news_collect_win", "전체"))
        self.label_2.setText(_translate("news_collect_win", "~"))
        self.label.setText(_translate("news_collect_win", "수집기간: "))
        self.sel_yy_end.setItemText(0, _translate("news_collect_win", str(datetime.today().year)))
        self.sel_yy_end.setItemText(1, _translate("news_collect_win", str(datetime.today().year-1)))
        self.sel_yy_end.setItemText(2, _translate("news_collect_win", str(datetime.today().year-2)))
        self.sel_yy_end.setItemText(3, _translate("news_collect_win", str(datetime.today().year-3)))
        self.sel_yy_end.setItemText(4, _translate("news_collect_win", str(datetime.today().year-4)))
        self.sel_yy_end.setItemText(5, _translate("news_collect_win", str(datetime.today().year-5)))
        self.sel_yy_end.setCurrentText(str(datetime.today().year))
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
        self.btn_sel.setText(_translate("news_collect_win", "데이터 수집"))
        self.btn_mart.setText(_translate("news_collect_win", "데이터 적재"))
        self.sel_yy_start.setItemText(0, _translate("news_collect_win", str(datetime.today().year)))
        self.sel_yy_start.setItemText(1, _translate("news_collect_win", str(datetime.today().year-1)))
        self.sel_yy_start.setItemText(2, _translate("news_collect_win", str(datetime.today().year-2)))
        self.sel_yy_start.setItemText(3, _translate("news_collect_win", str(datetime.today().year-3)))
        self.sel_yy_start.setItemText(4, _translate("news_collect_win", str(datetime.today().year-4)))
        self.sel_yy_start.setItemText(5, _translate("news_collect_win", str(datetime.today().year-5)))
        self.sel_yy_start.setCurrentText(str(datetime.today().year))
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
        self.sel_mm_end.setCurrentText(str(datetime.today().month))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    news_collect_win = QtWidgets.QMainWindow()
    ui = Ui_news_collect_win()
    ui.setupUi(news_collect_win)
    news_collect_win.show()
    sys.exit(app.exec_())
