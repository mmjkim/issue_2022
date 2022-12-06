import pandas as pd

from common.database import db_mdb
from common.function.funcC3Chart import c3chart_html_write as c3Chart
#네이버 키워드 그래프 시각화
# keyword(,)시작일자, 종료일자,
def get_view_naver_keyword(keyword, std_ymd, end_ymd ):

    #db 연결
    db_conn = db_mdb.DbUseAnalClass()
    keywords = keyword.split(',')

    #데이터 조회
    df_marge = pd.DataFrame()
    i = 0

    for word in keywords:
        temp = word.replace(' ', '')
        #키워드가 컬럼값이 되도록 쿼리
        sql = " SELECT YMD, VAL AS {0} FROM NAVER_KEYWORD WHERE YMD BETWEEN '{1}' AND '{2}' AND KEYWORD = '{3}'"
        sql = sql.format(temp, std_ymd, end_ymd, temp)
        df_rs = db_conn.select_qry(sql)

        #키워드별 컬럼을 날짜에 Merge 한다. -> 쿼리도 가능함.
        if i == 0 :
           df_marge = df_rs
           i = 1
        else:
           df_marge = pd.merge(df_marge, df_rs, how='outer', on='YMD')

    df_marge = df_marge.rename(columns={'YMD':'ymd'})
    # print(df_marge)

    # html = c3Chart(df_marge, 'line')
    # print(html)

    return df_marge


# get_view_naver_keyword("이태원,어린이집,할로윈", '2021-01-01', '2022-11-30')
# chart 스크립트 호출
# html = c3Chart(df_marge, 'line')
# # c3chart_html_write(df_marge, 'line'):
# print(html)
