import os
import sys
import warnings
warnings.filterwarnings(action='ignore')

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QAbstractItemView, QCheckBox, QWidget, QHBoxLayout

from common.config.filepassclass import FilePathClass
from source.anal_contents_lda import *


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1324, 868)
        Dialog.setMaximumSize(1324, 868)
        Dialog.setMinimumSize(1324, 868)

        # 분석/내용 탭 생성
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(11, 8, 1306, 190))
        self.tabWidget.setObjectName("tabWidget")
        # 분석 탭
        self.tab_anal = QtWidgets.QWidget()
        self.tab_anal.setObjectName("tab_anal")
        self.tabWidget.addTab(self.tab_anal, "")
        # 내용 탭
        self.tab_content = QtWidgets.QWidget()
        self.tab_content.setObjectName("tab_content")
        self.tabWidget.addTab(self.tab_content, "")
    
        self.tabWidget.setCurrentIndex(0)
        
        self.group1 = QtWidgets.QGroupBox(self.tab_anal)
        self.group1.setGeometry(QtCore.QRect(10, 10, 251, 148))
        self.group1.setObjectName("group1")
        
        self.btn_search = QtWidgets.QPushButton(self.group1)
        self.btn_search.setGeometry(QtCore.QRect(162, 15, 77, 21))
        self.btn_search.setObjectName("btn_search")
        
        # 데이터 테이블
        self.tbl_keyword = QtWidgets.QTableWidget(self.group1)
        self.tbl_keyword.setGeometry(QtCore.QRect(5, 40, 241, 101))
        self.tbl_keyword.setObjectName("tbl_keyword")
        self.tbl_keyword.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_keyword.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_keyword.setHorizontalHeaderItem(1, item)
        self.tbl_keyword.horizontalHeader().setStretchLastSection(False)
        self.tbl_keyword.verticalHeader().setStretchLastSection(False)
        
        self.group2 = QtWidgets.QGroupBox(self.tab_anal)
        self.group2.setGeometry(QtCore.QRect(280, 10, 341, 148))
        self.group2.setObjectName("group2")
        
        # LDA 분석 파일 테이블
        self.tbl_lda_file = QtWidgets.QTableWidget(self.group2)
        self.tbl_lda_file.setGeometry(QtCore.QRect(5, 19, 331, 121))
        self.tbl_lda_file.setObjectName("tbl_lda_file")
        self.tbl_lda_file.setColumnCount(2)
        self.tbl_lda_file.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_lda_file.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_lda_file.setHorizontalHeaderItem(1, item)
        self.tbl_lda_file.horizontalHeader().setStretchLastSection(False)
        self.tbl_lda_file.verticalHeader().setStretchLastSection(False)
        
        self.group3 = QtWidgets.QGroupBox(self.tab_content)
        self.group3.setGeometry(QtCore.QRect(8, 10, 1284, 151))
        self.group3.setObjectName("group3")
        
        # 뉴스 내용 테이블
        self.tbl_contents = QtWidgets.QTableWidget(self.group3)
        self.tbl_contents.setGeometry(QtCore.QRect(8, 20, 631, 121))
        self.tbl_contents.setObjectName("tbl_contents")
        self.tbl_contents.setColumnCount(1)
        self.tbl_contents.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_contents.setHorizontalHeaderItem(0, item)
        self.tbl_contents.horizontalHeader().setStretchLastSection(True)
        self.tbl_contents.verticalHeader().setStretchLastSection(False)
        
        # 뉴스 상세 내용
        self.tbl_sel_content = QtWidgets.QTextEdit(self.group3)
        self.tbl_sel_content.setGeometry(QtCore.QRect(652, 19, 621, 121))
        self.tbl_sel_content.setObjectName("tbl_sel_content")
        
        self.group4 = QtWidgets.QGroupBox(Dialog)
        self.group4.setGeometry(QtCore.QRect(10, 210, 1306, 651))
        self.group4.setObjectName("group4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # 정렬 가능
        self.tbl_keyword.setSortingEnabled(True)
        self.tbl_contents.setSortingEnabled(True)
        self.tbl_lda_file.setSortingEnabled(True)

        # 테이블 사이즈 조정
        self.tbl_keyword.horizontalHeader().setSectionResizeMode(True)
        self.tbl_contents.horizontalHeader().setSectionResizeMode(True)
        self.tbl_lda_file.horizontalHeader().setSectionResizeMode(True)
        self.tbl_keyword.verticalHeader().setDefaultSectionSize(10)
        self.tbl_contents.verticalHeader().setDefaultSectionSize(10)
        self.tbl_lda_file.verticalHeader().setDefaultSectionSize(10)

        # 테이블 수정 금지
        self.tbl_keyword.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_contents.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_lda_file.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 테이블 스타일 적용
        self.tbl_keyword.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")
        self.tbl_contents.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")
        self.tbl_lda_file.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        # LDA 출력
        self.m_output = QtWebEngineWidgets.QWebEngineView()
        view = QtWidgets.QVBoxLayout(self.group4)
        view.addWidget(self.m_output)
        view.setStretch(200, 551)
        
        # 데이터 테이블, LDA 파일 테이블 출력
        self.show_files()

        self.btn_search.clicked.connect(self.get_lda) # LDA 분석
        self.tbl_lda_file.cellClicked.connect(self.get_content) # 내용 테이블 출력
        self.tbl_contents.cellClicked.connect(self.show_details) # 상세 내용 출력


    # 상세 내용 출력
    def show_details(self, row, column):
        self.tbl_sel_content.setText(self.tbl_contents.item(row, column).text())


    # 내용 테이블 출력
    def get_content(self, row, column):
        self.tbl_sel_content.setText("")
        self.tbl_contents.scrollToTop() # 테이블 맨 위로 이동

        file_path = FilePathClass()
        path = file_path.get_raw_use_path()
        s_path = file_path.get_result_path() + "LDA\\"

        if file_path.is_path_exist_check(s_path) is False:
            error_event()

        if file_path.is_path_exist_check(path) is False:
           error_event()

        data_all_list = os.listdir(path)

        part = self.tbl_lda_file.item(row, 0).text()
        keyword = self.tbl_lda_file.item(row, 1).text()

        for i in range(0, len(data_all_list)):
            filename = data_all_list[i].split('_')
            if len(filename) >= 3:
                if (data_all_list[i][-3:] == 'csv') & ((filename[0] == part) | (part in filename[1])) & (filename[2][:-4] == keyword):
                    if part == '뉴스':
                        df = pd.read_csv(path + "\\" + data_all_list[i])
                        self.tbl_contents.setRowCount(len(df['본문']))
                        for i in range(self.tbl_contents.rowCount()):
                            self.tbl_contents.setItem(i, 0, QTableWidgetItem(df['본문'][i]))
                    else:
                        df = pd.read_csv(path + "\\" + data_all_list[i])
                        self.tbl_contents.setRowCount(len(df['content']))
                        for i in range(self.tbl_contents.rowCount()):
                            self.tbl_contents.setItem(i, 0, QTableWidgetItem(df['content'][i]))

        self.load_lda_html(s_path + 'lda_result_{0}_{1}.html'.format(
            self.tbl_lda_file.item(self.tbl_lda_file.currentRow(), 0).text(),
            self.tbl_lda_file.item(self.tbl_lda_file.currentRow(), 1).text()))


    # LDA 분석
    def get_lda(self):
        file_path = FilePathClass()
        s_path = file_path.get_result_path() + "LDA\\"

        if file_path.is_path_exist_check(s_path) is False:
            error_event()
        
        # LDA 분석
        lda_model_proc(self.tbl_keyword.item(self.tbl_keyword.currentRow(), 0).text(),
                       self.tbl_keyword.item(self.tbl_keyword.currentRow(), 1).text())
        
        # 테이블 출력
        self.show_files()
        
        # LDA html 파일 가져오기
        self.load_lda_html(s_path + 'lda_result_{0}_{1}.html'.format(
            self.tbl_keyword.item(self.tbl_keyword.currentRow(), 0).text(),
            self.tbl_keyword.item(self.tbl_keyword.currentRow(), 1).text()))


    # 데이터 테이블, LDA 파일 테이블 출력
    def show_files(self):
        file_path = FilePathClass()
        path = file_path.get_raw_use_path() # 데이터 경로
        s_path = file_path.get_result_path() + "LDA\\" # LDA 파일 경로

        if file_path.is_path_exist_check(path) is False:
           error_event()
        if file_path.is_path_exist_check(s_path) is False:
            error_event()

        data_all_list = os.listdir(path)
        data_saved_list = os.listdir(s_path)

        data_list = [] # 데이터 리스트
        saved_list = [] # LDA 파일 리스트
        
        # 뉴스, 유사사례 데이터만 리스트에 저장
        for i in range(0, len(data_all_list)):
            filename = data_all_list[i].split('_')
            if (data_all_list[i][-3:] == 'csv') & ((filename[0] == '뉴스') | (filename[1] == '유사사례정보')):
                data_list.append(data_all_list[i])
        # self.tbl_keyword.setRowCount(len(data_list))
        
        # 테이블에 데이터 목록 출력
        for i in range(len(data_list)):
            self.tbl_keyword.insertRow(i)
            dataname = data_list[i].split('_')
            if dataname[1] == '유사사례정보':
                self.tbl_keyword.setItem(i, 0, QTableWidgetItem('유사사례'))
            else:
                self.tbl_keyword.setItem(i, 0, QTableWidgetItem(dataname[0]))
            self.tbl_keyword.setItem(i, 1, QTableWidgetItem(dataname[2][:-4]))


        for i in range(len(data_saved_list)):
            if data_saved_list[i][-4:] == 'html':
                saved_list.append(data_saved_list[i])
        # self.tbl_lda_file.setRowCount(len(saved_list))
        
        # 테이블에 LDA 파일 목록 출력
        for i in range(len(saved_list)):
            self.tbl_lda_file.insertRow(i)
            savedname = data_saved_list[i].split('_')
            self.tbl_lda_file.setItem(i, 0, QTableWidgetItem(savedname[2]))
            self.tbl_lda_file.setItem(i, 1, QTableWidgetItem(savedname[3][:-5]))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LDA 분석"))
        self.group1.setTitle(_translate("Dialog", " [ LDA 키워드 분석 ] "))
        self.btn_search.setText(_translate("Dialog", "분석"))
        item = self.tbl_keyword.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "분야"))
        item = self.tbl_keyword.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "키워드"))
        self.group2.setTitle(_translate("Dialog", " [ LDA 분석 결과 목록 ] "))
        item = self.tbl_lda_file.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "분야"))
        item = self.tbl_lda_file.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "키워드"))
        self.group3.setTitle(_translate("Dialog", " [ LDA 분석 내용 ] "))
        item = self.tbl_contents.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "내용"))
        self.group4.setTitle(_translate("Dialog", " [ LDA 분석시각화 ] "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_anal), _translate("Dialog", "분석"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_content), _translate("Dialog", "내용"))


    # LDA HTML 가져오기
    def load_lda_html(self, fileName):
        with open(fileName, 'r') as f:
            html = f.read()
        self.m_output.setHtml(html)


def error_event(self):
    QMessageBox.about(self, 'Error', 'file path not fount!!')


if __name__ == "__main__":

    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

    sys.exit(app.exec_())

