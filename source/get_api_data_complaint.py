import pandas as pd
import numpy as np
import json
import requests
from urllib.request import urlopen
from pandas import json_normalize

from common.config.filepassclass import *
from common.function.funcDataControl import *
import common.config.apiinfo as apifp
from datetime import datetime
from urllib.parse import quote # 문자열을 URL encoding
from urllib.parse import unquote

from common.function.funcCommon import *


#-----------------------------------------------------
#  공공데이터 포털에서 api i/f 통한 민원 데이터 가져오기
#  급등 키워드 정보
#  param :
#      target = 'pttn:일반민원, dfpt:고충민원, saeol:수집민원, prpl:제안, qna:정책Q&A, qna_origin:공개민원'
#      std_ymd = yyyymm (기준일자)
#  return :
#-----------------------------------------------------
def get_risting_keyword(std_ymd, target):

    #파일 path
    file_path = FilePathClass()
    # nowtime = str(datetime.now().time().strftime('%H'))
    analysis_date = std_ymd #.strftime("%Y%m%d") #+ nowtime
    maxResult = apifp.COMPLAIN_MAX_ROW
    url = apifp.COMPLAIN_API_URL + apifp.COMPLAIN_API_URL_RISE + '?serviceKey=' + apifp.COMPLAIN_API_KEY + '&analysisTime=' + analysis_date + '&maxResult=' + maxResult + '&target=' + target
    print('URL: ', url)

    dataPath = apifp.COMPLAIN_DATA_PATH_RISE
    # 분야별 데이터 저장 full path
    get_complain_data_path = file_path.get_raw_collect_path() + dataPath + "//"

    try:

        res = urlopen(url).read()  # URL 열고 읽음
        resJson = json.loads(res)  # json 문자열을 파이썬 객체로 변환
        df1 = json_normalize(resJson.get('returnObject'))  # json 데이터를 dataframe으로 변환

        # 폴더 존재 여부 확인하여 없으면 폴더 생성
        if file_path.is_path_exist_check(get_complain_data_path) == False:
            file_path.make_path(get_complain_data_path)
            print(get_complain_data_path)

        route = "{0}{1}_{2}.json".format(get_complain_data_path, dataPath, analysis_date)
        route_csv = "{0}{1}_{2}.csv".format(get_complain_data_path, dataPath, analysis_date)
        df1.to_csv(route_csv, index=False, encoding="utf-8-sig")
        df1.to_json(route, orient='table')

        print('The End!!!')

    except requests.exceptions.Timeout as errd:  # 요청 시간 초과
        print("Timeout Error : ", errd)

    except requests.exceptions.ConnectionError as errc:  # 네트워크 문제
        print("Error Connecting : ", errc)

    except requests.exceptions.HTTPError as errb:  # 잘못된 HTTP 응답
        print("Http Error : ", errb)

    except requests.exceptions.RequestException as erra:  # 요청에 의해 명시적으로 발생한 모든 예외에서 상속
        print("AnyException : ", erra)


    return df1


#-----------------------------------------------------
#  공공데이터 포털에서 api i/f 통한 민원 데이터 가져오기
#  핵심키워드 정보
#  param :
#      target = 'pttn:일반민원, dfpt:고충민원, saeol:수집민원, prpl:제안, qna:정책Q&A, qna_origin:공개민원'
#      std_ymd_fr = yyyymm (기준월 시작일자)
#      std_ymd_to = yyyymm (기준월 종료일자)
#  return :
#-----------------------------------------------------
def get_topN_keyword(std_ymd_fr, std_ymd_to, target):

    #파일 path
    file_path = FilePathClass()
    analysis_date_fr = std_ymd_fr
    analysis_date_to = std_ymd_to
    maxResult = apifp.COMPLAIN_MAX_ROW

    url = apifp.COMPLAIN_API_URL + apifp.COMPLAIN_API_URL_TOP + '?serviceKey=' + apifp.COMPLAIN_API_KEY + '&resultCount=' + maxResult + '&target=' + target + '&dateFrom=' + analysis_date_fr + '&dateTo=' + analysis_date_to
    print('URL: ', url)

    dataPath = apifp.COMPLAIN_DATA_PATH_TOP
    # 분야별 데이터 저장 full path
    get_complain_data_path = file_path.get_raw_collect_path() + dataPath + "//"

    try:

        res = urlopen(url).read()  # URL 열고 읽음
        resJson = json.loads(res)  # json 문자열을 파이썬 객체로 변환
        df1 = json_normalize(resJson)  # json 데이터를 dataframe으로 변환

        # 폴더 존재 여부 확인하여 없으면 폴더 생성
        if file_path.is_path_exist_check(get_complain_data_path) == False:
            file_path.make_path(get_complain_data_path)
        print(get_complain_data_path)
        route = "{0}{1}_{2}.json".format(get_complain_data_path,  dataPath, std_ymd_fr)
        route_csv = "{0}{1}_{2}.csv".format(get_complain_data_path, dataPath, std_ymd_fr)
        df1.to_csv(route_csv, index=False, encoding="utf-8-sig")
        df1.to_json(route, orient='table')

        print('The End!!!')

    except requests.exceptions.Timeout as errd:
        print("Timeout Error : ", errd)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting : ", errc)

    except requests.exceptions.HTTPError as errb:
        print("Http Error : ", errb)

    except requests.exceptions.RequestException as erra:
        print("AnyException : ", erra)


    return df1


#-----------------------------------------------------
#  공공데이터 포털에서 api i/f 통한 민원 데이터 가져오기
#  오늘의 민원 이슈
#  param :
#      target = 'pttn:일반민원, dfpt:고충민원, saeol:수집민원, prpl:제안, qna:정책Q&A, qna_origin:공개민원'
#      std_ymd = yyyymm (기준 일자)

#  return :
#-----------------------------------------------------
def get_today_topic_keyword(std_ymd,  target):
    #파일 path
    file_path = FilePathClass()
    maxResult = apifp.COMPLAIN_MAX_ROW
    analysis_date = std_ymd

    url = apifp.COMPLAIN_API_URL + apifp.COMPLAIN_API_URL_TOPIC + '?serviceKey=' + apifp.COMPLAIN_API_KEY + '&searchDate=' + analysis_date + '&todayTopicTopN=' + maxResult + '&target=' + target
    print('URL: ', url)

    dataPath = apifp.COMPLAIN_DATA_PATH_TOPIC

    # 분야별 데이터 저장 full path
    get_complain_data_path = file_path.get_raw_collect_path() + dataPath + "//"

    try:

        res = urlopen(url).read()  # URL 열고 읽음
        resJson = json.loads(res)  # json 문자열을 파이썬 객체로 변환
        df1 = json_normalize(resJson)  # json 데이터를 dataframe으로 변환

        # 폴더 존재 여부 확인하여 없으면 폴더 생성
        if file_path.is_path_exist_check(get_complain_data_path) == False:
            file_path.make_path(get_complain_data_path)

        route = "{0}{1}_{2}.json".format(get_complain_data_path,  dataPath, analysis_date)
        route_csv = "{0}{1}_{2}.csv".format(get_complain_data_path, dataPath, analysis_date)
        df1.to_csv(route_csv, index=False, encoding="utf-8-sig")
        df1.to_json(route, orient='table')

        print('The End!!!')

    except requests.exceptions.Timeout as errd:
        print("Timeout Error : ", errd)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting : ", errc)

    except requests.exceptions.HTTPError as errb:
        print("Http Error : ", errb)

    except requests.exceptions.RequestException as erra:
        print("AnyException : ", erra)


    return df1


#-----------------------------------------------------
#  공공데이터 포털에서 api i/f 통한 민원 데이터 가져오기
#  최다민원
#  param :
#      target = 'pttn:일반민원, dfpt:고충민원, saeol:수집민원, prpl:제안, qna:정책Q&A, qna_origin:공개민원'
#      std_ymd = yyyymm (기준 일자)
#      rangeCount =  분석대상시간으로부터 period에 따른 기간을 입력 (수집 종료 년월 - 수집 시작년월), 문자열
#  return :
#-----------------------------------------------------
def get_dfTopN_keyword(std_ymd,  target):

    file_path = FilePathClass()
    maxResult = apifp.COMPLAIN_MAX_ROW
    analysis_date = std_ymd

    #적용 period(HOURLY, DAILY, WEEKLY, MONTHLY, YEARLY)
    #분석 데이터를 월별로 집계하므로 다른 데이타와 기간을 통일
    period = 'MONTHLY'
    rangeCount = '1'

    url = apifp.COMPLAIN_API_URL + apifp.COMPLAIN_API_URL_DFTOPKW + '?serviceKey=' + apifp.COMPLAIN_API_KEY + '&target=' + target + '&period=' + period + '&analysisTime=' + analysis_date + '&rangeCount=' + rangeCount + '&maxResult=' + maxResult
    print('URL: ', url)

    dataPath = apifp.COMPLAIN_DATA_PATH_DFTOPKW

    # 분야별 데이터 저장 full path
    get_complain_data_path = file_path.get_raw_collect_path() + dataPath + "//"

    try:

        res = urlopen(url).read()  # URL 열고 읽음
        resJson = json.loads(res)  # json 문자열을 파이썬 객체로 변환
        df1 = json_normalize(resJson)  # json 데이터를 dataframe으로 변환

        # 폴더 존재 여부 확인하여 없으면 폴더 생성
        if file_path.is_path_exist_check(get_complain_data_path) == False:
            file_path.make_path(get_complain_data_path)

        route = "{0}{1}_{2}.json".format(get_complain_data_path,  dataPath, std_ymd)
        route_csv = "{0}{1}_{2}.csv".format(get_complain_data_path, dataPath, std_ymd)
        df1.to_csv(route_csv, index=False, encoding="utf-8-sig")
        df1.to_json(route, orient='table')

        print('The End!!!')

    except requests.exceptions.Timeout as errd:
        print("Timeout Error : ", errd)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting : ", errc)

    except requests.exceptions.HTTPError as errb:
        print("Http Error : ", errb)

    except requests.exceptions.RequestException as erra:
        print("AnyException : ", erra)


    return df1


#-----------------------------------------------------
#  공공데이터 포털에서 api i/f 통한 민원 데이터 가져오기
#  유사사례 정보
#  param :
#      keyword = 분석 키워드
#      target = 'qna:정책Q&A, qna_origin:공개민원'
#  return :
#-----------------------------------------------------
def get_similarInfo(keyword):

    file_path = FilePathClass()
    maxResult = apifp.COMPLAIN_MAX_ROW
    start_page = '1'
    target = 'qna,qna_origin'

    url = apifp.COMPLAIN_API_URL + apifp.COMPLAIN_API_URL_SIMIL +'?serviceKey=' + apifp.COMPLAIN_API_KEY + '&startPos=' + start_page + '&retCount=' + maxResult + '&searchword=' + quote(keyword) + '&target=' + target

    print('URL: ', url)

    dataPath = apifp.COMPLAIN_DATA_PATH_SIMIL

    # 분야별 데이터 저장 full path
    get_complain_data_path = file_path.get_raw_use_path()  + "//"

    try:
        res = urlopen(url).read()  # URL 열고 읽음
        resJson = json.loads(res)  # json 문자열을 파이썬 객체로 변환
        df1 = json_normalize(resJson)  # json 데이터를 dataframe으로 변환

        # 폴더 존재 여부 확인하여 없으면 폴더 생성
        if file_path.is_path_exist_check(get_complain_data_path) == False:
            file_path.make_path(get_complain_data_path)

        route = "{0}{1}_{2}.json".format(get_complain_data_path,  dataPath, unquote(keyword))
        route_csv = "{0}{1}_{2}.csv".format(get_complain_data_path, dataPath, unquote(keyword))
        df1.to_csv(route_csv, index=False, encoding="utf-8-sig")
        df1.to_json(route, orient='table')

        print('The End!!!')

    except requests.exceptions.Timeout as errd:
        print("Timeout Error : ", errd)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting : ", errc)

    except requests.exceptions.HTTPError as errb:
        print("Http Error : ", errb)

    except requests.exceptions.RequestException as erra:
        print("AnyException : ", erra)


    return df1


#-----------------------------------------------------
#  공공데이터 포털에서 api i/f 통한 민원 데이터 가져오기
#  연관어 분석 정보
#  param :
#      target = 'pttn:일반민원, dfpt:고충민원, saeol:수집민원, prpl:제안, qna_origin:공개민원'
#  return :
#-----------------------------------------------------
def get_wd_cloud_info(keyword, std_ymd_fr, std_ymd_to, target):

    file_path = FilePathClass()
    maxResult = '10' #apifp.COMPLAIN_MAX_ROW
    analysis_date_fr = std_ymd_fr
    analysis_date_to = std_ymd_to


    url = apifp.COMPLAIN_API_URL + apifp.COMPLAIN_API_URL_WDCLOUD +'?serviceKey=' + apifp.COMPLAIN_API_KEY + '&searchword=' + quote(keyword) + '&resultCount=' + maxResult + '&target=' + target + '&omitDuplicate=true' + '&dateFrom=' + analysis_date_fr + '&dateTo='+ analysis_date_to

    print('URL: ', url)

    dataPath = apifp.COMPLAIN_DATA_PATH_WDCLOUD

    # 분야별 데이터 저장 full path
    get_complain_data_path = file_path.get_raw_use_path() + "//"

    try:

        res = urlopen(url).read()  # URL 열고 읽음
        resJson = json.loads(res)  # json 문자열을 파이썬 객체로 변환
        df1 = json_normalize(resJson)  # json 데이터를 dataframe으로 변환

        # 폴더 존재 여부 확인하여 없으면 폴더 생성
        if file_path.is_path_exist_check(get_complain_data_path) == False:
            file_path.make_path(get_complain_data_path)

        route = "{0}{1}_{2}.json".format(get_complain_data_path,  dataPath, keyword)
        route_csv = "{0}{1}_{2}.csv".format(get_complain_data_path, dataPath, keyword)
        df1.to_csv(route_csv, index=False, encoding="utf-8-sig")
        df1.to_json(route, orient='table')

        print('The End!!!')

    except requests.exceptions.Timeout as errd:
        print("Timeout Error : ", errd)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting : ", errc)

    except requests.exceptions.HTTPError as errb:
        print("Http Error : ", errb)

    except requests.exceptions.RequestException as erra:
        print("AnyException : ", erra)


    return df1


def get_complaint_data(part, date, target):
    day_list = getDayList(date)
    if part == '전체':
        for i in day_list:
            get_risting_keyword(i, target)
            get_today_topic_keyword(i,  target)
            get_dfTopN_keyword(i, target)
        get_topN_keyword(date+"01", getMonthRange(date[:4], date[-2:]).strftime('%Y%m%d'), target)
    elif part == '급등':
        for i in day_list:
            print(i)
            get_risting_keyword(i, target)
    elif part == '오늘':
        for i in day_list:
            get_today_topic_keyword(i,  target)
    elif part == '최다':
        for i in day_list:
            get_dfTopN_keyword(i, target)
    elif part == '핵심':
        get_topN_keyword(date+"01", getMonthRange(date[:4], date[-2:]).strftime('%Y%m%d'), target)


#get_complaint_data('오늘', '202203', 'pttn,dfpt,saeol,prpl,qna_origin')
#get_similarInfo('이태원')
#aa = get_news_uuid_list('정치')

#bb = get_news(aa, '정치', '20220430')
