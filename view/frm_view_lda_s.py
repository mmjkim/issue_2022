# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_view_lda_s.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets

from common.function import funcC3Chart
from common.function.funcCommon import *
from common.function.funcDataControl import dfToString


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1324, 868)
        self.group1 = QtWidgets.QGroupBox(Dialog)
        self.group1.setGeometry(QtCore.QRect(7, 10, 151, 191))
        self.group1.setObjectName("group1")
        self.btn_search = QtWidgets.QPushButton(self.group1)
        self.btn_search.setGeometry(QtCore.QRect(59, 22, 79, 23))
        self.btn_search.setObjectName("btn_search")
        self.tbl_keyword = QtWidgets.QTableWidget(self.group1)
        self.tbl_keyword.setGeometry(QtCore.QRect(10, 50, 131, 131))
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
        self.group2.setGeometry(QtCore.QRect(170, 10, 211, 191))
        self.group2.setObjectName("group2")
        self.tbl_lda_file = QtWidgets.QTableWidget(self.group2)
        self.tbl_lda_file.setGeometry(QtCore.QRect(10, 20, 191, 161))
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
        self.group3.setGeometry(QtCore.QRect(390, 10, 621, 191))
        self.group3.setObjectName("group3")
        self.tbl_contents = QtWidgets.QTableWidget(self.group3)
        self.tbl_contents.setGeometry(QtCore.QRect(10, 20, 601, 91))
        self.tbl_contents.setObjectName("tbl_contents")
        self.tbl_contents.setColumnCount(1)
        self.tbl_contents.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_contents.setHorizontalHeaderItem(0, item)
        self.tbl_contents.horizontalHeader().setStretchLastSection(False)
        self.tbl_contents.verticalHeader().setStretchLastSection(False)
        self.tbl_sel_content = QtWidgets.QTextEdit(self.group3)
        self.tbl_sel_content.setGeometry(QtCore.QRect(10, 120, 601, 51))
        self.tbl_sel_content.setObjectName("tbl_sel_content")
        self.group4 = QtWidgets.QGroupBox(Dialog)
        self.group4.setGeometry(QtCore.QRect(10, 210, 1300, 661))
        self.group4.setObjectName("group4")
        self.retranslateUi(Dialog)

        #QtCore.QMetaObject.connectSlotsByName(Dialog)
        #self.htmlView = QtWidgets.QTextBrowser(self)

        self.m_output = QtWebEngineWidgets.QWebEngineView()

        file_name = 'D:\\issue_2022\\data\\03_결과데이터\\LDA\\lda_result_유사사례_이태원_ 할로인.html'
        #file_name = 'D:\\issue_2022\\view\\chart_sample.html'
        self.load_lda_html(file_name)
        view = QtWidgets.QVBoxLayout(self.group4)
        view.addWidget(self.m_output)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.group1.setTitle(_translate("Dialog", " [ LDA 키워드 분석 ] "))
        self.btn_search.setText(_translate("Dialog", "분석"))
        item = self.tbl_keyword.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "선택"))
        item = self.tbl_keyword.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "키워드"))
        self.group2.setTitle(_translate("Dialog", " [ LDA 분석결과 목록 ] "))
        item = self.tbl_lda_file.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "선택"))
        item = self.tbl_lda_file.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "키워드"))
        self.group3.setTitle(_translate("Dialog", " [ LDA 분석결과 ] "))
        item = self.tbl_contents.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "내용"))
        self.group4.setTitle(_translate("Dialog", " [ LDA 분석시각화 ] "))


    def load_lda_html(self, fileName):

        with open(fileName, 'r') as f:
            html = f.read()
        self.m_output.setHtml(html)

        # data = dfToString()
        # print(type(data))
        # print("data:", data)
        # html = funcC3Chart.c3chart_html_write(data)
        # temp = "zoom:{enabled: false}"
        # self.m_output.setHtml(html.replace(temp, "zoom: {enabled: true}"))
        # loadCSS(self.m_output, "c3Chart/c3.css", "script1")

        #print(html)


def loadCSS(view, path, name):
    path = QtCore.QFile(path)
    if not path.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
        return
    css = path.readAll().data().decode("utf-8")
    SCRIPT = """
    (function() {
    css = document.createElement('style');
    css.type = 'text/css';
    css.id = "%s";
    document.head.appendChild(css);
    css.innerText = `%s`;
    })()
    """ % (name, css)

    script = QtWebEngineWidgets.QWebEngineScript()
    view.page().runJavaScript(SCRIPT, QtWebEngineWidgets.QWebEngineScript.ApplicationWorld)
    script.setName(name)
    script.setSourceCode(SCRIPT)
    script.setInjectionPoint(QtWebEngineWidgets.QWebEngineScript.DocumentReady)
    script.setRunsOnSubFrames(True)
    script.setWorldId(QtWebEngineWidgets.QWebEngineScript.ApplicationWorld)
    view.page().scripts().insert(script)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

