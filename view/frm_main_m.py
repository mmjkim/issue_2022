from PyQt5 import QtCore, QtGui, QtWidgets

from view.frm_news_api_s import Ui_news_collect_win
from view.frm_complaint_api_s import Ui_complaint_api_win
from view.frm_anal_s import Ui_Anal_Dialog

class Ui_MainWindow(object):
    def anal_window(self):
        self.anal_win = QtWidgets.QDialog()
        self.anal_ui = Ui_Anal_Dialog()
        self.anal_ui.setupUi(self.anal_win)
        self.anal_win.show()

    def collect_complaint_window(self):
        self.collect_complaint_win = QtWidgets.QMainWindow()
        self.collect_complaint_ui = Ui_complaint_api_win()
        self.collect_complaint_ui.setupUi(self.collect_complaint_win)
        self.collect_complaint_win.show()

    def collect_news_window(self):
        self.collect_news_win = QtWidgets.QMainWindow()
        self.collect_news_ui = Ui_news_collect_win()
        self.collect_news_ui.setupUi(self.collect_news_win)
        self.collect_news_win.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMaximumSize(1024,768)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 737))
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
        self.menu_anal = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menu_anal.setFont(font)
        self.menu_anal.setObjectName("menu_anal")
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

        self.actionNews = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionNews.setFont(font)
        self.actionNews.setObjectName("actionNews")

        self.actionAnal = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionAnal.setFont(font)
        self.actionAnal.setObjectName("actionAnal")

        self.menu_complaint.addAction(self.actionComplaint)
        self.menu_news.addAction(self.actionNews)
        self.menu_anal.addAction(self.actionAnal)
        self.menubar.addAction(self.menu_complaint.menuAction())
        self.menubar.addAction(self.menu_news.menuAction())
        self.menubar.addAction(self.menu_anal.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionComplaint.triggered.connect(self.collect_complaint_window)

        self.actionNews.triggered.connect(self.collect_news_window)
        self.actionAnal.triggered.connect(self.anal_window)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_complaint.setTitle(_translate("MainWindow", "민원 데이터 수집"))
        self.menu_news.setTitle(_translate("MainWindow", "뉴스 데이터 수집"))
        self.menu_anal.setTitle(_translate("MainWindow", "키워드 분석"))
        self.menu_4.setTitle(_translate("MainWindow", "SAMPLE"))
        self.actionComplaint.setText(_translate("MainWindow", "Complaint"))
        self.actionNews.setText(_translate("MainWindow", "News"))
        self.actionAnal.setText(_translate("MainWindow", "Analysis"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

