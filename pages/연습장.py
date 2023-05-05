


import streamlit as st
from annotated_text import annotated_text

# 데이터프레임 생성
import pandas as pd
df = pd.DataFrame({'키워드':['참', '걸'], '평균 영향도':[0.559585, 0.476684], 'URL':['https://band.us/band/86294308/post/322', 'https://band.us/band/86294308/post/358']})


### 글씨만 나옴#####
# 키워드와 평균 영향도를 annoted_text로 변환하는 함수
# def format_keyword_score(row):
#     keyword = row['키워드']
#     return keyword

# # 각 행을 annotated_text로 변환
# texts = []
# for i, row in df.iterrows():
#     keyword_score_text = format_keyword_score(row)
#     score = row['평균 영향도']
#     score = f'{score:.3f}'
#     link = row['URL']
#     texts.append((keyword_score_text, score, link))

# annotated_text(*texts)


def format_keyword_score(row):
    keyword = row['키워드']
    return keyword

texts = []
for i, row in df.iterrows():
    keyword_score_text = format_keyword_score(row)
    score = row['평균 영향도']
    score = f'{score:.3f}'
    link = row['URL']
    texts.append((keyword_score_text, score, link))

annotated_text(*texts, hover_color="red")
