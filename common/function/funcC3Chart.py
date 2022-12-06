import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets

import glob      # 파일들의 리스트를 뽑을 때 사용(*.*)
import pandas as pd
import os.path
import datetime as dt

def test(row_data):
    print('row_data:', row_data)
    html = ""
    html += "<html>                                                                                \n"
    html += "<head>                                                                                 \n"
    html += "    <!-- stylesheet -->                                                                \n"
    html += "    <link href='c3Chart/c3.css' rel='stylesheet'>                                      \n"
    html += "    <script src='https://d3js.org/d3.v3.min.js'></script>                              \n"
    html += "    <script src='https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.11/c3.min.js'></script> \n"
    html += "</head>                                                                                \n"
    html += "<body width='100%', height ='100%'>                                                    \n"
    html += "    <!-- javascript -->                                                                \n"
    html += "    <div id='chart'></div>                                                             \n"
    html += "    <script type='text/javascript'>                                                    \n"
    html += "    	var chart = c3.generate({                                                         \n"
    html += "  				bindto: '#chart',                                                             \n"
    html += "			    data: {                                                                       \n"
    #s -- > data
    html += "               rows:[                                                                   \n"
    html += "				            ['data1', 'data2', 'data3','data4', 'data5', 'data6'],              \n"
    html += "				            [90, 120, 300, 90, 120, 30],                                        \n"
    html += "				            [40, 160, 240, 40, 160, 24],                                        \n"
    html += "				            [50, 200, 290, 50, 200, 29],                                        \n"
    html += "				            [120, 160,230, 120, 160,23],                                        \n"
    html += "				            [80, 130, 300, 80, 130, 30],                                        \n"
    html += "				            [90, 220, 320, 90, 220, 32],                                        \n"
    html += "			        ],                                                                        \n"

    #e -- > data
    #s -- > names
    html += "			        names: {                                                                  \n"
    html += "			            data: 'bar',                                                         \n"
    html += "			            data2: 'bar',                                                         \n"
    html += "			            data3: 'spline',                                                      \n"
    html += "			            data4: 'line',                                                        \n"
    html += "			            data5: 'bar',                                                         \n"
    html += "			            data6: 'area',                                                        \n"
    html += "			        },			                                                              \n"
    #e -- > names

    html += "					    type:'bar',                                                           \n"

    html += "					    labels: true,                                                         \n"
    #s -- > multi_types
    html += "			            types: {                                                              \n"
    html += "			            data: 'bar',                                                         \n"
    html += "			            data2: 'bar',                                                         \n"
    html += "			            data3: 'spline',                                                      \n"
    html += "			            data4: 'line',                                                        \n"
    html += "			            data5: 'bar',                                                         \n"
    html += "			            data6: 'area',                                                        \n"
    #e -- > multi_types
    html += "			        },                                                                        \n"
    html += "			        groups: [                                                                 \n"
    #s -- > groups
    html += "			            ['data1','data2']                                                     \n"
    #e -- > groups
    html += "			        ]                                                                         \n"
    html += "			    },                                                                            \n"
    html += "					axis: {                                                                       \n"
    html += "						                                                                            \n"
    html += "					     x: {                                                                     \n"
    html += "					         type: 'category',                                                    \n"
    #s -- > x_categories
    html += "					         categories: ['cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6']         \n"
    #e -- > x_categories
    html += "					        }                                                                     \n"
    html += "					},                                                                            \n"
    html += "			    subchart: {                                                                   \n"
    #s -- > subchart
    html += "			        show: true,                                                               \n"
    #e -- > subchart
    html += "							size: {                                                                   \n"
    html += "                    height: 50,                                                        \n"
    html += "                    width: 100                                                         \n"
    html += "                                                                                       \n"
    html += "                },			                                                                \n"
    html += "			    },                                                                            \n"
    #s -- > zoom
    html += "			    zoom:{enabled: false}                                                         \n"
    #e -- > zoom
    html += "			});                                                                               \n"
    html += "    </script>                                                                          \n"
    html += "</body>                                                                                \n"
    html += "</html>                                                                                \n"

    print(html)
    return html


def c3chart_html_write(df_data, type):


    json_temp = df_data.to_json(orient="records")
    json_data = json.loads(json_temp)
    str_json_data = json.dumps(json_data, ensure_ascii=False, indent=4)

    df_categories_data = df_data['ymd']
    json_temp = df_categories_data.to_json(orient="values")
    categories = json.loads(json_temp)
    str_json_categories = json.dumps(categories,ensure_ascii=False, indent=4)

    keys_data = "'" + "','".join(df_data.columns.values) + "'"
    # print(keys_data)
    keys_data = keys_data.replace("'ymd',", '')
    # print("keys_data:", keys_data)

    chart_type = type
    blable = 'false'
    bsub_chart = 'true'
    bzoom = 'true'

    html = ""
    html += "<html>                                                                                \n"
    html += "<head>                                                                                 \n"
    html += "    <!-- stylesheet -->                                                                \n"
    html += "    <link href='c3Chart/c3.css' rel='stylesheet'>                                      \n"
    html += "    <script src='https://d3js.org/d3.v3.min.js'></script>                              \n"
    html += "    <script src='https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.11/c3.min.js'></script> \n"
    html += "</head>                                                                                \n"
    html += "<body width='100%', height ='100%'>                                                    \n"
    html += "    <!-- javascript -->                                                                \n"
    html += "    <div id='chart'></div>                                                             \n"
    html += "    <script type='text/javascript'>                                                    \n"
    html += "    	var chart = c3.generate({                                                         \n"
    html += "  				bindto: '#chart',  " \
            "               size: { height: 550, width: 940 },                                                           \n"
    html += "			    data: {                                                                       \n"
    html += "                     json : " + str_json_data + " , \n"
    html += "                     keys: { value: ["+ keys_data +"] },  \n"
    html += "					  type:'" + chart_type + "',  \n"
    html += "					  labels: "+ blable+",        \n"
    html += "               },  \n"
    html += "				axis: {                                                                       \n"
    html += "					     x: {                                                                     \n"
    html += "					         type: 'category',    " \
            "                            tick: { rotate: 50, multiline: false },                                                \n"
    html += "					         categories: "+ str_json_categories  +"   \n"
    html += "					        }                                                                     \n"
    html += "				},  \n"
    html += "			    subchart: {  \n"
    html += "			        show: "+ bsub_chart+",   \n"
    html += "							size: {  \n"
    html += "                    height: 50,                                                        \n"
    html += "                    width: 100                                                         \n"
    html += "                                                                                       \n"
    html += "                },	\n"
    html += "			    },   \n"
    #s -- > zoom
    html += "			    zoom:{enabled: "+ bzoom+"} \n"
    #e -- > zoom
    html += "			});                                                                               \n"
    html += "    </script>                                                                          \n"
    html += "</body>                                                                                \n"
    html += "</html>                                                                                \n"

    return html





# 네이버 데이터 그래프 전처리

# file_name = 'D:\\issue_2022\\data\\02_분석데이터\\네이버_검색어_할로인.csv'
# df_dis_use = pd.read_csv(file_name, encoding='CP949')
# # YMD -> YM으로 변경
# df_dis_use['Time'] = pd.Series(df_dis_use['Time'], dtype="string")
# df_dis_use['Time'] = df_dis_use['Time'].str[:7]
#
# # 필요한 컬럼만
# df_data = df_dis_use[['Time', 'Value']]
# df_data.columns = ['ymd', '할로인']
#
# file_name = 'D:\\issue_2022\\data\\02_분석데이터\\네이버_검색어_이태원.csv'
# df_dis_use = pd.read_csv(file_name, encoding='CP949')
# # YMD -> YM으로 변경
# df_dis_use['Time'] = pd.Series(df_dis_use['Time'], dtype="string")
# df_dis_use['Time'] = df_dis_use['Time'].str[:7]
# # 필요한 컬럼만
# df_data1 = df_dis_use[['Time', 'Value']]
# df_data1.columns = ['ymd', '이태원']
#
# df = pd.merge(df_data, df_data1, how='outer', on='ymd')
#
# #print(df)
# print("','".join(df.columns.values))
# a = c3chart_html_write(df)



# 뉴스 데이터 그래프 전치리
# file_name = 'D:\\issue_2022\\data\\02_분석데이터\\뉴스_사회\\1차마트_사회.csv'
# df_dis_use = pd.read_csv(file_name)
#
# dfpt = pd.pivot_table(df_dis_use, index='keyword', columns='stdym', values='freq', fill_value=0)
#
# dfpt = dfpt.sort_values((202208), ascending=False)
# temp = dfpt.head(5)
#
# df_marge = pd.DataFrame()
# i = 0
# for key_word in temp.index.values:
#     df_temp = df_dis_use[df_dis_use['keyword'] == key_word]
#     df_data = df_temp[['stdym', 'freq']]
#     df_data = df_data.rename(columns={'stdym':'ymd', 'freq':key_word})
#     if i == 0 :
#        df_marge = df_data
#        i = 1
#     else:
#        df_marge = pd.merge(df_marge, df_data, how='outer', on='ymd')
#
# df_marge = df_marge.fillna(0)
#
# a = c3chart_html_write(df_marge)
# #print(a)
#
#
