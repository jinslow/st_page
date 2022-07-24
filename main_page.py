import streamlit as st
from PIL import Image

st.markdown('## 쇼핑몰 리뷰 평점 분류')

st.markdown('### 1PICK (1팀 - 자연어 처리)')
    
path = ""
image1 = Image.open(f'{path}RNN.png')
image2 = Image.open(f'{path}pytorch.png')
    
with st.container():
    st.image(image1, width=400)
    st.image(image2, width=400)
