import streamlit as st
st.set_page_config(layout="wide")
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


MODEL_NAME = "jason9693/SoongsilBERT-base-beep"


@st.cache
def load_model():
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=6, ignore_mismatched_sizes=True)
    model.load_state_dict(torch.load("model.pt", map_location="cpu"))
    model.eval()
    return model


@st.cache(allow_output_mutation=True)
def load_tokenizer():
    return AutoTokenizer.from_pretrained(MODEL_NAME, do_lower_case=False)

model = load_model()
tokenizer = load_tokenizer()

st.title("리뷰 평점 분류")
review = st.text_input("리뷰를 입력하세요.", "대박 멋져요. 짱 좋아요")
if st.button('분석하기'):
    st.write("결과:")
    if review:
        encoded = tokenizer(review ,padding="max_length",truncation=True,max_length=71)
        with torch.no_grad():
            logits = model(input_ids=torch.tensor([encoded['input_ids']]), attention_mask=torch.tensor([encoded['attention_mask']])).logits
        st.success(f"예상 점수: {torch.argmax(logits, dim=-1)[0]}점")
    else:
        st.error("리뷰를 입력해주세요.")
