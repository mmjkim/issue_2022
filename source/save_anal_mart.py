#------------- 분석에 사용될 1차 마트 생성 ---------------------
# 수집된 데이타를 하나의 파일로 저장
#-----------------------------------------------------------


#
# 디렉토리안에 있는 파일들의 데이타를 하나로 합치기
# parameter : filePath = 파일 Path, colList = 컬럼 리스트
# return : dataframe(colList + 파일식별 Key)
#

import glob      # 파일들의 리스트를 뽑을 때 사용(*.*)
import os.path

from PyQt5.QtWidgets import QMessageBox

from common.config.filepassclass import *
import common.config.apiinfo as apifp
from common.function.funcCommon import *
from common.database import db_mdb as mdb
import common.config.errormessage as em

from datetime import datetime

def anal_mart_news(part):

    try:
        #파일 path
        file_path = FilePathClass()

        #분야별 데이터 저장 path
        if part == '정치':
            dataPath = apifp.NEWS_DATA_PATH_POLITICS
        elif part == '경제':
            dataPath = apifp.NEWS_DATA_PATH_ECONOMY
        elif part == '사회':
            dataPath = apifp.NEWS_DATA_PATH_SOCIETY

        temp = "{0}{1}\*.csv".format(file_path.get_raw_collect_path(), dataPath)

        all_files = glob.glob(temp)
        dfAllData = pd.DataFrame()

        if len(all_files) != 0:
            for filename in all_files:
                temp = filename.split('_')
                i = len(temp)-1
                df_dis_use = pd.read_csv(filename, encoding="utf-8-sig")
                # 컬럼명 변경
                df_dis_use.rename(columns={'빈도수':'freq', '순위':'rank', '키워드':'keyword'}, inplace=True)

                # '수집년월' 컬럼 추가
                df_dis_use['stdym'] = os.path.basename(temp[i][:6]).replace('.csv', '')
                dfAllData = pd.concat([dfAllData, df_dis_use])

            #데이터 컬럼 재정의
            dfAllData = dfAllData[['stdym', 'keyword', 'freq', 'rank']]

            #데이터 저장
            temp = "{0}{1}".format(file_path.get_raw_use_path(), dataPath)

            #저장될 폴더가 있는지 확인
            if not os.path.exists(temp):
                os.makedirs(temp)

            # 저장할 파일명 생성
            savefile = "{0}{1}\{2}_{3}.csv".format(file_path.get_raw_use_path(), dataPath, '1차마트', part)
            # 파일저장
            dfAllData.to_csv(savefile, encoding="utf-8-sig", index=False)

            print("마트 적재 데이타 Log 저장-->", part)
            #마트 적재 데이타 Log 저장
            save_log = mdb.DbUseAnalClass()
            save_log.mart_log_qry(dfAllData, '뉴스', part)

            print("The End!!!")

        else:
            error_event(em.NO_DATA)

    except Exception as e:
        print("anal_mart_news error :", e)

#----------------------------------------------------------------
# 민원데이터 월별 합계 마트 생성
#  part : 급등, 오늘, 최다, 핵심
#----------------------------------------------------------------
def anal_mart_complaint(part):
    try:
        #파일 path
        file_path = FilePathClass()
        #분야별 데이터 저장 path
        if part == '급등':
            dataPath = apifp.COMPLAIN_DATA_PATH_RISE
        elif part == '오늘':
            dataPath = apifp.COMPLAIN_DATA_PATH_TOPIC
        elif part == '최다':
            dataPath = apifp.COMPLAIN_DATA_PATH_DFTOPKW
        elif part == '핵심':
            dataPath = apifp.COMPLAIN_DATA_PATH_TOP

        # 데이타를 읽어서 df에 저장 (std_ymd, keyword, freq, rank=0)
        temp = "{0}{1}\*.csv".format(file_path.get_raw_collect_path(), dataPath)

        all_files = glob.glob(temp)

        if len(all_files) != 0:
            # 저장할 데이터 정리
            if part == '급등':
                df_mart_data = set_rising_data(all_files)
            elif part == '오늘':
                df_mart_data = set_topic_data(all_files)
            elif part == '최다':
                df_mart_data = set_dftopkw_data(all_files)
            elif part == '핵심':
                df_mart_data = set_top_data(all_files)

            #읽은 데이터를 키워드 기준 월별 빈도수 합계로 그룹
            df_mart_data_group = df_mart_data.groupby(['stdym', 'keyword'])['freq'].agg(**{'freq': 'sum'}).reset_index()

            #print(df_mart_data_group)
            #월별빈도수 키워드 데이터 저장
            temp = "{0}{1}".format(file_path.get_raw_use_path(), dataPath)

            #저장될 폴더가 있는지 확인
            if not os.path.exists(temp):
                os.makedirs(temp)

            # 저장할 파일명 생성
            savefile = "{0}{1}\{2}_{3}.csv".format(file_path.get_raw_use_path(), dataPath, '1차마트', part)
            # 파일저장
            df_mart_data_group.to_csv(savefile, encoding="utf-8-sig", index=False)

            print("마트 적재 데이타 Log 저장-->", part)
            #마트 적재 데이타 Log 저장
            save_log = mdb.DbUseAnalClass()
            save_log.mart_log_qry(df_mart_data_group,'민원' ,part)

            print("The End!!!")
        else:
            error_event(em.NO_DATA)

    except Exception:
        import traceback
        traceback.print_exc()


#급등키워드 데이터 생성
def set_rising_data(files):
    try:
        dfAllData = pd.DataFrame()

        for filename in files:
            temp = filename.split('_')
            i = len(temp) - 1
            df_dis_use = pd.read_csv(filename, encoding="utf-8-sig")

            # 컬럼명 변경
            df_dis_use.rename(columns={'df':'freq'}, inplace=True)

            # '수집년월' 컬럼 추가
            df_dis_use['stdym'] = pd.Series(df_dis_use['date'], dtype="string")
            df_dis_use['stdym'] = df_dis_use['stdym'].str[:6]

            dfAllData = pd.concat([dfAllData, df_dis_use])

        df_mart_data = dfAllData[['stdym', 'keyword', 'freq']]
        df_mart_data = df_mart_data.assign(rank=0)

        return df_mart_data
    except Exception:
        import traceback
        traceback.print_exc()


#오늘의 민원 키워드 데이터 생성
def set_topic_data(files):

    try:
        dfAllData = pd.DataFrame()

        # print(all_files)
        for filename in files:
            temp = filename.split('_')
            i = len(temp) - 1
            df_dis_use = pd.read_csv(filename, encoding="utf-8-sig")

            # 컬럼명 변경
            df_dis_use.rename(columns={'topic': 'keyword', 'count': 'freq'}, inplace=True)

            # '수집년월' 컬럼 추가(파일명을 활용하여 기준년월 삽입)
            temp = str(os.path.basename(temp[i]).replace('.csv', ''))
            df_dis_use['stdym'] = temp[:6]

            dfAllData = pd.concat([dfAllData, df_dis_use])

        df_mart_data = dfAllData[['stdym', 'keyword', 'freq']]
        df_mart_data = df_mart_data.assign(rank=0)

        return df_mart_data

    except Exception:
        import traceback
        traceback.print_exc()


#핵심 키워드 데이터 생성
def set_top_data(files):

    try:
        dfAllData = pd.DataFrame()

        # print(all_files)
        for filename in files:
            temp = filename.split('_')
            i = len(temp) - 1
            df_dis_use = pd.read_csv(filename, encoding="utf-8-sig")

            # 컬럼명 변경
            df_dis_use.rename(columns={'label': 'keyword', 'value': 'freq'}, inplace=True)

            # '수집년월' 컬럼 추가(파일명을 활용하여 기준년월 삽입)
            temp = str(os.path.basename(temp[i]).replace('.csv', ''))
            df_dis_use['stdym'] = temp[:6]

            dfAllData = pd.concat([dfAllData, df_dis_use])

        df_mart_data = dfAllData[['stdym', 'keyword', 'freq']]
        df_mart_data = df_mart_data.assign(rank=0)

        return df_mart_data

    except Exception:
       import traceback
       traceback.print_exc()


#최다 키워드 데이터 생성
def set_dftopkw_data(files):

    try:
        dfAllData = pd.DataFrame()

        # print(all_files)
        for filename in files:
            temp = filename.split('_')
            i = len(temp) - 1
            df_dis_use = pd.read_csv(filename, encoding="utf-8-sig")

            # 컬럼명 변경
            df_dis_use.rename(columns={'term': 'keyword', 'df': 'freq'}, inplace=True)

            # '수집년월' 컬럼 추가(파일명을 활용하여 기준년월 삽입)
            temp = str(os.path.basename(temp[i]).replace('.csv', ''))
            df_dis_use['stdym'] = temp[:6]

            dfAllData = pd.concat([dfAllData, df_dis_use])

        df_mart_data = dfAllData[['stdym', 'keyword', 'freq']]
        df_mart_data = df_mart_data.assign(rank=0)

        return df_mart_data

    except Exception:
        import traceback
        traceback.print_exc()


#네이버 키워드 데이터 생성(MDB에 저장)
def save_db_naver_data():

    try:
        #파일 path
        file_path = FilePathClass()
        dataPath = apifp.COMPLAIN_DATA_PATH_TOPIC

        # 데이타를 읽어서 df에 저장 (std_ymd, keyword, freq, rank=0)
        temp = "{0}\*네이버*.csv".format(file_path.get_raw_use_path())

        all_files = glob.glob(temp)
        #print(all_files)
        connect_db = mdb.DbUseAnalClass()
        connect_db.delete_qry("DELETE FROM NAVER_KEYWORD")

        insert_qry = "insert into NAVER_KEYWORD (KEYWORD, YMD, VAL) VALUES ("
        for i in range(0, len(all_files)):
            filename = all_files[i] #.split('_')
            list_qry = []
            #네이버 데이터 파일 읽기
            df_temp = pd.read_csv(filename, encoding='euc-kr')
            df_dis_use = df_temp[['keyword','Time','Value']]


            for row in df_dis_use.values.tolist():
                #print(type(row))
                value_qry = "'"
                value_qry += "', '".join(str(e) for e in row) + "'"
                value_qry += ");\n"
                list_qry.append(insert_qry + value_qry)
               # print (insert_qry + value_qry)

            connect_db.insert_many_qry(list_qry)
    except Exception:
        import traceback
        traceback.print_exc()


# 오늘의 민원 키워드 데이터 생성(MDB에 저장)
def save_db_topic_data():
    # 파일 path
    file_path = FilePathClass()
    dataPath = apifp.COMPLAIN_DATA_PATH_TOPIC

    # 데이타를 읽어서 df에 저장 (std_ymd, keyword, freq, rank=0)
    temp = "{0}{1}\*.csv".format(file_path.get_raw_collect_path(), dataPath)

    all_files = glob.glob(temp)

    # print(all_files)
    connect_db = mdb.DbUseAnalClass()
    connect_db.delete_qry("DELETE FROM CONPLAIN_TO_DAY")
    for filename in all_files:
        temp = filename.split('_')
        i = len(temp) - 1
        # '수집년월' 컬럼 추가(파일명을 활용하여 기준년월 삽입)
        ymd = str(os.path.basename(temp[i]).replace('.csv', ''))

        df_dis_use = pd.read_csv(filename, encoding="utf-8-sig")
        insert_qry = "insert into CONPLAIN_TO_DAY (YMD, TOPIC, RANK, COUNT) VALUES ("
        list_qry = []
        for row in df_dis_use.values.tolist():
            # print(type(row))
            value_qry = "'" + str(ymd) + "', '"
            value_qry += "', '".join(str(e) for e in row) + "'"
            value_qry += ");"
            list_qry.append(insert_qry + value_qry)

        connect_db.insert_many_qry(list_qry)


def error_event(msg):
    msgbox = QMessageBox()
    msgbox.setWindowTitle("error")
    msgbox.setText(msg)
    msgbox.exec_()

# mdb.DbUseAnalClass.select_qry("select * from CONPLAIN_TO_DAY")
# anal_mart_complaint('핵심')
# anal_mart_news('경제')
#save_db_topic_data()
#connect_db = mdb.DbUseAnalClass()
#df = connect_db.select_qry("select * from NAVER_KEYWORD ")

#print(df)


#save_db_naver_data()

#anal_mart_news('경제')
