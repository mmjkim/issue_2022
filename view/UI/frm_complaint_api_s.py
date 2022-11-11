from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import common.config.apiinfo as apifp
from common.config.filepassclass import *
from source.get_api_data_complaint import *

class Ui_complaint_api_win(object):
    def setupUi(self, complaint_api_win):
        complaint_api_win.setObjectName("complaint_api_win")
        complaint_api_win.resize(779, 587)
        self.centralwidget = QtWidgets.QWidget(complaint_api_win)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 11, 761, 118))
        self.groupBox.setObjectName("groupBox")
        self.rad_type_rising = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_rising.setGeometry(QtCore.QRect(20, 24, 86, 20))
        self.rad_type_rising.setObjectName("rad_type_rising")
        self.rad_type_top = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_top.setGeometry(QtCore.QRect(121, 24, 86, 21))
        self.rad_type_top.setObjectName("rad_type_top")
        self.rad_type_today = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_today.setGeometry(QtCore.QRect(20, 52, 86, 21))
        self.rad_type_today.setObjectName("rad_type_today")
        self.rad_type_dftop = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_dftop.setGeometry(QtCore.QRect(121, 52, 81, 20))
        self.rad_type_dftop.setObjectName("rad_type_dftop")
        self.label_seldate = QtWidgets.QLabel(self.groupBox)
        self.label_seldate.setGeometry(QtCore.QRect(233, 24, 78, 16))
        self.label_seldate.setObjectName("label_seldate")
        self.mart_mm_end_2 = QtWidgets.QComboBox(self.groupBox)
        self.mart_mm_end_2.setGeometry(QtCore.QRect(561, 54, 71, 23))
        self.mart_mm_end_2.setObjectName("mart_mm_end_2")
        self.mart_mm_end_2.addItem("")
        self.mart_mm_end_2.addItem("")
        self.mart_mm_end_2.addItem("")
        self.mart_mm_end_2.addItem("")
        self.mart_mm_end_2.addItem("")
        self.mart_mm_end_2.addItem("")
        self.mart_mm_end_2.addItem("")
        self.mart_mm_end_2.addItem("")
        self.mart_mm_end_2.addItem("")
        self.mart_mm_end_2.addItem("")
        self.mart_mm_end_2.addItem("")
        self.mart_mm_end_2.addItem("")
        self.mart_yy_start_2 = QtWidgets.QComboBox(self.groupBox)
        self.mart_yy_start_2.setGeometry(QtCore.QRect(317, 54, 71, 22))
        self.mart_yy_start_2.setObjectName("mart_yy_start_2")
        self.mart_yy_start_2.addItem("")
        self.mart_yy_start_2.addItem("")
        self.mart_yy_start_2.addItem("")
        self.mart_yy_start_2.addItem("")
        self.mart_yy_start_2.addItem("")
        self.mart_yy_start_2.addItem("")
        self.mart_mm_start_2 = QtWidgets.QComboBox(self.groupBox)
        self.mart_mm_start_2.setGeometry(QtCore.QRect(392, 54, 71, 23))
        self.mart_mm_start_2.setObjectName("mart_mm_start_2")
        self.mart_mm_start_2.addItem("")
        self.mart_mm_start_2.addItem("")
        self.mart_mm_start_2.addItem("")
        self.mart_mm_start_2.addItem("")
        self.mart_mm_start_2.addItem("")
        self.mart_mm_start_2.addItem("")
        self.mart_mm_start_2.addItem("")
        self.mart_mm_start_2.addItem("")
        self.mart_mm_start_2.addItem("")
        self.mart_mm_start_2.addItem("")
        self.mart_mm_start_2.addItem("")
        self.mart_mm_start_2.addItem("")
        self.sel_mm_start = QtWidgets.QComboBox(self.groupBox)
        self.sel_mm_start.setGeometry(QtCore.QRect(392, 21, 71, 23))
        self.sel_mm_start.setObjectName("sel_mm_start_2")
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
        self.mart_yy_end_2 = QtWidgets.QComboBox(self.groupBox)
        self.mart_yy_end_2.setGeometry(QtCore.QRect(486, 54, 71, 23))
        self.mart_yy_end_2.setObjectName("mart_yy_end_2")
        self.mart_yy_end_2.addItem("")
        self.mart_yy_end_2.addItem("")
        self.mart_yy_end_2.addItem("")
        self.mart_yy_end_2.addItem("")
        self.mart_yy_end_2.addItem("")
        self.mart_yy_end_2.addItem("")
        self.btn_sel = QtWidgets.QPushButton(self.groupBox)
        self.btn_sel.setGeometry(QtCore.QRect(637, 19, 110, 28))
        self.btn_sel.setObjectName("btn_sel")
        self.btn_mart = QtWidgets.QPushButton(self.groupBox)
        self.btn_mart.setGeometry(QtCore.QRect(637, 52, 110, 28))
        self.btn_mart.setObjectName("btn_mart")
        self.sel_yy_start = QtWidgets.QComboBox(self.groupBox)
        self.sel_yy_start.setGeometry(QtCore.QRect(317, 21, 71, 22))
        self.sel_yy_start.setObjectName("sel_yy_start_2")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.label_martdate = QtWidgets.QLabel(self.groupBox)
        self.label_martdate.setGeometry(QtCore.QRect(233, 57, 78, 16))
        self.label_martdate.setObjectName("label_martdate")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(468, 59, 20, 17))
        self.label_8.setObjectName("label_8")
        self.rad_type_all = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_all.setGeometry(QtCore.QRect(20, 82, 86, 21))
        self.rad_type_all.setObjectName("rad_type_all")
        self.chkbox_saeol = QtWidgets.QCheckBox(self.groupBox)
        self.chkbox_saeol.setGeometry(QtCore.QRect(466, 88, 81, 20))
        self.chkbox_saeol.setObjectName("chkbox_saeol")
        self.chkbox_qna = QtWidgets.QCheckBox(self.groupBox)
        self.chkbox_qna.setGeometry(QtCore.QRect(596, 88, 85, 20))
        self.chkbox_qna.setObjectName("chkbox_qna")
        self.chkbox_dfpt = QtWidgets.QCheckBox(self.groupBox)
        self.chkbox_dfpt.setGeometry(QtCore.QRect(389, 88, 81, 20))
        self.chkbox_dfpt.setObjectName("chkbox_dfpt")
        self.chkbox_qnao = QtWidgets.QCheckBox(self.groupBox)
        self.chkbox_qnao.setGeometry(QtCore.QRect(677, 88, 81, 20))
        self.chkbox_qnao.setObjectName("chkbox_qnao")
        self.label_target = QtWidgets.QLabel(self.groupBox)
        self.label_target.setGeometry(QtCore.QRect(233, 89, 60, 16))
        self.label_target.setObjectName("label_target")
        self.chkbox_prpl = QtWidgets.QCheckBox(self.groupBox)
        self.chkbox_prpl.setGeometry(QtCore.QRect(543, 88, 57, 20))
        self.chkbox_prpl.setObjectName("chkbox_prpl")
        self.chkbox_pttn = QtWidgets.QCheckBox(self.groupBox)
        self.chkbox_pttn.setGeometry(QtCore.QRect(312, 88, 81, 20))
        self.chkbox_pttn.setObjectName("chkbox_pttn")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 122, 761, 459))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tbl_dftop = QtWidgets.QTableWidget(self.frame_2)
        self.tbl_dftop.setGeometry(QtCore.QRect(570, 20, 181, 424))
        self.tbl_dftop.setObjectName("tbl_dftop")
        self.tbl_dftop.setColumnCount(1)
        self.tbl_dftop.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dftop.setHorizontalHeaderItem(0, item)
        self.tbl_dftop.horizontalHeader().setStretchLastSection(True)
        self.tbl_dftop.verticalHeader().setDefaultSectionSize(35)
        self.tbl_rising = QtWidgets.QTableWidget(self.frame_2)
        self.tbl_rising.setGeometry(QtCore.QRect(8, 20, 181, 424))
        self.tbl_rising.setObjectName("tbl_rising")
        self.tbl_rising.setColumnCount(1)
        self.tbl_rising.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_rising.setHorizontalHeaderItem(0, item)
        self.tbl_rising.horizontalHeader().setStretchLastSection(True)
        self.tbl_rising.verticalHeader().setDefaultSectionSize(35)
        self.tbl_today = QtWidgets.QTableWidget(self.frame_2)
        self.tbl_today.setGeometry(QtCore.QRect(383, 20, 181, 424))
        self.tbl_today.setObjectName("tbl_today")
        self.tbl_today.setColumnCount(1)
        self.tbl_today.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_today.setHorizontalHeaderItem(0, item)
        self.tbl_today.horizontalHeader().setStretchLastSection(True)
        self.tbl_today.verticalHeader().setDefaultSectionSize(35)
        self.tbl_top = QtWidgets.QTableWidget(self.frame_2)
        self.tbl_top.setGeometry(QtCore.QRect(195, 20, 181, 424))
        self.tbl_top.setObjectName("tbl_top")
        self.tbl_top.setColumnCount(1)
        self.tbl_top.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_top.setHorizontalHeaderItem(0, item)
        self.tbl_top.horizontalHeader().setStretchLastSection(True)
        self.tbl_top.verticalHeader().setDefaultSectionSize(35)
        complaint_api_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(complaint_api_win)
        QtCore.QMetaObject.connectSlotsByName(complaint_api_win)

        # self.btn_sel.clicked.connect(self.get_news)

        self.tbl_rising.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_today.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_top.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_dftop.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.show_folders()

        self.btn_sel.clicked.connect(self.get_complaints)


    def get_complaints(self):
        global part
        s_yy_start = self.sel_yy_start.currentText()
        s_mm_start = self.sel_mm_start.currentText()

        if self.rad_type_rising.isChecked():
            part = '급등'
        elif self.rad_type_top.isChecked():
            part = '핵심'
        elif self.rad_type_today.isChecked():
            part = '오늘'
        elif self.rad_type_dftop.isChecked():
            part = '최다'
        elif self.rad_type_all.isChecked():
            part = '전체'

        target_list = []
        if self.chkbox_pttn.isChecked():
            target_list.append('pttn')
        if self.chkbox_dfpt.isChecked():
            target_list.append('dfpt')
        if self.chkbox_saeol.isChecked():
            target_list.append('saeol')
        if self.chkbox_prpl.isChecked():
            target_list.append('prpl')
        if self.chkbox_qna.isChecked():
            target_list.append('qna')
        if self.chkbox_qnao.isChecked():
            target_list.append('qna_origin')

        target = "%s" % ",".join(target_list)
        get_complaint_data(part, s_yy_start+s_mm_start, target)
        self.show_folders()


    def show_folders(self):
        file_path = FilePathClass()

        pathRising = file_path.get_raw_collect_path() + apifp.COMPLAIN_DATA_PATH_RISE
        pathTop = file_path.get_raw_collect_path() + apifp.COMPLAIN_DATA_PATH_TOP
        pathToday = file_path.get_raw_collect_path() + apifp.COMPLAIN_DATA_PATH_TOPIC
        pathDftop = file_path.get_raw_collect_path() + apifp.COMPLAIN_DATA_PATH_DFTOPKW

        if file_path.is_path_exist_check(pathRising) is False:
            file_path.make_path(pathRising)
        if file_path.is_path_exist_check(pathTop) is False:
            file_path.make_path(pathTop)
        if file_path.is_path_exist_check(pathToday) is False:
            file_path.make_path(pathToday)
        if file_path.is_path_exist_check(pathDftop) is False:
            file_path.make_path(pathDftop)

        folderRising = os.listdir(pathRising)
        folderTop = os.listdir(pathTop)
        folderToday = os.listdir(pathToday)
        folderDftop = os.listdir(pathDftop)

        rising_list = []
        top_list = []
        today_list = []
        dftop_list = []

        for i in range(0, len(folderRising)):
            if folderRising[i][-3:] == 'csv':
                rising_list.append(folderRising[i])
        for i in range(0, len(folderTop)):
            if folderTop[i][-3:] == 'csv':
                top_list.append(folderTop[i])
        for i in range(0, len(folderToday)):
            if folderToday[i][-3:] == 'csv':
                today_list.append(folderToday[i])
        for i in range(0, len(folderDftop)):
            if folderDftop[i][-3:] == 'csv':
                dftop_list.append(folderDftop[i])

        self.tbl_rising.setRowCount(len(rising_list))
        self.tbl_top.setRowCount(len(top_list))
        self.tbl_today.setRowCount(len(today_list))
        self.tbl_dftop.setRowCount(len(dftop_list))

        for j in range(0, len(rising_list)):
            self.tbl_rising.setItem(j, 0, QTableWidgetItem(rising_list[j]))
        for j in range(0, len(top_list)):
            self.tbl_top.setItem(j, 0, QTableWidgetItem(top_list[j]))
        for j in range(0, len(today_list)):
            self.tbl_today.setItem(j, 0, QTableWidgetItem(today_list[j]))
        for j in range(0, len(dftop_list)):
            self.tbl_dftop.setItem(j, 0, QTableWidgetItem(dftop_list[j]))

    #     self.tbl_rising.cellClicked.connect(self.get_value)
    #
    #
    # def get_value(self, row, column):
    #     item = self.tbl_rising.item(row, column).text()
    #     print(item)

    def retranslateUi(self, complaint_api_win):
        _translate = QtCore.QCoreApplication.translate
        complaint_api_win.setWindowTitle(_translate("complaint_api_win", "MainWindow"))
        self.groupBox.setTitle(_translate("complaint_api_win", " [ 민원 ] "))
        self.rad_type_rising.setText(_translate("complaint_api_win", "급등"))
        self.rad_type_top.setText(_translate("complaint_api_win", "핵심"))
        self.rad_type_today.setText(_translate("complaint_api_win", "오늘"))
        self.rad_type_dftop.setText(_translate("complaint_api_win", "최다"))
        self.label_seldate.setText(_translate("complaint_api_win", "수집기간: "))
        self.mart_mm_end_2.setItemText(0, _translate("complaint_api_win", "01"))
        self.mart_mm_end_2.setItemText(1, _translate("complaint_api_win", "02"))
        self.mart_mm_end_2.setItemText(2, _translate("complaint_api_win", "03"))
        self.mart_mm_end_2.setItemText(3, _translate("complaint_api_win", "04"))
        self.mart_mm_end_2.setItemText(4, _translate("complaint_api_win", "05"))
        self.mart_mm_end_2.setItemText(5, _translate("complaint_api_win", "06"))
        self.mart_mm_end_2.setItemText(6, _translate("complaint_api_win", "07"))
        self.mart_mm_end_2.setItemText(7, _translate("complaint_api_win", "08"))
        self.mart_mm_end_2.setItemText(8, _translate("complaint_api_win", "09"))
        self.mart_mm_end_2.setItemText(9, _translate("complaint_api_win", "10"))
        self.mart_mm_end_2.setItemText(10, _translate("complaint_api_win", "11"))
        self.mart_mm_end_2.setItemText(11, _translate("complaint_api_win", "12"))
        self.mart_yy_start_2.setItemText(0, _translate("complaint_api_win", "2022"))
        self.mart_yy_start_2.setItemText(1, _translate("complaint_api_win", "2021"))
        self.mart_yy_start_2.setItemText(2, _translate("complaint_api_win", "2020"))
        self.mart_yy_start_2.setItemText(3, _translate("complaint_api_win", "2019"))
        self.mart_yy_start_2.setItemText(4, _translate("complaint_api_win", "2018"))
        self.mart_yy_start_2.setItemText(5, _translate("complaint_api_win", "2017"))
        self.mart_mm_start_2.setItemText(0, _translate("complaint_api_win", "01"))
        self.mart_mm_start_2.setItemText(1, _translate("complaint_api_win", "02"))
        self.mart_mm_start_2.setItemText(2, _translate("complaint_api_win", "03"))
        self.mart_mm_start_2.setItemText(3, _translate("complaint_api_win", "04"))
        self.mart_mm_start_2.setItemText(4, _translate("complaint_api_win", "05"))
        self.mart_mm_start_2.setItemText(5, _translate("complaint_api_win", "06"))
        self.mart_mm_start_2.setItemText(6, _translate("complaint_api_win", "07"))
        self.mart_mm_start_2.setItemText(7, _translate("complaint_api_win", "08"))
        self.mart_mm_start_2.setItemText(8, _translate("complaint_api_win", "09"))
        self.mart_mm_start_2.setItemText(9, _translate("complaint_api_win", "10"))
        self.mart_mm_start_2.setItemText(10, _translate("complaint_api_win", "11"))
        self.mart_mm_start_2.setItemText(11, _translate("complaint_api_win", "12"))
        self.sel_mm_start.setItemText(0, _translate("complaint_api_win", "01"))
        self.sel_mm_start.setItemText(1, _translate("complaint_api_win", "02"))
        self.sel_mm_start.setItemText(2, _translate("complaint_api_win", "03"))
        self.sel_mm_start.setItemText(3, _translate("complaint_api_win", "04"))
        self.sel_mm_start.setItemText(4, _translate("complaint_api_win", "05"))
        self.sel_mm_start.setItemText(5, _translate("complaint_api_win", "06"))
        self.sel_mm_start.setItemText(6, _translate("complaint_api_win", "07"))
        self.sel_mm_start.setItemText(7, _translate("complaint_api_win", "08"))
        self.sel_mm_start.setItemText(8, _translate("complaint_api_win", "09"))
        self.sel_mm_start.setItemText(9, _translate("complaint_api_win", "10"))
        self.sel_mm_start.setItemText(10, _translate("complaint_api_win", "11"))
        self.sel_mm_start.setItemText(11, _translate("complaint_api_win", "12"))
        self.mart_yy_end_2.setItemText(0, _translate("complaint_api_win", "2022"))
        self.mart_yy_end_2.setItemText(1, _translate("complaint_api_win", "2021"))
        self.mart_yy_end_2.setItemText(2, _translate("complaint_api_win", "2020"))
        self.mart_yy_end_2.setItemText(3, _translate("complaint_api_win", "2019"))
        self.mart_yy_end_2.setItemText(4, _translate("complaint_api_win", "2018"))
        self.mart_yy_end_2.setItemText(5, _translate("complaint_api_win", "2017"))
        self.btn_sel.setText(_translate("complaint_api_win", "데이터 수집"))
        self.btn_mart.setText(_translate("complaint_api_win", "데이터 적재"))
        self.sel_yy_start.setItemText(0, _translate("complaint_api_win", "2022"))
        self.sel_yy_start.setItemText(1, _translate("complaint_api_win", "2021"))
        self.sel_yy_start.setItemText(2, _translate("complaint_api_win", "2020"))
        self.sel_yy_start.setItemText(3, _translate("complaint_api_win", "2019"))
        self.sel_yy_start.setItemText(4, _translate("complaint_api_win", "2018"))
        self.sel_yy_start.setItemText(5, _translate("complaint_api_win", "2017"))
        self.label_martdate.setText(_translate("complaint_api_win", "적재기간: "))
        self.label_8.setText(_translate("complaint_api_win", "~"))
        self.rad_type_all.setText(_translate("complaint_api_win", "전체"))
        self.chkbox_saeol.setText(_translate("complaint_api_win", "수집민원"))
        self.chkbox_qna.setText(_translate("complaint_api_win", "정책QNA"))
        self.chkbox_dfpt.setText(_translate("complaint_api_win", "고충민원"))
        self.chkbox_qnao.setText(_translate("complaint_api_win", "공개민원"))
        self.label_target.setText(_translate("complaint_api_win", "분석대상:"))
        self.chkbox_prpl.setText(_translate("complaint_api_win", "제안"))
        self.chkbox_pttn.setText(_translate("complaint_api_win", "일반민원"))
        self.tbl_dftop.setSortingEnabled(True)
        item = self.tbl_dftop.horizontalHeaderItem(0)
        item.setText(_translate("complaint_api_win", "최다 민원 키워드"))
        self.tbl_rising.setSortingEnabled(True)
        item = self.tbl_rising.horizontalHeaderItem(0)
        item.setText(_translate("complaint_api_win", "급등 키워드"))
        self.tbl_today.setSortingEnabled(True)
        item = self.tbl_today.horizontalHeaderItem(0)
        item.setText(_translate("complaint_api_win", "오늘의 민원 이슈"))
        self.tbl_top.setSortingEnabled(True)
        item = self.tbl_top.horizontalHeaderItem(0)
        item.setText(_translate("complaint_api_win", "핵심 키워드"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    complaint_api_win = QtWidgets.QMainWindow()
    ui = Ui_complaint_api_win()
    ui.setupUi(complaint_api_win)
    complaint_api_win.show()
    sys.exit(app.exec_())
