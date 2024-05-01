### Integrate our code OpenAI API

import os
from constans import openai_key
os.environ['OPENAI_API_KEY'] = openai_key
from langchain.llms import OpenAI
import streamlit as st

## streamlit framework

st.title("Langchain Demo with OpenAI API")
input_text = st.text_input("Search::::")

## OPENAI LLMS
llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))
