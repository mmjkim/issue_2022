import os
import fnmatch
import pandas as pd
from matplotlib import pyplot as plt
from wordcloud import WordCloud

from PyQt5 import QtCore, QtGui, QtWidgets

from common.config.filepassclass import FilePathClass


class Ui_frmComplaintWC(object):
    def setupUi(self, frmComplaintWC):
        # 화면 크기 설정 및 고정
        frmComplaintWC.setObjectName("frmComplaintWC")
        frmComplaintWC.resize(1024, 968)
        frmComplaintWC.setMaximumSize(1024, 968)
        frmComplaintWC.setMinimumSize(1024, 968)

        self.gridLayoutWidget = QtWidgets.QWidget(frmComplaintWC)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 1005, 931))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridlayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setObjectName("gridlayout")

        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName("groupBox")

        self.sel_keyword_1 = QtWidgets.QComboBox(self.groupBox)
        self.sel_keyword_1.setGeometry(QtCore.QRect(7, 10, 485, 30))
        self.sel_keyword_1.setObjectName("sel_keyword_1")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(7, 50, 485, 400))
        self.label.setObjectName("label")

        self.gridlayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.sel_keyword_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.sel_keyword_2.setGeometry(QtCore.QRect(7, 10, 485, 30))
        self.sel_keyword_2.setObjectName("sel_keyword_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(7, 50, 485, 400))
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox_3 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.sel_keyword_3 = QtWidgets.QComboBox(self.groupBox_3)
        self.sel_keyword_3.setGeometry(QtCore.QRect(7, 10, 485, 30))
        self.sel_keyword_3.setObjectName("sel_keyword_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(7, 50, 485, 400))
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.groupBox_4 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.sel_keyword_4 = QtWidgets.QComboBox(self.groupBox_4)
        self.sel_keyword_4.setGeometry(QtCore.QRect(7, 10, 485, 30))
        self.sel_keyword_4.setObjectName("sel_keyword_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(7, 50, 485, 400))
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.groupBox_4, 1, 1, 1, 1)

        self.label_5 = QtWidgets.QLabel(frmComplaintWC)
        self.label_5.setGeometry(QtCore.QRect(15, 5, 291, 18))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(frmComplaintWC)
        QtCore.QMetaObject.connectSlotsByName(frmComplaintWC)

        # 콤보 박스에 키워드 값 삽입
        self.set_combobox()

        # 워드클라우드 출력
        self.sel_keyword_1.textActivated.connect(
            lambda: self.draw_wordcloud(self.sel_keyword_1.currentText(), self.label))
        self.sel_keyword_2.textActivated.connect(
            lambda: self.draw_wordcloud(self.sel_keyword_2.currentText(), self.label_2))
        self.sel_keyword_3.textActivated.connect(
            lambda: self.draw_wordcloud(self.sel_keyword_3.currentText(), self.label_3))
        self.sel_keyword_4.textActivated.connect(
            lambda: self.draw_wordcloud(self.sel_keyword_4.currentText(), self.label_4))


    def set_combobox(self):
        file_path = FilePathClass()
        path = file_path.get_raw_use_path()
        file_list = os.listdir(path)
        keyword_list = []

        file_name = "민원_연관어분석정보_*.csv"
        csv_all_list = [file for file in file_list if fnmatch.fnmatch(file, file_name)]  # os.listdir(path_file)

        # 연관어분석정보 데이터 파일 리스트에 담기
        for i in range(len(csv_all_list)):
            filename = csv_all_list[i].split('_')
            if (filename[1] == '연관어분석정보'):
                keyword_list.append(csv_all_list[i])
        # 콤보 박스에 키워드 값 삽입
        for i in range(len(keyword_list)):
            dataname = keyword_list[i].split('_')
            self.sel_keyword_1.addItem(dataname[2][:-4])
            self.sel_keyword_2.addItem(dataname[2][:-4])
            self.sel_keyword_3.addItem(dataname[2][:-4])
            self.sel_keyword_4.addItem(dataname[2][:-4])


    def draw_wordcloud(self, keyword, canvas):
        file_path = FilePathClass()
        path = file_path.get_raw_use_path()

        df = pd.read_csv(path + '민원_연관어분석정보_' + keyword + '.csv')
        wc = df.set_index('label').to_dict()['value']
        wordCloud = WordCloud(
            font_path="malgun",
            width=430,
            height=430,
            max_font_size=80,
            background_color='white'
        ).generate_from_frequencies(wc)
        plt.figure(figsize=(5, 5))
        plt.imshow(wordCloud)
        plt.axis('off')
        plt.savefig(keyword + '_wc.png', dpi=100)
        canvas.setPixmap(QtGui.QPixmap(keyword + '_wc.png'))


    def retranslateUi(self, frmComplaintWC):
        _translate = QtCore.QCoreApplication.translate
        frmComplaintWC.setWindowTitle(_translate("frmComplaintWC", "민원 연관어 분석"))
        self.groupBox.setTitle(_translate("frmComplaintWC", ""))
        self.label.setText(_translate("frmComplaintWC", ""))
        self.groupBox_2.setTitle(_translate("frmComplaintWC", ""))
        self.label_2.setText(_translate("frmComplaintWC", ""))
        self.groupBox_3.setTitle(_translate("frmComplaintWC", ""))
        self.label_3.setText(_translate("frmComplaintWC", ""))
        self.groupBox_4.setTitle(_translate("frmComplaintWC", ""))
        self.label_4.setText(_translate("frmComplaintWC", ""))
        self.label_5.setText(_translate("frmComplaintWC", "[ 민원 연관어분석 정보 ]"))


if __name__ == "__main__":
    import sys

    # 에러 발생 > 에러 출력(강제 종료 X)
    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)

    app = QtWidgets.QApplication(sys.argv)
    frmComplaintWC = QtWidgets.QDialog()
    ui = Ui_frmComplaintWC()
    ui.setupUi(frmComplaintWC)
    frmComplaintWC.show()

    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

    sys.exit(app.exec_())
