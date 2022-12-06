import os
import pandas as pd
from matplotlib import pyplot as plt
from wordcloud import WordCloud

from PyQt5 import QtCore, QtGui, QtWidgets

from common.config.filepassclass import FilePathClass


class Ui_frmComplaintWC(object):
    def setupUi(self, frmComplaintWC):
        frmComplaintWC.setObjectName("frmComplaintWC")
        frmComplaintWC.resize(1024, 968)
        frmComplaintWC.setMaximumSize(1024, 968)
        self.gridLayoutWidget = QtWidgets.QWidget(frmComplaintWC)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 1005, 931))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridlayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setObjectName("gridlayout")
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(7, 19, 481, 71))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(7, 100, 481, 350))
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_2.setGeometry(QtCore.QRect(7, 19, 481, 71))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(7, 100, 481, 361))
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_3.setGeometry(QtCore.QRect(7, 19, 481, 71))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(7, 100, 481, 361))
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.listWidget_4 = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_4.setGeometry(QtCore.QRect(7, 19, 481, 71))
        self.listWidget_4.setObjectName("listWidget_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(7, 100, 481, 361))
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(frmComplaintWC)
        self.label_5.setGeometry(QtCore.QRect(15, 5, 291, 18))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(frmComplaintWC)
        QtCore.QMetaObject.connectSlotsByName(frmComplaintWC)

        self.show_list()

        self.listWidget.itemClicked.connect(self.show_wc)
        self.listWidget_2.itemClicked.connect(self.show_wc2)
        self.listWidget_3.itemClicked.connect(self.show_wc3)
        self.listWidget_4.itemClicked.connect(self.show_wc4)

    def show_wc(self):
        file_path = FilePathClass()
        path = file_path.get_raw_use_path()

        df = pd.read_csv(path + '민원_연관어분석정보_' + self.listWidget.currentItem().text() + '.csv')
        wc = df.set_index('label').to_dict()['value']
        wordCloud = WordCloud(
            font_path="malgun",
            width=450,
            height=350,
            max_font_size=80,
            background_color='white'
        ).generate_from_frequencies(wc)
        plt.figure(figsize=(5,5))
        plt.imshow(wordCloud)
        plt.axis('off')
        plt.savefig('wc1.png', dpi=100)
        self.label.setPixmap(QtGui.QPixmap('wc1.png'))

    def show_wc2(self):
        file_path = FilePathClass()
        path = file_path.get_raw_use_path()

        df = pd.read_csv(path + '민원_연관어분석정보_' + self.listWidget_2.currentItem().text() + '.csv')
        wc = df.set_index('label').to_dict()['value']
        wordCloud = WordCloud(
            font_path="malgun",
            width=450,
            height=350,
            max_font_size=80,
            background_color='white'
        ).generate_from_frequencies(wc)
        plt.figure(figsize=(5,5))
        plt.imshow(wordCloud)
        plt.axis('off')
        plt.savefig('wc2.png', dpi=100)
        self.label_2.setPixmap(QtGui.QPixmap('wc2.png'))

    def show_wc3(self):
        file_path = FilePathClass()
        path = file_path.get_raw_use_path()

        df = pd.read_csv(path + '민원_연관어분석정보_' + self.listWidget_3.currentItem().text() + '.csv')
        wc = df.set_index('label').to_dict()['value']
        wordCloud = WordCloud(
            font_path="malgun",
            width=450,
            height=350,
            max_font_size=80,
            background_color='white'
        ).generate_from_frequencies(wc)
        plt.figure(figsize=(5,5))
        plt.imshow(wordCloud)
        plt.axis('off')
        plt.savefig('wc3.png', dpi=100)
        self.label_3.setPixmap(QtGui.QPixmap('wc3.png'))

    def show_wc4(self):
        file_path = FilePathClass()
        path = file_path.get_raw_use_path()

        df = pd.read_csv(path + '민원_연관어분석정보_' + self.listWidget_4.currentItem().text() + '.csv')
        wc = df.set_index('label').to_dict()['value']
        wordCloud = WordCloud(
            font_path="malgun",
            width=450,
            height=350,
            max_font_size=80,
            background_color='white'
        ).generate_from_frequencies(wc)
        plt.figure(figsize=(5,5))
        plt.imshow(wordCloud)
        plt.axis('off')
        plt.savefig('wc4.png', dpi=100)
        self.label_4.setPixmap(QtGui.QPixmap('wc4.png'))


    def show_list(self):
        file_path = FilePathClass()
        path = file_path.get_raw_use_path()
        data_all_list = os.listdir(path)
        data_list = []

        for i in range(len(data_all_list)):
            filename = data_all_list[i].split('_')
            if (data_all_list[i][-3:] == 'csv') & (filename[1] == '연관어분석정보'):
                data_list.append(data_all_list[i])
        for i in range(len(data_list)):
            dataname = data_list[i].split('_')
            self.listWidget.addItem(dataname[2][:-4])
            self.listWidget_2.addItem(dataname[2][:-4])
            self.listWidget_3.addItem(dataname[2][:-4])
            self.listWidget_4.addItem(dataname[2][:-4])


    def retranslateUi(self, frmComplaintWC):
        _translate = QtCore.QCoreApplication.translate
        frmComplaintWC.setWindowTitle(_translate("frmComplaintWC", "민원 연관어 분석"))
        self.groupBox.setTitle(_translate("frmComplaintWC", "  Word Cloud 1  "))
        self.label.setText(_translate("frmComplaintWC", ""))
        self.groupBox_2.setTitle(_translate("frmComplaintWC", "  Word Cloud 2  "))
        self.label_2.setText(_translate("frmComplaintWC", ""))
        self.groupBox_3.setTitle(_translate("frmComplaintWC", "  Word Cloud 3 "))
        self.label_3.setText(_translate("frmComplaintWC", ""))
        self.groupBox_4.setTitle(_translate("frmComplaintWC", "  Word Cloud 4  "))
        self.label_4.setText(_translate("frmComplaintWC", ""))
        self.label_5.setText(_translate("frmComplaintWC", "[ 민원 연관어분석 정보 ]"))


if __name__ == "__main__":
    import sys

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
