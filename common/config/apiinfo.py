# API I/F 정보 관리
# 인증키, url, 저장 폴더 정의

#------------- 뉴스 API I/F 정보 ---------------------
NEWS_API_KEY = 'NAiIcJsR2pyzyHlYnLqu9gnPC7D1kVAhhfg6cEq6Y9p6GXiTrbFBbf5ivs%2FmMlAAFuemeNPFbwp2yyJ1G07o9A%3D%3D'

NEWS_API_URL = 'https://api.odcloud.kr/api'

NEWS_API_URL_UUID = 'https://infuser.odcloud.kr/oas/docs?'
#정치
NEWS_API_URL_POLITICS = 'namespace=15065411/v1'
#경제
NEWS_API_URL_ECONOMY = 'namespace=15068899/v1'
#사회
NEWS_API_URL_SOCIETY = 'namespace=15065434/v1'

#------------- 뉴스 데이터 저장 폴더 ---------------------
NEWS_DATA_PATH_POLITICS = '뉴스_정치'
NEWS_DATA_PATH_ECONOMY = '뉴스_경제'
NEWS_DATA_PATH_SOCIETY = '뉴스_사회'

#------------- 민원 API I/F 정보 ---------------------
# COMPLAIN_API_KEY = '8PvVYRda2ocf1OZTdsTwNczETCQL%2FiOshpEAWGzqVLdWXJrNmIzl7OzC2FCrD80SbCdDbd39a4Rz6azpxpMFmg%3D%3D'
COMPLAIN_API_KEY = 'NAiIcJsR2pyzyHlYnLqu9gnPC7D1kVAhhfg6cEq6Y9p6GXiTrbFBbf5ivs%2FmMlAAFuemeNPFbwp2yyJ1G07o9A%3D%3D'
COMPLAIN_API_URL = 'https://apis.data.go.kr/1140100/minAnalsInfoView5/'
#급등키워드
COMPLAIN_API_URL_RISE = 'minRisingKeyword5'
#핵심키워드
COMPLAIN_API_URL_TOP = 'minTopNKeyword5'
#민원분석 분류체계
COMPLAIN_API_URL_CLFC = 'minClfcInfo5'
#맞춤형통계 정보
COMPLAIN_API_URL_STATIC = 'minStaticsInfo5'
#유사사례 정보
COMPLAIN_API_URL_SIMIL = 'minSimilarInfo5'
#키워드 트렌드 정보
COMPLAIN_API_URL_TREND = 'minTimeSeriseView5'
#오늘의 민원 이슈
COMPLAIN_API_URL_TOPIC = 'minTodayTopicInfo5'
#연관어 분석 정보
COMPLAIN_API_URL_WDCLOUD = 'minWdcloudInfo5'
#민원발생 기관 순위
COMPLAIN_API_URL_GOVRANK = 'minMofacetInfo5'
#민원발생 지역 순위
COMPLAIN_API_URL_ARERANK = 'minMrfacetInfo5'
#키워드 기반 민원 건수 정보
COMPLAIN_API_URL_KWCNT = 'minSearchDocCnt5'
#지역 인구수 대비 민원 현황 정보
COMPLAIN_API_URL_PEVCOMP = 'minMrPopltnRtInfo5'
#최다 민원 키워드 정보
COMPLAIN_API_URL_DFTOPKW = 'minDFTopNKeyword5'
#분석보고서 정보
COMPLAIN_API_URL_ANLRPT = 'minAnalsRptstInfo5'
#키워드 기반 성별 정보
COMPLAIN_API_URL_KWSEX = 'minPttnStstGndrInfo5'
#키워드 기반 연령 정보
COMPLAIN_API_URL_KWAGE = 'minPttnStstAgeInfo5'

#------------- 민원 데이터 저장 폴더 ---------------------
#급등키워드
COMPLAIN_DATA_PATH_RISE = '민원_급등키워드'
#핵심키워드
COMPLAIN_DATA_PATH_TOP = '민원_핵심키워드'
#민원분석 분류체계
COMPLAIN_DATA_PATH_CLFC = '민원_분석분류체계'
#맞춤형통계 정보
COMPLAIN_DATA_PATH_STATIC = '민원_맞춤형통계정보'
#유사사례 정보
COMPLAIN_DATA_PATH_SIMIL = '민원_유사사례정보'
#키워드 트렌드 정보
COMPLAIN_DATA_PATH_TREND = '민원_키워드트렌드정보'
#오늘의 민원 이슈
COMPLAIN_DATA_PATH_TOPIC = '민원_오늘의민원이슈'
#연관어 분석 정보
COMPLAIN_DATA_PATH_WDCLOUD = '민원_연관어분석정보'
#민원발생 기관 순위
COMPLAIN_DATA_PATH_GOVRANK = '민원_발생기관순위'
#민원발생 지역 순위
COMPLAIN_DATA_PATH_ARERANK = '민원_발생지역순위'
#키워드 기반 민원 건수 정보
COMPLAIN_DATA_PATH_KWCNT = '민원_키워드기반민원건수정보'
#지역 인구수 대비 민원 현황 정보
COMPLAIN_DATA_PATH_PEVCOMP = '민원_지역인구수대비민원현황정보'
#최다 민원 키워드 정보
COMPLAIN_DATA_PATH_DFTOPKW = '민원_최다민원키워드정보'
#분석보고서 정보
COMPLAIN_DATA_PATH_ANLRPT = '민원_분석보고서정보'
#키워드 기반 성별 정보
COMPLAIN_DATA_PATH_KWSEX = '민원_키워드기반성별정보'
#키워드 기반 연령 정보
COMPLAIN_DATA_PATH_KWAGE = '민원_키워드기반연령정보'

COMPLAIN_MAX_ROW = '20'
COMPLAIN_TOPN_MAX_ROW = '100'


#------------- 네이버 API I/F 정보 ---------------------
NAVER_API_URL = 'https://openapi.naver.com/v1/datalab/search'
NAVER_API_ID = 'ofFM6m12_MDK11rfyoct'
NAVER_API_PW = 'jYvpWgXSZg'
NAVER_DATA_PATH_KEYWORD = '네이버_검색어'
NAVER_TIME_UNIT = 'month'


#----------------- 빅카인즈 로그인 정보 -----------------
BIGKINDS_ID = '20191497@daejin.ac.kr'
BIGKINDS_PW = 'wqw1301wqw**'
