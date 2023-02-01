import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets

import glob      # 파일들의 리스트를 뽑을 때 사용(*.*)
import pandas as pd
import os.path
import datetime as dt


def c3chart_html_write(df_data, type, types):

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

    # chart_types = str(types).split(",", "")
    multi_types = types

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
    html += "			          types: { " + multi_types + "}, \n"

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
    #s -- > color
    html += "			    color: { \n"
    html += "			        pattern: ['#c4e0a6','#ff5f00', '#ffe082', '#80deeb',  '#bdaba3']\n"
    html += "			    }, \n"
    #s -- > zoom
    html += "			    zoom:{enabled: "+ bzoom+"} \n"
    #e -- > zoom
    html += "			});                                                                               \n"
    html += "    </script>                                                                          \n"
    html += "</body>                                                                                \n"
    html += "</html>                                                                                \n"

    return html
