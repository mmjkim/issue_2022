import calendar
import pandas as pd
from datetime import datetime
from dateutil import rrule
from dateutil.relativedelta import relativedelta


# calendar를 사용하여 마지막 날짜 얻기
# param :
#     year = '년도'(yyyy)
#     mm = '월'(mm)
# return :
#     해당년월 + 마지막 일자
def getMonthRange(year, month):

    if (year == str(datetime.today().year)) & (month == str(datetime.today().month)):
        date = datetime.strptime(datetime.today().date().strftime("%Y%m%d"), "%Y%m%d").date()
    else:
        last_day = calendar.monthrange(int(year), int(month))[1]
        date = datetime(year=int(year), month=int(month), day=last_day).date()

    return date


# 두 날짜 사이 월의 간격 계산
# param :
#     d1 = datetime.strptime("20201201", "%Y%m%d") 매월 시작일자
#     d2 = datetime.strptime("20211201", "%Y%m%d") 매월 시작일자
# return :
#     d2-d1의 값(숫자)
def getMonthGap(d1, d2):

    months = rrule.rrule(rrule.MONTHLY, dtstart=d1, until=d2).count()
    return months


# (시작 일자 ~ 시작 일자 + cnt개월)의 마지막 날짜 계산
# param :
#     d1 = datetime.strptime("20201225", "%Y%m%d")
#     cnt = 간격
# return :
#     list(해당 월의 간격에 대한 마지막 날짜 list)
def getMonthList(d1, cnt):

    monthlist = []

    for i in range(cnt):
        date = d1 + relativedelta(months=i)
        monthlist.append(getMonthRange(date.year, date.month).strftime('%Y%m%d'))

    return monthlist


# 해당 월의 모든 일자 계산
# param :
#     d1 = "202202"
# return :
#     list(해당 월의 모든 일자 list)
def getDayList(d1):
    
    start = datetime.strptime(d1 + "01", "%Y%m%d")

    if (int(d1[:4]) == datetime.today().year) & (int(d1[-2:]) == datetime.today().month):
        end = datetime.strptime(datetime.today().date().strftime("%Y%m%d"), "%Y%m%d")
    else:
        end = datetime.strptime(getMonthRange(int(d1[:4]), int(d1[-2:])).strftime('%Y%m%d'), "%Y%m%d")

    daylist = [date.strftime("%Y%m%d") for date in pd.date_range(start, periods=(end - start).days + 1)]

    return daylist
