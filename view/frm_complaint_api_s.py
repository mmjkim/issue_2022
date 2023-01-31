from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import common.config.apiinfo as apifp
from common.config.filepassclass import *
from source.get_api_data_complaint import *
from source.save_anal_mart import *
import common.config.errormessage as em

#Thread Class
class Worker(QThread):
    loadingP = pyqtSignal(bool)

    def __init__(self):
        QThread.__init__(self)
        self.working = False
        self.part = None
        self.date = None
        self.target = None

    #Thread에 적용할 파라메터 값 정의
    def setLabel(self, part, date, target):
        self.part = part
        self.date = date
        self.target = target

    #Thread 실행
    def run(self):
        #thread 실행
        self.working = True

        if self.working:
            # 로딩바 실행 (로딩바 hidden = False)
            self.loadingP.emit(False)
            #민원 데이터 수집 기능 실행
            get_complaint_data(self.part, self.date, self.target)
            #로딩바 멈춤 (로딩바 hidden = True)
            self.loadingP.emit(True)


class Ui_complaint_api_win(object):
    def __init__(self):
        self.th_load = Worker()


    def setupUi(self, complaint_api_win):
        # 화면 크기 설정 및 고정
        complaint_api_win.setObjectName("complaint_api_win")
        complaint_api_win.resize(1024, 768)
        complaint_api_win.setMaximumSize(1024, 768)
        complaint_api_win.setMinimumSize(1024, 768)

        self.centralwidget = QtWidgets.QWidget(complaint_api_win)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(12, 11, 1001, 120))
        self.groupBox.setObjectName("groupBox")

        # 라디오 버튼 - 급등/핵심/오늘/최다/전체
        self.rad_type_rising = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_rising.setGeometry(QtCore.QRect(20, 26, 130, 20))
        self.rad_type_rising.setObjectName("rad_type_rising")
        self.rad_type_rising.setChecked(True)
        self.rad_type_top = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_top.setGeometry(QtCore.QRect(160, 26, 141, 21))
        self.rad_type_top.setObjectName("rad_type_top")
        self.rad_type_today = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_today.setGeometry(QtCore.QRect(20, 54, 135, 21))
        self.rad_type_today.setObjectName("rad_type_today")
        self.rad_type_dftop = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_dftop.setGeometry(QtCore.QRect(160, 54, 160, 20))
        self.rad_type_dftop.setObjectName("rad_type_dftop")
        self.rad_type_all = QtWidgets.QRadioButton(self.groupBox)
        self.rad_type_all.setGeometry(QtCore.QRect(20, 84, 86, 21))
        self.rad_type_all.setObjectName("rad_type_all")

        # 라벨 - 수집기간
        self.label_seldate = QtWidgets.QLabel(self.groupBox)
        self.label_seldate.setGeometry(QtCore.QRect(368, 70, 78, 16))
        self.label_seldate.setObjectName("label_seldate")

        # 콤보 박스 - 수집 연월
        self.sel_yy_start = QtWidgets.QComboBox(self.groupBox)
        self.sel_yy_start.setGeometry(QtCore.QRect(444, 67, 71, 22))
        self.sel_yy_start.setObjectName("sel_yy_start_2")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_yy_start.addItem("")
        self.sel_mm_start = QtWidgets.QComboBox(self.groupBox)
        self.sel_mm_start.setGeometry(QtCore.QRect(527, 67, 71, 23))
        self.sel_mm_start.setObjectName("sel_mm_start_2")
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

        # 버튼 - 데이터 수집/적재
        self.btn_sel = QtWidgets.QPushButton(self.groupBox)
        self.btn_sel.setGeometry(QtCore.QRect(618, 65, 110, 28))
        self.btn_sel.setObjectName("btn_sel")
        self.btn_mart = QtWidgets.QPushButton(self.groupBox)
        self.btn_mart.setGeometry(QtCore.QRect(740, 65, 110, 28))
        self.btn_mart.setObjectName("btn_mart")

        # 체크박스
        self.chkbox_saeol = QtWidgets.QCheckBox(self.groupBox)
        self.chkbox_saeol.setGeometry(QtCore.QRect(633, 31, 81, 20))
        self.chkbox_saeol.setObjectName("chkbox_saeol")
        self.chkbox_saeol.setChecked(True)
        self.chkbox_qna = QtWidgets.QCheckBox(self.groupBox)
        self.chkbox_qna.setGeometry(QtCore.QRect(793, 31, 85, 20))
        self.chkbox_qna.setObjectName("chkbox_qna")
        self.chkbox_qna.setChecked(True)
        self.chkbox_dfpt = QtWidgets.QCheckBox(self.groupBox)
        self.chkbox_dfpt.setGeometry(QtCore.QRect(541, 31, 81, 20))
        self.chkbox_dfpt.setObjectName("chkbox_dfpt")
        self.chkbox_dfpt.setChecked(True)
        self.chkbox_qnao = QtWidgets.QCheckBox(self.groupBox)
        self.chkbox_qnao.setGeometry(QtCore.QRect(890, 31, 81, 20))
        self.chkbox_qnao.setObjectName("chkbox_qnao")
        self.chkbox_qnao.setChecked(True)
        self.label_target = QtWidgets.QLabel(self.groupBox)
        self.label_target.setGeometry(QtCore.QRect(368, 33, 60, 16))
        self.label_target.setObjectName("label_target")
        self.chkbox_prpl = QtWidgets.QCheckBox(self.groupBox)
        self.chkbox_prpl.setGeometry(QtCore.QRect(725, 31, 57, 20))
        self.chkbox_prpl.setObjectName("chkbox_prpl")
        self.chkbox_prpl.setChecked(True)
        self.chkbox_pttn = QtWidgets.QCheckBox(self.groupBox)
        self.chkbox_pttn.setGeometry(QtCore.QRect(448, 31, 81, 20))
        self.chkbox_pttn.setObjectName("chkbox_pttn")
        self.chkbox_pttn.setChecked(True)

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(12, 122, 1001, 631))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        # 최다 민원 키워드 테이블
        self.tbl_dftop = QtWidgets.QTableWidget(self.frame_2)
        self.tbl_dftop.setGeometry(QtCore.QRect(756, 25, 234, 596))
        self.tbl_dftop.setObjectName("tbl_dftop")
        self.tbl_dftop.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dftop.setHorizontalHeaderItem(0, item)
        self.tbl_dftop.horizontalHeader().setStretchLastSection(True)
        self.tbl_dftop.verticalHeader().setDefaultSectionSize(35)
        self.tbl_dftop.setSortingEnabled(True)
        # 급등 키워드 테이블
        self.tbl_rising = QtWidgets.QTableWidget(self.frame_2)
        self.tbl_rising.setGeometry(QtCore.QRect(8, 25, 234, 596))
        self.tbl_rising.setObjectName("tbl_rising")
        self.tbl_rising.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_rising.setHorizontalHeaderItem(0, item)
        self.tbl_rising.horizontalHeader().setStretchLastSection(True)
        self.tbl_rising.verticalHeader().setDefaultSectionSize(35)
        self.tbl_rising.setSortingEnabled(True)
        # 오늘의 민원 키워드 테이블
        self.tbl_today = QtWidgets.QTableWidget(self.frame_2)
        self.tbl_today.setGeometry(QtCore.QRect(506, 25, 234, 596))
        self.tbl_today.setObjectName("tbl_today")
        self.tbl_today.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_today.setHorizontalHeaderItem(0, item)
        self.tbl_today.horizontalHeader().setStretchLastSection(True)
        self.tbl_today.verticalHeader().setDefaultSectionSize(35)
        self.tbl_today.setSortingEnabled(True)
        # 핵심 키워드 테이블
        self.tbl_top = QtWidgets.QTableWidget(self.frame_2)
        self.tbl_top.setGeometry(QtCore.QRect(257, 25, 234, 596))
        self.tbl_top.setObjectName("tbl_top")
        self.tbl_top.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_top.setHorizontalHeaderItem(0, item)
        self.tbl_top.horizontalHeader().setStretchLastSection(True)
        self.tbl_top.verticalHeader().setDefaultSectionSize(35)
        self.tbl_top.setSortingEnabled(True)

        # progress bar
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(400, 150, 300, 300))
        self.label.setText("")
        self.label.setObjectName("label")

        self.movie = QMovie('./loading.gif')
        self.label.setMovie(self.movie)
        self.movie.start()
        self.label.setHidden(True)

        complaint_api_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(complaint_api_win)
        QtCore.QMetaObject.connectSlotsByName(complaint_api_win)

        # 테이블 스타일 설정
        self.tbl_rising.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")
        self.tbl_today.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")
        self.tbl_top.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")
        self.tbl_dftop.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color:#404040;color:#FFFFFF;}")

        # 테이블 수정 불가
        self.tbl_rising.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_today.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_top.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_dftop.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.show_folders()  # 데이터 수집 리스트 출력

        self.btn_sel.clicked.connect(self.get_complaints)  # 민원 데이터 수집
        self.btn_mart.clicked.connect(self.save_mart)  # 데이터 적재


    # 데이터 적재
    def save_mart(self):
        if self.rad_type_rising.isChecked():
            anal_mart_complaint('급등')
        elif self.rad_type_top.isChecked():
            anal_mart_complaint('핵심')
        elif self.rad_type_today.isChecked():
            anal_mart_complaint('오늘')
        elif self.rad_type_dftop.isChecked():
            anal_mart_complaint('최다')
        elif self.rad_type_all.isChecked():
            anal_mart_complaint('급등')
            anal_mart_complaint('핵심')
            anal_mart_complaint('오늘')
            anal_mart_complaint('최다')


    # 민원 API 데이터 수집
    def get_complaints(self):
        # 분야
        global part
        # 수집 연월
        s_yy_start = self.sel_yy_start.currentText()
        s_mm_start = self.sel_mm_start.currentText()

        if self.rad_type_rising.isChecked():
            part = '급등'
        elif self.rad_type_top.isChecked():
            part = '핵심'
        elif self.rad_type_today.isChecked():
            part = '오늘'
        elif self.rad_type_dftop.isChecked():
            part = '최다'
        elif self.rad_type_all.isChecked():
            part = '전체'

        # 분석 대상 리스트
        target_list = []
        if self.chkbox_pttn.isChecked():
            target_list.append('pttn')
        if self.chkbox_dfpt.isChecked():
            target_list.append('dfpt')
        if self.chkbox_saeol.isChecked():
            target_list.append('saeol')
        if self.chkbox_prpl.isChecked():
            target_list.append('prpl')
        if self.chkbox_qna.isChecked():
            target_list.append('qna')
        if self.chkbox_qnao.isChecked():
            target_list.append('qna_origin')

        target = "%s" % ",".join(target_list)

        if len(target) > 1:
            self.th_load.setLabel(part, s_yy_start + s_mm_start, target)
            self.th_load.loadingP.connect(self.label.setHidden)
            self.th_load.start()
            self.th_load.finished.connect(self.show_folders)  # 스레드 종료되면 파일 목록 출력
        else:
            error_event(em.SELECT_CHKBOX)


    # 데이터 수집 리스트 출력
    def show_folders(self):
        file_path = FilePathClass()

        # 폴더 경로 설정
        pathRising = file_path.get_raw_collect_path() + apifp.COMPLAIN_DATA_PATH_RISE
        pathTop = file_path.get_raw_collect_path() + apifp.COMPLAIN_DATA_PATH_TOP
        pathToday = file_path.get_raw_collect_path() + apifp.COMPLAIN_DATA_PATH_TOPIC
        pathDftop = file_path.get_raw_collect_path() + apifp.COMPLAIN_DATA_PATH_DFTOPKW

        # 폴더 존재 X > 생성
        if file_path.is_path_exist_check(pathRising) is False:
            file_path.make_path(pathRising)
        if file_path.is_path_exist_check(pathTop) is False:
            file_path.make_path(pathTop)
        if file_path.is_path_exist_check(pathToday) is False:
            file_path.make_path(pathToday)
        if file_path.is_path_exist_check(pathDftop) is False:
            file_path.make_path(pathDftop)

        # 폴더 내 전체 파일 리스트
        folderRising = os.listdir(pathRising)
        folderTop = os.listdir(pathTop)
        folderToday = os.listdir(pathToday)
        folderDftop = os.listdir(pathDftop)

        # 분야별 파일 리스트 생성
        rising_list = []
        top_list = []
        today_list = []
        dftop_list = []

        # csv 파일만 리스트에 추가
        for i in range(0, len(folderRising)):
            if folderRising[i][-3:] == 'csv':
                rising_list.append(folderRising[i])
        for i in range(0, len(folderTop)):
            if folderTop[i][-3:] == 'csv':
                top_list.append(folderTop[i])
        for i in range(0, len(folderToday)):
            if folderToday[i][-3:] == 'csv':
                today_list.append(folderToday[i])
        for i in range(0, len(folderDftop)):
            if folderDftop[i][-3:] == 'csv':
                dftop_list.append(folderDftop[i])

        # 테이블 행 수 지정
        self.tbl_rising.setRowCount(len(rising_list))
        self.tbl_top.setRowCount(len(top_list))
        self.tbl_today.setRowCount(len(today_list))
        self.tbl_dftop.setRowCount(len(dftop_list))
        # 리스트 값 테이블에 추가
        for j in range(0, len(rising_list)):
            self.tbl_rising.setItem(j, 0, QTableWidgetItem(rising_list[j]))
        for j in range(0, len(top_list)):
            self.tbl_top.setItem(j, 0, QTableWidgetItem(top_list[j]))
        for j in range(0, len(today_list)):
            self.tbl_today.setItem(j, 0, QTableWidgetItem(today_list[j]))
        for j in range(0, len(dftop_list)):
            self.tbl_dftop.setItem(j, 0, QTableWidgetItem(dftop_list[j]))


    def retranslateUi(self, complaint_api_win):
        _translate = QtCore.QCoreApplication.translate
        complaint_api_win.setWindowTitle(_translate("complaint_api_win", "민원 데이터 수집"))
        self.groupBox.setTitle(_translate("complaint_api_win", " [ 민원 ] "))
        self.rad_type_rising.setText(_translate("complaint_api_win", "급등 키워드 정보"))
        self.rad_type_top.setText(_translate("complaint_api_win", "핵심 키워드 정보"))
        self.rad_type_today.setText(_translate("complaint_api_win", "오늘의 민원 이슈"))
        self.rad_type_dftop.setText(_translate("complaint_api_win", "최다 민원 키워드 정보"))
        self.label_seldate.setText(_translate("complaint_api_win", "수집기간: "))
        self.sel_mm_start.setItemText(0, _translate("complaint_api_win", "01"))
        self.sel_mm_start.setItemText(1, _translate("complaint_api_win", "02"))
        self.sel_mm_start.setItemText(2, _translate("complaint_api_win", "03"))
        self.sel_mm_start.setItemText(3, _translate("complaint_api_win", "04"))
        self.sel_mm_start.setItemText(4, _translate("complaint_api_win", "05"))
        self.sel_mm_start.setItemText(5, _translate("complaint_api_win", "06"))
        self.sel_mm_start.setItemText(6, _translate("complaint_api_win", "07"))
        self.sel_mm_start.setItemText(7, _translate("complaint_api_win", "08"))
        self.sel_mm_start.setItemText(8, _translate("complaint_api_win", "09"))
        self.sel_mm_start.setItemText(9, _translate("complaint_api_win", "10"))
        self.sel_mm_start.setItemText(10, _translate("complaint_api_win", "11"))
        self.sel_mm_start.setItemText(11, _translate("complaint_api_win", "12"))
        self.sel_mm_start.setCurrentText(str(datetime.today().month)) # 현재 월로 기본값 설정
        self.btn_sel.setText(_translate("complaint_api_win", "데이터 수집"))
        self.btn_mart.setText(_translate("complaint_api_win", "데이터 적재"))
        # 현재 연도까지 6년
        self.sel_yy_start.setItemText(0, _translate("complaint_api_win", str(datetime.today().year)))
        self.sel_yy_start.setItemText(1, _translate("complaint_api_win", str(datetime.today().year-1)))
        self.sel_yy_start.setItemText(2, _translate("complaint_api_win", str(datetime.today().year-2)))
        self.sel_yy_start.setItemText(3, _translate("complaint_api_win", str(datetime.today().year-3)))
        self.sel_yy_start.setItemText(4, _translate("complaint_api_win", str(datetime.today().year-4)))
        self.sel_yy_start.setItemText(5, _translate("complaint_api_win", str(datetime.today().year-5)))
        self.sel_yy_start.setCurrentText(str(datetime.today().year)) # 현재 연도로 기본값 설정
        self.rad_type_all.setText(_translate("complaint_api_win", "전체"))
        self.chkbox_saeol.setText(_translate("complaint_api_win", "수집민원"))
        self.chkbox_qna.setText(_translate("complaint_api_win", "정책QNA"))
        self.chkbox_dfpt.setText(_translate("complaint_api_win", "고충민원"))
        self.chkbox_qnao.setText(_translate("complaint_api_win", "공개민원"))
        self.label_target.setText(_translate("complaint_api_win", "분석대상:"))
        self.chkbox_prpl.setText(_translate("complaint_api_win", "제안"))
        self.chkbox_pttn.setText(_translate("complaint_api_win", "일반민원"))
        item = self.tbl_dftop.horizontalHeaderItem(0)
        item.setText(_translate("complaint_api_win", "최다 민원 키워드"))
        item = self.tbl_rising.horizontalHeaderItem(0)
        item.setText(_translate("complaint_api_win", "급등 키워드"))
        item = self.tbl_today.horizontalHeaderItem(0)
        item.setText(_translate("complaint_api_win", "오늘의 민원 이슈"))
        item = self.tbl_top.horizontalHeaderItem(0)
        item.setText(_translate("complaint_api_win", "핵심 키워드"))


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
    complaint_api_win = QtWidgets.QMainWindow()
    ui = Ui_complaint_api_win()
    ui.setupUi(complaint_api_win)
    complaint_api_win.show()

    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

    sys.exit(app.exec_())
