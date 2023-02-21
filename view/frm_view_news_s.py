import os.path
import pandas as pd
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *

import math
from matplotlib.dates import MonthLocator
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from common.config.filepassclass import FilePathClass
import common.config.errormessage as em


class Ui_frmViewNews(object):
    def setupUi(self, frmViewNews):
        frmViewNews.setObjectName("frmViewNews")
        frmViewNews.resize(1024, 968)
        frmViewNews.setMaximumSize(1024, 968)
        frmViewNews.setMinimumSize(1024, 968)
        self.group1 = QtWidgets.QGroupBox(frmViewNews)
        self.group1.setGeometry(QtCore.QRect(10, 10, 1001, 61))
        self.group1.setObjectName("group1")
        self.label_5 = QtWidgets.QLabel(self.group1)
        self.label_5.setGeometry(QtCore.QRect(234, 28, 16, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.group1)
        self.label_6.setGeometry(QtCore.QRect(28, 27, 60, 15))
        self.label_6.setObjectName("label_6")
        self.sel_yy_end = QtWidgets.QComboBox(self.group1)
        self.sel_yy_end.setGeometry(QtCore.QRect(251, 23, 67, 23))
        self.sel_yy_end.setObjectName("sel_yy_end")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_mm_start = QtWidgets.QComboBox(self.group1)
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
        self.sel_yy_start = QtWidgets.QComboBox(self.group1)
        self.sel_yy_start.setGeometry(QtCore.QRect(99, 23, 67, 23))
        self.sel_yy_start.setObjectName("sel_yy_start")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_mm_end = QtWidgets.QComboBox(self.group1)
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
        self.btn_search = QtWidgets.QPushButton(self.group1)
        self.btn_search.setGeometry(QtCore.QRect(890, 23, 79, 24))
        self.btn_search.setObjectName("btn_search")
        self.rdo_line = QtWidgets.QRadioButton(self.group1)
        self.rdo_line.setGeometry(QtCore.QRect(430, 27, 86, 20))
        self.rdo_line.setObjectName("rdo_line")
        self.rdo_line.setChecked(True)
        self.rdo_bar = QtWidgets.QRadioButton(self.group1)
        self.rdo_bar.setGeometry(QtCore.QRect(494, 27, 86, 20))
        self.rdo_bar.setObjectName("rdo_bar")
        self.rdo_area = QtWidgets.QRadioButton(self.group1)
        self.rdo_area.setGeometry(QtCore.QRect(554, 27, 86, 20))
        self.rdo_area.setObjectName("rdo_area")
        self.group2 = QtWidgets.QGroupBox(frmViewNews)
        self.group2.setGeometry(QtCore.QRect(10, 80, 1001, 311))
        self.group2.setObjectName("group2")
        self.tabWidget = QtWidgets.QTabWidget(self.group2)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 981, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_today = QtWidgets.QWidget()
        self.tab_today.setObjectName("tab_today")
        self.tbl_data1 = QtWidgets.QTableWidget(self.tab_today)
        self.tbl_data1.setGeometry(QtCore.QRect(0, 0, 971, 251))
        self.tbl_data1.setObjectName("tbl_data1")
        self.tbl_data1.setColumnCount(1)
        self.tbl_data1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data1.setHorizontalHeaderItem(3, item)
        self.tbl_data1.horizontalHeader().setStretchLastSection(False)
        self.tbl_data1.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab_today, "")
        self.tab_rise = QtWidgets.QWidget()
        self.tab_rise.setObjectName("tab_rise")
        self.tbl_data2 = QtWidgets.QTableWidget(self.tab_rise)
        self.tbl_data2.setGeometry(QtCore.QRect(0, 0, 971, 251))
        self.tbl_data2.setObjectName("tbl_data2")
        self.tbl_data2.setColumnCount(1)
        self.tbl_data2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data2.setHorizontalHeaderItem(3, item)
        self.tbl_data2.horizontalHeader().setStretchLastSection(False)
        self.tbl_data2.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab_rise, "")
        self.tab_top = QtWidgets.QWidget()
        self.tab_top.setObjectName("tab_top")
        self.tbl_data3 = QtWidgets.QTableWidget(self.tab_top)
        self.tbl_data3.setGeometry(QtCore.QRect(0, 0, 971, 251))
        self.tbl_data3.setObjectName("tbl_data3")
        self.tbl_data3.setColumnCount(1)
        self.tbl_data3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data3.setHorizontalHeaderItem(3, item)
        self.tbl_data3.horizontalHeader().setStretchLastSection(False)
        self.tbl_data3.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab_top, "")
        self.group3 = QtWidgets.QGroupBox(frmViewNews)
        self.group3.setGeometry(QtCore.QRect(10, 400, 1001, 560))
        self.group3.setObjectName("group3")
        self.label_8 = QtWidgets.QLabel(self.group3)
        self.label_8.setGeometry(QtCore.QRect(770, 26, 51, 16))
        self.label_8.setObjectName("label_8")
        self.txt_top_n = QtWidgets.QLineEdit(self.group3)
        self.txt_top_n.setGeometry(QtCore.QRect(820, 20, 61, 24))
        self.txt_top_n.setToolTip("")
        self.txt_top_n.setObjectName("txt_top_n")
        self.btn_print = QtWidgets.QPushButton(self.group3)
        self.btn_print.setGeometry(QtCore.QRect(890, 19, 79, 24))
        self.btn_print.setObjectName("btn_print")
        self.gridLayoutWidget = QtWidgets.QWidget(self.group3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 51, 981, 500))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.tbl_data1.setSortingEnabled(True)
        self.tbl_data1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_data1.verticalHeader().setDefaultSectionSize(25)
        self.tbl_data1.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.tbl_data2.setSortingEnabled(True)
        self.tbl_data2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_data2.verticalHeader().setDefaultSectionSize(25)
        self.tbl_data2.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.tbl_data3.setSortingEnabled(True)
        self.tbl_data3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_data3.verticalHeader().setDefaultSectionSize(25)
        self.tbl_data3.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        # 그래프 출력 공간
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.gridLayout.addWidget(self.canvas)

        # 정수만 입력 가능
        self.onlyInt = QIntValidator()
        self.txt_top_n.setValidator(self.onlyInt)
        self.txt_top_n.setText('5')

        self.retranslateUi(frmViewNews)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmViewNews)

        self.btn_search.clicked.connect(self.show_chart)  # 테이블 출력
        self.btn_print.clicked.connect(self.show_graph)  # 그래프 출력

        self.rdo_line.clicked.connect(self.reset)  # 라디오 버튼 변경 > 그래프 초기화
        self.rdo_bar.clicked.connect(self.reset)  # 라디오 버튼 변경 > 그래프 초기화
        self.rdo_area.clicked.connect(self.reset)  # 라디오 버튼 변경 > 그래프 초기화

        self.tbl_data1.cellClicked.connect(self.table_select)  # 셀 선택 > 그래프 출력
        self.tbl_data2.cellClicked.connect(self.table_select)  # 셀 선택 > 그래프 출력
        self.tbl_data3.cellClicked.connect(self.table_select)  # 셀 선택 > 그래프 출력


    # 테이블 초기화
    def reset(self):
        self.fig.clear(True)
        self.canvas.draw()


    # 선택된 키워드 그래프 출력
    def table_select(self, row, col):
        if self.tabWidget.currentIndex() == 0:
            table = self.tbl_data1
        elif self.tabWidget.currentIndex() == 1:
            table = self.tbl_data2
        elif self.tabWidget.currentIndex() == 2:
            table = self.tbl_data3

        self.fig.clear(True)

        df = self.setTblToDf(table)
        df.columns = df.columns + '01'
        df.columns = pd.to_datetime(df.columns).date

        ax = self.fig.add_subplot(111)

        if self.rdo_line.isChecked():
            ax.plot(df.columns, df.values[row].astype(float),
                    label=df.index.values[row], alpha=0.5, linewidth=2)
        elif self.rdo_area.isChecked():
            ax.scatter(df.columns, df.values[row].astype(float),
                       label=df.index.values[row], alpha=0.5)
        elif self.rdo_bar.isChecked():
            ax.bar(df.columns, df.values[row].astype(float),
                   label=df.index.values[row], alpha=0.5, width=5)

        ax.legend()
        ax.set_title('월별 키워드 빈도수 추이')
        ax.xaxis.set_major_locator(MonthLocator(interval=math.ceil(len(df.columns)/12)))  # 주눈금
        ax.xaxis.set_minor_locator(MonthLocator(interval=1))  # 보조 눈금
        ax.set_ylim([0, df.values[row].astype(float).max() + df.values[row].astype(float).max() * 0.07])  # y축 값 범위 설정
        ax.get_yaxis().get_major_formatter().set_scientific(False)  # 숫자 지수형 변환 X

        self.canvas.draw()


    # 그래프 출력
    def show_graph(self):
        self.fig.clear(True)
        ax = self.fig.add_subplot(111)

        if self.tabWidget.currentIndex() == 0:
            table = self.tbl_data1
        elif self.tabWidget.currentIndex() == 1:
            table = self.tbl_data2
        elif self.tabWidget.currentIndex() == 2:
            table = self.tbl_data3

        df = self.setTblToDf(table)
        #x축 라벨 데이터 - 날짜 형태로 변경
        if len(df) > 0:
            df.columns = df.columns + '01'
            df.columns = pd.to_datetime(df.columns).date

            # 선 그래프
            if self.rdo_line.isChecked():
                for i in range(int(self.txt_top_n.text())):
                    ax.plot(df.columns, df.head(int(self.txt_top_n.text())).values[i],
                            label=df.index.values[i], alpha=0.5, linewidth=2)

            # 막대 그래프
            elif self.rdo_bar.isChecked():
                for i in range(int(self.txt_top_n.text())):
                    ax.bar(df.columns,
                           df.head(int(self.txt_top_n.text())).values[i],
                           label=df.index.values[i], alpha=0.3, width=10)
                # df = df.head(int(self.txt_top_n.text()))
                # df.T.plot.bar(figsize=(10, 5), ax=ax, alpha=0.5)
                # ax.xaxis.set_visible(False)

            # 산점도
            elif self.rdo_area.isChecked():
                for i in range(int(self.txt_top_n.text())):
                    ax.scatter(df.columns,
                           df.head(int(self.txt_top_n.text())).values[i],
                           label=df.index.values[i], alpha=0.5)

            ax.legend(df.index)
            ax.set_title('월별 키워드 빈도수 추이')
            ax.xaxis.set_major_locator(MonthLocator(interval=math.ceil(len(df.columns) / 12)))  # 주눈금
            ax.xaxis.set_minor_locator(MonthLocator(interval=1))  # 보조 눈금
            ax.set_ylim([0, df.values.astype(float).max() + df.values.astype(float).max() * 0.07])  # y축 값 범위
            ax.get_yaxis().get_major_formatter().set_scientific(False)  # 숫자 지수형 변환 X

            self.canvas.draw()
        else:
            error_event(em.NO_DATA)


    # 차트 출력
    def show_chart(self):
        file_path = FilePathClass()

        if self.tabWidget.currentIndex() == 0:
            part = '정치'
        elif self.tabWidget.currentIndex() == 1:
            part = '경제'
        elif self.tabWidget.currentIndex() == 2:
            part = '사회'

        anal_s_date = self.sel_yy_start.currentText() + self.sel_mm_start.currentText()
        anal_e_date = self.sel_yy_end.currentText() + self.sel_mm_end.currentText()

        # 종료 일자가 시작 일자보다 과거인 경우
        if int(anal_e_date) - int(anal_s_date) < 0:
            error_event(em.CHK_DATE)
        else:
            path = file_path.get_raw_use_path() + '뉴스_' + part + '\\1차마트_' + part + '.csv'

            if os.path.exists(path):
                news = pd.read_csv(path)

                #조회 조건에 맞는 데이타만 가져오기
                news = news[(news['stdym'].astype(int) >= int(anal_s_date)) & (news['stdym'].astype(int) <= int(anal_e_date))]

                if news.empty == False:
                    #중복 제거
                    news = news.drop_duplicates(['stdym', 'keyword'], keep='first', inplace=False, ignore_index=False)

                    #데이타 수집년월 기준으로 피벗
                    news_pivot = news.pivot(index='keyword', columns='stdym', values='freq')

                    # 가장 마지막 컬럼 값으로 정렬
                    sort_date = news_pivot.columns[news_pivot.shape[1]-1]
                    news_sel = news_pivot.sort_values(sort_date, ascending=False)

                    for i in news_sel.columns:
                        temp = str(i)[0:4] + "-" + str(i)[4:6]
                        news_sel.rename(columns={i:temp}, inplace=True)

                    if self.tabWidget.currentIndex() == 0:
                         self.set_table_data(news_sel,  self.tbl_data1)
                    elif self.tabWidget.currentIndex() == 1:
                         self.set_table_data(news_sel,  self.tbl_data2)
                    elif self.tabWidget.currentIndex() == 2:
                         self.set_table_data(news_sel,  self.tbl_data3)

                    return news_sel
                else:
                    error_event(em.NO_DATA)
            else:
                msg = "'" + path + "'\n" + em.NO_DATA
                error_event(msg)


    #조회한 데이타 테이블에 넣기
    def set_table_data(self, news_sel, table):
        try:
            #컬럼 생성
            table.setColumnCount(len(news_sel.columns)+1)
            table.setRowCount(len(news_sel))

            table.setHorizontalHeaderItem(0, QTableWidgetItem("키워드"))
            for j in range(0, len(news_sel.columns)):
                table.setHorizontalHeaderItem(j+1, QTableWidgetItem(news_sel.columns[j]))

            for i in range(0, len(news_sel)):
                table.setItem(i, 0, QTableWidgetItem(news_sel.index[i]))
                for j in range(len(news_sel.columns)):
                    item = QTableWidgetItem()
                    if pd.isna(news_sel[news_sel.columns[j]][i]):
                       item.setData(Qt.DisplayRole, float(0.0))  # 실수형으로 데이터 설정
                    else:
                       item.setData(Qt.DisplayRole, float(news_sel[news_sel.columns[j]][i]))
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)  # 텍스트 오른쪽 정렬
                    table.setItem(i, j+1, item)

        except Exception as e:
            print("set_table_data Error : ", e)


    # 테이블 데이터를 dataframe으로 변경
    def setTblToDf(self, table):
        col_count = table.columnCount()
        row_count = table.rowCount()

        headers = [str(table.horizontalHeaderItem(i).text()).replace('-', '') for i in range(col_count)]

        # df indexing is slow, so use lists
        df_list = []
        for row in range(row_count):
            df_list2 = []
            for col in range(col_count):
                table_item = table.item(row, col)
                df_list2.append('' if table_item is None else str(table_item.text()))
            df_list.append(df_list2)

        df = pd.DataFrame(df_list, columns=headers)
        df = df.set_index(keys=['키워드'], inplace=False, drop=True)
        df = df.astype(float)

        return df


    def retranslateUi(self, frmViewNews):
        _translate = QtCore.QCoreApplication.translate
        frmViewNews.setWindowTitle(_translate("frmViewNews", "뉴스 키워드 시각화"))
        self.group1.setTitle(_translate("frmViewNews", " [ 분석 ] "))
        self.label_5.setText(_translate("frmViewNews", "~"))
        self.label_6.setText(_translate("frmViewNews", "분석기간: "))
        self.sel_yy_end.setItemText(0, _translate("frmViewNews", str(datetime.today().year)))
        self.sel_yy_end.setItemText(1, _translate("frmViewNews", str(datetime.today().year-1)))
        self.sel_yy_end.setItemText(2, _translate("frmViewNews", str(datetime.today().year-2)))
        self.sel_yy_end.setItemText(3, _translate("frmViewNews", str(datetime.today().year-3)))
        self.sel_yy_end.setItemText(4, _translate("frmViewNews", str(datetime.today().year-4)))
        self.sel_yy_end.setItemText(5, _translate("frmViewNews", str(datetime.today().year-5)))
        self.sel_mm_start.setItemText(0, _translate("frmViewNews", "01"))
        self.sel_mm_start.setItemText(1, _translate("frmViewNews", "02"))
        self.sel_mm_start.setItemText(2, _translate("frmViewNews", "03"))
        self.sel_mm_start.setItemText(3, _translate("frmViewNews", "04"))
        self.sel_mm_start.setItemText(4, _translate("frmViewNews", "05"))
        self.sel_mm_start.setItemText(5, _translate("frmViewNews", "06"))
        self.sel_mm_start.setItemText(6, _translate("frmViewNews", "07"))
        self.sel_mm_start.setItemText(7, _translate("frmViewNews", "08"))
        self.sel_mm_start.setItemText(8, _translate("frmViewNews", "09"))
        self.sel_mm_start.setItemText(9, _translate("frmViewNews", "10"))
        self.sel_mm_start.setItemText(10, _translate("frmViewNews", "11"))
        self.sel_mm_start.setItemText(11, _translate("frmViewNews", "12"))
        self.sel_yy_start.setItemText(0, _translate("frmViewNews", str(datetime.today().year)))
        self.sel_yy_start.setItemText(1, _translate("frmViewNews", str(datetime.today().year-1)))
        self.sel_yy_start.setItemText(2, _translate("frmViewNews", str(datetime.today().year-2)))
        self.sel_yy_start.setItemText(3, _translate("frmViewNews", str(datetime.today().year-3)))
        self.sel_yy_start.setItemText(4, _translate("frmViewNews", str(datetime.today().year-4)))
        self.sel_yy_start.setItemText(5, _translate("frmViewNews", str(datetime.today().year-5)))
        self.sel_mm_end.setItemText(0, _translate("frmViewNews", "01"))
        self.sel_mm_end.setItemText(1, _translate("frmViewNews", "02"))
        self.sel_mm_end.setItemText(2, _translate("frmViewNews", "03"))
        self.sel_mm_end.setItemText(3, _translate("frmViewNews", "04"))
        self.sel_mm_end.setItemText(4, _translate("frmViewNews", "05"))
        self.sel_mm_end.setItemText(5, _translate("frmViewNews", "06"))
        self.sel_mm_end.setItemText(6, _translate("frmViewNews", "07"))
        self.sel_mm_end.setItemText(7, _translate("frmViewNews", "08"))
        self.sel_mm_end.setItemText(8, _translate("frmViewNews", "09"))
        self.sel_mm_end.setItemText(9, _translate("frmViewNews", "10"))
        self.sel_mm_end.setItemText(10, _translate("frmViewNews", "11"))
        self.sel_mm_end.setItemText(11, _translate("frmViewNews", "12"))
        self.sel_yy_end.setCurrentText(str(datetime.today().year))
        self.sel_mm_end.setCurrentText(str(datetime.today().month))
        self.sel_yy_start.setCurrentText(str(datetime.today().year))
        self.btn_search.setText(_translate("frmViewNews", "조회"))
        self.group2.setTitle(_translate("frmViewNews", " [ 데이터 현황 ] "))
        item = self.tbl_data1.horizontalHeaderItem(0)
        item.setText(_translate("frmViewNews", "키워드"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_today), _translate("frmViewNews", "뉴스_정치"))
        item = self.tbl_data2.horizontalHeaderItem(0)
        item.setText(_translate("frmViewNews", "키워드"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rise), _translate("frmViewNews", "뉴스_경제"))
        item = self.tbl_data3.horizontalHeaderItem(0)
        item.setText(_translate("frmViewNews", "키워드"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_top), _translate("frmViewNews", "뉴스_사회"))
        self.group3.setTitle(_translate("frmViewNews", " [ 그래프 ] "))
        self.rdo_line.setText(_translate("frmViewNews", "Line"))
        self.rdo_bar.setText(_translate("frmViewNews", "Bar"))
        self.rdo_area.setText(_translate("frmViewNews", "Scatter"))
        self.label_8.setText(_translate("frmViewNews", "Top N :"))
        self.btn_print.setText(_translate("frmViewNews", "조회"))


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
    frmViewNews = QtWidgets.QDialog()
    ui = Ui_frmViewNews()
    ui.setupUi(frmViewNews)
    frmViewNews.show()

    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

    sys.exit(app.exec_())
