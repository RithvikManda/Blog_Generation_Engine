
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        # ("system","You are a blog generating assistant. Please response to the user queries"),
        ("system","You are a blog generator you need to provide a unique blog on the user's topics"),
        ("system","You are touris asistant you need to give top 10 places near it")
        ("user","Question:{question}")
    ]
)
## streamlit framework

st.title('BLOG GENERATER')
input_text=st.text_input("Enter a topic for the blog")
size=st.text_input("Number of words")

# ollama LLAma2 LLm 
llm=Ollama(model="llama3")
output_parser=StrOutputParser()

chain=prompt|llm|output_parser

if input_text.lower():
    st.write(chain.invoke({"question":"You are a blog generator you need to generate a unique blog for the topic "+input_text +"with "+size+"number of word only not less than that or more than that."  }))


