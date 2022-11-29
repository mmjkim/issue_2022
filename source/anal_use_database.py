import pyodbc
import pandas as pd
from common.config.filepassclass import *

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
#
#udb = DbUseAnalClass()
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
# aa = 'select * from CONPLAIN_TO_DAY'
# udb.select_qry(aa)
# # print(bb)

#aa = 'DELETE FROM CONPLAIN_TO_DAY'
#udb.delete_qry(aa)
