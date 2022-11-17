import calendar
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from common.config.filepassclass import *
import common.config.apiinfo as apifp
from source.get_api_data_naver import *
from common.function.funcCommon import *
from source.get_api_data_complaint import get_wd_cloud_info
from source.anal_keyword_compare import *


class Ui_Anal_Dialog(object):
    def setupUi(self, Anal_Dialog):
        Anal_Dialog.setObjectName("Anal_Dialog")
        Anal_Dialog.resize(1024, 768)
        self.frame_2 = QtWidgets.QFrame(Anal_Dialog)
        self.frame_2.setGeometry(QtCore.QRect(10, 9, 1001, 321))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tbl_word = QtWidgets.QTableWidget(self.frame_2)
        self.tbl_word.setGeometry(QtCore.QRect(7, 40, 989, 271))
        self.tbl_word.setObjectName("tbl_word")
        self.tbl_word.setColumnCount(4)
        self.tbl_word.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_word.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_word.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_word.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_word.setHorizontalHeaderItem(3, item)
        # self.tbl_word.horizontalHeader().setStretchLastSection(True)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label.setObjectName("label")
        self.btn_anal = QtWidgets.QPushButton(self.frame_2)
        self.btn_anal.setGeometry(QtCore.QRect(910, 10, 79, 23))
        self.btn_anal.setObjectName("btn_anal")
        self.frame_5 = QtWidgets.QFrame(Anal_Dialog)
        self.frame_5.setGeometry(QtCore.QRect(360, 401, 651, 351))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_3.setObjectName("label_3")
        self.btn_coll_c = QtWidgets.QPushButton(self.frame_5)
        self.btn_coll_c.setGeometry(QtCore.QRect(560, 9, 75, 25))
        self.btn_coll_c.setObjectName("btn_coll_c")
        self.frame_4 = QtWidgets.QFrame(Anal_Dialog)
        self.frame_4.setGeometry(QtCore.QRect(10, 401, 341, 351))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.tbl_naver = QtWidgets.QTableWidget(self.frame_4)
        self.tbl_naver.setGeometry(QtCore.QRect(10, 40, 321, 301))
        self.tbl_naver.setObjectName("tbl_naver")
        self.tbl_naver.setColumnCount(1)
        self.tbl_naver.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(225, 225, 225))
        self.tbl_naver.setHorizontalHeaderItem(0, item)
        self.tbl_naver.horizontalHeader().setStretchLastSection(True)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(18, 10, 121, 16))
        self.label_2.setObjectName("label_2")
        self.btn_coll = QtWidgets.QPushButton(self.frame_4)
        self.btn_coll.setGeometry(QtCore.QRect(249, 10, 79, 23))
        self.btn_coll.setObjectName("btn_coll")
        self.groupBox = QtWidgets.QGroupBox(Anal_Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 337, 1001, 61))
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(234, 28, 16, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(28, 27, 54, 15))
        self.label_6.setObjectName("label_6")
        self.sel_yy_end = QtWidgets.QComboBox(self.groupBox)
        self.sel_yy_end.setGeometry(QtCore.QRect(251, 23, 67, 23))
        self.sel_yy_end.setObjectName("sel_yy_end")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_mm_start = QtWidgets.QComboBox(self.groupBox)
        self.sel_mm_start.setGeometry(QtCore.QRect(176, 23, 51, 23))
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
        self.sel_yy_start = QtWidgets.QComboBox(self.groupBox)
        self.sel_yy_start.setGeometry(QtCore.QRect(99, 23, 67, 23))
        self.sel_yy_start.setObjectName("sel_yy_start")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_mm_end = QtWidgets.QComboBox(self.groupBox)
        self.sel_mm_end.setGeometry(QtCore.QRect(327, 23, 51, 23))
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
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(400, 19, 20, 31))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(441, 26, 71, 16))
        self.label_7.setObjectName("label_7")
        self.txt_anal_word = QtWidgets.QTextEdit(self.groupBox)
        self.txt_anal_word.setGeometry(QtCore.QRect(523, 21, 448, 24))
        self.txt_anal_word.setToolTip("")
        self.txt_anal_word.setObjectName("txt_anal_word")

        self.retranslateUi(Anal_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Anal_Dialog)

        self.tbl_naver.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_naver.verticalHeader().setDefaultSectionSize(35)
        self.tbl_word.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_word.verticalHeader().setDefaultSectionSize(35)

        self.btn_coll.clicked.connect(self.get_data)
        self.btn_anal.clicked.connect(self.get_anal)

        self.show_folders()


    def get_anal(self):
        data = compare_keyword()
        data_p = data[data['type'] == '뉴스_정치']
        data_s = data[data['type'] == '뉴스_사회']
        data_e = data[data['type'] == '뉴스_경제']

        dataJoin = pd.merge(data_p, data_s, how='outer', on=['keyword'])
        dataJoin1 = pd.merge(dataJoin, data_e, how='outer', on=['keyword'])

        dataJoin1.columns = ['keyword', 'part_p', '뉴스_정치', 'part_s', '뉴스_사회', 'part_e', '뉴스_경제']
        dataAnal = dataJoin1[['keyword', '뉴스_정치', '뉴스_사회', '뉴스_경제']]
        dataAnal = dataAnal.fillna(('-'))

        self.tbl_word.setRowCount(len(dataAnal))

        for i in range(len(dataAnal)):
            self.tbl_word.setItem(i, 0, QTableWidgetItem(dataAnal['keyword'][i]))
            self.tbl_word.setItem(i, 1, QTableWidgetItem(dataAnal['뉴스_정치'][i]))
            self.tbl_word.setItem(i, 2, QTableWidgetItem(dataAnal['뉴스_경제'][i]))
            self.tbl_word.setItem(i, 3, QTableWidgetItem(dataAnal['뉴스_사회'][i]))


    def show_folders(self):
        file_path = FilePathClass()
        path_naver = file_path.get_raw_use_path()

        if file_path.is_path_exist_check(path_naver) is False:
            file_path.make_path(path_naver)

        folderNaver = os.listdir(path_naver)

        naver_list = []

        for i in range(0, len(folderNaver)):
            if (folderNaver[i][-3:] == 'csv') & (folderNaver[i][:3] == '네이버'):
                naver_list.append(folderNaver[i])

        self.tbl_naver.setRowCount(len(naver_list))

        for j in range(0, len(naver_list)):
            self.tbl_naver.setItem(j, 0, QTableWidgetItem(naver_list[j]))


    def get_data(self):
        s_yy_start = self.sel_yy_start.currentText()
        s_mm_start = self.sel_mm_start.currentText()
        s_yy_end = self.sel_yy_end.currentText()
        s_mm_end = self.sel_mm_end.currentText()

        keywords = '검색,' + self.txt_anal_word.toPlainText()
        anal_keywords = keywords.split(',')

        naver_trend_search(datetime.strptime(s_yy_start+s_mm_start+"01", '%Y%m%d'),
                           getMonthRange(s_yy_end,s_mm_end),
                           anal_keywords)

        self.show_folders()
        # get_wd_cloud_info(anal_keywords, s_yy_start+s_mm_start, s_yy_end,s_mm_end, 'pttn,dfpt,saeol,prpl,qna,qna_origin')


    def retranslateUi(self, Anal_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Anal_Dialog.setWindowTitle(_translate("Anal_Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Anal_Dialog", " [ 분석 ] "))
        self.label_5.setText(_translate("Anal_Dialog", "~"))
        self.label_6.setText(_translate("Anal_Dialog", "분석기간: "))
        self.sel_yy_end.setItemText(0, _translate("Anal_Dialog", str(datetime.today().year)))
        self.sel_yy_end.setItemText(1, _translate("Anal_Dialog", str(datetime.today().year-1)))
        self.sel_yy_end.setItemText(2, _translate("Anal_Dialog", str(datetime.today().year-2)))
        self.sel_yy_end.setItemText(3, _translate("Anal_Dialog", str(datetime.today().year-3)))
        self.sel_yy_end.setItemText(4, _translate("Anal_Dialog", str(datetime.today().year-4)))
        self.sel_yy_end.setItemText(5, _translate("Anal_Dialog", str(datetime.today().year-5)))
        self.sel_mm_start.setItemText(0, _translate("Anal_Dialog", "01"))
        self.sel_mm_start.setItemText(1, _translate("Anal_Dialog", "02"))
        self.sel_mm_start.setItemText(2, _translate("Anal_Dialog", "03"))
        self.sel_mm_start.setItemText(3, _translate("Anal_Dialog", "04"))
        self.sel_mm_start.setItemText(4, _translate("Anal_Dialog", "05"))
        self.sel_mm_start.setItemText(5, _translate("Anal_Dialog", "06"))
        self.sel_mm_start.setItemText(6, _translate("Anal_Dialog", "07"))
        self.sel_mm_start.setItemText(7, _translate("Anal_Dialog", "08"))
        self.sel_mm_start.setItemText(8, _translate("Anal_Dialog", "09"))
        self.sel_mm_start.setItemText(9, _translate("Anal_Dialog", "10"))
        self.sel_mm_start.setItemText(10, _translate("Anal_Dialog", "11"))
        self.sel_mm_start.setItemText(11, _translate("Anal_Dialog", "12"))
        self.btn_anal.setText(_translate("Anal_Dialog", "분석"))
        self.sel_yy_start.setItemText(0, _translate("Anal_Dialog", str(datetime.today().year)))
        self.sel_yy_start.setItemText(1, _translate("Anal_Dialog", str(datetime.today().year-1)))
        self.sel_yy_start.setItemText(2, _translate("Anal_Dialog", str(datetime.today().year-2)))
        self.sel_yy_start.setItemText(3, _translate("Anal_Dialog", str(datetime.today().year-3)))
        self.sel_yy_start.setItemText(4, _translate("Anal_Dialog", str(datetime.today().year-4)))
        self.sel_yy_start.setItemText(5, _translate("Anal_Dialog", str(datetime.today().year-5)))
        self.sel_mm_end.setItemText(0, _translate("Anal_Dialog", "01"))
        self.sel_mm_end.setItemText(1, _translate("Anal_Dialog", "02"))
        self.sel_mm_end.setItemText(2, _translate("Anal_Dialog", "03"))
        self.sel_mm_end.setItemText(3, _translate("Anal_Dialog", "04"))
        self.sel_mm_end.setItemText(4, _translate("Anal_Dialog", "05"))
        self.sel_mm_end.setItemText(5, _translate("Anal_Dialog", "06"))
        self.sel_mm_end.setItemText(6, _translate("Anal_Dialog", "07"))
        self.sel_mm_end.setItemText(7, _translate("Anal_Dialog", "08"))
        self.sel_mm_end.setItemText(8, _translate("Anal_Dialog", "09"))
        self.sel_mm_end.setItemText(9, _translate("Anal_Dialog", "10"))
        self.sel_mm_end.setItemText(10, _translate("Anal_Dialog", "11"))
        self.sel_mm_end.setItemText(11, _translate("Anal_Dialog", "12"))
        self.label_7.setText(_translate("Anal_Dialog", "분석 키워드"))
        item = self.tbl_word.horizontalHeaderItem(0)
        item.setText(_translate("Anal_Dialog", "민원"))
        item = self.tbl_word.horizontalHeaderItem(1)
        item.setText(_translate("Anal_Dialog", "뉴스_정치"))
        item = self.tbl_word.horizontalHeaderItem(2)
        item.setText(_translate("Anal_Dialog", "뉴스_경제"))
        item = self.tbl_word.horizontalHeaderItem(3)
        item.setText(_translate("Anal_Dialog", "뉴스_사회"))
        self.label.setText(_translate("Anal_Dialog", "동시 출현 키워드"))
        self.btn_anal.setText(_translate("Anal_Dialog", "분석"))
        item = self.tbl_naver.horizontalHeaderItem(0)
        item.setText(_translate("Anal_Dialog", "파일명"))
        self.label_2.setText(_translate("Anal_Dialog", "네이버 검색어"))
        self.btn_coll.setText(_translate("Anal_Dialog", "데이터 수집"))
        self.btn_coll_c.setText(_translate("Anal_Dialog", "데이터 수집"))
        self.label_3.setText(_translate("Anal_Dialog", "뉴스 크롤링 데이터"))
        self.tbl_naver.setSortingEnabled(True)
        self.tbl_word.setSortingEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Anal_Dialog = QtWidgets.QDialog()
    ui = Ui_Anal_Dialog()
    ui.setupUi(Anal_Dialog)
    Anal_Dialog.show()
    sys.exit(app.exec_())
