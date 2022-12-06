import os
import warnings
from datetime import datetime

warnings.filterwarnings(action='ignore')

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from common.config.filepassclass import FilePathClass
from source.get_chart_data import *
from common.function.funcC3Chart import c3chart_html_write as c3Chart


class Ui_frmViewNaver(object):
    def setupUi(self, frmViewNaver):
        frmViewNaver.setObjectName("frmViewNaver")
        frmViewNaver.resize(1024, 968)
        frmViewNaver.setMaximumSize(1024, 968)
        self.group1 = QtWidgets.QGroupBox(frmViewNaver)
        self.group1.setGeometry(QtCore.QRect(11, 11, 1001, 311))
        self.group1.setObjectName("group1")
        self.label2 = QtWidgets.QLabel(self.group1)
        self.label2.setGeometry(QtCore.QRect(372, 30, 16, 17))
        self.label2.setObjectName("label2")
        self.label = QtWidgets.QLabel(self.group1)
        self.label.setGeometry(QtCore.QRect(170, 29, 54, 15))
        self.label.setObjectName("label")
        self.sel_yy_end = QtWidgets.QComboBox(self.group1)
        self.sel_yy_end.setGeometry(QtCore.QRect(389, 25, 67, 23))
        self.sel_yy_end.setObjectName("sel_yy_end")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_mm_start = QtWidgets.QComboBox(self.group1)
        self.sel_mm_start.setGeometry(QtCore.QRect(314, 25, 51, 23))
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
        self.sel_yy_start = QtWidgets.QComboBox(self.group1)
        self.sel_yy_start.setGeometry(QtCore.QRect(237, 25, 67, 23))
        self.sel_yy_start.setObjectName("sel_yy_start")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_mm_end = QtWidgets.QComboBox(self.group1)
        self.sel_mm_end.setGeometry(QtCore.QRect(465, 25, 51, 23))
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
        self.btn_search = QtWidgets.QPushButton(self.group1)
        self.btn_search.setGeometry(QtCore.QRect(890, 23, 79, 24))
        self.btn_search.setObjectName("btn_search")
        self.tbl_naver = QtWidgets.QTableWidget(self.group1)
        self.tbl_naver.setGeometry(QtCore.QRect(160, 57, 831, 241))
        self.tbl_naver.setObjectName("tbl_naver")
        self.tbl_naver.setColumnCount(0)
        self.tbl_naver.setRowCount(0)
        self.tbl_naver.horizontalHeader().setStretchLastSection(False)
        self.tbl_naver.verticalHeader().setDefaultSectionSize(25)
        self.tbl_naver.verticalHeader().setStretchLastSection(False)
        self.listWidget = QtWidgets.QListWidget(self.group1)
        self.listWidget.setGeometry(QtCore.QRect(10, 57, 141, 241))
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName("listWidget")
        self.label4 = QtWidgets.QLabel(self.group1)
        self.label4.setGeometry(QtCore.QRect(18, 29, 91, 18))
        self.label4.setObjectName("label4")
        self.group2 = QtWidgets.QGroupBox(frmViewNaver)
        self.group2.setGeometry(QtCore.QRect(10, 330, 1001, 631))
        self.group2.setObjectName("group2")
        self.rdo_line = QtWidgets.QRadioButton(self.group2)
        self.rdo_line.setGeometry(QtCore.QRect(20, 26, 86, 16))
        self.rdo_line.setObjectName("rdo_line")
        self.rdo_line.setChecked(True)
        self.rdo_bar = QtWidgets.QRadioButton(self.group2)
        self.rdo_bar.setGeometry(QtCore.QRect(80, 26, 86, 16))
        self.rdo_bar.setObjectName("rdo_bar")
        self.rdo_area = QtWidgets.QRadioButton(self.group2)
        self.rdo_area.setGeometry(QtCore.QRect(138, 26, 86, 16))
        self.rdo_area.setObjectName("rdo_area")
        # self.label3 = QtWidgets.QLabel(self.group2)
        # self.label3.setGeometry(QtCore.QRect(220, 26, 51, 16))
        # self.label3.setObjectName("label3")
        # self.txt_top_n = QtWidgets.QTextEdit(self.group2)
        # self.txt_top_n.setGeometry(QtCore.QRect(270, 20, 61, 24))
        # self.txt_top_n.setAcceptDrops(True)
        # self.txt_top_n.setToolTip("")
        # self.txt_top_n.setInputMethodHints(QtCore.Qt.ImhNone)
        # self.txt_top_n.setObjectName("txt_top_n")
        self.btn_print = QtWidgets.QPushButton(self.group2)
        self.btn_print.setGeometry(QtCore.QRect(890, 23, 79, 24))
        self.btn_print.setObjectName("btn_print")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.group2)
        self.webEngineView.setGeometry(QtCore.QRect(10, 50, 981, 571))
        # self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")

        self.retranslateUi(frmViewNaver)
        QtCore.QMetaObject.connectSlotsByName(frmViewNaver)

        self.show_list()
        self.btn_search.clicked.connect(self.show_table)
        self.btn_print.clicked.connect(self.show_graph)


    def show_graph(self):
        df = self.show_table()
        if self.rdo_line.isChecked():
            type = 'line'
        elif self.rdo_bar.isChecked():
            type = 'bar'
        elif self.rdo_area.isChecked():
            type = 'area'
        html = c3Chart(df, type)
        temp = "zoom:{enabled: false}"
        self.webEngineView.setHtml(html.replace(temp, "zoom: {enabled: true}"))
        loadCSS(self.webEngineView, "c3Chart/c3.css", "script1")


    def show_list(self):
        file_path = FilePathClass()
        path = file_path.get_raw_use_path()
        data_all_list = os.listdir(path)
        data_list = []

        for i in range(len(data_all_list)):
            if (data_all_list[i][-3:] == 'csv') & (data_all_list[i].startswith('네이버')):
                data_list.append(data_all_list[i])

        for i in range(len(data_list)):
            dataname = data_list[i].split('_')
            self.listWidget.addItem(dataname[2][:-4])


    def show_table(self):
        keywords = []
        for i in range(len(self.listWidget.selectedItems())):
            keywords.append(str(self.listWidget.selectedItems()[i].text()))
        words = ','.join(keywords)
        df = get_view_naver_keyword(words, self.sel_yy_start.currentText()+'-'+self.sel_mm_start.currentText()+'-'+'01',
                                    self.sel_yy_end.currentText()+'-'+self.sel_mm_end.currentText()+'-'+'01')
        df = df.sort_values(by=['ymd'])

        self.tbl_naver.setRowCount(len(df))
        self.tbl_naver.setColumnCount(len(df.columns))
        self.tbl_naver.setHorizontalHeaderLabels(df.columns)

        for c in range(len(df.columns)):
            for i in range(len(df)):
                self.tbl_naver.setItem(i, c, QTableWidgetItem(str(df[df.columns[c]][i])))

        return df


    def retranslateUi(self, frmViewNaver):
        _translate = QtCore.QCoreApplication.translate
        frmViewNaver.setWindowTitle(_translate("frmViewNaver", "네이버 키워드 시각화"))
        self.group1.setTitle(_translate("frmViewNaver", " [ 네이버 키워드 시각화 ] "))
        self.label2.setText(_translate("frmViewNaver", "~"))
        self.label.setText(_translate("frmViewNaver", "분석기간: "))
        self.sel_yy_end.setItemText(0, _translate("frmViewNaver", str(datetime.today().year)))
        self.sel_yy_end.setItemText(1, _translate("frmViewNaver", str(datetime.today().year-1)))
        self.sel_yy_end.setItemText(2, _translate("frmViewNaver", str(datetime.today().year-2)))
        self.sel_yy_end.setItemText(3, _translate("frmViewNaver", str(datetime.today().year-3)))
        self.sel_yy_end.setItemText(4, _translate("frmViewNaver", str(datetime.today().year-4)))
        self.sel_yy_end.setItemText(5, _translate("frmViewNaver", str(datetime.today().year-5)))
        self.sel_mm_start.setItemText(0, _translate("frmViewNaver", "01"))
        self.sel_mm_start.setItemText(1, _translate("frmViewNaver", "02"))
        self.sel_mm_start.setItemText(2, _translate("frmViewNaver", "03"))
        self.sel_mm_start.setItemText(3, _translate("frmViewNaver", "04"))
        self.sel_mm_start.setItemText(4, _translate("frmViewNaver", "05"))
        self.sel_mm_start.setItemText(5, _translate("frmViewNaver", "06"))
        self.sel_mm_start.setItemText(6, _translate("frmViewNaver", "07"))
        self.sel_mm_start.setItemText(7, _translate("frmViewNaver", "08"))
        self.sel_mm_start.setItemText(8, _translate("frmViewNaver", "09"))
        self.sel_mm_start.setItemText(9, _translate("frmViewNaver", "10"))
        self.sel_mm_start.setItemText(10, _translate("frmViewNaver", "11"))
        self.sel_mm_start.setItemText(11, _translate("frmViewNaver", "12"))
        self.sel_yy_start.setItemText(0, _translate("frmViewNaver", str(datetime.today().year)))
        self.sel_yy_start.setItemText(1, _translate("frmViewNaver", str(datetime.today().year-1)))
        self.sel_yy_start.setItemText(2, _translate("frmViewNaver", str(datetime.today().year-2)))
        self.sel_yy_start.setItemText(3, _translate("frmViewNaver", str(datetime.today().year-3)))
        self.sel_yy_start.setItemText(4, _translate("frmViewNaver", str(datetime.today().year-4)))
        self.sel_yy_start.setItemText(5, _translate("frmViewNaver", str(datetime.today().year-5)))
        self.sel_mm_end.setItemText(0, _translate("frmViewNaver", "01"))
        self.sel_mm_end.setItemText(1, _translate("frmViewNaver", "02"))
        self.sel_mm_end.setItemText(2, _translate("frmViewNaver", "03"))
        self.sel_mm_end.setItemText(3, _translate("frmViewNaver", "04"))
        self.sel_mm_end.setItemText(4, _translate("frmViewNaver", "05"))
        self.sel_mm_end.setItemText(5, _translate("frmViewNaver", "06"))
        self.sel_mm_end.setItemText(6, _translate("frmViewNaver", "07"))
        self.sel_mm_end.setItemText(7, _translate("frmViewNaver", "08"))
        self.sel_mm_end.setItemText(8, _translate("frmViewNaver", "09"))
        self.sel_mm_end.setItemText(9, _translate("frmViewNaver", "10"))
        self.sel_mm_end.setItemText(10, _translate("frmViewNaver", "11"))
        self.sel_mm_end.setItemText(11, _translate("frmViewNaver", "12"))
        self.sel_yy_start.setCurrentText(str(datetime.today().year))
        self.sel_yy_end.setCurrentText(str(datetime.today().year))
        self.sel_mm_end.setCurrentText(str(datetime.today().month))
        self.btn_search.setText(_translate("frmViewNaver", "조회"))
        self.listWidget.setSortingEnabled(True)
        self.label4.setText(_translate("frmViewNaver", "[ 키워드 목록 ]"))
        self.group2.setTitle(_translate("frmViewNaver", " [ 그래프 ] "))
        self.rdo_line.setText(_translate("frmViewNaver", "Line"))
        self.rdo_bar.setText(_translate("frmViewNaver", "Bar"))
        self.rdo_area.setText(_translate("frmViewNaver", "Area"))
        # self.label3.setText(_translate("frmViewNaver", "Top N :"))
        self.btn_print.setText(_translate("frmViewNaver", "조회"))


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

    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)

    app = QtWidgets.QApplication(sys.argv)
    frmViewNaver = QtWidgets.QDialog()
    ui = Ui_frmViewNaver()
    ui.setupUi(frmViewNaver)
    frmViewNaver.show()

    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

    sys.exit(app.exec_())
