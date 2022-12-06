import pyodbc
import pandas as pd
from common.config.filepassclass import *
from datetime import datetime

class DbUseAnalClass:


    MDB_FILE_NAME = "issue_db.accdb;"
    file_path = FilePathClass()
    db_name_path = file_path.get_data_path() + MDB_FILE_NAME  # "D:\issue_2022\data\issue_db.accdb;"

    def __init__(self):

        self.conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                                   r'DBQ=' + self.db_name_path + '')
        self.cursor = self.conn.cursor()

    def select_count(self, qry):
        self.cursor.execute('{0}'.format(qry))
       # print(len(self.cursor.fetchall()))
        return len(self.cursor.fetchall())

    def select_qry(self, qry):
        df = pd.read_sql(qry, self.conn)
        #print(df)
        return df
        # for row in self.cursor.fetchall():
        #     print(row)

    def insert_one_qry(self, qry):
        self.cursor.execute(qry)
        self.conn.commit()

    def insert_many_qry(self, qry_list):

        for qry in qry_list:
            self.cursor.execute(qry)

        self.conn.commit()


    def update_qry(self, qry):
        self.cursor.execute(qry)
        self.conn.commit()

    def delete_qry(self, qry):
        self.cursor.execute(qry)
        self.conn.commit()

    # values의 값은 list type으로 전달
    # values = ['현재일자','데이터 타입' ,'파일명', '수집기간_시작', '수집기간_종료', '저장총건수','마트구분(API, 1마트, 분석, 키워드'), '키워드']
    def mart_log_save(self, value):
        insertQry = " INSERT INTO ISSUE_DATA_MART_INFO (WRITE_YMD,DATA_TYPE, DATA_NAME, COLLECT_YMD_STD, COLLECT_YMD_END, DATA_TOT_CNT, MART_TYPE, KEYWORD) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}' )"
        qry = insertQry.format(value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7])
        self.insert_one_qry(qry)


    #----------------------------------------------------------------
    # DB에 수집된 데이터 LOG 정보 저장 1차 마트
    #----------------------------------------------------------------
    def mart_log_qry(self, dfAllData, type, part):

        # values의 값은 list type으로 전달
        # values = ['현재일자','데이터 타입' ,'파일명', '수집기간_시작', '수집기간_종료', '저장총건수','마트구분(API, 1마트, 분석, 키워드'), '키워드']
        now = datetime.now()
        savefile_name = "{0}_{1}.csv".format('1차마트', part)
        # 데이터 정렬
        dfAllData = dfAllData.sort_values(by=['stdym'], ascending=True)
        std_ymd = dfAllData['stdym'].iloc[0]
        end_ymd = dfAllData['stdym'].iloc[-1]
        #print("end_ymd:", end_ymd)
        values = [now.strftime('%Y-%m-%d %H:%M%S'),type, savefile_name, std_ymd, end_ymd, len(dfAllData), '1차마트', '']
        self.mart_log_save(values)

    #----------------------------------------------------------------
    # DB에 수집된 데이터 LOG 정보 저장 1차 마트
    #----------------------------------------------------------------
   # def save_db_keyword_log(self, dfAllData, part):

##udb = DbUseAnalClass()
# aa = ["insert into CONPLAIN_TO_DAY (YMD, TOPIC, RANK, COUNT) VALUES ('20221129', '테스트3', 2, 5);",
#      "insert into CONPLAIN_TO_DAY (YMD, TOPIC, RANK, COUNT) VALUES ('20221130', '테스트4', 2, 5);",
#      "insert into CONPLAIN_TO_DAY (YMD, TOPIC, RANK, COUNT) VALUES ('20221201', '테스트5', 2, 5);"]
#
#
#
#aa = "insert into CONPLAIN_TO_DAY (YMD, TOPIC, RANK, COUNT) VALUES ('20221128', '테스트2', '2', '5'); \n"
# # #aa += " insert into CONPLAIN_TO_DAY (YMD, TOPIC, RANK, COUNT) VALUES ('20221128', '테스트2', 2, 5);  \n"
# # #aa += " insert into CONPLAIN_TO_DAY (YMD, TOPIC, RANK, COUNT) VALUES ('20221128', '테스트2', 2, 5);  \n"
# #
#udb.insert_one_qry(aa)
#
#aa = 'select * from CONPLAIN_TO_DAY'
#udb.select_qry(aa)
# # print(bb)

#aa = 'DELETE FROM CONPLAIN_TO_DAY'
#udb.delete_qry(aa)
