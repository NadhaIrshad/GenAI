'''
https://python.langchain.com/v0.2/docs/integrations/chat/google_generative_ai/
'''

import getpass
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Now we can instantiate our model object and generate chat completions:
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key="AIzaxxxxxxxxxxxxxxxxxxxxxxxxxxxxx9H8"
    # other params...
)


# We can chain our model with a prompt template like so:    
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)


# Streamlit App Design
st.set_page_config(page_title="Language Translator", page_icon="🌍", layout="wide")
st.title('🌍 Langchain Demo With Gemini (Language Translator)')

# Language selection dropdown
languages = ['English', 'Spanish', 'Tamil', 'Sinhala', 'Chinese']
output_languages = ['Spanish', 'Tamil', 'Sinhala', 'Chinese']

input_language = st.selectbox("Select Input Language", languages)
output_language = st.selectbox("Select Output Language", output_languages)

input_text = st.text_area(f"Enter text in {input_language} to translate", height=150)

# Chain creation for translation
output_parser = StrOutputParser()
chain = prompt | llm | output_parser  

if input_text:
    st.markdown(f"### Translation from {input_language} to {output_language}:")
    try:
        response = chain.invoke(
            {
                "input_language": input_language,
                "output_language": output_language,
                "input": input_text,
            }
        )
        st.write(response)
    except Exception as e:
        st.error(f"Error occurred: {e}")

# Style the page for a more user-friendly experience
st.markdown("""
    <style>
        .stTextInput input {
            font-size: 18px;
        }
        .stTextArea textarea {
            font-size: 16px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
        }
        .stMarkdown {
            font-size: 18px;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# Add instructions to guide users
st.markdown("""
    **Instructions:**
    1. Select the language you want to translate from.
    2. Choose the target language.
    3. Enter your sentence in the input box.
    4. The translation will be displayed below.
""")

# Run app- `streamlit run gemini_applanguage_translator.py`