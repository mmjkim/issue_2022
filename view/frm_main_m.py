from PyQt5 import QtCore, QtGui, QtWidgets
# from rising2 import Ui_rising_win
# from top1 import Ui_top_win
# from today1 import Ui_today_win
# from dftop1 import Ui_dftop_win
from frm_news_api_s import Ui_news_collect_win
from frm_complaint_api_s import Ui_complaint_api_win

class Ui_MainWindow(object):
    def collect_complaint_window(self):
        self.collect_complaint_win = QtWidgets.QMainWindow()
        self.collect_complaint_ui = Ui_complaint_api_win()
        self.collect_complaint_ui.setupUi(self.collect_complaint_win)
        self.collect_complaint_win.show()

    # def top_window(self):
    #     self.top_win = QtWidgets.QMainWindow()
    #     self.top_ui = Ui_top_win()
    #     self.top_ui.setupUi(self.top_win)
    #     self.top_win.show()
    #
    # def today_window(self):
    #     self.today_win = QtWidgets.QMainWindow()
    #     self.today_ui = Ui_today_win()
    #     self.today_ui.setupUi(self.today_win)
    #     self.today_win.show()
    #
    # def dftop_window(self):
    #     self.dftop_win = QtWidgets.QMainWindow()
    #     self.dftop_ui = Ui_dftop_win()
    #     self.dftop_ui.setupUi(self.dftop_win)
    #     self.dftop_win.show()

    def collect_news_window(self):
        self.collect_news_win = QtWidgets.QMainWindow()
        self.collect_news_ui = Ui_news_collect_win()
        self.collect_news_ui.setupUi(self.collect_news_win)
        self.collect_news_win.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 586)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 26))
        self.menubar.setObjectName("menubar")
        self.menu_complaint= QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menu_complaint.setFont(font)
        self.menu_complaint.setObjectName("menu_complaint")
        self.menu_news = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menu_news.setFont(font)
        self.menu_news.setObjectName("menu_news")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menu_3.setFont(font)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menu_4.setFont(font)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionComplaint = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionComplaint.setFont(font)
        self.actionComplaint.setObjectName("actionComplaint")
        # self.actionTop_Keyword = QtWidgets.QAction(MainWindow)
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.actionTop_Keyword.setFont(font)
        # self.actionTop_Keyword.setObjectName("actionTop_Keyword")
        # self.actionToday_Keyword = QtWidgets.QAction(MainWindow)
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.actionToday_Keyword.setFont(font)
        # self.actionToday_Keyword.setObjectName("actionToday_Keyword")
        # self.actionDFTop_Keyword = QtWidgets.QAction(MainWindow)
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.actionDFTop_Keyword.setFont(font)
        # self.actionDFTop_Keyword.setObjectName("actionDFTop_Keyword")
        self.actionNews = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionNews.setFont(font)
        self.actionNews.setObjectName("actionNews")
        self.menu_complaint.addAction(self.actionComplaint)
        # self.menu_complaint.addAction(self.actionTop_Keyword)
        # self.menu_complaint.addAction(self.actionToday_Keyword)
        # self.menu_complaint.addAction(self.actionDFTop_Keyword)
        self.menu_news.addAction(self.actionNews)
        self.menubar.addAction(self.menu_complaint.menuAction())
        self.menubar.addAction(self.menu_news.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionComplaint.triggered.connect(self.collect_complaint_window)
        # self.actionTop_Keyword.triggered.connect(self.top_window)
        # self.actionToday_Keyword.triggered.connect(self.today_window)
        # self.actionDFTop_Keyword.triggered.connect(self.dftop_window)

        self.actionNews.triggered.connect(self.collect_news_window)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_complaint.setTitle(_translate("MainWindow", "민원 데이터 수집"))
        self.menu_news.setTitle(_translate("MainWindow", "뉴스 데이터 수집"))
        self.menu_3.setTitle(_translate("MainWindow", "빅카인즈 크롤링"))
        self.menu_4.setTitle(_translate("MainWindow", "키워드 추이 비교"))
        self.actionComplaint.setText(_translate("MainWindow", "Complaint"))
        # self.actionTop_Keyword.setText(_translate("MainWindow", "Top Keyword"))
        # self.actionToday_Keyword.setText(_translate("MainWindow", "Today Keyword"))
        # self.actionDFTop_Keyword.setText(_translate("MainWindow", "DFTop Keyword"))
        self.actionNews.setText(_translate("MainWindow", "News"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
