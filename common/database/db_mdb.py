import pyodbc
import pandas as pd
from common.config.filepassclass import *
from datetime import datetime

class DbUseAnalClass:

    MDB_FILE_NAME = "issue_db.accdb;"
    file_path = FilePathClass()
    db_name_path = file_path.get_root_path() + '\\' + MDB_FILE_NAME  # "D:\issue_2022\issue_db.accdb;"

    def __init__(self):
        try:
            self.conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                                       r'DBQ=' + self.db_name_path + '')
            self.cursor = self.conn.cursor()
        except pyodbc.Error as e:
            print("Data Base Error:", e, "\n 데이터 베이스 확인 필요")
        except Exception as e:
            print("Data Base Error:", e, "\n 데이터 베이스 확인 필요")

    #쿼리 실행
    def execute_qry(self, qry):
        try:
            self.cursor.execute('{0}'.format(qry))
            self.conn.commit()
            return 1
        except pyodbc.Error as e:
            print(e)
            return -1

    def select_count(self, qry):
        try:
            self.cursor.execute('{0}'.format(qry))
            return len(self.cursor.fetchall())
        except pyodbc.Error as e:
            print(e)
            return -1

    def select_qry(self, qry):
        try:
            df = pd.read_sql(qry, self.conn)
            return df
        except pyodbc.Error as e:
            print(e)
            return -1

    def insert_one_qry(self, qry):
        try:
            self.cursor.execute(qry)
            self.conn.commit()
        except pyodbc.Error as e:
            print(e)

    def insert_many_qry(self, qry_list):

        try:
            for qry in qry_list:
                self.cursor.execute(qry)

            self.conn.commit()
        except pyodbc.Error as e:
            print(e)

    def update_qry(self, qry):

        try:
            self.cursor.execute(qry)
            self.conn.commit()
        except pyodbc.Error as e:
            print(e)


    def delete_qry(self, qry):
        try:
            self.cursor.execute(qry)
            self.conn.commit()
        except pyodbc.Error as e:
            print(e)

    # values의 값은 list type으로 전달
    # values = ['현재일자','데이터 타입' ,'파일명', '수집기간_시작', '수집기간_종료', '저장총건수','마트구분(API, 1마트, 분석, 키워드'), '키워드']
    def mart_log_save(self, value):
        try:
            insertQry = " INSERT INTO ISSUE_DATA_MART_INFO (WRITE_YMD,DATA_TYPE, DATA_NAME, COLLECT_YMD_STD, COLLECT_YMD_END, DATA_TOT_CNT, MART_TYPE, KEYWORD) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')"
            qry = insertQry.format(value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7])
            self.insert_one_qry(qry)
        except pyodbc.Error as e:
            print(e)


    #----------------------------------------------------------------
    # DB에 수집된 데이터 LOG 정보 저장 1차 마트
    #----------------------------------------------------------------
    def mart_log_qry(self, dfAllData, type, part):

        try:
            # values의 값은 list type으로 전달
            # values = ['현재일자','데이터 타입' ,'파일명', '수집기간_시작', '수집기간_종료', '저장총건수','마트구분(API, 1마트, 분석, 키워드'), '키워드']
            now = datetime.now()
            savefile_name = "{0}_{1}.csv".format('1차마트', part)
            # 데이터 정렬
            dfAllData = dfAllData.sort_values(by=['stdym'], ascending=True)
            std_ymd = dfAllData['stdym'].iloc[0]
            end_ymd = dfAllData['stdym'].iloc[-1]

            values = [now.strftime('%Y-%m-%d %H:%M:%S'),type, savefile_name, std_ymd, end_ymd, len(dfAllData), '1차마트', '']
            self.mart_log_save(values)
        except pyodbc.Error as e:
            print(e)
