import json
import requests
from urllib.request import urlopen
from pandas import json_normalize

from common.config.filepassclass import *
from common.function.funcCommon import *

#-----------------------------------------------------
#  공공데이터 포털에서 api i/f 한국주택금융공사_전세자금대출 금리 정보
#  전세자금대출 금리 정보
#  param :
#  return :
#-----------------------------------------------------
def get_rent_loan_rate():
    #파일 path
    file_path = FilePathClass()

    #test 폴더 생성
    get_test_data_path = file_path.get_data_path() + "test\\"

    #최대 요청 건수
    maxResult = '10'

    #테스트용
    TEST_API_KEY = 'NAiIcJsR2pyzyHlYnLqu9gnPC7D1kVAhhfg6cEq6Y9p6GXiTrbFBbf5ivs%2FmMlAAFuemeNPFbwp2yyJ1G07o9A%3D%3D'
    TEST_API_URL = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'

    #API 호출
    url = TEST_API_URL + '?serviceKey=' + TEST_API_KEY +'&numOfRows='+ maxResult + '&pageNo=1&dataType=json'
    print('URL: ', url)


    try:
        res = urlopen(url).read()  # URL 열고 읽음
        resJson = json.loads(res)  # json 문자열을 파이썬 객체로 변환

        print("resJson: \n", resJson)
        #Json 구조 파악 후 key 값을 정의
        df1 = json_normalize(resJson.get("body")['items'])  # json 데이터를 dataframe으로 변환

        print(df1)
        # 폴더 존재 여부 확인하여 없으면 폴더 생성
        if file_path.is_path_exist_check(get_test_data_path) == False:
            file_path.make_path(get_test_data_path)
            print(get_test_data_path)

        now = datetime.now()
        print()
        route = "{0}{1}_{2}.json".format(get_test_data_path, "test", now.strftime('%Y%m%d'))
        df1.to_json(route, orient='table')

        route_csv = "{0}{1}_{2}.csv".format(get_test_data_path, "test", now.strftime('%Y%m%d'))
        df1.to_csv(route_csv, index=False, encoding="utf-8-sig")

        return df1

    except requests.exceptions.Timeout as errd:  # 요청 시간 초과
        print("Timeout Error : ", errd)

    except requests.exceptions.ConnectionError as errc:  # 네트워크 문제
        print("Error Connecting : ", errc)

    except requests.exceptions.HTTPError as errb:  # 잘못된 HTTP 응답
        print("Http Error : ", errb)

    except requests.exceptions.RequestException as erra:  # 요청에 의해 명시적으로 발생한 모든 예외에서 상속
        print("AnyException : ", erra)

    except Exception:
        import traceback
        traceback.print_exc()


#-----------------------------------------------------
#  공공데이터 포털에서 api i/f 한국주택금융공사_전세자금대출 금리 정보
#  전세자금대출 금리 정보  여러페이지 적용
#  param :
#  return :
#-----------------------------------------------------
def get_rent_loan_rate_page():
    #파일 path
    file_path = FilePathClass()

    #test 폴더 생성
    get_test_data_path = file_path.get_data_path() + "test\\"

    #최대 요청 건수
    maxResult = '10'

    #테스트용
    TEST_API_KEY = 'NAiIcJsR2pyzyHlYnLqu9gnPC7D1kVAhhfg6cEq6Y9p6GXiTrbFBbf5ivs%2FmMlAAFuemeNPFbwp2yyJ1G07o9A%3D%3D'
    TEST_API_URL = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'

    # 최종 결과 df
    df = pd.DataFrame()
    for i in range(1,10):
        # page 번호
        pageNo = i
        #API 호출
        url = TEST_API_URL + '?serviceKey=' + TEST_API_KEY +'&numOfRows='+ maxResult + '&pageNo='+ str(pageNo) + '&dataType=json'
        print('URL: ', url)
        res = urlopen(url).read()  # URL 열고 읽음
        resJson = json.loads(res)  # json 문자열을 파이썬 객체로 변환

        print("resJson: \n", resJson)
        #Json 구조 파악 후 key 값을 정의
        df1 = json_normalize(resJson.get("body")['items'])  # json 데이터를 dataframe으로 변환
        #데이터 붙이기
        df = pd.concat([df, df1])
        #pd.merge(df, df1, how='left', left_on='organId', right_on='organId')

    # 폴더 존재 여부 확인하여 없으면 폴더 생성
    if file_path.is_path_exist_check(get_test_data_path) == False:
        file_path.make_path(get_test_data_path)
        print(get_test_data_path)

    now = datetime.now()

    route_csv = "{0}{1}_{2}.csv".format(get_test_data_path, "test_", now.strftime('%Y%m%d'))
    df.to_csv(route_csv, index=False, encoding="utf-8-sig")

    return df

