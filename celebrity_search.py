import os
from constans import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title('Celebrity Search Results')
input_text=st.text_input("Search the topic u want")

## Prompt Template
first_input_prompt = PromptTemplate(
    input_variable = ['name'],
    template = 'tell me about celebrity {name}'
)

## OPENAI LLMS
llm = OpenAI(tempreture = 0.8)
chain = LLMChain(llm = llm, prompt = first_input_prompt, verbose = True, output_key = 'person')

if input_text:
    st.write(chain(input_text))
    # with st.expander('Person Name'):
    #     st.info(person_memory.buffer)
    #
    # with st.expander('Major Events'):
    #     st.info(descr_memory.buffer)
