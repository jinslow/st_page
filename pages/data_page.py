import streamlit as st
import pandas as pd
import time

with st.spinner('Wait for it...'):
    time.sleep(5)

# train, test 데이터 불러오기
# 파일: data폴더 안에 train_review.csv, test_review.csv


@st.cache

def load_data(type):
    df = pd.read_csv(f'pages/{type}_review.csv', encoding="utf-8", index_col="id")
    return df

train_data = load_data("train")
train_data_grd = pd.DataFrame(train_data["target"].value_counts(normalize=True))
test_data = load_data("test")

# data_page 표시

st.markdown('### Shopping Reviews Data')

## train data 나타내기
with st.container():
    
    if st.button("Train Set", key="train"):
        with st.container():
            st.markdown("* Train data (25000개)")
            st.dataframe(train_data)
        with st.container():
            st.markdown("* Train data 리뷰점수별 비중 (1점, 2점, 4점, 5점으로 구성)")
            st.bar_chart(train_data_grd)

## test data 나타내기
with st.container():

    if st.button("Test Set", key="test"):
        st.markdown("* Test data (5000개)")
        st.dataframe(test_data)


