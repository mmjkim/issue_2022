#
# 디렉토리 안에 있는 파일들의 데이타를 하나로 합치기
# parameter : filePath = 파일 Path, colList = 컬럼 리스트
# return : dataframe(colList + 파일식별 Key)
#

import glob      # 파일들의 리스트를 뽑을 때 사용(*.*)
import pandas as pd
import os.path
import datetime as dt

def file_data_conflate(filePath, colList) :

    all_files = glob.glob(filePath + "/*.csv")
    dfAllData = pd.DataFrame()

    for filename in all_files:
        df_dis_use = pd.read_csv(filename, encoding='CP949')
        # '수집년월' 컬럼 추가
        df_dis_use['fileKey'] = os.path.basename(filename).replace('.csv', '')
        dfAllData = pd.concat([dfAllData, df_dis_use])

    return dfAllData


#
# 데이타 파일로 저장하기
# parameter : filePath = 파일 Path, fileName = 파일명, dfSaveData = 저장할 데이타
# return : dataframe(colList + 파일식별 Key)
#
def file_data_save(file_path, file_name, df_save_data, bindex):

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    # 저장할 파일명 생성
    savefile = file_path + file_name + str(dt.datetime.now().strftime('%y%m%d') + '.csv')
    # 파일 저장
    df_save_data.to_csv(savefile, encoding='euc-kr', index=bindex)
