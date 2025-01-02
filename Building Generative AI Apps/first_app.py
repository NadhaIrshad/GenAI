#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Now we can instantiate our model object and generate chat completions:
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key="AIzxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxH8"
)

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a chatbot"),
        ("human","Question:{question}")
    ]
)



st.title('My_First_App - Langchain Demo With Gemini 🌟')
st.subheader("Ask any question and get instant responses powered by Gemini!")
st.sidebar.title("Examples")
st.sidebar.write("- What is the capital of Sri Lanka?")
st.sidebar.write("- Who won the latest T20 world cup?")
st.sidebar.write("- How does machine learning work?")
st.sidebar.write("- Explain about GenAI?")

input_text=st.text_input("Enter your question here")
output_area = st.empty()  # Placeholder for the output

output_parser=StrOutputParser()

chain=prompt|llm|output_parser   
  
if input_text:
    st.write(chain.invoke({'question':input_text})) 


# cd C:\Users\nadha\GenAI
      
# To run this code, write-  streamlit run gemini_app_qa.py
