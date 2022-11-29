import os
import sys
import warnings
warnings.filterwarnings(action='ignore')

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
# from PyQt5.QtWebKit import *
# from PyQt5.QtWebKitWidgets import *
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QAbstractItemView, QCheckBox, QWidget, QHBoxLayout

from common.config.filepassclass import FilePathClass
from source.anal_contents_lda import *


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1324, 868)
        self.group1 = QtWidgets.QGroupBox(Dialog)
        self.group1.setGeometry(QtCore.QRect(7, 10, 251, 191))
        self.group1.setObjectName("group1")
        self.btn_search = QtWidgets.QPushButton(self.group1)
        self.btn_search.setGeometry(QtCore.QRect(160, 22, 79, 23))
        self.btn_search.setObjectName("btn_search")
        self.tbl_keyword = QtWidgets.QTableWidget(self.group1)
        self.tbl_keyword.setGeometry(QtCore.QRect(10, 50, 231, 131))
        self.tbl_keyword.setObjectName("tbl_keyword")
        self.tbl_keyword.setColumnCount(2)
        self.tbl_keyword.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_keyword.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_keyword.setHorizontalHeaderItem(1, item)
        self.tbl_keyword.horizontalHeader().setStretchLastSection(False)
        self.tbl_keyword.verticalHeader().setStretchLastSection(False)
        self.group2 = QtWidgets.QGroupBox(Dialog)
        self.group2.setGeometry(QtCore.QRect(270, 10, 241, 191))
        self.group2.setObjectName("group2")
        self.tbl_lda_file = QtWidgets.QTableWidget(self.group2)
        self.tbl_lda_file.setGeometry(QtCore.QRect(10, 20, 231, 161))
        self.tbl_lda_file.setObjectName("tbl_lda_file")
        self.tbl_lda_file.setColumnCount(2)
        self.tbl_lda_file.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_lda_file.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_lda_file.setHorizontalHeaderItem(1, item)
        self.tbl_lda_file.horizontalHeader().setStretchLastSection(False)
        self.tbl_lda_file.verticalHeader().setStretchLastSection(False)
        self.group3 = QtWidgets.QGroupBox(Dialog)
        self.group3.setGeometry(QtCore.QRect(520, 10, 791, 191))
        self.group3.setObjectName("group3")
        self.tbl_contents = QtWidgets.QTableWidget(self.group3)
        self.tbl_contents.setGeometry(QtCore.QRect(10, 20, 771, 91))
        self.tbl_contents.setObjectName("tbl_contents")
        self.tbl_contents.setColumnCount(1)
        self.tbl_contents.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_contents.setHorizontalHeaderItem(0, item)
        self.tbl_contents.horizontalHeader().setStretchLastSection(True)
        self.tbl_contents.verticalHeader().setStretchLastSection(False)
        self.tbl_sel_content = QtWidgets.QTextEdit(self.group3)
        self.tbl_sel_content.setGeometry(QtCore.QRect(10, 120, 771, 60))
        self.tbl_sel_content.setObjectName("tbl_sel_content")
        self.group4 = QtWidgets.QGroupBox(Dialog)
        self.group4.setGeometry(QtCore.QRect(10, 210, 1311, 651))
        self.group4.setObjectName("group4")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.tbl_keyword.setSortingEnabled(True)
        self.tbl_contents.setSortingEnabled(True)
        self.tbl_lda_file.setSortingEnabled(True)

        self.tbl_keyword.horizontalHeader().setSectionResizeMode(True)
        self.tbl_contents.horizontalHeader().setSectionResizeMode(True)
        self.tbl_lda_file.horizontalHeader().setSectionResizeMode(True)

        self.tbl_keyword.verticalHeader().setDefaultSectionSize(10)
        self.tbl_contents.verticalHeader().setDefaultSectionSize(10)
        self.tbl_lda_file.verticalHeader().setDefaultSectionSize(10)

        self.tbl_keyword.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_contents.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_lda_file.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tbl_keyword.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")
        self.tbl_contents.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")
        self.tbl_lda_file.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.m_output = QtWebEngineWidgets.QWebEngineView()
        view = QtWidgets.QVBoxLayout(self.group4)
        view.addWidget(self.m_output)
        view.setStretch(200, 551)

        self.show_files()

        self.btn_search.clicked.connect(self.get_lda)
        self.tbl_lda_file.cellClicked.connect(self.get_content)
        self.tbl_contents.cellClicked.connect(self.show_details)


    def show_details(self, row, column):
        self.tbl_sel_content.setText(self.tbl_contents.item(row, column).text())


    def get_content(self, row, column):
        self.tbl_sel_content.setText("")
        self.tbl_contents.scrollToTop()

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


    def get_lda(self):
        file_path = FilePathClass()
        s_path = file_path.get_result_path() + "LDA\\"

        if file_path.is_path_exist_check(s_path) is False:
            error_event()

        lda_model_proc(self.tbl_keyword.item(self.tbl_keyword.currentRow(), 0).text(),
                       self.tbl_keyword.item(self.tbl_keyword.currentRow(), 1).text())

        self.show_files()
        self.load_lda_html(s_path + 'lda_result_{0}_{1}.html'.format(
            self.tbl_keyword.item(self.tbl_keyword.currentRow(), 0).text(),
            self.tbl_keyword.item(self.tbl_keyword.currentRow(), 1).text()))


    def show_files(self):
        file_path = FilePathClass()
        path = file_path.get_raw_use_path()
        s_path = file_path.get_result_path() + "LDA\\"

        if file_path.is_path_exist_check(path) is False:
           error_event()
        if file_path.is_path_exist_check(s_path) is False:
            error_event()

        data_all_list = os.listdir(path)
        data_saved_list = os.listdir(s_path)

        data_list = []
        saved_list = []

        for i in range(0, len(data_all_list)):
            filename = data_all_list[i].split('_')
            if (data_all_list[i][-3:] == 'csv') & ((filename[0] == '뉴스') | (filename[1] == '유사사례정보')):
                data_list.append(data_all_list[i])
        self.tbl_keyword.setRowCount(len(data_list))
        for i in range(len(data_list)):
            dataname = data_list[i].split('_')
            if dataname[1] == '유사사례정보':
                self.tbl_keyword.setItem(i, 0, QTableWidgetItem('유사사례'))
            else:
                self.tbl_keyword.setItem(i, 0, QTableWidgetItem(dataname[0]))
            self.tbl_keyword.setItem(i, 1, QTableWidgetItem(dataname[2][:-4]))


        for i in range(len(data_saved_list)):
            if data_saved_list[i][-4:] == 'html':
                saved_list.append(data_saved_list[i])
        self.tbl_lda_file.setRowCount(len(saved_list))
        for i in range(len(saved_list)):
            savedname = data_saved_list[i].split('_')
            self.tbl_lda_file.setItem(i, 0, QTableWidgetItem(savedname[2]))
            self.tbl_lda_file.setItem(i, 1, QTableWidgetItem(savedname[3][:-5]))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LDA 분석"))
        self.group1.setTitle(_translate("Dialog", " [ LDA 키워드 분석 ] "))
        self.btn_search.setText(_translate("Dialog", "분석"))
        # item = self.tbl_keyword.horizontalHeaderItem(0)
        # item.setText(_translate("Dialog", "선택"))
        item = self.tbl_keyword.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "분야"))
        item = self.tbl_keyword.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "키워드"))
        self.group2.setTitle(_translate("Dialog", " [ LDA 분석 결과 목록 ] "))
        # item = self.tbl_lda_file.horizontalHeaderItem(0)
        # item.setText(_translate("Dialog", "선택"))
        item = self.tbl_lda_file.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "분야"))
        item = self.tbl_lda_file.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "키워드"))
        self.group3.setTitle(_translate("Dialog", " [ LDA 분석 내용 ] "))
        item = self.tbl_contents.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "내용"))
        self.group4.setTitle(_translate("Dialog", " [ LDA 분석 결과 시각화 ] "))


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

