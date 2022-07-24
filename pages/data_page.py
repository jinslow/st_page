import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

with st.spinner('Wait for it...'):
    time.sleep(5)

# train, test 데이터 불러오기
# 파일: data폴더 안에 train_review.csv, test_review.csv

data_url = "data/"

@st.cache
def load_data(url, type):
    df = pd.read_csv(f'{url}{type}_review.csv', encoding="utf-8", index_col="id")
    return df

train_data = load_data(data_url, "train")
train_data_grd = pd.DataFrame(train_data["target"].value_counts(normalize=True))

test_data = load_data(data_url, "test")

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


