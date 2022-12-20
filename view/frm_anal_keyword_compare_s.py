import glob
import calendar
import pandas as pd
from datetime import datetime

import warnings
warnings.filterwarnings(action='ignore')

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from common.config.filepassclass import *
from source.get_api_data_naver import *
from common.function.funcCommon import *
from source.get_api_data_complaint import get_wd_cloud_info, get_similarInfo
from source.anal_keyword_compare import *
import common.config.apiinfo as apifp


class Ui_Anal_Dialog(object):

#  -------------------------------------------------< view def >-------------------------------------------------
    def setupUi(self, Anal_Dialog):
        # 화면 크기 설정 및 고정
        Anal_Dialog.setObjectName("Anal_Dialog")
        Anal_Dialog.resize(1024, 768)
        Anal_Dialog.setMaximumSize(1024, 768)
        Anal_Dialog.setMinimumSize(1024, 768)

        self.group1 = QtWidgets.QGroupBox(Anal_Dialog)
        self.group1.setGeometry(QtCore.QRect(10, 10, 1001, 311))
        self.group1.setObjectName("group1")

        self.tabWidget = QtWidgets.QTabWidget(self.group1)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 981, 271))
        self.tabWidget.setObjectName("tabWidget")
        
        # 오늘의 민원 키워드 탭
        self.tab_today = QtWidgets.QWidget()
        self.tab_today.setObjectName("tab_today")
        # 오늘의 민원 키워드 & 뉴스 키워드 테이블
        self.tbl_today = QtWidgets.QTableWidget(self.tab_today)
        self.tbl_today.setGeometry(QtCore.QRect(0, 0, 971, 241))
        self.tbl_today.setObjectName("tbl_today")
        self.tbl_today.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_today.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_today.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_today.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_today.setHorizontalHeaderItem(3, item)
        self.tbl_today.horizontalHeader().setStretchLastSection(False)
        self.tbl_today.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab_today, "")
        # 급등 키워드 탭
        self.tab_rise = QtWidgets.QWidget()
        self.tab_rise.setObjectName("tab_rise")
        # 급등 키워드 & 뉴스 키워드 테이블
        self.tbl_rise = QtWidgets.QTableWidget(self.tab_rise)
        self.tbl_rise.setGeometry(QtCore.QRect(0, 0, 971, 241))
        self.tbl_rise.setObjectName("tbl_rise")
        self.tbl_rise.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_rise.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_rise.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_rise.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_rise.setHorizontalHeaderItem(3, item)
        self.tbl_rise.horizontalHeader().setStretchLastSection(False)
        self.tbl_rise.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab_rise, "")
        # 최다 키워드 탭
        self.tab_top = QtWidgets.QWidget()
        self.tab_top.setObjectName("tab_top")
        # 최다 키워드 & 뉴스 키워드 테이블
        self.tbl_top = QtWidgets.QTableWidget(self.tab_top)
        self.tbl_top.setGeometry(QtCore.QRect(0, 0, 971, 241))
        self.tbl_top.setObjectName("tbl_top")
        self.tbl_top.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_top.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_top.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_top.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_top.setHorizontalHeaderItem(3, item)
        self.tbl_top.horizontalHeader().setStretchLastSection(False)
        self.tbl_top.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab_top, "")

        # 버튼 - 분석
        self.btn_anal = QtWidgets.QPushButton(self.group1)
        self.btn_anal.setGeometry(QtCore.QRect(904, 20, 79, 23))
        self.btn_anal.setObjectName("btn_search")

        self.group2 = QtWidgets.QGroupBox(Anal_Dialog)
        self.group2.setGeometry(QtCore.QRect(10, 330, 1001, 61))
        self.group2.setObjectName("group2")

        # 라벨 - 분석 기간
        self.label_5 = QtWidgets.QLabel(self.group2)
        self.label_5.setGeometry(QtCore.QRect(234, 28, 16, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.group2)
        self.label_6.setGeometry(QtCore.QRect(28, 27, 54, 15))
        self.label_6.setObjectName("label_6")

        # 콤보 박스 - 분석 기간
        self.sel_yy_start = QtWidgets.QComboBox(self.group2)
        self.sel_yy_start.setGeometry(QtCore.QRect(99, 23, 67, 23))
        self.sel_yy_start.setObjectName("sel_yy_start")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_mm_start = QtWidgets.QComboBox(self.group2)
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
        self.sel_yy_end = QtWidgets.QComboBox(self.group2)
        self.sel_yy_end.setGeometry(QtCore.QRect(251, 23, 67, 23))
        self.sel_yy_end.setObjectName("sel_yy_end")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_yy_end.addItem("")
        self.sel_mm_end = QtWidgets.QComboBox(self.group2)
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

        self.line = QtWidgets.QFrame(self.group2)
        self.line.setGeometry(QtCore.QRect(380, 20, 20, 31))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # 라벨 - 분석 키워드
        self.label_7 = QtWidgets.QLabel(self.group2)
        self.label_7.setGeometry(QtCore.QRect(400, 28, 71, 16))
        self.label_7.setObjectName("label_7")

        # 분석 키워드 입력
        self.txt_anal_word = QtWidgets.QTextEdit(self.group2)
        self.txt_anal_word.setGeometry(QtCore.QRect(472, 21, 521, 24))
        self.txt_anal_word.setToolTip("")
        self.txt_anal_word.setObjectName("txt_anal_word")

        self.group3 = QtWidgets.QGroupBox(Anal_Dialog)
        self.group3.setGeometry(QtCore.QRect(10, 400, 271, 361))
        self.group3.setObjectName("group3")

        # 네이버 데이터 수집 테이블
        self.tbl_naver = QtWidgets.QTableWidget(self.group3)
        self.tbl_naver.setGeometry(QtCore.QRect(5, 50, 261, 301))
        self.tbl_naver.setObjectName("tbl_naver")
        self.tbl_naver.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(225, 225, 225))
        self.tbl_naver.setHorizontalHeaderItem(0, item)
        self.tbl_naver.horizontalHeader().setStretchLastSection(True)
        # 네이버 데이터 수집 버튼
        self.btn_naver = QtWidgets.QPushButton(self.group3)
        self.btn_naver.setGeometry(QtCore.QRect(185, 22, 79, 23))
        self.btn_naver.setObjectName("btn_naver")

        self.group5 = QtWidgets.QGroupBox(Anal_Dialog)
        self.group5.setGeometry(QtCore.QRect(570, 400, 441, 361))
        self.group5.setObjectName("group5")

        # 민원 데이터 수집 버튼
        self.btn_complain = QtWidgets.QPushButton(self.group5)
        self.btn_complain.setGeometry(QtCore.QRect(350, 20, 79, 23))
        self.btn_complain.setObjectName("btn_complain")
        # 민원 유사사례 라벨
        self.lbl_simil = QtWidgets.QLabel(self.group5)
        self.lbl_simil.setGeometry(QtCore.QRect(10, 18, 350, 10))
        self.lbl_simil.setObjectName("lbl_simil")
        self.lbl_simil.setFont(QtGui.QFont("Gulim", 8))
        self.lbl_simil.setText("")
        # 민원 연관어분석 라벨
        self.lbl_relate = QtWidgets.QLabel(self.group5)
        self.lbl_relate.setGeometry(QtCore.QRect(10, 35, 350, 10))
        self.lbl_relate.setObjectName("lbl_relate")
        self.lbl_relate.setFont(QtGui.QFont("Gulim", 8))
        self.lbl_relate.setText("")
        # 민원 유사사례 데이터 수집 테이블
        self.tbl_complain_simil = QtWidgets.QTableWidget(self.group5)
        self.tbl_complain_simil.setGeometry(QtCore.QRect(8, 50, 211, 301))
        self.tbl_complain_simil.setObjectName("tbl_complain_simil")
        self.tbl_complain_simil.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(225, 225, 225))
        self.tbl_complain_simil.setHorizontalHeaderItem(0, item)
        self.tbl_complain_simil.horizontalHeader().setStretchLastSection(True)
        # 민원 연관어분석 데이터 수집 테이블
        self.tbl_complain_wdcloud = QtWidgets.QTableWidget(self.group5)
        self.tbl_complain_wdcloud.setGeometry(QtCore.QRect(224, 50, 211, 301))
        self.tbl_complain_wdcloud.setObjectName("tbl_complain_wdcloud")
        self.tbl_complain_wdcloud.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(225, 225, 225))
        self.tbl_complain_wdcloud.setHorizontalHeaderItem(0, item)
        self.tbl_complain_wdcloud.horizontalHeader().setStretchLastSection(True)

        self.group4 = QtWidgets.QGroupBox(Anal_Dialog)
        self.group4.setGeometry(QtCore.QRect(290, 400, 271, 361))
        self.group4.setObjectName("group4")

        # 뉴스 데이터 크롤링 테이블
        self.tbl_news = QtWidgets.QTableWidget(self.group4)
        self.tbl_news.setGeometry(QtCore.QRect(5, 50, 261, 301))
        self.tbl_news.setObjectName("tbl_news")
        self.tbl_news.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(225, 225, 225))
        self.tbl_news.setHorizontalHeaderItem(0, item)
        self.tbl_news.horizontalHeader().setStretchLastSection(True)
        # 뉴스 데이터 크롤링 버튼
        self.btn_news = QtWidgets.QPushButton(self.group4)
        self.btn_news.setGeometry(QtCore.QRect(185, 22, 79, 23))
        self.btn_news.setObjectName("btn_news")

        self.retranslateUi(Anal_Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Anal_Dialog)

        #테이블 스타일 조정
        self.tbl_today.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #테이블 행 높이 조정
        self.tbl_today.verticalHeader().setDefaultSectionSize(25)
        #테이블 열너비 조정
        self.tbl_today.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        #테이블 헤더 배경색, 글자색
        self.tbl_today.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.tbl_rise.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_rise.verticalHeader().setDefaultSectionSize(25)
        self.tbl_rise.horizontalHeader().setSectionResizeMode(True)
        self.tbl_rise.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.tbl_top.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_top.verticalHeader().setDefaultSectionSize(25)
        self.tbl_top.horizontalHeader().setSectionResizeMode(True)
        self.tbl_top.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.tbl_top.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_top.verticalHeader().setDefaultSectionSize(25)
        self.tbl_top.horizontalHeader().setSectionResizeMode(True)
        self.tbl_top.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.tbl_naver.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_naver.verticalHeader().setDefaultSectionSize(25)
        self.tbl_naver.horizontalHeader().setSectionResizeMode(True)
        self.tbl_naver.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.tbl_news.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_news.verticalHeader().setDefaultSectionSize(25)
        self.tbl_news.horizontalHeader().setSectionResizeMode(True)
        self.tbl_news.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.tbl_complain_simil.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_complain_simil.verticalHeader().setDefaultSectionSize(25)
        self.tbl_complain_simil.horizontalHeader().setSectionResizeMode(True)
        self.tbl_complain_simil.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.tbl_complain_wdcloud.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_complain_wdcloud.verticalHeader().setDefaultSectionSize(25)
        self.tbl_complain_wdcloud.horizontalHeader().setSectionResizeMode(True)
        self.tbl_complain_wdcloud.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        self.btn_news.clicked.connect(self.get_news) # 뉴스 데이터 크롤링
        self.btn_naver.clicked.connect(self.get_naver_data) # 네이버 키워드 데이터 수집
        self.btn_anal.clicked.connect(self.get_anal) # 동시출현 키워드 테이블 출력
        self.btn_complain.clicked.connect(self.get_complain_data) # 민원 데이터 수집

        # 탭 변경 > 해당 탭 테이블 변경
        self.tabWidget.currentChanged.connect(self.get_word_compare)

        # 데이터 수집 리스트 출력
        self.show_folders('네이버')
        self.show_folders('민원')
        self.show_folders('크롤링')

        # 동시출현 키워드 데이터 조회
        self.get_word_compare()


    def retranslateUi(self, Anal_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Anal_Dialog.setWindowTitle(_translate("Anal_Dialog", "키워드 분석"))
        self.group1.setTitle(_translate("Anal_Dialog", " [ 동시출현 키워드 ] "))
        item = self.tbl_today.horizontalHeaderItem(0)
        item.setText(_translate("Anal_Dialog", "민원_오늘"))
        item = self.tbl_today.horizontalHeaderItem(1)
        item.setText(_translate("Anal_Dialog", "뉴스_정치"))
        item = self.tbl_today.horizontalHeaderItem(2)
        item.setText(_translate("Anal_Dialog", "뉴스_경제"))
        item = self.tbl_today.horizontalHeaderItem(3)
        item.setText(_translate("Anal_Dialog", "뉴스_사회"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_today), _translate("Anal_Dialog", "민원_오늘"))
        item = self.tbl_rise.horizontalHeaderItem(0)
        item.setText(_translate("Anal_Dialog", "민원_급등"))
        item = self.tbl_rise.horizontalHeaderItem(1)
        item.setText(_translate("Anal_Dialog", "뉴스_정치"))
        item = self.tbl_rise.horizontalHeaderItem(2)
        item.setText(_translate("Anal_Dialog", "뉴스_경제"))
        item = self.tbl_rise.horizontalHeaderItem(3)
        item.setText(_translate("Anal_Dialog", "뉴스_사회"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rise), _translate("Anal_Dialog", "민원_급등"))
        item = self.tbl_top.horizontalHeaderItem(0)
        item.setText(_translate("Anal_Dialog", "민원_최다"))
        item = self.tbl_top.horizontalHeaderItem(1)
        item.setText(_translate("Anal_Dialog", "뉴스_정치"))
        item = self.tbl_top.horizontalHeaderItem(2)
        item.setText(_translate("Anal_Dialog", "뉴스_경제"))
        item = self.tbl_top.horizontalHeaderItem(3)
        item.setText(_translate("Anal_Dialog", "뉴스_사회"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_top), _translate("Anal_Dialog", "민원_최다"))
        self.btn_anal.setText(_translate("Anal_Dialog", "분석"))
        self.group2.setTitle(_translate("Anal_Dialog", " [ 분석 ] "))
        self.label_5.setText(_translate("Anal_Dialog", "~"))
        self.label_6.setText(_translate("Anal_Dialog", "분석기간: "))
        self.sel_yy_end.setItemText(0, _translate("Anal_Dialog", str(datetime.today().year)))
        self.sel_yy_end.setItemText(1, _translate("Anal_Dialog", str(datetime.today().year-1)))
        self.sel_yy_end.setItemText(2, _translate("Anal_Dialog", str(datetime.today().year-2)))
        self.sel_yy_end.setItemText(3, _translate("Anal_Dialog", str(datetime.today().year-3)))
        self.sel_yy_end.setItemText(4, _translate("Anal_Dialog", str(datetime.today().year-4)))
        self.sel_yy_end.setItemText(5, _translate("Anal_Dialog", str(datetime.today().year-5)))
        self.sel_yy_end.setCurrentText(str(datetime.today().year))
        self.sel_mm_start.setItemText(0, _translate("Anal_Dialog", "01"))
        self.sel_mm_start.setItemText(1, _translate("Anal_Dialog", "02"))
        self.sel_mm_start.setItemText(2, _translate("Anal_Dialog", "03"))
        self.sel_mm_start.setItemText(3, _translate("Anal_Dialog", "04"))
        self.sel_mm_start.setItemText(4, _translate("Anal_Dialog", "05"))
        self.sel_mm_start.setItemText(5, _translate("Anal_Dialog", "06"))
        self.sel_mm_start.setItemText(6, _translate("Anal_Dialog", "07"))
        self.sel_mm_start.setItemText(7, _translate("Anal_Dialog", "08"))
        self.sel_mm_start.setItemText(8, _translate("Anal_Dialog", "09"))
        self.sel_mm_start.setItemText(9, _translate("Anal_Dialog", "10"))
        self.sel_mm_start.setItemText(10, _translate("Anal_Dialog", "11"))
        self.sel_mm_start.setItemText(11, _translate("Anal_Dialog", "12"))
        # 현재 연도까지 6년
        self.sel_yy_start.setItemText(0, _translate("Anal_Dialog", str(datetime.today().year)))
        self.sel_yy_start.setItemText(1, _translate("Anal_Dialog", str(datetime.today().year - 1)))
        self.sel_yy_start.setItemText(2, _translate("Anal_Dialog", str(datetime.today().year - 2)))
        self.sel_yy_start.setItemText(3, _translate("Anal_Dialog", str(datetime.today().year - 3)))
        self.sel_yy_start.setItemText(4, _translate("Anal_Dialog", str(datetime.today().year - 4)))
        self.sel_yy_start.setItemText(5, _translate("Anal_Dialog", str(datetime.today().year - 5)))
        self.sel_yy_start.setCurrentText(str(datetime.today().year)) # 현재 연도로 기본값 설정
        self.sel_mm_end.setItemText(0, _translate("Anal_Dialog", "01"))
        self.sel_mm_end.setItemText(1, _translate("Anal_Dialog", "02"))
        self.sel_mm_end.setItemText(2, _translate("Anal_Dialog", "03"))
        self.sel_mm_end.setItemText(3, _translate("Anal_Dialog", "04"))
        self.sel_mm_end.setItemText(4, _translate("Anal_Dialog", "05"))
        self.sel_mm_end.setItemText(5, _translate("Anal_Dialog", "06"))
        self.sel_mm_end.setItemText(6, _translate("Anal_Dialog", "07"))
        self.sel_mm_end.setItemText(7, _translate("Anal_Dialog", "08"))
        self.sel_mm_end.setItemText(8, _translate("Anal_Dialog", "09"))
        self.sel_mm_end.setItemText(9, _translate("Anal_Dialog", "10"))
        self.sel_mm_end.setItemText(10, _translate("Anal_Dialog", "11"))
        self.sel_mm_end.setItemText(11, _translate("Anal_Dialog", "12"))
        self.sel_mm_end.setCurrentText(str(datetime.today().month)) # 현재 월로 기본값 설정
        self.label_7.setText(_translate("Anal_Dialog", "분석 키워드"))
        self.group3.setTitle(_translate("Anal_Dialog", " [ 네이버 ] "))
        item = self.tbl_naver.horizontalHeaderItem(0)
        item.setText(_translate("Anal_Dialog", "파일명"))
        self.btn_naver.setText(_translate("Anal_Dialog", "데이터 수집"))
        self.group5.setTitle(_translate("Anal_Dialog", " [ 민원 ] "))
        self.btn_complain.setText(_translate("Anal_Dialog", "데이터 수집"))
        item = self.tbl_complain_simil.horizontalHeaderItem(0)
        item.setText(_translate("Anal_Dialog", "파일명[유사사례]"))
        item = self.tbl_complain_wdcloud.horizontalHeaderItem(0)
        item.setText(_translate("Anal_Dialog", "파일명[연관어]"))
        self.group4.setTitle(_translate("Anal_Dialog", " [ 뉴스 크롤링 ] "))
        item = self.tbl_news.horizontalHeaderItem(0)
        item.setText(_translate("Anal_Dialog", "파일명"))
        self.btn_news.setText(_translate("Anal_Dialog", "데이터 수집"))

        # 테이블 정렬 가능
        self.tbl_news.setSortingEnabled(True)
        self.tbl_today.setSortingEnabled(True)
        self.tbl_naver.setSortingEnabled(True)
        self.tbl_rise.setSortingEnabled(True)
        self.tbl_top.setSortingEnabled(True)
        self.tbl_complain_simil.setSortingEnabled(True)
        self.tbl_complain_wdcloud.setSortingEnabled(True)

#  -------------------------------------------------<  logic def >----------------------------------------------------------
    def get_anal(self):
        if self.tabWidget.currentIndex() == 0:
            part_name = '오늘'
        elif self.tabWidget.currentIndex() == 1:
            part_name = '급등'
        elif self.tabWidget.currentIndex() == 2:
            part_name = '최다'

        # 키워드 동시출현 분석 > 파일 저장 및 데이터프레임 반환
        compare_keyword(part_name)
        # 동시출현 키워드 테이블 조회
        self.get_word_compare()


    # 뉴스 데이터 크롤링
    def get_news(self):
        import time
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.chrome.options import Options # 크롬 옵션 설정
        from webdriver_manager.chrome import ChromeDriverManager # 크롬 드라이버 자동 업데이트
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        # 다운로드 경로
        down_path = FilePathClass()

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True) # 브라우저 자동 종료 방지
        dr = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        dr.implicitly_wait(3) # 3초 대기
        dr.get('https://www.bigkinds.or.kr/v2/news/index.do') # 빅카인즈 주소로 이동
        dr.maximize_window() # 창 최대화

        # 빅카인즈 로그인
        login_element = dr.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/div[2]/button[1]')
        login_element.click()
        id_element = dr.find_element(By.ID, 'login-user-id')
        id_element.send_keys(apifp.BIGKINDS_ID)
        pw_element = dr.find_element(By.ID, 'login-user-password')
        pw_element.send_keys(apifp.BIGKINDS_PW)
        pw_element.send_keys(Keys.ENTER)
        # 로그인창 닫기
        time.sleep(1)
        modal_content = dr.find_element(By.XPATH, '//*[@id="login-modal"]/div')
        modal_content.click()

        # 검색 키워드
        anal_word = self.txt_anal_word.toPlainText().replace(", ", ",")
        anal_word = anal_word.split(',')

        # 데이터 수집
        for i in anal_word:
            # 키워드 입력
            input_element = dr.find_element(By.XPATH, '//*[@id="total-search-key"]')
            input_element.send_keys(Keys.CONTROL + "a")
            input_element.send_keys(Keys.DELETE)
            input_element.send_keys(i)
            input_element.send_keys(Keys.TAB)

            if i == self.txt_anal_word.toPlainText().split(',')[0]:
                # 기간 설정
                date_tab_element = dr.find_element(By.XPATH, '//*[@id="collapse-step-1-body"]/div[3]/div/div[1]/div[1]/a')
                date_tab_element.send_keys(Keys.ENTER)

                start_element = dr.find_element(By.ID, 'search-begin-date')
                start_element.click()
                start_element.send_keys(Keys.CONTROL + "a")
                start_element.send_keys(Keys.DELETE)
                start_date = self.sel_yy_start.currentText() + self.sel_mm_start.currentText() + "01"
                start_element.send_keys(start_date)
                end_element = dr.find_element(By.ID, 'search-end-date')
                end_element.send_keys(Keys.CONTROL + "a")
                end_element.send_keys(Keys.DELETE)
                end_date = getMonthRange(self.sel_yy_end.currentText(), self.sel_mm_end.currentText()).strftime("%Y%m%d")
                end_element.send_keys(end_date)

            apply_element = dr.find_element(By.XPATH, '//*[@id="search-foot-div"]/div[2]/button[2]')
            apply_element.click()

            # 데이터 다운로드
            time.sleep(1)
            step3_element = dr.find_element(By.ID, 'collapse-step-3')
            step3_element.send_keys(Keys.ENTER)

            import getpass
            down_file_path = "{0}{1}_{2}-{3}.xlsx".format('C:\\Users\\' + getpass.getuser() + '\\Downloads\\', "NewsResult", start_date, end_date)

            # 파일 존재 > 삭제
            if os.path.isfile(down_file_path):
                os.remove(down_file_path)

            time.sleep(1)
            down_element = dr.find_element(By.XPATH, '//*[@id="analytics-data-download"]/div[3]/button')
            down_element.send_keys(Keys.ENTER)

            # alert 창 닫기
            try:
                WebDriverWait(dr, 3).until(EC.alert_is_present())
                alert = dr.switch_to.alert

                # 확인하기
                alert.accept()
            except:
                print("no alert")

            # 데이터 경로 이동(다운로드 폴더 > 분석데이터 폴더) 및 파일명 변경
            time.sleep(1)
            downloaded = False
            while downloaded == False:
                try:
                    down_file = pd.read_excel(down_file_path)
                    route = "{0}\\{1}_{2}_{3}.csv".format(down_path.get_raw_use_path(), "뉴스", '크롤링', i)
                    down_file.to_csv(route, encoding="utf-8-sig", index=False)
                    downloaded = True
                except FileNotFoundError:
                    downloaded = False
                except PermissionError:
                    time.sleep(1)
                    downloaded = False

            # 뉴스 검색으로 돌아가기
            step1_element = dr.find_element(By.ID, 'collapse-step-1')
            step1_element.send_keys(Keys.ENTER)

        self.show_folders('크롤링') # 크롤링 파일 리스트 출력


    # 네이버 데이터 수집
    def get_naver_data(self):
        # 시작 연월 및 종료 연월
        s_yy_start = self.sel_yy_start.currentText()
        s_mm_start = self.sel_mm_start.currentText()
        s_yy_end = self.sel_yy_end.currentText()
        s_mm_end = self.sel_mm_end.currentText()

        # 검색 키워드
        keywords = self.txt_anal_word.toPlainText().split(',')

        for i in keywords:
            i = ('검색,' + i).split(',')
            # 네이버 데이터 수집
            naver_trend_search(datetime.strptime(s_yy_start+s_mm_start+"01", '%Y%m%d'),
                               getMonthRange(s_yy_end,s_mm_end), i)

        self.show_folders('네이버') # 네이버 데이터 수집 리스트 출력

    
    # 민원 데이터 수집
    def get_complain_data(self):
        # 수집 시작 연월/종료 연월
        s_yy_start = self.sel_yy_start.currentText()
        s_mm_start = self.sel_mm_start.currentText()
        s_yy_end = self.sel_yy_end.currentText()
        s_mm_end = self.sel_mm_end.currentText()

        # 키워드
        keywords = self.txt_anal_word.toPlainText().split(',')

        empty_relate_list = []
        empty_simil_list = []

        for i in keywords:
            # 민원_연관어분석 데이터 수집
            if get_wd_cloud_info(i, (s_yy_start+s_mm_start+"01"),
                           getMonthRange(s_yy_end,s_mm_end).strftime("%Y%m%d"), 'pttn,dfpt,saeol,prpl,qna_origin') is None:
                empty_relate_list.append(i)
            # 민원_유사사례정보 데이터 수집
            if get_similarInfo(i) is None:
                empty_simil_list.append(i)

        empty_relate_str = ', '.join(empty_relate_list)
        empty_simil_str = ', '.join(empty_simil_list)
        self.lbl_relate.repaint()  # 라벨 초기화
        self.lbl_simil.repaint()
        self.lbl_relate.setText('X 연관어: ' + empty_relate_str)
        self.lbl_simil.setText('X 유사사례: ' + empty_simil_str)

        self.show_folders('민원')  # 민원 데이터 수집 리스트 출력

    
    # 수집 파일 리스트 출력
    def show_folders(self, part):
        # 폴더 경로 설정
        file_path = FilePathClass()
        search_path = file_path.get_raw_use_path()
        
        # 경로 존재 X > 에러 출력
        if file_path.is_path_exist_check(search_path) is False:
           error_event(em.NO_PATH)

        data_all_list = os.listdir(search_path)

        data_list_news = []
        data_list_naver = []
        data_list_simil = []
        data_list_wdcloud = []

        # 각 분야별 파일명 리스트에 저장
        for i in range(0, len(data_all_list)):
            filename = data_all_list[i].split('_')
            if len(filename) > 2 :
                if (data_all_list[i][-3:] == 'csv') & (filename[0] == '네이버'):
                    data_list_naver.append(data_all_list[i])
                elif (data_all_list[i][-3:] == 'csv') & (filename[0] == '민원'):
                    if filename[1] == '유사사례정보':
                        data_list_simil.append(data_all_list[i])
                    elif filename[1] == '연관어분석정보':
                        data_list_wdcloud.append(data_all_list[i])
                elif (data_all_list[i][-3:] == 'csv') & (filename[0] == '뉴스'):
                    data_list_news.append(data_all_list[i])

        if part == '네이버' :
            #네이버
            self.tbl_naver.setRowCount(len(data_list_naver))
            for j in range(0, len(data_list_naver)):
                self.tbl_naver.setItem(j, 0, QTableWidgetItem(data_list_naver[j]))
        elif part == '크롤링':
            self.tbl_news.setRowCount(len(data_list_news))
            for j in range(0, len(data_list_news)):
                self.tbl_news.setItem(j, 0, QTableWidgetItem(data_list_news[j]))
        else:
            #민원_유사사례
            self.tbl_complain_simil.setRowCount(len(data_list_simil))
            for j in range(0, len(data_list_simil)):
                self.tbl_complain_simil.setItem(j, 0, QTableWidgetItem(data_list_simil[j]))
            #민원_연관어
            self.tbl_complain_wdcloud.setRowCount(len(data_list_wdcloud))
            for j in range(0, len(data_list_wdcloud)):
                self.tbl_complain_wdcloud.setItem(j, 0, QTableWidgetItem(data_list_wdcloud[j]))


    #-----------------------------------------------------------
    # 탭 클릭시 데이터 조회
    # self.tabWidget.currentIndex() : 0=오늘, 1=급등, 2=최다
    #-----------------------------------------------------------
    def get_word_compare(self):
        file_path = FilePathClass()

        if self.tabWidget.currentIndex() == 0:
            file_name = '동시출현키워드_pivot_오늘'
        elif self.tabWidget.currentIndex() == 1:
            file_name = '동시출현키워드_pivot_급등'
        elif self.tabWidget.currentIndex() == 2:
            file_name = '동시출현키워드_pivot_최다'

        # csv인 모든 파일 가져오기
        all_files = glob.glob(file_path.get_raw_use_path() + file_name + ".csv")

        if len(all_files) > 0:
            search_file_name = "{0}/{1}.csv".format(file_path.get_raw_use_path(), file_name)
            df_data_anal = pd.read_csv(search_file_name, encoding="utf-8-sig")
        else:
            return

        self.tbl_today.setRowCount(len(df_data_anal))
        self.tbl_rise.setRowCount(len(df_data_anal))
        self.tbl_top.setRowCount(len(df_data_anal))

        if self.tabWidget.currentIndex() == 0:
            for i in range(len(df_data_anal)):
                self.tbl_today.setItem(i, 0, QTableWidgetItem(df_data_anal['keyword'][i]))
                self.tbl_today.setItem(i, 1, QTableWidgetItem(df_data_anal['뉴스_정치'][i]))
                self.tbl_today.setItem(i, 2, QTableWidgetItem(df_data_anal['뉴스_경제'][i]))
                self.tbl_today.setItem(i, 3, QTableWidgetItem(df_data_anal['뉴스_사회'][i]))
        elif self.tabWidget.currentIndex() == 1:
            for i in range(len(df_data_anal)):
                self.tbl_rise.setItem(i, 0, QTableWidgetItem(df_data_anal['keyword'][i]))
                self.tbl_rise.setItem(i, 1, QTableWidgetItem(df_data_anal['뉴스_정치'][i]))
                self.tbl_rise.setItem(i, 2, QTableWidgetItem(df_data_anal['뉴스_경제'][i]))
                self.tbl_rise.setItem(i, 3, QTableWidgetItem(df_data_anal['뉴스_사회'][i]))
        elif self.tabWidget.currentIndex() == 2:
            for i in range(len(df_data_anal)):
                self.tbl_top.setItem(i, 0, QTableWidgetItem(df_data_anal['keyword'][i]))
                self.tbl_top.setItem(i, 1, QTableWidgetItem(df_data_anal['뉴스_정치'][i]))
                self.tbl_top.setItem(i, 2, QTableWidgetItem(df_data_anal['뉴스_경제'][i]))
                self.tbl_top.setItem(i, 3, QTableWidgetItem(df_data_anal['뉴스_사회'][i]))


def error_event(msg):
    msgbox = QMessageBox()
    msgbox.setWindowTitle("error")
    msgbox.setText(msg)
    msgbox.exec_()


if __name__ == "__main__":
    import sys

    # 에러 발생 > 에러 출력(강제 종료 X)
    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)

    app = QtWidgets.QApplication(sys.argv)
    Anal_Dialog = QtWidgets.QDialog()
    ui = Ui_Anal_Dialog()
    ui.setupUi(Anal_Dialog)
    Anal_Dialog.show()

    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

    sys.exit(app.exec_())
