import numpy as np
import pandas as pd
import warnings # 경고 메시지 무시
warnings.filterwarnings(action='ignore')
from konlpy.tag import Mecab # 형태소 분석기
#경로 픽스
mecab  = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")
# 작업 프로세스 시각화
from tqdm import tqdm
# 문자열 처리를 위한 정규표현식 패키지
import re
# 단어 빈도수 계산 패키지
from gensim import corpora
# LDA 모델 활용 목적
import gensim
# LDA 시각화용 패키지
import pyLDAvis.gensim_models
# 단어 등장 횟수 카운트
from collections import Counter

import glob

from common.config.filepassclass import *
import common.config.apiinfo as apifp


import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# 유사사례, 크롤링 정보의 데이타 파일을 머지하여 토픽 키워드를 찾는다.
# input value 값은 사례 구분[유사사례, 크롤링], 키워드[,]
def lda_model_proc(part, keyword):

    filePath = FilePathClass().get_raw_use_path()

    find_files = "*{0}*.csv".format(part)
    # print(find_files, ":", filePath + find_files)
    all_files = glob.glob(filePath + find_files)
    #분석대상 키워드
    list_keyword = keyword.replace(' ', '' ).split(',')

    # print(list_keyword)
    df_anal_data = pd.DataFrame()
    for anal_keyword in list_keyword:
        for anal_file in all_files:
            list_anal_keyword = anal_file.replace(filePath, '').replace('.csv', '').split('_')
            if anal_keyword == list_anal_keyword[2]:
               print(anal_file, ':', list_anal_keyword[2])

               #키워드가 존재하면 파일로 머지
               df_dis_use = pd.read_csv(anal_file, encoding="utf-8-sig")
               if part == "유사사례":
                   df_dis_use = df_dis_use.loc[:, ['title','content']]
               elif part == "크롤링":
                   df_dis_use = df_dis_use.loc[:, ['제목', '본문']]
                   df_dis_use.rename(columns={'제목': 'title', '본문': 'content'}, inplace=True)


               df_dis_use = df_dis_use.drop_duplicates()
               df_anal_data = pd.concat([df_anal_data, df_dis_use])

    #문자열 데이터 치환????
   # df_anal_data['content'] = ''
    #data_replaced_list = []
    #for data in tqdm(df_anal_data['content']):
       # data_replaced = replace_word(data)  # 문자열 데이터 치환
       # data_replaced_list.append(data_replaced)

    #df_anal_data['content'] = data_replaced_list
    #df_anal_data = df_anal_data.loc[:, ['title', 'content']]
    #df_anal_data.head()

    anal_data_token = list(map(lambda df_anal_data: mecab.nouns(df_anal_data), df_anal_data['content']))  # 토큰화(형태소 분석)

    anal_data_token_removed = []
    temp = 0
    for i, v in enumerate(anal_data_token):
        #     print('news_taxi_token > ', i, v)
        line = []
        for j, k in enumerate(v):
            if not (len(k) == 1) :
                #  한 단어가 아니고 분석대상 키워드가 아닌 경우
                for anal_keyword in list_keyword:
                    if k == anal_keyword:
                       temp = 1
                if temp == 0:
                    line.append(anal_data_token[i][j])
                temp = 0

        anal_data_token_removed.append(line)

    #print(anal_data_token_removed)
    # 단어 인코딩 및 빈도수 계산
    model, corpus, dictionary = lda_modeling(anal_data_token_removed)
    NUM_WORDS = 10
    #RATING = 'taxi_OR'
    lda_keyword = "{0}_{1}".format(part,keyword.replace(',', '_').replace(' ', ''))
    topics = model.print_topics(num_words=NUM_WORDS)
    print_topic_prop(topics, lda_keyword)
    lda_visualize(model, corpus, dictionary, lda_keyword)
    print("The End!!!")
    # dfAllData = pd.DataFrame()

def lda_modeling(anal_data_token):
    global NUM_TOPICS
    NUM_TOPICS = 3
    PASSES = 20

    # 단어 인코딩 및 빈도수 계산
    dictionary = corpora.Dictionary(anal_data_token)
    corpus = [dictionary.doc2bow(token) for token in anal_data_token]
    # LDA 모델 학습
    model = gensim.models.ldamodel.LdaModel(corpus,
                                            num_topics = NUM_TOPICS,
                                            id2word = dictionary,
                                            passes = PASSES)
    return model, corpus, dictionary


def print_topic_prop(topics, lda_keyword):
    # 토픽에 따른 단어와 값 엑셀로 저장
    topic_values = []
    file_path = FilePathClass()
    file_save_path = file_path.get_result_path() + "LDA\\"
    file_name = file_save_path + "topic_prop_"
    for topic in topics:
        topic_value = topic[1]
        topic_values.append(topic_value)
        # 폴더 존재 여부 확인하여 없으면 폴더 생성
    #print("print_topic_prop:save_path->", file_save_path)

    if file_path.is_path_exist_check(file_save_path) == False:
       #print("false")
       file_path.make_path(file_save_path)

   # print("print_topic_prop:topic_values->", topic_values)
    topic_prop = pd.DataFrame({"topic_num" : list(range(1, NUM_TOPICS + 1)), "word_prop": topic_values})
    topic_prop.to_excel(file_name + lda_keyword +  '.xlsx')


def lda_visualize(model, corpus, dictionary, lda_keyword):

    #pyLDAvis.enable_notebook()
    result_visualized = pyLDAvis.gensim_models.prepare(model, corpus, dictionary)
    pyLDAvis.display(result_visualized)

    # 시각화 결과 저장
    file_path = FilePathClass()
    file_save_path = "{0}LDA\\".format(file_path.get_result_path())
    file_name = "{0}lda_result_".format(file_save_path)

    if file_path.is_path_exist_check(file_save_path) == False:
       file_path.make_path(file_save_path)

    #file_name = FilePathClass().get_result_path() + "LDA/lda_result_"
    RESULT_FILE = file_name + lda_keyword + '.html'
    pyLDAvis.save_html(result_visualized, RESULT_FILE)


# def replace_word(data):
#
#     for i in range(len(replace_list['before_replacement'])):
#         try:
#             # 치환할 단어가 있는 경우에만 데이터 치환 수행
#             if replace_list['before_replacement'][i] in data:
#                 data = data.replace(replace_list['before_replacement'][i], replace_list['after_replacement'][i])
#         except Exception as e:
#             print(f"Error 발생 / 에러명: {e}")
#     return data


#lda_model_proc("유사사례", "이태원, 할로인")
