import os
from datetime import datetime

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QValidator, QIntValidator
from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox
#from pyqt_checkbox_table_widget.checkBoxTableWidget import CheckBoxTableWidget

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from common.config.filepassclass import FilePathClass


class Ui_frmViewComplaints(object):
    def setupUi(self, frmViewComplaints):
        frmViewComplaints.setObjectName("frmViewComplaints")
        frmViewComplaints.resize(1024, 968)
        frmViewComplaints.setMaximumSize(1024, 968)
        self.group1 = QtWidgets.QGroupBox(frmViewComplaints)
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
        self.group2 = QtWidgets.QGroupBox(frmViewComplaints)
        self.group2.setGeometry(QtCore.QRect(10, 80, 1001, 881))
        self.group2.setObjectName("group2")
        self.tabWidget = QtWidgets.QTabWidget(self.group2)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 981, 851))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_rise = QtWidgets.QWidget()
        self.tab_rise.setObjectName("tab_rise")
        self.tbl_data1 = QtWidgets.QTableWidget(self.tab_rise)
        self.tbl_data1.setGeometry(QtCore.QRect(0, 0, 971, 241))
        self.tbl_data1.setObjectName("tbl_data1")
        self.tbl_data1.setColumnCount(1)
        self.tbl_data1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data1.setHorizontalHeaderItem(0, item)
        self.tbl_data1.horizontalHeader().setStretchLastSection(False)
        self.tbl_data1.verticalHeader().setDefaultSectionSize(25)
        self.tbl_data1.verticalHeader().setStretchLastSection(False)
        self.group3 = QtWidgets.QGroupBox(self.tab_rise)
        self.group3.setGeometry(QtCore.QRect(3, 250, 968, 570))
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
        self.btn_print.setGeometry(QtCore.QRect(880, 19, 79, 24))
        self.btn_print.setObjectName("btn_print")
        self.gridLayoutWidget = QtWidgets.QWidget(self.group3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(7, 50, 954, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.group3)
        self.label.setGeometry(QtCore.QRect(10, 51, 951, 500))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_rise, "")
        self.tab_dftop = QtWidgets.QWidget()
        self.tab_dftop.setObjectName("tab_dftop")
        self.tbl_data2 = QtWidgets.QTableWidget(self.tab_dftop)
        self.tbl_data2.setGeometry(QtCore.QRect(0, 0, 971, 241))
        self.tbl_data2.setObjectName("tbl_data2")
        self.tbl_data2.setColumnCount(1)
        self.tbl_data2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data2.setHorizontalHeaderItem(0, item)
        self.tbl_data2.horizontalHeader().setStretchLastSection(False)
        self.tbl_data2.verticalHeader().setDefaultSectionSize(25)
        self.tbl_data2.verticalHeader().setStretchLastSection(False)
        self.group3_2 = QtWidgets.QGroupBox(self.tab_dftop)
        self.group3_2.setGeometry(QtCore.QRect(3, 250, 968, 570))
        self.group3_2.setObjectName("group3_2")
        self.rdo_line_2 = QtWidgets.QRadioButton(self.group3_2)
        self.rdo_line_2.setGeometry(QtCore.QRect(20, 26, 86, 16))
        self.rdo_line_2.setObjectName("rdo_line_2")
        self.rdo_line_2.setChecked(True)
        self.rdo_bar_2 = QtWidgets.QRadioButton(self.group3_2)
        self.rdo_bar_2.setGeometry(QtCore.QRect(80, 26, 86, 16))
        self.rdo_bar_2.setObjectName("rdo_bar_2")
        self.rdo_area_2 = QtWidgets.QRadioButton(self.group3_2)
        self.rdo_area_2.setGeometry(QtCore.QRect(138, 26, 86, 16))
        self.rdo_area_2.setObjectName("rdo_area_2")
        self.label_9 = QtWidgets.QLabel(self.group3_2)
        self.label_9.setGeometry(QtCore.QRect(220, 26, 51, 16))
        self.label_9.setObjectName("label_9")
        self.txt_top_n_2 = QtWidgets.QLineEdit(self.group3_2)
        self.txt_top_n_2.setGeometry(QtCore.QRect(270, 20, 61, 24))
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
        self.label_2 = QtWidgets.QLabel(self.group3_2)
        self.label_2.setGeometry(QtCore.QRect(10, 51, 951, 500))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_dftop, "")
        self.tab_top = QtWidgets.QWidget()
        self.tab_top.setObjectName("tab_top")
        self.tbl_data3 = QtWidgets.QTableWidget(self.tab_top)
        self.tbl_data3.setGeometry(QtCore.QRect(0, 0, 971, 241))
        self.tbl_data3.setObjectName("tbl_data3")
        self.tbl_data3.setColumnCount(1)
        self.tbl_data3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data3.setHorizontalHeaderItem(0, item)
        self.tbl_data3.horizontalHeader().setStretchLastSection(False)
        self.tbl_data3.verticalHeader().setDefaultSectionSize(25)
        self.tbl_data3.verticalHeader().setStretchLastSection(False)
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

        self.label.setAlignment(Qt.AlignCenter)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.retranslateUi(frmViewComplaints)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmViewComplaints)

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.gridLayout.addWidget(self.canvas)
        self.fig2 = plt.Figure()
        self.canvas2 = FigureCanvas(self.fig2)
        self.gridLayout_2.addWidget(self.canvas2)
        self.fig3 = plt.Figure()
        self.canvas3 = FigureCanvas(self.fig3)
        self.gridLayout_3.addWidget(self.canvas3)

        self.txt_top_n.setValidator(QIntValidator())
        self.txt_top_n.setText('5')
        self.txt_top_n_2.setValidator(QIntValidator())
        self.txt_top_n_2.setText('5')
        self.txt_top_n_3.setValidator(QIntValidator())
        self.txt_top_n_3.setText('5')

        self.btn_search.clicked.connect(self.show_chart)
        self.btn_print.clicked.connect(self.show_graph)
        self.btn_print_2.clicked.connect(self.show_graph)
        self.btn_print_3.clicked.connect(self.show_graph)


    # 그래프 출력
    def show_graph(self):
        df = self.show_chart()

        # 민원 급등
        if self.tabWidget.currentIndex() == 0:
            df.columns = df.columns + '01'
            df.columns = pd.to_datetime(df.columns).date

            self.label.clear()
            self.fig.clear(True)
            ax = self.fig.add_subplot(111)

            if self.rdo_line.isChecked():
                for i in range(int(self.txt_top_n.text())):
                    ax.plot(df.columns,
                            df.head(int(self.txt_top_n.text())).values[i].astype(int),
                            label=df.index.values[i], alpha=0.5, linewidth=2)
                ax.grid(True)
                ax.legend()
                ax.set_title('월별 키워드 빈도수 추이')
                ax.set_xticks(df.columns)
                ax.set_xticklabels(df.columns, rotation=15)
                ax.set_ylim([0, df.values.astype(int).max() + 5000])

                self.canvas.draw()

            elif self.rdo_bar.isChecked():
                df.head(int(self.txt_top_n.text())).T.plot.bar(figsize=(10, 5), alpha=0.5)
                plt.xticks(rotation=15)
                plt.legend(df.head(int(self.txt_top_n.text())).T.columns)
                plt.ylim([0, df.values.astype(int).max() + 5000])
                plt.title('월별 키워드 빈도수 추이')
                plt.savefig('graph_img.png', dpi=100)
                self.label.setPixmap(QtGui.QPixmap('graph_img.png'))

            elif self.rdo_area.isChecked():
                for i in range(int(self.txt_top_n.text())):
                    ax.scatter(df.columns,
                               df.head(int(self.txt_top_n.text())).values[i].astype(int),
                               label=df.index.values[i], alpha=0.5)
                ax.grid(True)
                ax.legend()
                ax.set_title('월별 키워드 빈도수 추이')
                ax.set_xticks(df.columns)
                ax.set_xticklabels(df.columns, rotation=15)
                ax.set_ylim([0, df.values.astype(int).max() + 5000])

                self.canvas.draw()

        # 민원 최다
        elif self.tabWidget.currentIndex() == 1:
            df.columns = df.columns + '01'
            df.columns = pd.to_datetime(df.columns).date

            self.label_2.clear()
            self.fig2.clear(True)
            ax2 = self.fig2.add_subplot(111)

            if self.rdo_line_2.isChecked():
                for i in range(int(self.txt_top_n_2.text())):
                    ax2.plot(df.columns,
                            df.head(int(self.txt_top_n_2.text())).values[i].astype(int),
                            label=df.index.values[i], alpha=0.5, linewidth=2)
                ax2.grid(True)
                ax2.legend()
                ax2.set_title('월별 키워드 빈도수 추이')
                ax2.set_xticks(df.columns)
                ax2.set_xticklabels(df.columns, rotation=15)
                ax2.set_ylim([0, df.values.astype(int).max() + 5000])

                self.canvas2.draw()

            elif self.rdo_bar_2.isChecked():
                df.head(int(self.txt_top_n_2.text())).T.plot.bar(figsize=(10, 5), alpha=0.5)
                plt.xticks(rotation=15)
                plt.legend(df.head(int(self.txt_top_n_2.text())).T.columns)
                plt.ylim([0, df.values.astype(int).max() + 5000])
                plt.title('월별 키워드 빈도수 추이')
                plt.savefig('graph_img.png', dpi=100)
                self.label_2.setPixmap(QtGui.QPixmap('graph_img.png'))

            elif self.rdo_area_2.isChecked():
                for i in range(int(self.txt_top_n_2.text())):
                    ax2.scatter(df.columns,
                               df.head(int(self.txt_top_n_2.text())).values[i].astype(int),
                               label=df.index.values[i], alpha=0.5)
                ax2.grid(True)
                ax2.legend()
                ax2.set_title('월별 키워드 빈도수 추이')
                ax2.set_xticks(df.columns)
                ax2.set_xticklabels(df.columns, rotation=15)
                ax2.set_ylim([0, df.values.astype(int).max() + 5000])

                self.canvas2.draw()

        # 민원 핵심
        elif self.tabWidget.currentIndex() == 2:
            df = df[[self.sort_yy_2.currentText() + self.sort_mm_2.currentText()]]
            df = df.dropna(axis = 0)
            # df = df.fillna(0)
            # df = df.apply(lambda x: x + 0.000001)
            df.columns = df.columns.astype(str) + '01'
            df.columns = pd.to_datetime(df.columns).date
            self.label_3.clear()
            self.fig3.clear(True)
            plt.cla()
            import squarify
            squarify.plot(sizes=df.head(int(self.txt_top_n_3.text())).values.astype(float),
                          label=df.head(int(self.txt_top_n_3.text())).index, alpha=.5,
                          bar_kwargs=dict(linewidth=1.5, edgecolor="white"))
            # df.head(int(self.txt_top_n_3.text())).T.plot.bar(figsize=(10, 5), alpha=0.5)
            # plt.xticks(rotation=15)
            # plt.legend(df.head(int(self.txt_top_n_3.text())).T.columns)
            # plt.ylim([0, df.values.astype(int).max() + 5000])
            # plt.title('월별 키워드 빈도수 추이')
            plt.savefig('graph_img.png', dpi=100)
            self.label_3.setPixmap(QtGui.QPixmap('graph_img.png'))

            self.canvas3.draw()

            # self.label_3.clear()
            # self.fig3.clear(True)
            # plt.cla()
            #
            # import seaborn as sns
            # ax3 = sns.heatmap(df.head(int(self.txt_top_n_3.text())), annot=True, fmt='.0f',
            #                   cbar=False, cmap='Blues')
            # plt.yticks(rotation=0)
            # plt.ylabel('')
            # plt.savefig('heatmap_img.png', dpi=105)
            # self.label_3.setPixmap(QtGui.QPixmap('heatmap_img.png'))


    # 차트 출력
    def show_chart(self):
        file_path = FilePathClass()

        # if self.tabWidget.currentIndex() == 3:
        #     path = file_path.get_raw_use_path()
        #     data_all_list = os.listdir(path)
        #     data_list = []
        #
        #     self.checkBoxList = []
        #
        #     for i in range(len(data_all_list)):
        #         filename = data_all_list[i].split('_')
        #         if (data_all_list[i][-3:] == 'csv') & (filename[1] == '연관어분석정보'):
        #             data_list.append(data_all_list[i])
        #     self.tbl_data4.setRowCount(len(data_list))
        #     self.tbl_data4.setColumnCount(2)
        #     for i in range(len(data_list)):
        #         ckbox = QCheckBox()
        #         self.checkBoxList.append(ckbox)
        #
        #     for i in range(len(data_list)):
        #         # self.tbl_data4.setCellWidget(i, 0, self.checkBoxList[i])
        #         dataname = data_list[i].split('_')
        #         self.tbl_data4.setItem(i, 1, QTableWidgetItem(dataname[2][:-4]))
        #     #     if self.checkBoxList[i].stateChanged():
        #     #         print('!')
        #     #     else:
        #     #         print('--')
        #         # self.item = MyQTableWidgetItemCheckBox()
        #         # self.tbl_data4.setItem(i, 0, self.item)
        #         # self.chbox = MyCheckBox(self.item)
        #         # self.tbl_data4.setCellWidget(i, 0, self.chbox)
        #         # print(self.chbox.checkState())
        #         # print(self.cellclicked(self.chbox.checkState()))
        #         # self.chbox.stateChanged.connect(self.cellclicked)
        #         # self.cellclicked()
        #         # if self.chbox.stateChanged.connect(self.cellclicked) == 2:
        #         #     print(i)
        #         # else:
        #         #     print(self.chbox.stateChanged.connect(self.cellclicked))
        #         # if self.chbox.checkState() == :
        #         #     self.cellclicked(self.chbox.checkState(), i)
        #
        #     for i in range(len(data_list)):
        #         self.checkBoxList[i].stateChanged.connect(lambda : self.cellclicked(i, self.checkBoxList[i].checkState()))
        #
        #     # self.tbl_data4.resizeColumnsToContents()
        #     self.tbl_data4.setColumnWidth(0, 5)
        #     self.tbl_data4.setColumnWidth(1, 100)


        if self.tabWidget.currentIndex() == 0:
            df = pd.read_csv(file_path.get_raw_use_path() + '민원_급등키워드\\1차마트_급등.csv')
        elif self.tabWidget.currentIndex() == 1:
            df = pd.read_csv(file_path.get_raw_use_path() + '민원_최다민원키워드정보\\1차마트_최다.csv')
        elif self.tabWidget.currentIndex() == 2:
            df = pd.read_csv(file_path.get_raw_use_path() + '민원_핵심키워드\\1차마트_핵심.csv')

        df_pivot = df.pivot(index='keyword', columns='stdym', values='freq')

        anal_s_date = self.sel_yy_start.currentText() + self.sel_mm_start.currentText()
        anal_e_date = self.sel_yy_end.currentText() + self.sel_mm_end.currentText()
        sort_date = self.sort_yy.currentText() + self.sort_mm.currentText()

        if df_pivot.columns[0] >= int(anal_s_date):
            anal_s_date = df_pivot.columns[0].astype(str)
        if df_pivot.columns[-1] <= int(anal_e_date):
            anal_e_date = df_pivot.columns[-1].astype(str)

        df_sel = df_pivot.loc[:, anal_s_date:anal_e_date]
        if (int(sort_date) < df_sel.columns[0]) | (int(sort_date) > df_sel.columns[-1]):
            sort_date = df_sel.columns[-1].astype(str)

        df_sel.columns = df_sel.columns.astype(str)
        df_sel = df_sel.sort_values(sort_date, ascending=False)

        # 민원 급등
        if self.tabWidget.currentIndex() == 0:
            self.tbl_data1.setRowCount(len(df_sel))
            self.tbl_data1.setColumnCount(len(df_sel.columns)+1)

            for i in range(len(df_sel)):
                self.tbl_data1.setItem(i, 0, QTableWidgetItem(df_sel.index[i]))
                for j in range(len(df_sel.columns)):
                    if pd.isna(df_sel[df_sel.columns[j]][i]):
                        self.tbl_data1.setItem(i, j+1, QTableWidgetItem('0.0'))
                    else:
                        self.tbl_data1.setItem(i, j+1, QTableWidgetItem(str(df_sel[df_sel.columns[j]][i])))
                    self.tbl_data1.setHorizontalHeaderItem(j+1, QTableWidgetItem(df_sel.columns[j]))

        # 민원 최다
        elif self.tabWidget.currentIndex() == 1:
            self.tbl_data2.setRowCount(len(df_sel))
            self.tbl_data2.setColumnCount(len(df_sel.columns) + 1)

            for i in range(len(df_sel)):
                self.tbl_data2.setItem(i, 0, QTableWidgetItem(df_sel.index[i]))
                for j in range(len(df_sel.columns)):
                    if pd.isna(df_sel[df_sel.columns[j]][i]):
                        self.tbl_data2.setItem(i, j + 1, QTableWidgetItem('0.0'))
                    else:
                        self.tbl_data2.setItem(i, j + 1, QTableWidgetItem(str(df_sel[df_sel.columns[j]][i])))
                    self.tbl_data2.setHorizontalHeaderItem(j + 1, QTableWidgetItem(df_sel.columns[j]))

        # 민원 핵심
        elif self.tabWidget.currentIndex() == 2:
            self.tbl_data3.setRowCount(len(df_sel))
            self.tbl_data3.setColumnCount(len(df_sel.columns) + 1)

            for i in range(len(df_sel)):
                self.tbl_data3.setItem(i, 0, QTableWidgetItem(df_sel.index[i]))
                for j in range(len(df_sel.columns)):
                    if pd.isna(df_sel[df_sel.columns[j]][i]):
                        self.tbl_data3.setItem(i, j + 1, QTableWidgetItem('0.0'))
                    else:
                        self.tbl_data3.setItem(i, j + 1, QTableWidgetItem(str(df_sel[df_sel.columns[j]][i])))
                    self.tbl_data3.setHorizontalHeaderItem(j + 1, QTableWidgetItem(df_sel.columns[j]))

        return df_sel

    # def cellclicked(self, i, state):
    #     print(i)
    #     print(state)
    #     # return i

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
        self.label_7.setText(_translate("frmViewComplaints", "정렬기준 년월 :"))
        self.sort_yy.setItemText(0, _translate("frmViewComplaints", str(datetime.today().year)))
        self.sort_yy.setItemText(1, _translate("frmViewComplaints", str(datetime.today().year-1)))
        self.sort_yy.setItemText(2, _translate("frmViewComplaints", str(datetime.today().year-2)))
        self.sort_yy.setItemText(3, _translate("frmViewComplaints", str(datetime.today().year-3)))
        self.sort_yy.setItemText(4, _translate("frmViewComplaints", str(datetime.today().year-4)))
        self.sort_yy.setItemText(5, _translate("frmViewComplaints", str(datetime.today().year-5)))
        self.sort_mm.setItemText(0, _translate("frmViewComplaints", "01"))
        self.sort_mm.setItemText(1, _translate("frmViewComplaints", "02"))
        self.sort_mm.setItemText(2, _translate("frmViewComplaints", "03"))
        self.sort_mm.setItemText(3, _translate("frmViewComplaints", "04"))
        self.sort_mm.setItemText(4, _translate("frmViewComplaints", "05"))
        self.sort_mm.setItemText(5, _translate("frmViewComplaints", "06"))
        self.sort_mm.setItemText(6, _translate("frmViewComplaints", "07"))
        self.sort_mm.setItemText(7, _translate("frmViewComplaints", "08"))
        self.sort_mm.setItemText(8, _translate("frmViewComplaints", "09"))
        self.sort_mm.setItemText(9, _translate("frmViewComplaints", "10"))
        self.sort_mm.setItemText(10, _translate("frmViewComplaints", "11"))
        self.sort_mm.setItemText(11, _translate("frmViewComplaints", "12"))
        self.group2.setTitle(_translate("frmViewComplaints", " [ 데이터 현황 ] "))
        item = self.tbl_data1.horizontalHeaderItem(0)
        item.setText(_translate("frmViewComplaints", "키워드"))
        self.group3.setTitle(_translate("frmViewComplaints", " [ 그래프 ] "))
        self.rdo_line.setText(_translate("frmViewComplaints", "Line"))
        self.rdo_bar.setText(_translate("frmViewComplaints", "Bar"))
        self.rdo_area.setText(_translate("frmViewComplaints", "Area"))
        self.label_8.setText(_translate("frmViewComplaints", "Top N :"))
        self.btn_print.setText(_translate("frmViewComplaints", "조회"))
        self.label.setText(_translate("frmViewComplaints", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rise), _translate("frmViewComplaints", "민원_급등"))
        item = self.tbl_data2.horizontalHeaderItem(0)
        item.setText(_translate("frmViewComplaints", "키워드"))
        self.group3_2.setTitle(_translate("frmViewComplaints", " [ 그래프 ] "))
        self.rdo_line_2.setText(_translate("frmViewComplaints", "Line"))
        self.rdo_bar_2.setText(_translate("frmViewComplaints", "Bar"))
        self.rdo_area_2.setText(_translate("frmViewComplaints", "Area"))
        self.label_9.setText(_translate("frmViewComplaints", "Top N :"))
        self.btn_print_2.setText(_translate("frmViewComplaints", "조회"))
        self.label_2.setText(_translate("frmViewComplaints", ""))
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