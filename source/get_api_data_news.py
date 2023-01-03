import pandas as pd
import json
from urllib.request import urlopen
from pandas import json_normalize
from datetime import datetime

from common.config.filepassclass import *
import common.config.apiinfo as apifp
from common.function.funcCommon import *
from common.database import db_mdb as mdb


# -----------------------------------------------------
#  공공데이터포털에서 api i/f 통한 뉴스 데이터 uddi 가져오기
#  param :
#      part = '정치, 사회, 경제, 전체'
#  return :
#      df = dataframe
# -----------------------------------------------------
def get_news_uddi_list(psPart):

    url = apifp.NEWS_API_URL_UUID

    if psPart == '정치':
        url = url + apifp.NEWS_API_URL_POLITICS  # namespace=15065411/v1
        namespace = apifp.NEWS_API_URL_POLITICS.replace('namespace=', '/') + "/"
    elif psPart == '경제':
        url = url + apifp.NEWS_API_URL_ECONOMY   # namespace=15068899/v1
        namespace = apifp.NEWS_API_URL_ECONOMY.replace('namespace=', '/') + "/"
    elif psPart == '사회':
        url = url + apifp.NEWS_API_URL_SOCIETY   # namespace=15065434/v1
        namespace = apifp.NEWS_API_URL_SOCIETY.replace('namespace=', '/') + "/"

    res = urlopen(url).read()
    json_data = json.loads(res)
    uddi_list = list(json_data.get('paths').values())
    df = pd.DataFrame(columns=['part', 'date', 'uddi'])

    for i in range(len(uddi_list)):
        df.loc[i] = [psPart, uddi_list[i]['get']['summary'][-8:],
                     namespace + uddi_list[i]['get']['operationId'][3:]]

    return df


#-----------------------------------------------------
#  공공데이터포털에서 api i/f 통한 뉴스 데이터 가져오기
#  param :
#      uddi = uddi 값
#      part = '정치, 사회, 경제, 전체'
#      date = yyyymmdd, ALL (일자는 숫자형 해당 월의 마지막 날짜)
#  return :
#-----------------------------------------------------
def get_news(uddi, part, day):
    try:
        df_uddi = uddi

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
        get_news_data_path = file_path.get_raw_collect_path() + dataPath + "//"

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
            df = df.drop(index=df.loc[df['키워드'] == ''].index)
            route = get_news_data_path + "{0}_{1}.csv".format(dataPath, row['date'])
            df.to_csv(route, index=False, encoding="utf-8-sig")

            #------------------------- 마트 적재 데이타 Log 저장 -------------------------
            save_log = mdb.DbUseAnalClass()
            now = datetime.now()
            # values = ['현재일자','데이터 타입' ,'파일명', '수집기간_시작', '수집기간_종료',
            # '저장총건수','마트구분(API, 1마트, 분석, 키워드'), '키워드']
            save_log.mart_log_save([now.strftime('%Y-%m-%d %H:%M:%S'),'뉴스',route,
                                    row['date'], row['date'], len(df), 'API', ''])

    except Exception as e:
        print(part + " get_news -> Error :", e)


def get_news_data(part, day1, day2):
    if part == '전체':
        list_part = ['정치', '사회', '경제']
    else:
        list_part = [part]

    date_list = getMonthList(datetime.strptime(day1+"01", "%Y%m%d"),
                 getMonthGap(datetime.strptime(day1+"01", "%Y%m%d"),
                             datetime.strptime(day2+"01", "%Y%m%d")))

    for i in list_part:
        uddi = get_news_uddi_list(i)
        for j in date_list:
            get_news(uddi, i, j)
