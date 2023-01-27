import pandas as pd
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

import math
from matplotlib.dates import MonthLocator
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas  # 그래프 출력 캔버스

from common.config.filepassclass import FilePathClass
import common.config.errormessage as em


class Ui_frmViewComplaints(object):
    def setupUi(self, frmViewComplaints):
        # 화면 크기 설정 및 고정
        frmViewComplaints.setObjectName("frmViewComplaints")
        frmViewComplaints.resize(1024, 968)
        frmViewComplaints.setMaximumSize(1024, 968)
        frmViewComplaints.setMinimumSize(1024, 968)

        self.group1 = QtWidgets.QGroupBox(frmViewComplaints)
        self.group1.setGeometry(QtCore.QRect(10, 10, 1001, 61))
        self.group1.setObjectName("group1")

        self.label_5 = QtWidgets.QLabel(self.group1)
        self.label_5.setGeometry(QtCore.QRect(234, 28, 16, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.group1)
        self.label_6.setGeometry(QtCore.QRect(28, 27, 54, 15))
        self.label_6.setObjectName("label_6")

        self.sel_yy_start = QtWidgets.QComboBox(self.group1)
        self.sel_yy_start.setGeometry(QtCore.QRect(99, 23, 67, 23))
        self.sel_yy_start.setObjectName("sel_yy_start")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
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
        self.sel_yy_end = QtWidgets.QComboBox(self.group1)
        self.sel_yy_end.setGeometry(QtCore.QRect(251, 23, 67, 23))
        self.sel_yy_end.setObjectName("sel_yy_end")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
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

        self.group2 = QtWidgets.QGroupBox(frmViewComplaints)
        self.group2.setGeometry(QtCore.QRect(10, 80, 1001, 881))
        self.group2.setObjectName("group2")

        self.tabWidget = QtWidgets.QTabWidget(self.group2)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 980, 851))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        # 민원 급등 키워드 탭
        self.tab_rise = QtWidgets.QWidget()
        self.tab_rise.setObjectName("tab_rise")
        # 민원 급등 키워드 테이블
        self.tbl_data1 = QtWidgets.QTableWidget(self.tab_rise)
        self.tbl_data1.setGeometry(QtCore.QRect(0, 0, 974, 241))
        self.tbl_data1.setObjectName("tbl_data1")
        self.tbl_data1.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data1.setHorizontalHeaderItem(0, item)
        self.tbl_data1.horizontalHeader().setStretchLastSection(False)
        self.tbl_data1.verticalHeader().setDefaultSectionSize(25)
        self.tbl_data1.verticalHeader().setStretchLastSection(False)
        self.tbl_data1.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.group3 = QtWidgets.QGroupBox(self.tab_rise)
        self.group3.setGeometry(QtCore.QRect(3, 250, 968, 570))
        self.group3.setObjectName("group3")

        self.rdo_line = QtWidgets.QRadioButton(self.group1)
        self.rdo_line.setGeometry(QtCore.QRect(410, 28, 86, 20))
        self.rdo_line.setObjectName("rdo_line")
        self.rdo_line.setChecked(True)
        self.rdo_bar = QtWidgets.QRadioButton(self.group1)
        self.rdo_bar.setGeometry(QtCore.QRect(470, 28, 86, 20))
        self.rdo_bar.setObjectName("rdo_bar")
        self.rdo_area = QtWidgets.QRadioButton(self.group1)
        self.rdo_area.setGeometry(QtCore.QRect(530, 28, 86, 20))
        self.rdo_area.setObjectName("rdo_area")

        self.label_8 = QtWidgets.QLabel(self.group3)
        self.label_8.setGeometry(QtCore.QRect(750, 26, 55, 16))
        self.label_8.setObjectName("label_8")

        self.txt_top_n = QtWidgets.QLineEdit(self.group3)
        self.txt_top_n.setGeometry(QtCore.QRect(800, 20, 61, 24))
        self.txt_top_n.setToolTip("")
        self.txt_top_n.setObjectName("txt_top_n")

        self.btn_print = QtWidgets.QPushButton(self.group3)
        self.btn_print.setGeometry(QtCore.QRect(880, 19, 79, 24))
        self.btn_print.setObjectName("btn_print")

        self.gridLayoutWidget = QtWidgets.QWidget(self.group3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(7, 50, 954, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.tabWidget.addTab(self.tab_rise, "")

        # 민원 최다 키워드 탭
        self.tab_dftop = QtWidgets.QWidget()
        self.tab_dftop.setObjectName("tab_dftop")
        # 민원 최다 키워드 테이블
        self.tbl_data2 = QtWidgets.QTableWidget(self.tab_dftop)
        self.tbl_data2.setGeometry(QtCore.QRect(0, 0, 974, 241))
        self.tbl_data2.setObjectName("tbl_data2")
        self.tbl_data2.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data2.setHorizontalHeaderItem(0, item)
        self.tbl_data2.horizontalHeader().setStretchLastSection(False)
        self.tbl_data2.verticalHeader().setDefaultSectionSize(25)
        self.tbl_data2.verticalHeader().setStretchLastSection(False)
        self.tbl_data2.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")
        self.group3_2 = QtWidgets.QGroupBox(self.tab_dftop)
        self.group3_2.setGeometry(QtCore.QRect(3, 250, 968, 570))
        self.group3_2.setObjectName("group3_2")
        self.label_9 = QtWidgets.QLabel(self.group3_2)
        self.label_9.setGeometry(QtCore.QRect(750, 26, 51, 16))
        self.label_9.setObjectName("label_9")
        self.txt_top_n_2 = QtWidgets.QLineEdit(self.group3_2)
        self.txt_top_n_2.setGeometry(QtCore.QRect(800, 20, 61, 24))
        self.txt_top_n_2.setToolTip("")
        self.txt_top_n_2.setObjectName("txt_top_n_2")
        self.btn_print_2 = QtWidgets.QPushButton(self.group3_2)
        self.btn_print_2.setGeometry(QtCore.QRect(880, 19, 79, 24))
        self.btn_print_2.setObjectName("btn_print_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.group3_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(7, 50, 954, 501))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget.addTab(self.tab_dftop, "")

        # 민원 핵심 키워드 탭
        self.tab_top = QtWidgets.QWidget()
        self.tab_top.setObjectName("tab_top")
        # 민원 핵심 키워드 테이블
        self.tbl_data3 = QtWidgets.QTableWidget(self.tab_top)
        self.tbl_data3.setGeometry(QtCore.QRect(0, 0, 974, 241))
        self.tbl_data3.setObjectName("tbl_data3")
        self.tbl_data3.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data3.setHorizontalHeaderItem(0, item)
        self.tbl_data3.horizontalHeader().setStretchLastSection(False)
        self.tbl_data3.verticalHeader().setDefaultSectionSize(25)
        self.tbl_data3.verticalHeader().setStretchLastSection(False)
        self.tbl_data3.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")
        self.group3_3 = QtWidgets.QGroupBox(self.tab_top)
        self.group3_3.setGeometry(QtCore.QRect(3, 250, 968, 570))
        self.group3_3.setObjectName("group3_3")
        self.label_10 = QtWidgets.QLabel(self.group3_3)
        self.label_10.setGeometry(QtCore.QRect(20, 26, 61, 16))
        self.label_10.setObjectName("label_10")
        self.btn_print_3 = QtWidgets.QPushButton(self.group3_3)
        self.btn_print_3.setGeometry(QtCore.QRect(880, 19, 79, 24))
        self.btn_print_3.setObjectName("btn_print_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.group3_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(7, 50, 954, 501))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.group3_3)
        self.label_3.setGeometry(QtCore.QRect(10, 51, 951, 500))
        self.label_3.setObjectName("label_3")
        self.label_topn = QtWidgets.QLabel(self.group3_3)
        self.label_topn.setGeometry(QtCore.QRect(90, 26, 51, 16))
        self.label_topn.setObjectName("label_topn")
        self.txt_top_n_3 = QtWidgets.QLineEdit(self.group3_3)
        self.txt_top_n_3.setGeometry(QtCore.QRect(360, 20, 61, 24))
        self.txt_top_n_3.setToolTip("")
        self.txt_top_n_3.setObjectName("txt_top_n_3")
        self.tabWidget.addTab(self.tab_top, "")

        self.label_12 = QtWidgets.QLabel(self.group3_3)
        self.label_12.setGeometry(QtCore.QRect(310, 26, 51, 16))
        self.label_12.setObjectName("label_12")

        self.sort_yy_2 = QtWidgets.QComboBox(self.group3_3)
        self.sort_yy_2.setGeometry(QtCore.QRect(164, 22, 67, 23))
        self.sort_yy_2.setObjectName("sort_yy_2")
        self.sort_yy_2.addItem("")
        self.sort_yy_2.addItem("")
        self.sort_yy_2.addItem("")
        self.sort_yy_2.addItem("")
        self.sort_yy_2.addItem("")
        self.sort_yy_2.addItem("")
        self.label_13 = QtWidgets.QLabel(self.group3_3)
        self.label_13.setGeometry(QtCore.QRect(98, 26, 91, 16))
        self.label_13.setObjectName("label_13")
        self.sort_mm_2 = QtWidgets.QComboBox(self.group3_3)
        self.sort_mm_2.setGeometry(QtCore.QRect(240, 22, 51, 23))
        self.sort_mm_2.setObjectName("sort_mm_2")
        self.sort_mm_2.addItem("")
        self.sort_mm_2.addItem("")
        self.sort_mm_2.addItem("")
        self.sort_mm_2.addItem("")
        self.sort_mm_2.addItem("")
        self.sort_mm_2.addItem("")
        self.sort_mm_2.addItem("")
        self.sort_mm_2.addItem("")
        self.sort_mm_2.addItem("")
        self.sort_mm_2.addItem("")
        self.sort_mm_2.addItem("")
        self.sort_mm_2.addItem("")

        self.label_3.setAlignment(Qt.AlignCenter)

        self.tbl_data1.setSortingEnabled(True)
        self.tbl_data2.setSortingEnabled(True)
        self.tbl_data3.setSortingEnabled(True)

        self.retranslateUi(frmViewComplaints)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmViewComplaints)

        # 그래프 출력 공간
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.gridLayout.addWidget(self.canvas)
        self.fig2 = plt.Figure()
        self.canvas2 = FigureCanvas(self.fig2)
        self.gridLayout_2.addWidget(self.canvas2)
        self.fig3 = plt.Figure()
        self.canvas3 = FigureCanvas(self.fig3)
        self.gridLayout_3.addWidget(self.canvas3)

        # 기본값 '5'로 설정
        self.txt_top_n.setValidator(QIntValidator())
        self.txt_top_n.setText('5')
        self.txt_top_n_2.setValidator(QIntValidator())
        self.txt_top_n_2.setText('5')
        self.txt_top_n_3.setValidator(QIntValidator())
        self.txt_top_n_3.setText('5')

        # 테이블 출력
        self.btn_search.clicked.connect(self.show_chart)
        
        # 상위 키워드 그래프 출력
        self.btn_print.clicked.connect(lambda: self.show_graph(self.fig, self.canvas))
        self.btn_print_2.clicked.connect(lambda: self.show_graph(self.fig2, self.canvas2))
        self.btn_print_3.clicked.connect(lambda: self.show_graph(self.fig3, self.canvas3))

        self.rdo_line.clicked.connect(self.reset)  # 라디오 버튼 변경 > 그래프 초기화
        self.rdo_bar.clicked.connect(self.reset)  # 라디오 버튼 변경 > 그래프 초기화
        self.rdo_area.clicked.connect(self.reset)  # 라디오 버튼 변경 > 그래프 초기화

        self.tbl_data1.cellClicked.connect(self.table_select)  # 셀 선택 > 그래프 출력
        self.tbl_data2.cellClicked.connect(self.table_select)  # 셀 선택 > 그래프 출력
        self.tbl_data3.cellClicked.connect(self.table_select)  # 셀 선택 > 그래프 출력


    # 테이블 > 데이터프레임 변환
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

    
    # 선택된 키워드 그래프 출력
    def table_select(self, row):
        if self.tabWidget.currentIndex() == 0:
            table = self.tbl_data1
            fig = self.fig
            canvas = self.canvas
        elif self.tabWidget.currentIndex() == 1:
            table = self.tbl_data2
            fig = self.fig2
            canvas = self.canvas2
        elif self.tabWidget.currentIndex() == 2:
            table = self.tbl_data3
            fig = self.fig3
            canvas = self.canvas3

        fig.clear(True)
        self.label_3.clear()

        df = self.setTblToDf(table)
        df.columns = df.columns + '01'
        df.columns = pd.to_datetime(df.columns).date

        ax = fig.add_subplot(111)

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
        ax.xaxis.set_major_locator(MonthLocator(interval=math.ceil(len(df.columns) / 12)))  # 주눈금
        ax.xaxis.set_minor_locator(MonthLocator(interval=1))  # 보조 눈금
        ax.set_ylim([0, df.values[row].astype(float).max() + df.values[row].astype(float).max() * 0.07])  # y축 값 범위 설정
        ax.get_yaxis().get_major_formatter().set_scientific(False)  # 숫자 지수형 변환 X

        canvas.draw()


    # 그래프 초기화
    def reset(self):
        self.label_3.clear()
        self.fig.clear(True)
        self.fig2.clear(True)
        self.fig3.clear(True)
        self.canvas.draw()
        self.canvas2.draw()
        self.canvas3.draw()


    # 그래프 출력
    def show_graph(self, fig, canvas):
        file_path = FilePathClass()
        # 그래프 이미지 저장
        savepath = file_path.get_result_path() + 'graph\\'

        if file_path.is_path_exist_check(savepath) == False:
            file_path.make_path(savepath)

        # 민원 급등 그래프(선, 막대, 산점도)
        if self.tabWidget.currentIndex() == 0:
            df = self.setTblToDf(self.tbl_data1)
            # 컬럼 날짜 형식으로 변경
            df.columns = df.columns + '01'
            df.columns = pd.to_datetime(df.columns).date

            # 그래프 초기화
            fig.clear(True)
            ax = fig.add_subplot(111)

            if self.rdo_line.isChecked():
                self.draw_graph(self.txt_top_n, ax, df, self.canvas, 'line')
            elif self.rdo_bar.isChecked():
                self.draw_graph(self.txt_top_n, ax, df, self.canvas, 'bar')
            elif self.rdo_area.isChecked():
                self.draw_graph(self.txt_top_n, ax, df, self.canvas, 'scatter')

        # 민원 최다 그래프(선, 막대, 산점도)
        elif self.tabWidget.currentIndex() == 1:
            df = self.setTblToDf(self.tbl_data2)
            df.columns = df.columns + '01'
            df.columns = pd.to_datetime(df.columns).date

            # 그래프 초기화
            fig.clear(True)
            ax2 = fig.add_subplot(111)

            if self.rdo_line.isChecked():
                self.draw_graph(self.txt_top_n_2, ax2, df, self.canvas, 'line')
            elif self.rdo_bar.isChecked():
                self.draw_graph(self.txt_top_n_2, ax2, df, self.canvas, 'bar')
            elif self.rdo_area.isChecked():
                self.draw_graph(self.txt_top_n_2, ax2, df, self.canvas, 'scatter')

        # 민원 핵심 그래프(트리맵)
        elif self.tabWidget.currentIndex() == 2:
            df = self.setTblToDf(self.tbl_data3)

            if (self.sort_yy_2.currentText() + self.sort_mm_2.currentText()) in df.columns:
                df = df.sort_values(self.sort_yy_2.currentText() + self.sort_mm_2.currentText(), ascending=False)
                df = df[[self.sort_yy_2.currentText() + self.sort_mm_2.currentText()]]
                # 0인 값을 NaN으로 변경 후 삭제
                import numpy as np
                df = df.replace(0, np.NaN)
                df = df.dropna(axis=0)
                df.columns = df.columns.astype(str) + '01'
                df.columns = pd.to_datetime(df.columns).date

                # 그래프 초기화
                self.label_3.clear()
                fig.clear(True)
                plt.cla()

                #트리맵
                import squarify
                squarify.plot(sizes=df.head(int(self.txt_top_n_3.text())).values,
                              label=df.head(int(self.txt_top_n_3.text())).index, alpha=.5,
                              bar_kwargs=dict(linewidth=1.5, edgecolor="white"))

                plt.savefig(savepath + 'graph_img.png', dpi=100)
                self.label_3.setPixmap(QtGui.QPixmap(savepath + 'graph_img.png'))
            else:
                error_event(em.NO_DATA)

        canvas.draw()


    def draw_graph(self, topn, ax, df, canvas, part):
        if len(df) > 0:
            if part == 'line':
                for i in range(int(topn.text())):
                    ax.plot(df.columns,
                            df.head(int(topn.text())).values[i],
                            label=df.index.values[i], alpha=0.5, linewidth=2)
            elif part == 'bar':
                df.head(int(topn.text())).T.plot.bar(figsize=(10, 5), ax=ax, alpha=0.5)
                ax.xaxis.set_visible(False)
            elif part == 'scatter':
                for i in range(int(topn.text())):
                    ax.scatter(df.columns,
                               df.head(int(topn.text())).values[i].astype(int),
                               label=df.index.values[i], alpha=0.5)

            ax.legend(df.index)
            ax.set_title('월별 키워드 빈도수 추이')
            ax.xaxis.set_major_locator(MonthLocator(interval=math.ceil(len(df.columns) / 12)))  # 주눈금
            ax.xaxis.set_minor_locator(MonthLocator(interval=1))  # 보조 눈금
            ax.set_ylim([0, df.values.astype(float).max() + df.values.astype(float).max() * 0.07])  # y축 값 범위
            ax.get_yaxis().get_major_formatter().set_scientific(False)  # 숫자 지수형 변환 X

            canvas.draw()
        else:
            error_event(em.NO_DATA)


    # 차트 출력
    def show_chart(self):
        try:
            anal_s_date = self.sel_yy_start.currentText() + self.sel_mm_start.currentText()
            anal_e_date = self.sel_yy_end.currentText() + self.sel_mm_end.currentText()

            # 종료 일자가 시작 일자보다 과거인 경우
            if int(anal_e_date) - int(anal_s_date) < 0:
                error_event(em.CHK_DATE)
            else:
                file_path = FilePathClass()

                if self.tabWidget.currentIndex() == 0:
                    df = pd.read_csv(file_path.get_raw_use_path() + '민원_급등키워드\\1차마트_급등.csv')
                elif self.tabWidget.currentIndex() == 1:
                    df = pd.read_csv(file_path.get_raw_use_path() + '민원_최다민원키워드정보\\1차마트_최다.csv')
                elif self.tabWidget.currentIndex() == 2:
                    df = pd.read_csv(file_path.get_raw_use_path() + '민원_핵심키워드\\1차마트_핵심.csv')

                df = df[(df['stdym'] >= int(anal_s_date)) & (df['stdym'] <= int(anal_e_date))]

                df_pivot = df.pivot(index='keyword', columns='stdym', values='freq')

                # 분석 시작 일자가 수집된 데이터에 없는 경우 가장 과거 일자로 변경
                if df_pivot.columns[0] >= int(anal_s_date):
                    anal_s_date = df_pivot.columns[0].astype(str)
                # 분석 종료 일자가 수집된 데이터에 없는 경우 가장 최근 일자로 변경
                if df_pivot.columns[-1] <= int(anal_e_date):
                    anal_e_date = df_pivot.columns[-1].astype(str)

                df_sel = df_pivot.loc[:, anal_s_date:anal_e_date]

                if df_sel.empty == False:
                    # 가장 최근 일자 기준으로 정렬
                    sort_date = df_sel.columns[-1].astype(str)
                    df_sel.columns = df_sel.columns.astype(str)
                    df_sel = df_sel.sort_values(sort_date, ascending=False)

                    for i in df_sel.columns:
                        temp = str(i)[0:4] + "-" + str(i)[4:6]
                        df_sel.rename(columns={i: temp}, inplace=True)

                    # 민원 급등 테이블
                    if self.tabWidget.currentIndex() == 0:
                        self.set_table(df_sel, self.tbl_data1)
                    # 민원 최다 테이블
                    elif self.tabWidget.currentIndex() == 1:
                        self.set_table(df_sel, self.tbl_data2)
                    # 민원 핵심 테이블
                    elif self.tabWidget.currentIndex() == 2:
                        self.set_table(df_sel, self.tbl_data3)

                    return df_sel
                else:
                    error_event(em.NO_DATA)
        except FileNotFoundError:
            error_event(em.NO_DATA)

    
    # 테이블에 값 삽입
    def set_table(self, df, table):
        try:
            table.setRowCount(len(df))
            table.setColumnCount(len(df.columns) + 1)
            table.setHorizontalHeaderItem(0, QTableWidgetItem("키워드"))

            for j in range(0, len(df.columns)):
                table.setHorizontalHeaderItem(j + 1, QTableWidgetItem(df.columns[j]))

            for i in range(0, len(df)):
                table.setItem(i, 0, QTableWidgetItem(df.index[i]))

                for j in range(len(df.columns)):
                    item = QTableWidgetItem()
                    if pd.isna(df[df.columns[j]][i]):
                        item.setData(Qt.DisplayRole, float(0.0))  # 테이블 데이터 실수형으로 설정
                    else:
                        if self.tabWidget.currentIndex() == 1:
                            item.setData(Qt.DisplayRole, round(float(df[df.columns[j]][i]/1000), 0))
                        else:
                            item.setData(Qt.DisplayRole, float(df[df.columns[j]][i]))
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)  # 테이블 텍스트 오른쪽 정렬
                    table.setItem(i, j + 1, item)

        except Exception as e:
            print("set_table_data Error : ", e)


    def retranslateUi(self, frmViewComplaints):
        _translate = QtCore.QCoreApplication.translate
        frmViewComplaints.setWindowTitle(_translate("frmViewComplaints", "민원 키워드 시각화"))
        self.group1.setTitle(_translate("frmViewComplaints", " [ 분석 ] "))
        self.label_5.setText(_translate("frmViewComplaints", "~"))
        self.label_6.setText(_translate("frmViewComplaints", "분석기간: "))
        self.sel_yy_end.setItemText(0, _translate("frmViewComplaints", str(datetime.today().year)))
        self.sel_yy_end.setItemText(1, _translate("frmViewComplaints", str(datetime.today().year-1)))
        self.sel_yy_end.setItemText(2, _translate("frmViewComplaints", str(datetime.today().year-2)))
        self.sel_yy_end.setItemText(3, _translate("frmViewComplaints", str(datetime.today().year-3)))
        self.sel_yy_end.setItemText(4, _translate("frmViewComplaints", str(datetime.today().year-4)))
        self.sel_yy_end.setItemText(5, _translate("frmViewComplaints", str(datetime.today().year-5)))
        self.sel_mm_start.setItemText(0, _translate("frmViewComplaints", "01"))
        self.sel_mm_start.setItemText(1, _translate("frmViewComplaints", "02"))
        self.sel_mm_start.setItemText(2, _translate("frmViewComplaints", "03"))
        self.sel_mm_start.setItemText(3, _translate("frmViewComplaints", "04"))
        self.sel_mm_start.setItemText(4, _translate("frmViewComplaints", "05"))
        self.sel_mm_start.setItemText(5, _translate("frmViewComplaints", "06"))
        self.sel_mm_start.setItemText(6, _translate("frmViewComplaints", "07"))
        self.sel_mm_start.setItemText(7, _translate("frmViewComplaints", "08"))
        self.sel_mm_start.setItemText(8, _translate("frmViewComplaints", "09"))
        self.sel_mm_start.setItemText(9, _translate("frmViewComplaints", "10"))
        self.sel_mm_start.setItemText(10, _translate("frmViewComplaints", "11"))
        self.sel_mm_start.setItemText(11, _translate("frmViewComplaints", "12"))
        self.sel_yy_start.setItemText(0, _translate("frmViewComplaints", str(datetime.today().year)))
        self.sel_yy_start.setItemText(1, _translate("frmViewComplaints", str(datetime.today().year-1)))
        self.sel_yy_start.setItemText(2, _translate("frmViewComplaints", str(datetime.today().year-2)))
        self.sel_yy_start.setItemText(3, _translate("frmViewComplaints", str(datetime.today().year-3)))
        self.sel_yy_start.setItemText(4, _translate("frmViewComplaints", str(datetime.today().year-4)))
        self.sel_yy_start.setItemText(5, _translate("frmViewComplaints", str(datetime.today().year-5)))
        self.sel_mm_end.setItemText(0, _translate("frmViewComplaints", "01"))
        self.sel_mm_end.setItemText(1, _translate("frmViewComplaints", "02"))
        self.sel_mm_end.setItemText(2, _translate("frmViewComplaints", "03"))
        self.sel_mm_end.setItemText(3, _translate("frmViewComplaints", "04"))
        self.sel_mm_end.setItemText(4, _translate("frmViewComplaints", "05"))
        self.sel_mm_end.setItemText(5, _translate("frmViewComplaints", "06"))
        self.sel_mm_end.setItemText(6, _translate("frmViewComplaints", "07"))
        self.sel_mm_end.setItemText(7, _translate("frmViewComplaints", "08"))
        self.sel_mm_end.setItemText(8, _translate("frmViewComplaints", "09"))
        self.sel_mm_end.setItemText(9, _translate("frmViewComplaints", "10"))
        self.sel_mm_end.setItemText(10, _translate("frmViewComplaints", "11"))
        self.sel_mm_end.setItemText(11, _translate("frmViewComplaints", "12"))
        self.sel_yy_end.setCurrentText(str(datetime.today().year))
        self.sel_mm_end.setCurrentText(str(datetime.today().month))
        self.sel_yy_start.setCurrentText(str(datetime.today().year))
        self.btn_search.setText(_translate("frmViewComplaints", "조회"))
        self.group2.setTitle(_translate("frmViewComplaints", " [ 데이터 현황 ] "))
        item = self.tbl_data1.horizontalHeaderItem(0)
        item.setText(_translate("frmViewComplaints", "키워드"))
        self.group3.setTitle(_translate("frmViewComplaints", " [ 그래프 ] "))
        self.rdo_line.setText(_translate("frmViewComplaints", "Line"))
        self.rdo_bar.setText(_translate("frmViewComplaints", "Bar"))
        self.rdo_area.setText(_translate("frmViewComplaints", "Scatter"))
        self.label_8.setText(_translate("frmViewComplaints", "Top N :"))
        self.btn_print.setText(_translate("frmViewComplaints", "조회"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rise), _translate("frmViewComplaints", "민원_급등"))
        item = self.tbl_data2.horizontalHeaderItem(0)
        item.setText(_translate("frmViewComplaints", "키워드"))
        self.group3_2.setTitle(_translate("frmViewComplaints", " [ 그래프 ] "))
        self.label_9.setText(_translate("frmViewComplaints", "Top N :"))
        self.btn_print_2.setText(_translate("frmViewComplaints", "조회"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dftop), _translate("frmViewComplaints", "민원_최다"))
        item = self.tbl_data3.horizontalHeaderItem(0)
        item.setText(_translate("frmViewComplaints", "키워드"))
        self.group3_3.setTitle(_translate("frmViewComplaints", " [ 그래프 ] "))
        self.label_10.setText(_translate("frmViewComplaints", "Tree Map"))
        self.btn_print_3.setText(_translate("frmViewComplaints", "조회"))
        self.label_3.setText(_translate("frmViewComplaints", ""))
        self.label_12.setText(_translate("frmViewComplaints", "Top N :"))
        self.sort_yy_2.setItemText(0, _translate("frmViewComplaints", str(datetime.today().year)))
        self.sort_yy_2.setItemText(1, _translate("frmViewComplaints", str(datetime.today().year-1)))
        self.sort_yy_2.setItemText(2, _translate("frmViewComplaints", str(datetime.today().year-2)))
        self.sort_yy_2.setItemText(3, _translate("frmViewComplaints", str(datetime.today().year-3)))
        self.sort_yy_2.setItemText(4, _translate("frmViewComplaints", str(datetime.today().year-4)))
        self.sort_yy_2.setItemText(5, _translate("frmViewComplaints", str(datetime.today().year-5)))
        self.label_13.setText(_translate("frmViewComplaints", "선택년월 :"))
        self.sort_mm_2.setItemText(0, _translate("frmViewComplaints", "01"))
        self.sort_mm_2.setItemText(1, _translate("frmViewComplaints", "02"))
        self.sort_mm_2.setItemText(2, _translate("frmViewComplaints", "03"))
        self.sort_mm_2.setItemText(3, _translate("frmViewComplaints", "04"))
        self.sort_mm_2.setItemText(4, _translate("frmViewComplaints", "05"))
        self.sort_mm_2.setItemText(5, _translate("frmViewComplaints", "06"))
        self.sort_mm_2.setItemText(6, _translate("frmViewComplaints", "07"))
        self.sort_mm_2.setItemText(7, _translate("frmViewComplaints", "08"))
        self.sort_mm_2.setItemText(8, _translate("frmViewComplaints", "09"))
        self.sort_mm_2.setItemText(9, _translate("frmViewComplaints", "10"))
        self.sort_mm_2.setItemText(10, _translate("frmViewComplaints", "11"))
        self.sort_mm_2.setItemText(11, _translate("frmViewComplaints", "12"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_top), _translate("frmViewComplaints", "민원_핵심"))


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
    frmViewComplaints = QtWidgets.QDialog()
    ui = Ui_frmViewComplaints()
    ui.setupUi(frmViewComplaints)
    frmViewComplaints.show()

    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

    sys.exit(app.exec_())
