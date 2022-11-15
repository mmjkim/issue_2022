import calendar
import pandas as pd
from datetime import datetime
from dateutil import rrule
from dateutil.relativedelta import relativedelta

# calendar를 사용하여 마지막날 얻기
# param :
#     year = '년도'(yyyy)
#     mm = '월'(mm)
# return :
#     해당년월 + 마지막 일자

# def getMonthRage(year, month):
#
#     date = datetime(year=year, month=month, day=1).date()
#     last_day = calendar.monthrange(date.year, date.month)[1]
#     return (year,month,last_day)
def getMonthRange(year, month):
    # date = datetime(year=year, month=month, day=1).date()
    if (year == str(datetime.today().year)) & (month == str(datetime.today().month)):
        date = datetime.strptime(datetime.today().date().strftime("%Y%m%d"), "%Y%m%d").date()
    else:
        last_day = calendar.monthrange(int(year), int(month))[1]
        date = datetime(year=int(year), month=int(month), day=last_day).date()
    # last_day = 5
    return date


# 두 날짜 사이 월의 간격 계산
# param :
#     d1 = datetime.strptime("20201201", "%Y%m%d") 매월 시작일자
#     d2 = datetime.strptime("20211201", "%Y%m%d") 매월 시작일자
# return :
#    d2-d1의 값(숫자)

def getMonthGap(d1, d2):
    # date1 = datetime(d1.year, d1.month, d1.day)
    # date2 = datetime(d2.year, d2.month, d2.day)

    # diff_month_list = list(rrule.rrule(rrule.MONTHLY, dtstart=date1, until=date2))
    # print(diff_month_list)

    months = rrule.rrule(rrule.MONTHLY, dtstart=d1, until=d2).count()
    return months


# 두 날짜 사이 월의 간격 계산
# param :
#     d1 = datetime.strptime("20201225", "%Y%m%d")
#     d2 = datetime.strptime("20211225", "%Y%m%d")
#     cnt = 간격
# return :
#    list(해당 월의 간격에 대한 마지막 날짜 list)
def getMonthList(d1, d2, cnt):

    monthlist = []

    for i in range(cnt):
        date = d1 + relativedelta(months=i)
        # print(date.strftime('%Y%m%d'))
        # daylist.append(date.strftime('%Y%m%d'))
        monthlist.append(getMonthRange(date.year, date.month).strftime('%Y%m%d'))

    return monthlist


# 해당 월의 모든 일자 계산
# param :
#     d1 = "202202"
# retrun :
#    list(해당 월의 모든 일자 list)
def getDayList(d1):
    start = datetime.strptime(d1 + "01", "%Y%m%d")

    if (int(d1[:4]) == datetime.today().year) & (int(d1[-2:]) == datetime.today().month):
        end = datetime.strptime(datetime.today().date().strftime("%Y%m%d"), "%Y%m%d")
    else:
        end = datetime.strptime(getMonthRange(int(d1[:4]), int(d1[-2:])).strftime('%Y%m%d'), "%Y%m%d")

    daylist = [date.strftime("%Y%m%d") for date in pd.date_range(start, periods=(end - start).days + 1)]

    return daylist


# # 두 날짜사의 월의 간격 계산
# # param :
# #     d1 = datetime.strptime("20201225", "%Y%m%d")
# #     d2 = datetime.strptime("20211225", "%Y%m%d")
# #     cnt = 간격
# # retrun :
# #    list(해당 월의 간격에 대한 마지막 날짜 list)
# def getMonthList(d1, d2, cnt):
#
#     daylist = []
#
#     for i in range(cnt):
#         date = d1 + relativedelta(months=i)
#         print(date.strftime('%Y%m%d'))
#         daylist.append(date.strftime('%Y%m%d'))
#
#     return daylist
