import pandas as pd
import matplotlib

from matplotlib import pyplot as plt
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QTableWidgetItem

from common.config.filepassclass import FilePathClass
from source.get_api_data_rent_loan_rate import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        # UI 크기 고정
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 968)
        Dialog.setMinimumSize(QtCore.QSize(1024, 968))
        Dialog.setMaximumSize(QtCore.QSize(1024, 968))

        self.group1 = QtWidgets.QGroupBox(Dialog)
        self.group1.setGeometry(QtCore.QRect(10, 10, 1001, 61))
        self.group1.setObjectName("group1")
        # 데이터 수집 버튼
        self.btn_collect = QtWidgets.QPushButton(self.group1)
        self.btn_collect.setGeometry(QtCore.QRect(110, 23, 79, 24))
        self.btn_collect.setObjectName("btn_collect")
        # 데이터 수집 라벨
        self.lbl_collect = QtWidgets.QLabel(self.group1)
        self.lbl_collect.setGeometry(QtCore.QRect(30, 23, 79, 24))
        self.lbl_collect.setObjectName("lbl_collect")

        self.group3 = QtWidgets.QGroupBox(Dialog)
        self.group3.setGeometry(QtCore.QRect(10, 400, 1001, 560))
        self.group3.setObjectName("group3")
        # 라벨 topN
        self.lbl_topN = QtWidgets.QLabel(self.group3)
        self.lbl_topN.setGeometry(QtCore.QRect(20, 26, 51, 16))
        self.lbl_topN.setObjectName("lbl_topN")
        # TopN 텍스트 입력
        self.txt_top_n = QtWidgets.QLineEdit(self.group3)
        self.txt_top_n.setGeometry(QtCore.QRect(70, 20, 61, 24))
        self.txt_top_n.setAcceptDrops(True)
        self.txt_top_n.setToolTip("")
        self.txt_top_n.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_top_n.setObjectName("txt_top_n")
        self.txt_top_n.setValidator(QIntValidator())  # 정수만 입력 가능
        self.txt_top_n.setText('5')
        # 그래프 출력 버튼
        self.btn_print = QtWidgets.QPushButton(self.group3)
        self.btn_print.setGeometry(QtCore.QRect(140, 19, 79, 24))
        self.btn_print.setObjectName("btn_print")
        # 그래프 출력 공간
        self.gridLayoutWidget = QtWidgets.QWidget(self.group3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 981, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.gridLayout.addWidget(self.canvas)
        
        self.group2 = QtWidgets.QGroupBox(Dialog)
        self.group2.setGeometry(QtCore.QRect(10, 80, 1001, 311))
        self.group2.setObjectName("group2")
        # 테이블 출력 공간
        self.tbl_data = QtWidgets.QTableWidget(self.group2)
        self.tbl_data.setGeometry(QtCore.QRect(10, 20, 981, 281))
        self.tbl_data.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 테이블 수정 불가
        self.tbl_data.setObjectName("tbl_data")
        self.tbl_data.setColumnCount(11)
        self.tbl_data.setRowCount(0)
        # 테이블 스타일 지정
        self.tbl_data.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        item = QtWidgets.QTableWidgetItem()
        self.tbl_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_data.setHorizontalHeaderItem(10, item)
        self.tbl_data.verticalHeader().setDefaultSectionSize(25)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btn_collect.clicked.connect(self.get_data)  # 데이터 수집
        self.set_data()  # 데이터프레임 생성
        self.get_table()  # 테이블 출력
        self.btn_print.clicked.connect(self.get_graph)  # 그래프 출력


    # 데이터프레임 생성
    def set_data(self):
        file_path = FilePathClass()

        df = pd.read_csv(file_path.get_data_path() + "test\\" + 'test__20230119.csv')
        df = df.drop(columns='callCenter')
        df.columns = ['시작연월일', '적용금리1', '가산금리2', '적용금리2', '기준금리1', '부분보증비율2',
                      '가산금리1', '기준금리2', '부분보증비율1', '종료연월일', '은행명']
        df = df[['시작연월일', '종료연월일', '은행명', '부분보증비율1', '기준금리1', '가산금리1',
                 '적용금리1', '부분보증비율2', '기준금리2', '가산금리2', '적용금리2']]

        df['시작연월일'] = df['시작연월일'].astype('str')
        df['시작연월일'] = pd.to_datetime(df['시작연월일'], format='%Y-%m-%d').astype(str)
        df['종료연월일'] = df['종료연월일'].astype('str')
        df['종료연월일'] = pd.to_datetime(df['종료연월일'], format='%Y-%m-%d').astype(str)

        return df

    
    # 데이터 수집
    def get_data(self):
        data = get_rent_loan_rate_page()
        self.get_table()

        return data


    # 테이블 출력
    def get_table(self):
        df = self.set_data()
        self.tbl_data.setRowCount(len(df))
        self.tbl_data.setColumnCount(len(df.columns))

        # 테이블에 값 삽입
        for i in range(len(df)):
            for j in range(len(df.columns)):
                item = QTableWidgetItem()
                item.setData(Qt.DisplayRole, str(df[df.columns[j]][i]))
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)  # 테이블 텍스트 정렬

                self.tbl_data.setItem(i, j, item)


    # 그래프 출력
    def get_graph(self):
        self.fig.clear(True)  # 그래프 초기화
        ax = self.fig.add_subplot(111)

        data = self.set_data()
        data = data.sort_values('적용금리1', ascending=False)
        data = data.head(int(self.txt_top_n.text()))
        data = data.reset_index(drop=True)
        ax.tick_params(axis='x', rotation=45)
        ax.bar(data['은행명'].str[:-2], data['적용금리1'].astype(float), alpha=0.5)

        # 그래프에 값 출력
        for i, v in enumerate(data['은행명']):
            ax.text(i, data['적용금리1'][i], data['적용금리1'][i],
                    horizontalalignment='center', verticalalignment='bottom')

        self.canvas.draw()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.group1.setTitle(_translate("Dialog", " [ 전세자금 대출 금리 ] "))
        self.btn_collect.setText(_translate("Dialog", "수집"))
        self.lbl_collect.setText(_translate("Dialog", "데이터 수집"))
        self.group3.setTitle(_translate("Dialog", " [ 그래프 ] "))
        self.lbl_topN.setText(_translate("Dialog", "Top N :"))
        self.btn_print.setText(_translate("Dialog", "조회"))
        self.group2.setTitle(_translate("Dialog", " [ 데이터 현황 ] "))
        self.tbl_data.setSortingEnabled(True)
        item = self.tbl_data.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "시작연월일"))
        item = self.tbl_data.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "종료연월일"))
        item = self.tbl_data.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "은행명"))
        item = self.tbl_data.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "부분보증비율1"))
        item = self.tbl_data.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "기준금리1"))
        item = self.tbl_data.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "가산금리1"))
        item = self.tbl_data.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "적용금리1"))
        item = self.tbl_data.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "부분보증비율2"))
        item = self.tbl_data.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "기준금리2"))
        item = self.tbl_data.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "가산금리2"))
        item = self.tbl_data.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "적용금리2"))


if __name__ == "__main__":
    import sys

    # 에러 발생 > 에러 출력(강제 종료 X)
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
