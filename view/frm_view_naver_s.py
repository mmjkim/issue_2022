import os
import warnings
from datetime import datetime

warnings.filterwarnings(action='ignore')

from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QMessageBox

from common.config.filepassclass import FilePathClass
from source.get_chart_data import *
from common.function.funcC3Chart import c3chart_html_write as c3Chart
import common.config.errormessage as em


class Ui_frmViewNaver(object):
    def setupUi(self, frmViewNaver):
        frmViewNaver.setObjectName("frmViewNaver")
        frmViewNaver.resize(1024, 968)
        frmViewNaver.setMaximumSize(1024, 968)
        frmViewNaver.setMinimumSize(1024, 968)

        self.group1 = QtWidgets.QGroupBox(frmViewNaver)
        self.group1.setGeometry(QtCore.QRect(11, 11, 1001, 311))
        self.group1.setObjectName("group1")

        self.label2 = QtWidgets.QLabel(self.group1)
        self.label2.setGeometry(QtCore.QRect(372, 30, 20, 17))
        self.label2.setObjectName("label2")

        self.label = QtWidgets.QLabel(self.group1)
        self.label.setGeometry(QtCore.QRect(170, 29, 60, 15))
        self.label.setObjectName("label")

        self.sel_yy_start = QtWidgets.QComboBox(self.group1)
        self.sel_yy_start.setGeometry(QtCore.QRect(237, 25, 67, 23))
        self.sel_yy_start.setObjectName("sel_yy_start")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
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
        self.sel_yy_end = QtWidgets.QComboBox(self.group1)
        self.sel_yy_end.setGeometry(QtCore.QRect(389, 25, 67, 23))
        self.sel_yy_end.setObjectName("sel_yy_end")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
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
        self.rdo_line.setGeometry(QtCore.QRect(20, 26, 86, 20))
        self.rdo_line.setObjectName("rdo_line")
        self.rdo_line.setChecked(True)
        self.rdo_bar = QtWidgets.QRadioButton(self.group2)
        self.rdo_bar.setGeometry(QtCore.QRect(80, 26, 86, 20))
        self.rdo_bar.setObjectName("rdo_bar")
        self.rdo_area = QtWidgets.QRadioButton(self.group2)
        self.rdo_area.setGeometry(QtCore.QRect(138, 26, 86, 20))
        self.rdo_area.setObjectName("rdo_area")
        self.rdo_multi = QtWidgets.QRadioButton(self.group2)
        self.rdo_multi.setGeometry(QtCore.QRect(200, 26, 86, 20))
        self.rdo_multi.setObjectName("rdo_multi")
        self.rdo_multi.setEnabled(False)

        self.btn_print = QtWidgets.QPushButton(self.group2)
        self.btn_print.setGeometry(QtCore.QRect(890, 23, 79, 24))
        self.btn_print.setObjectName("btn_print")

        # C3 Chart 출력 공간
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.group2)
        self.webEngineView.setGeometry(QtCore.QRect(10, 50, 981, 571))
        self.webEngineView.setObjectName("webEngineView")

        self.retranslateUi(frmViewNaver)
        QtCore.QMetaObject.connectSlotsByName(frmViewNaver)

        self.show_list()  # 수집된 네이버 데이터의 키워드 출력
        self.btn_search.clicked.connect(self.show_table)  # 테이블 출력
        self.btn_print.clicked.connect(self.show_graph)  # 그래프 출력

        self.tbl_naver.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 테이블 수정 불가
        self.tbl_naver.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")  # 테이블 스타일 설정


    def show_graph(self):
        df = self.show_table()
        if df is not None:
            multi_types = ''
            if self.rdo_line.isChecked():
                type = 'line'
            elif self.rdo_bar.isChecked():
                type = 'bar'
            elif self.rdo_area.isChecked():
                type = 'area'
            else:
                type = ''
                for i in range(1, len(df.columns)):
                    if i == 1:
                        multi_types += "'" + df.columns[i] + "':'bar',\n"
                    else:
                        multi_types += "'" + df.columns[i] + "':'line',\n"

            html = c3Chart(df, type, multi_types)  # 그래프 html 가져오기
            temp = "zoom:{enabled: false}"
            self.webEngineView.setHtml(html.replace(temp, "zoom: {enabled: true}"))  # 그래프 그리기
            loadCSS(self.webEngineView, "c3Chart/c3.css", "script1")  # 그래프 스타일 설정
        else:
            self.webEngineView.setHtml('')
            error_event(em.NO_DATA)


    # 수집된 네이버 데이터의 키워드 출력
    def show_list(self):
        file_path = FilePathClass()
        path = file_path.get_raw_use_path()
        data_all_list = os.listdir(path)
        data_list = []

        # 네이버_*.csv 파일 리스트에 추가
        for i in range(len(data_all_list)):
            if (data_all_list[i][-3:] == 'csv') & (data_all_list[i].startswith('네이버')):
                data_list.append(data_all_list[i])
        
        # 키워드 출력
        for i in range(len(data_list)):
            dataname = data_list[i].split('_')
            self.listWidget.addItem(dataname[2][:-4])


    def show_table(self):
        self.webEngineView.setHtml('')

        keywords = []
        # 선택된 키워드 리스트 저장
        for i in range(len(self.listWidget.selectedItems())):
            keywords.append(str(self.listWidget.selectedItems()[i].text()))
        words = ','.join(keywords)

        # 종료 일자가 시작 일자보다 과거인 경우
        if int(self.sel_yy_end.currentText()+self.sel_mm_end.currentText()) - int(self.sel_yy_start.currentText()+self.sel_mm_start.currentText()) < 0:
            error_event(em.CHK_DATE)
        else:
            if len(words) > 1:
                # 데이터 가져오기
                df = get_view_naver_keyword(words, self.sel_yy_start.currentText()+'-'+self.sel_mm_start.currentText()+'-'+'01',
                                            self.sel_yy_end.currentText()+'-'+self.sel_mm_end.currentText()+'-'+'01')
                df = df.sort_values(by=['ymd'])  # ymd 기준으로 정렬
                df = df.fillna('0')

                # 테이블 행/열 길이 지정
                self.tbl_naver.setRowCount(len(df))
                self.tbl_naver.setColumnCount(len(df.columns))

                df = df.rename(columns={'ymd':'기준일자'})
                self.tbl_naver.setHorizontalHeaderLabels(df.columns)

                # 테이블 값 삽입
                for c in range(len(df.columns)):
                    for i in range(len(df)):
                        item = QTableWidgetItem()
                        text = df[df.columns[c]][i]
                        if c != 0:  # 첫 번째 열(기준일자)이면 오른쪽 정렬 X
                            item.setData(Qt.DisplayRole, float(text))
                            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                        else:
                            item.setText(str(text))
                        self.tbl_naver.setItem(i, c, item)

                self.tbl_naver.sortItems(0, QtCore.Qt.AscendingOrder)  # 기준일자 기준으로 정렬

                df = df.rename(columns={'기준일자': 'ymd'})

                # 데이터 프레임 컬럼이 3개 이상인 경우 멀티 라디오 버튼 선택 가능함
                if len(self.listWidget.selectedItems()) >= 3:
                    self.rdo_multi.setEnabled(True)
                else:
                    self.rdo_multi.setEnabled(False)

                return df
            else:  # 선택된 키워드 X > error
                self.tbl_naver.setRowCount(0)
                error_event(em.SELECT_KEYWORD)


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
        self.rdo_multi.setText(_translate("frmViewNaver", "Multi"))
        self.btn_print.setText(_translate("frmViewNaver", "조회"))


# 그래프 스타일 적용
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


def error_event(msg):
    msgbox = QMessageBox()
    msgbox.setWindowTitle("error")
    msgbox.setText(msg)
    msgbox.exec_()


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
