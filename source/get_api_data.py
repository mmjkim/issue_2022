import pandas as pd
import numpy as np
import json
import requests
from urllib.request import urlopen
from pandas import json_normalize

from common.config.filepassclass import *
from common.function.funcDataControl import *
import common.config.apiinfo as apifp

from common.function.funcCommon import *

# -----------------------------------------------------
#  공공데이터 포덜에서 api i/f 통한 뉴스 데이터 uuid 가져오기
#  param :
#      part = '정치, 사회, 경제, 전체'
#  return :
#      df = dataframe
# -----------------------------------------------------

def get_news_uuid_list(psPart):

    url = apifp.NEWS_API_URL_UUID

    if psPart == '정치':
        url = url + apifp.NEWS_API_URL_POLITICS  # namespace=15065411/v1
        namespace = apifp.NEWS_API_URL_POLITICS.replace('namespace=', '/') + "/"
        dataPath = apifp.NEWS_DATA_PATH_POLITICS
    elif psPart == '경제':
        url = url + apifp.NEWS_API_URL_ECONOMY   # namespace=15068899/v1
        namespace = apifp.NEWS_API_URL_ECONOMY.replace('namespace=', '/') + "/"
        dataPath = apifp.NEWS_DATA_PATH_ECONOMY
    elif psPart == '사회':
        url = url + apifp.NEWS_API_URL_SOCIETY   # namespace=15065434/v1
        namespace = apifp.NEWS_API_URL_SOCIETY.replace('namespace=', '/') + "/"
        dataPath = apifp.NEWS_DATA_PATH_SOCIETY

    res = urlopen(url).read()
    json_data = json.loads(res)
    uddi_list = list(json_data.get('paths').values())
    df = pd.DataFrame(columns=['part', 'date', 'uddi'])

    for i in range(len(uddi_list)):
        df.loc[i] = [psPart, uddi_list[i]['get']['summary'][-8:],
                     namespace + uddi_list[i]['get']['operationId'][3:]]

    return df


#-----------------------------------------------------
#  공공데이터 포덜에서 api i/f 통한 뉴스 데이터 가져오기
#  param :
#      uddi = uddi 값
#      part = '정치, 사회, 경제, 전체'
#      date = yyyymmdd, ALL (일자는 숫자형 해당월의 마지막날짜)
#  return :
#-----------------------------------------------------
def get_news(uddi, part, day):

    df_uddi = uddi

    # if day == 'ALL':
    #     get_uddi = df_uddi[(df_uddi['part'] == part)]
    #     get_data = get_uddi[['uddi', 'date']]
    #     #list_day = df[(df['part'] == psPart)]['date']
    # else:
    #     get_uddi = df_uddi[(df_uddi['part'] == part) & (df_uddi['date'] == day)]
    #     get_data = get_uddi[['uddi', 'date']]


    get_uddi = df_uddi[(df_uddi['part'] == part) & (df_uddi['date'] == day)]
    get_data = get_uddi[['uddi', 'date']]

    #파일 path
    file_path = FilePathClass()

    #분야별 데이터 저장 path
    if part == '정치':
        dataPath = apifp.NEWS_DATA_PATH_POLITICS
    elif part == '경제':
        dataPath = apifp.NEWS_DATA_PATH_ECONOMY
    elif part == '사회':
        dataPath = apifp.NEWS_DATA_PATH_SOCIETY

    #분야별 데이터 저장 full path
    get_news_data_path = file_path.get_raw_collect_path() +  dataPath + "//"

    #폴더 존재 여부 확인하여 없으면 폴더 생성
    if file_path.is_path_exist_check(get_news_data_path) == False:
       file_path.make_path(get_news_data_path)

    #uuid 값으로 api 호출 후 데이터를 csv로 저장
    for index, row in get_data.iterrows():

        url = apifp.NEWS_API_URL + row['uddi'] + '?age=1&perPage=200&serviceKey=' + apifp.NEWS_API_KEY
        url = url.replace("['", '')
        url = url.replace("']", '')

        res = urlopen(url).read()
        resJson = json.loads(res)
        df = json_normalize(resJson.get('data'))
        # print("---")
        route = get_news_data_path + "{0}_{1}.csv".format(dataPath, row['date'])
        df.to_csv(route, index=False, encoding="utf-8-sig")


def get_news_data(part, day1, day2):
    if part == '전체':
        list_part = ['정치', '사회', '경제']
    else:
        list_part = [part]


    date_list = getMonthList(datetime.strptime(day1+"01", "%Y%m%d"),
                 datetime.strptime(day2+"01", "%Y%m%d"),
                 getMonthGap(datetime.strptime(day1+"01", "%Y%m%d"),
                             datetime.strptime(day2+"01", "%Y%m%d")))

    for i in list_part:
        uddi = get_news_uuid_list(i)
        for j in date_list:
            news_data = get_news(uddi, i, j)


# aa = get_news_uuid_list('경제')
# bb = get_news(aa, '경제', '20220630')

# test('전체', '202109', '202209')
