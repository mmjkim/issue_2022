#------------- 분석에 사용될 1차 마트 생성 ---------------------
# 수집된 데이타를 하나의 파일로 저장
#-----------------------------------------------------------


#
# 디렉토리안에 있는 파일들의 데이타를 하나로 합치기
# parameter : filePath = 파일 Path, colList = 컬럼 리스트
# return : dataframe(colList + 파일식별 Key)
#

import glob      # 파일들의 리스트를 뽑을 때 사용(*.*)
import pandas as pd
import os.path
import datetime as dt
import pandas as pd
import numpy as np


from common.config.filepassclass import *
import common.config.apiinfo as apifp
from common.function.funcCommon import *

def anal_mart_news(part):

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
    print("The End!!!")

#----------------------------------------------------------------
# 민원데이터 월별 합계 마트 생성
#  part : 급등, 오늘, 최다, 핵심
#----------------------------------------------------------------
def anal_mart_complaint(part):

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
    # print(temp)

    all_files = glob.glob(temp)
    # 저장할 데이터 정리
    if part == '급등':
        df_mart_data = set_risting_data(all_files)
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
    print("The End!!!")

#급등키워드 데이터 생성
def set_risting_data(files):

    dfAllData = pd.DataFrame()

    # print(all_files)
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

#오늘의 민원 키워드 데이터 생성
def set_topic_data(files):
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

#핵심 키워드 데이터 생성
def set_top_data(files):

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

#최다 키워드 데이터 생성
def set_dftopkw_data(files):
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


# anal_mart_complaint('핵심')
# anal_mart_news('경제')