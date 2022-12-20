from datetime import datetime

import pandas as pd

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *

import matplotlib.pyplot as plt
import matplotlib
import re

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from common.config.filepassclass import FilePathClass


class Ui_frmViewNews(object):
    def setupUi(self, frmViewNews):
        frmViewNews.setObjectName("frmViewNews")
        frmViewNews.resize(1024, 968)
        frmViewNews.setMaximumSize(1024, 968)
        self.group1 = QtWidgets.QGroupBox(frmViewNews)
        self.group1.setGeometry(QtCore.QRect(10, 10, 1001, 61))
        self.group1.setObjectName("group1")
        self.label_5 = QtWidgets.QLabel(self.group1)
        self.label_5.setGeometry(QtCore.QRect(234, 28, 16, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.group1)
        self.label_6.setGeometry(QtCore.QRect(28, 27, 54, 15))
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
        self.label_7 = QtWidgets.QLabel(self.group1)
        self.label_7.setGeometry(QtCore.QRect(410, 28, 91, 16))
        self.label_7.setObjectName("label_7")
        self.sort_yy = QtWidgets.QComboBox(self.group1)
        self.sort_yy.setGeometry(QtCore.QRect(512, 23, 67, 23))
        self.sort_yy.setObjectName("sort_yy")
        self.sort_yy.addItem("")
        self.sort_yy.addItem("")
        self.sort_yy.addItem("")
        self.sort_yy.addItem("")
        self.sort_yy.addItem("")
        self.sort_yy.addItem("")
        self.sort_mm = QtWidgets.QComboBox(self.group1)
        self.sort_mm.setGeometry(QtCore.QRect(588, 23, 51, 23))
        self.sort_mm.setObjectName("sort_mm")
        self.sort_mm.addItem("")
        self.sort_mm.addItem("")
        self.sort_mm.addItem("")
        self.sort_mm.addItem("")
        self.sort_mm.addItem("")
        self.sort_mm.addItem("")
        self.sort_mm.addItem("")
        self.sort_mm.addItem("")
        self.sort_mm.addItem("")
        self.sort_mm.addItem("")
        self.sort_mm.addItem("")
        self.sort_mm.addItem("")
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
        self.rdo_line = QtWidgets.QRadioButton(self.group3)
        self.rdo_line.setGeometry(QtCore.QRect(20, 26, 86, 16))
        self.rdo_line.setObjectName("rdo_line")
        self.rdo_line.setChecked(True)
        self.rdo_bar = QtWidgets.QRadioButton(self.group3)
        self.rdo_bar.setGeometry(QtCore.QRect(80, 26, 86, 16))
        self.rdo_bar.setObjectName("rdo_bar")
        self.rdo_area = QtWidgets.QRadioButton(self.group3)
        self.rdo_area.setGeometry(QtCore.QRect(138, 26, 86, 16))
        self.rdo_area.setObjectName("rdo_area")
        self.label_8 = QtWidgets.QLabel(self.group3)
        self.label_8.setGeometry(QtCore.QRect(220, 26, 51, 16))
        self.label_8.setObjectName("label_8")
        self.txt_top_n = QtWidgets.QLineEdit(self.group3)
        self.txt_top_n.setGeometry(QtCore.QRect(270, 20, 61, 24))
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

        self.tbl_data1.cellClicked.connect(self.table_select)



        self.tbl_data2.setSortingEnabled(True)
        self.tbl_data2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_data2.verticalHeader().setDefaultSectionSize(25)
        self.tbl_data2.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.tbl_data3.setSortingEnabled(True)
        self.tbl_data3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_data3.verticalHeader().setDefaultSectionSize(25)
        self.tbl_data3.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.label = QtWidgets.QLabel(self.group3)
        self.label.setGeometry(QtCore.QRect(10, 51, 981, 500))
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.gridLayout.addWidget(self.canvas)

        self.onlyInt = QIntValidator()
        self.txt_top_n.setValidator(self.onlyInt)
        self.txt_top_n.setText('5')

        self.retranslateUi(frmViewNews)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmViewNews)

        self.btn_search.clicked.connect(self.show_chart)
        self.btn_print.clicked.connect(self.show_graph)


    def table_select(self, row, col):

        if self.tabWidget.currentIndex() == 0:
            table = self.tbl_data1
        elif self.tabWidget.currentIndex() == 1:
            table = self.tbl_data2
        elif self.tabWidget.currentIndex() == 2:
            table = self.tbl_data3

        self.label.clear()
        self.fig.clear(True)

        df = self.setTblToDf(table)
        df.columns = df.columns + '01'
        df.columns = pd.to_datetime(df.columns).date

        ax = self.fig.add_subplot(111)
        ax.plot(df.columns,
                df.values[row].astype(float),
                label=df.values[row], alpha=0.5, linewidth=2)

        ax.legend()
        ax.set_title('월별 키워드 빈도수 추이')
        ax.set_xticks(df.columns)
        # print(temp_topN_df.columns)
        ax.set_xticklabels(df.columns, rotation=15)
        ax.set_ylim([0, df.values[row].astype(float).max() + df.values[row].astype(float).max() * 0.07])
        ax.get_yaxis().get_major_formatter().set_scientific(False)

        self.canvas.draw()


        print(table, row, col)

    # 그래프 출력
    def show_graph(self):

        self.label.clear()
        # df = self.show_chart()
        self.fig.clear(True)
        ax = self.fig.add_subplot(111)

        if self.tabWidget.currentIndex() == 0:
            table = self.tbl_data1
        elif self.tabWidget.currentIndex() == 1:
            table = self.tbl_data2
        elif self.tabWidget.currentIndex() == 2:
            table = self.tbl_data3


        df = self.setTblToDf(table)
        # print(df)
        #df = df.set_index(keys=['키워드'], inplace=False, drop=True)
        #print("df3----->\n", df)
        #x축 라벨 데이터 - 데이트 형태로 변경
        x_lable_value = df.columns
        # print('x_lable_value:', x_lable_value)
        df.columns = df.columns + '01'
        df.columns = pd.to_datetime(df.columns).date


        if self.rdo_line.isChecked():
            # print("df.head->\n", df.head(int(self.txt_top_n.text())).values)

            temp_topN_df = df.head(int(self.txt_top_n.text()))


            for i in range(len(temp_topN_df)):
               ax.plot(df.columns,
                        temp_topN_df.values[i].astype(float),
                        label=temp_topN_df.index.values[i], alpha=0.5, linewidth=2)

            ax.legend()
            ax.set_title('월별 키워드 빈도수 추이')
            ax.set_xticks(temp_topN_df.columns)
            #print(temp_topN_df.columns)
            ax.set_xticklabels(temp_topN_df.columns, rotation=15)
            ax.set_ylim([0, temp_topN_df.values.astype(float).max() + temp_topN_df.values.astype(float).max()*0.07])
            ax.get_yaxis().get_major_formatter().set_scientific(False)

            self.canvas.draw()

        elif self.rdo_bar.isChecked():
            df = df.head(int(self.txt_top_n.text()))
            #df.columns = pd.to_datetime(df.columns).date
            # print("==================================")
            # print(df.info())
            # print("==================================")
            df = df.apply(pd.to_numeric)
            # print(df.info())
            df.T.plot.bar(figsize=(10, 5), alpha=0.5)
            plt.xticks(rotation=15)
            plt.legend(df.index)
            plt.ylim([0, df.values.astype(float).max() + df.values.astype(float).max()*0.07])
            import matplotlib.ticker as mticker
            plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%i'))
            plt.title('월별 키워드 빈도수 추이')
            plt.savefig('graph_img.png', dpi=100)
            self.label.setPixmap(QtGui.QPixmap('graph_img.png'))

        elif self.rdo_area.isChecked():
            for i in range(int(self.txt_top_n.text())):
                ax.scatter(df.columns,
                       df.head(int(self.txt_top_n.text())).values[i].astype(float),
                       label=df.index.values[i], alpha=0.5)
            ax.legend()
            ax.set_title('월별 키워드 빈도수 추이')
            ax.set_xticks(df.columns)
            ax.set_xticklabels(df.columns, rotation=15)
            ax.set_ylim([0, df.values.astype(float).max() + df.values.astype(float).max()*0.07])
            ax.get_yaxis().get_major_formatter().set_scientific(False)

            self.canvas.draw()


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
        sort_date = self.sort_yy.currentText() + self.sort_mm.currentText()

        news = pd.read_csv(file_path.get_raw_use_path() + '뉴스_' + part + '\\1차마트_' + part + '.csv')


        #조회 조건에 맞는 데이타만 가져오기
        news = news[(news['stdym'].astype(int) >= int(anal_s_date)) & (news['stdym'].astype(int) <= int(anal_e_date))]

        #중복 제거
        news = news.drop_duplicates(['stdym', 'keyword'], keep='first', inplace=False, ignore_index=False)

        #데이타 수집년월 기준으로 피벗
        news_pivot = news.pivot(index='keyword', columns='stdym', values='freq')

        # 정렬기준 값으로 데이터 정렬하기
        # 정렬기준 값이 데이타가 존재 하지 않으면 가장 마지막 컬럼 값으로 정렬
        if (sort_date in news_pivot.columns) == False:
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

    #조회한 데이타 테이블에 넣기
    def set_table_data(self, news_sel, table):

        #table.setRowCount(len(news_sel))
        #table.setColumnCount(len(news_sel.columns) + 1)

        #컬럼 생성
        table.setColumnCount(len(news_sel.columns)+1)
        table.setRowCount(len(news_sel))


        table.setHorizontalHeaderItem(0, QTableWidgetItem("키워드"))
        for j in range(0, len(news_sel.columns)):
            #print(j , ";", news_sel.columns[j])
            table.setHorizontalHeaderItem(j+1, QTableWidgetItem(news_sel.columns[j]))

        for i in range(0, len(news_sel)):

            table.setItem(i, 0, QTableWidgetItem(news_sel.index[i]))
            for j in range(len(news_sel.columns)):
                if pd.isna(news_sel[news_sel.columns[j]][i]):
                    item = QTableWidgetItem('0.0')
                else:
                    item = QTableWidgetItem(str(news_sel[news_sel.columns[j]][i]))

                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)

                table.setItem(i, j+1, item)


    # 테이블 데이터를 dataframe으로 변경
    def setTblToDf(self, table):

        col_count = table.columnCount()
        row_count = table.rowCount()

        headers = [str(table.horizontalHeaderItem(i).text()).replace('-', '') for i in range(col_count)]
        # print("headers:" ,headers)

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
        # print("==================================")
        # print(df)
        # print("==================================")
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
        self.label_7.setText(_translate("frmViewNews", "정렬기준 년월 :"))
        self.sort_yy.setItemText(0, _translate("frmViewNews", str(datetime.today().year)))
        self.sort_yy.setItemText(1, _translate("frmViewNews", str(datetime.today().year-1)))
        self.sort_yy.setItemText(2, _translate("frmViewNews", str(datetime.today().year-2)))
        self.sort_yy.setItemText(3, _translate("frmViewNews", str(datetime.today().year-3)))
        self.sort_yy.setItemText(4, _translate("frmViewNews", str(datetime.today().year-4)))
        self.sort_yy.setItemText(5, _translate("frmViewNews", str(datetime.today().year-5)))
        self.sort_mm.setItemText(0, _translate("frmViewNews", "01"))
        self.sort_mm.setItemText(1, _translate("frmViewNews", "02"))
        self.sort_mm.setItemText(2, _translate("frmViewNews", "03"))
        self.sort_mm.setItemText(3, _translate("frmViewNews", "04"))
        self.sort_mm.setItemText(4, _translate("frmViewNews", "05"))
        self.sort_mm.setItemText(5, _translate("frmViewNews", "06"))
        self.sort_mm.setItemText(6, _translate("frmViewNews", "07"))
        self.sort_mm.setItemText(7, _translate("frmViewNews", "08"))
        self.sort_mm.setItemText(8, _translate("frmViewNews", "09"))
        self.sort_mm.setItemText(9, _translate("frmViewNews", "10"))
        self.sort_mm.setItemText(10, _translate("frmViewNews", "11"))
        self.sort_mm.setItemText(11, _translate("frmViewNews", "12"))
        self.sort_yy.setCurrentText(str(datetime.today().year))
        self.sort_mm.setCurrentText(str(datetime.today().month))
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
