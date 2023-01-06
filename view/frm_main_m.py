from PyQt5 import QtCore, QtGui, QtWidgets

from view.frm_news_api_s import Ui_news_collect_win  # 뉴스 데이터 수집
from view.frm_complaint_api_s import Ui_complaint_api_win  # 민원 데이터 수집
from view.frm_anal_keyword_compare_s import Ui_Anal_Dialog  # 키워드 분석
from view.frm_view_news_s import Ui_frmViewNews  # 뉴스 시각화
from view.frm_view_lda_s import Ui_Dialog  # LDA
from view.frm_view_complaints_s import Ui_frmViewComplaints  # 민원 시각화
from view.frm_view_relate_s import Ui_frmComplaintWC  # 연관어 분석 워드 클라우드
from view.frm_view_naver_s import Ui_frmViewNaver  # 네이버 검색어 시각화


class Ui_MainWindow(object):
    # 네이버 키워드 시각화 화면
    def view_naver_window(self):
        self.view_naver_win = QtWidgets.QDialog()
        self.view_naver_ui = Ui_frmViewNaver()
        self.view_naver_ui.setupUi(self.view_naver_win)
        self.view_naver_win.show()

    # 민원 연관어 분석 시각화 화면
    def view_wc_window(self):
        self.view_wc_win = QtWidgets.QDialog()
        self.view_wc_ui = Ui_frmComplaintWC()
        self.view_wc_ui.setupUi(self.view_wc_win)
        self.view_wc_win.show()

    # 민원 키워드 시각화 화면
    def view_complaint_window(self):
        self.view_com_win = QtWidgets.QDialog()
        self.view_com_ui = Ui_frmViewComplaints()
        self.view_com_ui.setupUi(self.view_com_win)
        self.view_com_win.show()

    # LDA 시각화 화면
    def lda_window(self):
        self.lda_win = QtWidgets.QDialog()
        self.lda_ui = Ui_Dialog()
        self.lda_ui.setupUi(self.lda_win)
        self.lda_win.show()

    # 뉴스 키워드 시각화 화면
    def visual_window(self):
        self.visual_win = QtWidgets.QDialog()
        self.visual_ui = Ui_frmViewNews()
        self.visual_ui.setupUi(self.visual_win)
        self.visual_win.show()

    # 민원 키워드 분석 및 분석 데이터 수집 화면
    def anal_window(self):
        self.anal_win = QtWidgets.QDialog()
        self.anal_ui = Ui_Anal_Dialog()
        self.anal_ui.setupUi(self.anal_win)
        self.anal_win.show()

    # 민원 데이터 수집 화면
    def collect_complaint_window(self):
        self.collect_complaint_win = QtWidgets.QMainWindow()
        self.collect_complaint_ui = Ui_complaint_api_win()
        self.collect_complaint_ui.setupUi(self.collect_complaint_win)
        self.collect_complaint_win.show()

    # 뉴스 데이터 수집 화면
    def collect_news_window(self):
        self.collect_news_win = QtWidgets.QMainWindow()
        self.collect_news_ui = Ui_news_collect_win()
        self.collect_news_ui.setupUi(self.collect_news_win)
        self.collect_news_win.show()

    # UI 설정
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # 화면 크기 설정 및 고정
        MainWindow.resize(1024, 768)
        MainWindow.setMaximumSize(1024, 768)
        MainWindow.setMinimumSize(1024, 768)

        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # 메뉴바 생성
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 737))
        self.menubar.setObjectName("menubar")
        # 민원 데이터 수집 메뉴
        self.menu_complaint = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menu_complaint.setFont(font)
        self.menu_complaint.setObjectName("menu_complaint")
        # 뉴스 데이터 수집 메뉴
        self.menu_news = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menu_news.setFont(font)
        self.menu_news.setObjectName("menu_news")
        # 키워드 분석 메뉴
        self.menu_anal = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menu_anal.setFont(font)
        self.menu_anal.setObjectName("menu_anal")
        # 시각화 메뉴
        self.menu_visual = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menu_visual.setFont(font)
        self.menu_visual.setObjectName("menu_visual")

        MainWindow.setMenuBar(self.menubar)

        # 민원 데이터 수집 메뉴바 동작 추가
        self.actionComplaint = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionComplaint.setFont(font)
        self.actionComplaint.setObjectName("actionComplaint")
        # 뉴스 데이터 수집 메뉴바 동작 추가
        self.actionNews = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionNews.setFont(font)
        self.actionNews.setObjectName("actionNews")
        # 키워드 분석 메뉴바 동작 추가 - 키워드 분석
        self.actionAnal = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionAnal.setFont(font)
        self.actionAnal.setObjectName("actionAnal")
        # 키워드 분석 메뉴바 동작 추가 - LDA
        self.actionAnal2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionAnal2.setFont(font)
        self.actionAnal2.setObjectName("actionAnal2")
        # 시각화 메뉴바 동작 추가 - 뉴스 현황
        self.actionVisual = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionVisual.setFont(font)
        self.actionVisual.setObjectName("actionVisual")
        # 시각화 메뉴바 동작 추가 - 민원 현황
        self.actionVisual2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionVisual2.setFont(font)
        self.actionVisual2.setObjectName("actionVisual2")
        # 시각화 메뉴바 동작 추가 - 민원 연관어 현황
        self.actionVisual3 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionVisual3.setFont(font)
        self.actionVisual3.setObjectName("actionVisual3")
        # 시각화 메뉴바 동작 추가 - 네이버 검색어 현황
        self.actionVisual5 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionVisual5.setFont(font)
        self.actionVisual5.setObjectName("actionVisual5")
        # 각 메뉴바 동작 설정
        self.menu_complaint.addAction(self.actionComplaint)
        self.menu_news.addAction(self.actionNews)
        self.menu_anal.addAction(self.actionAnal)
        self.menu_anal.addAction(self.actionAnal2)
        self.menu_visual.addAction(self.actionVisual)
        self.menu_visual.addAction(self.actionVisual2)
        self.menu_visual.addAction(self.actionVisual3)
        self.menu_visual.addAction(self.actionVisual5)
        self.menubar.addAction(self.menu_complaint.menuAction())
        self.menubar.addAction(self.menu_news.menuAction())
        self.menubar.addAction(self.menu_anal.menuAction())
        self.menubar.addAction(self.menu_visual.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 메뉴바 동작 클릭 > 해당 화면 연결
        self.actionComplaint.triggered.connect(self.collect_complaint_window)
        self.actionNews.triggered.connect(self.collect_news_window)
        self.actionAnal.triggered.connect(self.anal_window)
        self.actionAnal2.triggered.connect(self.lda_window)
        self.actionVisual.triggered.connect(self.visual_window)
        self.actionVisual2.triggered.connect(self.view_complaint_window)
        self.actionVisual3.triggered.connect(self.view_wc_window)
        self.actionVisual5.triggered.connect(self.view_naver_window)

        # 화면에 이미지 삽입
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(12, 30, 1000, 720))
        self.label.setAutoFillBackground(True)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setStyleSheet('background-color:white')
        self.label.setPixmap(QtGui.QPixmap("main_img.png"))

    # 타이틀 수정
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_complaint.setTitle(_translate("MainWindow", "민원 데이터 수집"))
        self.menu_news.setTitle(_translate("MainWindow", "뉴스 데이터 수집"))
        self.menu_anal.setTitle(_translate("MainWindow", "키워드 수집"))
        self.menu_visual.setTitle(_translate("MainWindow", "데이터 현황"))
        self.actionComplaint.setText(_translate("MainWindow", "민원(키워드)"))
        self.actionNews.setText(_translate("MainWindow", "뉴스(키워드)"))
        self.actionAnal.setText(_translate("MainWindow", "키워드 수집"))
        self.actionAnal2.setText(_translate("MainWindow", "토픽 키워드 수집"))
        self.actionVisual.setText(_translate("MainWindow", "뉴스 데이터 현황"))
        self.actionVisual2.setText(_translate("MainWindow", "민원 데이터 현황"))
        self.actionVisual3.setText(_translate("MainWindow", "민원 연관어 데이터 현황"))
        self.actionVisual5.setText(_translate("MainWindow", "네이버 검색 데이터 현황"))


if __name__ == "__main__":
    import sys

    # 에러 발생 > 에러 출력(강제 종료 X)
    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

    sys.exit(app.exec_())

