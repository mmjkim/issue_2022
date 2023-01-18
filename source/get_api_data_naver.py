import pandas as pd
import numpy as np
import urllib
import json
from pandas import json_normalize

from common.config.filepassclass import *
import common.config.apiinfo as apifp
from source.save_anal_mart import *

def naver_trend_search(std_ymd_fr, std_ymd_to, keys):
    from urllib import request

    #파일 path
    file_path = FilePathClass()

    client_id = apifp.NAVER_API_ID
    client_secret = apifp.NAVER_API_PW
    link = apifp.NAVER_API_URL
    request = request.Request(link)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    request.add_header("Content-Type", "application/json")

    start_date_t_s = std_ymd_fr.strftime("%Y-%m-%d")
    end_date_s = std_ymd_to.strftime("%Y-%m-%d")

    #timeUnit = date: 일간, week: 주간, month: 월간
    time_unit = apifp.NAVER_TIME_UNIT

    group_nm = keys[0]
    keyword_list = "\"" + keys[0] + "\""

    keyword_list = keyword_list + ",\"" + keys[1] + "\""

    body = "{\"startDate\":\"" + start_date_t_s + "\",\"endDate\":\"" + end_date_s + "\",\"timeUnit\":\"" + time_unit + \
           "\",\"keywordGroups\":[{\"groupName\":\"" + group_nm + "\",\"keywords\":[" + keyword_list + "]}]}"

    try:
        response = urllib.request.urlopen(request, data=body.encode("utf-8"))
        response_body = response.read()
        scraped = response_body.decode('utf-8')

        dataPath = apifp.NAVER_DATA_PATH_KEYWORD
        # 분야별 데이터 저장 full path
        get_complain_data_path = file_path.get_raw_use_path()

        # 폴더 존재 여부 확인하여 없으면 폴더 생성
        if file_path.is_path_exist_check(get_complain_data_path) == False:
            file_path.make_path(get_complain_data_path)

        result = json.loads(scraped)
        temp_db = result["results"][0]["data"]
        keyword = np.array([keys[1] for i in temp_db])
        time = np.array([i["period"] for i in temp_db])
        value = np.array([i["ratio"] for i in temp_db])

        data = pd.DataFrame({"keyword": keyword, "Time": time, "Value": value})
        df_save_data = data.copy()
        df_save_data = df_save_data.reset_index()
        df_save_data = df_save_data.drop(['index'], axis=1)

        savefile = "{0}/{1}_{2}.csv".format(get_complain_data_path, dataPath, keys[1])
        df_save_data.to_csv(savefile, encoding='euc-kr')

        #데이터를 db에 저장
        save_db_naver_data()

        print("The End!!!")

        return df_save_data

    except Exception as e:
        print(keys[1] + " get naver data -> Error :", e)
