from dotenv import load_dotenv
load_dotenv() #load the environment variables

import streamlit as st
import os
import time
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load google gemini model and provide sql query as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash-latest')
    response=model.generate_content([prompt[0],question])
    sql=response.text
    sql=sql.replace("```sql", "").replace("```","").strip()
    return sql

#function to retrieve query from sql database
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

prompt=[
    """You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME,CLASS,
    SECTION and MARKS \n\nFor example,\nExample 1- How many entries of records are present in 
    the SQL command will be something like the SELECT COUNT(*) FROM STUDENT ;
    \nExample 2- Tell me all the students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Machine Learning";
    also the sql code should not have ``` in beginning or end and sql word in the output
    """
]

st.set_page_config(page_title="SQL from Natural Language", page_icon="🧠")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit:
    start = time.time()
    response=get_gemini_response(question,prompt)
    print(response)
    st.success("✅ SQL Query Generated")
    st.code(response, language='sql')
    data=read_sql_query(response,"student.db")
    end = time.time()
    st.toast("📊 Query executed and displayed") #like apopup
    st.subheader("📊 Output")
    for row in data:
        print(row)
        st.header(row)
    st.write(f"⏱ Query executed in `{end - start:.2f}` seconds")


