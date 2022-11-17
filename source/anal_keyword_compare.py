#-------------------------------------------------------
# 키워드 동시 출현 분석
# 오늘의 민원이슈 vs 뉴스_정치, 뉴스_사회, 뉴스_사회
#
#-------------------------------------------------------
from common.config.filepassclass import *
import common.config.apiinfo as apifp
#from common.function.funcCommon import *

import pandas as pd
import numpy as np

def compare_keyword(part):

    # 파일 path
    file_path = FilePathClass()
    if part == "오늘" :
        #오늘의 민원 가져오기
        filename = "{0}{1}\\1차마트_{2}.csv".format(file_path.get_raw_use_path(), apifp.COMPLAIN_DATA_PATH_TOPIC, part)
    elif part == "급등":
        filename = "{0}{1}\\1차마트_{2}.csv".format(file_path.get_raw_use_path(), apifp.COMPLAIN_DATA_PATH_RISE, part)
    elif part == "최다":
        filename = "{0}{1}\\1차마트_{2}.csv".format(file_path.get_raw_use_path(), apifp.COMPLAIN_DATA_PATH_DFTOPKW, part)


    si_complain_data = pd.read_csv(filename, encoding="utf-8-sig")

    #뉴스_사회
    filename = "{0}{1}\\1차마트_{2}.csv".format(file_path.get_raw_use_path(), apifp.NEWS_DATA_PATH_SOCIETY, '사회')
    si_news_society_data = pd.read_csv(filename, encoding="utf-8-sig")

    #뉴스_정치
    filename = "{0}{1}\\1차마트_{2}.csv".format(file_path.get_raw_use_path(), apifp.NEWS_DATA_PATH_POLITICS, '정치')
    si_news_politics_data = pd.read_csv(filename, encoding="utf-8-sig")

    #뉴스_정치
    filename = "{0}{1}\\1차마트_{2}.csv".format(file_path.get_raw_use_path(), apifp.NEWS_DATA_PATH_ECONOMY, '경제')
    si_news_economy_data = pd.read_csv(filename, encoding="utf-8-sig")


    #시리즈형 데이타를 프레임임형으로 변한
    df_complain_data = si_complain_data['keyword'].to_frame()

    #중복되는 데이터 저장 데이타 프레임 정의
    df_overlap_keyword = pd.DataFrame()
    column_names = ['keyword','type', 'overlap_keyword']
    df_overlap_keyword = df_overlap_keyword.reindex(columns = column_names)

    #뉴스_사회
    df_result = get_overlap_keyword(df_complain_data, si_news_society_data, '뉴스_사회')
    df_overlap_keyword = pd.concat([df_overlap_keyword, df_result])


    #뉴스_정치
    df_result = get_overlap_keyword(df_complain_data, si_news_politics_data, '뉴스_정치')
    df_overlap_keyword = pd.concat([df_overlap_keyword, df_result])

    #뉴스_경제
    df_result = get_overlap_keyword(df_complain_data, si_news_economy_data, '뉴스_경제')
    df_overlap_keyword = pd.concat([df_overlap_keyword, df_result])
    #중복제거
    df_overlap_keyword = df_overlap_keyword.drop_duplicates(['keyword','type', 'overlap_keyword'])

    #print('---------------------------')
    #print(df_overlap_keyword.sort_values(by=['overlap_keyword']))

    #결과값 저장
    # 저장될 폴더가 있는지 확인
    if not os.path.exists(file_path.get_raw_use_path()):
        os.makedirs(file_path.get_raw_use_path())

    # 저장할 파일명 생성
    savefile = "{0}\\{1}_{2}.csv".format(file_path.get_raw_use_path(), "동시출현키워드", part)
    # 파일저장
    df_overlap_keyword = df_overlap_keyword.sort_values(by=['overlap_keyword'])
    df_overlap_keyword.to_csv(savefile, encoding="utf-8-sig", index=False)

    print('The End!!!')

    return df_overlap_keyword



# --------------------------------------------
# si_source_data = 민원 데이터
# si_target_data = 뉴스 데이터
# --------------------------------------------
def get_overlap_keyword(df_source_data, si_target_data, type_info):

    #결과값 저장 데이터 프레임 정의
    df_return = pd.DataFrame()
    column_names = ['keyword','type', 'overlap_keyword']
    df_return = df_return.reindex(columns = column_names)

    #동시 출현 데이터 추출
    #뉴스 데이타의 키워드와 민원데이터의 오늘의 민원 데이터를 비교
    for idx in si_target_data.index:  #뉴스 데이터 프레임
        df_temp = pd.DataFrame()
        # 비교할 뉴스 데이터의 키워드
        temp_keyword = si_target_data.loc[idx, 'keyword']
        # 오늘의 민원데이터 뉴스 키워드가 일치하는 데이타 추출
        df_temp = df_source_data[df_source_data['keyword'].str.contains(temp_keyword)]
        # 데이타 추출 건수
        cnt = df_temp.size
        if cnt > 0 :
           df_temp = df_temp.assign(type=type_info, overlap_keyword=temp_keyword)
           df_return = pd.concat([df_return, df_temp])


    return df_return

#compare_keyword('최다')
