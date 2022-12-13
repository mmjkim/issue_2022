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

import fnmatch
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

        # 크롤링 데이터 그룹
        self.group_crawl = QtWidgets.QGroupBox(self.tab_anal)
        self.group_crawl.setGeometry(QtCore.QRect(10, 10, 251, 148))
        self.group_crawl.setObjectName("group_crawl")
        # 크롤링 데이터 분석 버튼
        self.btn_search_crawl = QtWidgets.QPushButton(self.group_crawl)
        self.btn_search_crawl.setGeometry(QtCore.QRect(162, 15, 77, 21))
        self.btn_search_crawl.setObjectName("btn_search")
        # 크롤링 데이터 테이블
        self.tbl_keyword_crawl = QtWidgets.QListWidget(self.group_crawl)
        self.tbl_keyword_crawl.setGeometry(QtCore.QRect(5, 40, 241, 101))
        self.tbl_keyword_crawl.setObjectName("tbl_keyword")
        self.tbl_keyword_crawl.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        # 유사사례 데이터 테이블
        self.group_simil = QtWidgets.QGroupBox(self.tab_anal)
        self.group_simil.setGeometry(QtCore.QRect(280, 10, 251, 148))
        self.group_simil.setObjectName("group_simil")
        # 유사사례 데이터 분석 버튼
        self.btn_search_simil = QtWidgets.QPushButton(self.group_simil)
        self.btn_search_simil.setGeometry(QtCore.QRect(162, 15, 77, 21))
        self.btn_search_simil.setObjectName("btn_search_simil")
        # 유사사례 데이터 테이블
        self.tbl_keyword_simil = QtWidgets.QListWidget(self.group_simil)
        self.tbl_keyword_simil.setGeometry(QtCore.QRect(5, 40, 241, 101))
        self.tbl_keyword_simil.setObjectName("tbl_keyword_simil")
        self.tbl_keyword_simil.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        # LDA 분석 파일 그룹
        self.group2 = QtWidgets.QGroupBox(self.tab_anal)
        self.group2.setGeometry(QtCore.QRect(560, 10, 341, 148))
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

        # 분석 내용 테이블
        self.tbl_contents = QtWidgets.QTableWidget(self.group3)
        self.tbl_contents.setGeometry(QtCore.QRect(8, 20, 631, 121))
        self.tbl_contents.setObjectName("tbl_contents")
        self.tbl_contents.setColumnCount(1)
        self.tbl_contents.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_contents.setHorizontalHeaderItem(0, item)
        self.tbl_contents.horizontalHeader().setStretchLastSection(True)
        self.tbl_contents.verticalHeader().setStretchLastSection(False)

        # 분석 내용 상세
        self.tbl_sel_content = QtWidgets.QTextEdit(self.group3)
        self.tbl_sel_content.setGeometry(QtCore.QRect(652, 19, 623, 121))
        self.tbl_sel_content.setObjectName("tbl_sel_content")

        self.group4 = QtWidgets.QGroupBox(Dialog)
        self.group4.setGeometry(QtCore.QRect(10, 210, 1306, 651))
        self.group4.setObjectName("group4")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # 정렬 가능
        self.tbl_contents.setSortingEnabled(True)
        self.tbl_lda_file.setSortingEnabled(True)

        # 테이블 사이즈 조정
        self.tbl_contents.horizontalHeader().setSectionResizeMode(True)
        self.tbl_lda_file.horizontalHeader().setSectionResizeMode(True)
        self.tbl_contents.verticalHeader().setDefaultSectionSize(10)
        self.tbl_lda_file.verticalHeader().setDefaultSectionSize(10)

        # 테이블 수정 금지
        self.tbl_contents.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_lda_file.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 테이블 스타일 적용
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

        self.btn_search_crawl.clicked.connect(lambda: self.get_lda('크롤링', self.tbl_keyword_crawl))  # LDA 분석
        self.btn_search_simil.clicked.connect(lambda: self.get_lda('유사사례정보', self.tbl_keyword_simil))  # LDA 분석
        self.tbl_lda_file.cellClicked.connect(self.show_content)  # 내용 테이블 출력
        self.tbl_contents.cellClicked.connect(self.show_details)  # 상세 내용 출력



    # 상세 내용 출력
    def show_details(self, row, column):
        self.tbl_sel_content.setText(self.tbl_contents.item(row, column).text())


    # 내용 테이블 조회
    def show_content(self, row, column):
        # 분석결과 리스트에서 선택된 내용 조회
        self.tbl_sel_content.setText("") # 테이블 초기화
        self.tbl_contents.scrollToTop() # 테이블 맨 위로

        data_type = self.tbl_lda_file.item(row, 0).text()
        keyword = self.tbl_lda_file.item(row, 1).text()

        df_data = self.get_content(data_type, keyword)

        if df_data.empty == False:
            self.tbl_contents.setRowCount(len(df_data))

            for i in range(len(df_data)):
                self.tbl_contents.setItem(i, 0, QTableWidgetItem(df_data['content'][i]))


    # 내용 조회
    def get_content(self, dataType, keyword):

        file_path = FilePathClass()
        path = file_path.get_raw_use_path()

        if dataType == '크롤링':
            file_name = "뉴스_크롤링_*.csv"
        else:
            file_name = "민원_유사사례정보_*.csv"

        if file_path.is_path_exist_check(path) is False:
            error_event()

        # 분석 결과 파일 리스트
        all_file = os.listdir(path)
        csv_all_list = [file for file in all_file if fnmatch.fnmatch(file, file_name)]  # os.listdir(path_file)

        keyword_list = keyword.split('_')
        df_data = pd.DataFrame()

        # 분석 키워드 정보(키워드가 여러개 일 수 있어서 prefix 파일명을 제외한 모든 키워드를 보여줌, '_'로 구분)
        for i in range(len(keyword_list)):

            temp_list = [file for file in csv_all_list if fnmatch.fnmatch(file, file_name.replace('*', keyword_list[i]))]

            for j in range(len(temp_list)):
                try:
                    df = pd.read_csv(path + "\\" + temp_list[j])
                    if df.empty == False:
                       df_data = pd.concat([df_data, df], ignore_index=True)
                except pd.errors.EmptyDataError:
                    continue

        if df_data.empty == False:
            if dataType == '크롤링':
                df_data.rename(columns={'본문': 'content'}, inplace=True)

        # lda 시각화 출력
        self.load_lda_html(file_path.get_result_path() + "LDA\\" + 'lda_result_{0}_{1}.html'.format(dataType, keyword))

        return df_data


    # 민원 내용 조회
    def get_content_complaint(self, dataType, keyword):
        file_path = FilePathClass()
        path = file_path.get_raw_use_path()
        if file_path.is_path_exist_check(path) is False:
            error_event()
        return ""


    # LDA 분석
    def get_lda(self, part, list):
        anal_list = []
        for i in range(len(list.selectedItems())):
            anal_list.append(str(list.selectedItems()[i].text().replace(part+'_', '')))
        anal_str = ','.join(anal_list)

        file_path = FilePathClass()
        s_path = file_path.get_result_path() + "LDA\\"

        if file_path.is_path_exist_check(s_path) is False:
            error_event()

        # LDA 분석
        lda_model_proc(part, anal_str)

        # 테이블 출력
        self.show_files()

        # LDA html 파일 가져오기
        self.load_lda_html(s_path + 'lda_result_{0}_{1}.html'.format(part, anal_str.replace(',', '_')))


    # 데이터 테이블, LDA 파일 테이블 출력
    def show_files(self):
        # 키워드 기준 수집된 csv 파일 조회
        self.get_csv_keyword()
        # LDA 분석 결과 html 파일 조회
        self.get_html_lda()


    # LDA 분석 결과 html 파일 조회
    def get_html_lda(self):

        file_path = FilePathClass()
        s_path = file_path.get_result_path() + "LDA\\"  # LDA 파일 경로

        if file_path.is_path_exist_check(s_path) is False:
            error_event()

        # 분석 결과 파일 리스트
        html_all_files = os.listdir(s_path)
        # 선택 폴더에서 특정 파일만 가져오기(html 파일만 가져오기)
        html_saved_list = [file for file in html_all_files if file.endswith(".html")]
        html_list = []  # LDA 파일 리스트

        # 분석 결과 파일 목록 (html)
        self.tbl_lda_file.setRowCount(len(html_saved_list))
        for i in range(len(html_saved_list)):
            html_list.append(html_saved_list[i])
        self.tbl_lda_file.setRowCount(len(html_list))
        for i in range(len(html_list)):
            savedname = html_list[i].replace('lda_result_', '').replace('.html', '').split('_')
            self.tbl_lda_file.setItem(i, 0, QTableWidgetItem(savedname[0]))

            # 분석 키워드 정보(키워드가 여러개 일 수 있어서 prefix 파일명을 제외한 모든 키워드를 보여줌, '_'로 구분)
            temp = self.get_keyword(savedname, 1)
            self.tbl_lda_file.setItem(i, 1, QTableWidgetItem(temp))


    def get_csv_keyword(self):
        file_path = FilePathClass()
        path = file_path.get_raw_use_path()  # 데이터 경로

        if file_path.is_path_exist_check(path) is False:
            error_event()

        # 키워드 수집 마트 리스트 (csv 파일만 가져오기)
        csv_all_list = os.listdir(path)
        csv_saved_list = [file for file in csv_all_list if file.endswith(".csv")]

        crawl_list = []  # 크롤링 데이터 리스트
        simil_list = []  # 유사사례 데이터 리스트

        # 크롤링, 유사사례 데이터만 리스트에 저장(csv)
        for i in range(0, len(csv_saved_list)):
            filename = csv_saved_list[i].split('_')
            if filename[1] == '크롤링':
                crawl_list.append(csv_saved_list[i])
            elif filename[1] == '유사사례정보':
                simil_list.append(csv_saved_list[i])

        # 테이블에 데이터 목록 출력
        for i in range(len(crawl_list)):
            savedname = crawl_list[i].replace('.csv', '').split('_')
            temp = self.get_keyword(savedname, 2)  # 분석 키워드
            self.tbl_keyword_crawl.addItem(savedname[1] + "_" + temp)
        for i in range(len(simil_list)):
            savedname = simil_list[i].replace('.csv', '').split('_')
            temp = self.get_keyword(savedname, 2)  # 분석 키워드
            self.tbl_keyword_simil.addItem(savedname[1] + "_" + temp)


    # 분석 키워드 정보(키워드가 여러개 일 수 있어서 prefix 파일명을 제외한 모든 키워드를 보여줌, '_'로 구분)
    def get_keyword(self, savedname, startNum):
        temp = ""
        for j in range(startNum, len(savedname)):
            if temp == "":
                # temp += savedname[j].replace(" ", "")
                temp += savedname[j]
            else:
                # temp += "_" + savedname[j].replace(" ", "")
                temp += "_" + savedname[j]
        return temp


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LDA 분석"))
        self.group_crawl.setTitle(_translate("Dialog", " [ LDA 키워드 분석 - 크롤링 ] "))
        self.btn_search_crawl.setText(_translate("Dialog", "분석"))
        self.group_simil.setTitle(_translate("Dialog", " [ LDA 키워드 분석 - 유사사례 ] "))
        self.btn_search_simil.setText(_translate("Dialog", "분석"))
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


def error_event():
    msgbox = QMessageBox()
    msgbox.setWindowTitle("error")
    msgbox.setText('file path not fount!!')

    msgbox.exec_()

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

