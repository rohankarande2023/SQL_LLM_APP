from langchain_openai import ChatOpenAI
import google.generativeai as genai
import sqlite3
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os

os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# OPENAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo")


# GOOGLE AM MODEL to provide sql query

def get_gemini_response(question,prompt):
    model= genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Retrieve query from SQL database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows


# Define Your Prompt

prompt=[
    """
You are an expert in converting English quesiton into SQL queries.
The SQL database has following table StudentRecords with following columns
    Student VARCHAR(100),
    Class VARCHAR(50),
    Section VARCHAR(30),
    Marks INT.
Only create queries using the columns present in the table. 
The response should not contain '''.
   """
]



## Creating Streamlit App

st.set_page_config(page_title="Get SQL Query")
st.header("Gemini App to get SQL Data")

question=st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(question=question,prompt=prompt)
    print(response)
    data=read_sql_query(response,'student.db')
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)
