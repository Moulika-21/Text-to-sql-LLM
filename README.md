🧠 Text-to-SQL LLM Application
-> Overview:
This project is a Text-to-SQL Natural Language Interface powered by a Large Language Model (LLM). The application allows users to query structured data using natural language. Instead of writing SQL queries manually, users can simply ask questions like:

"Show me all employees who joined after 2020"
The model interprets the input, generates the appropriate SQL behind the scenes, executes it on the connected SQLite database, and returns the result in a readable format — without showing the SQL query.

🔧Tech Stack:
Streamlit – For the user interface
SQLite3 – As the local database backend
LLM API – Gemini/GPT used for translating natural language to SQL
Python – For backend and logic integration

✨ Features:
Accepts natural language queries from users
Dynamically generates SQL queries using LLMs
Connects to a custom SQLite database
Fetches and displays the result of the SQL query (not the query itself)
Simple and intuitive Streamlit interface

Project Structure:
|__app.py
|__sql.py
|__requirements.txt
|__env

Getting Started:
1.Clone the Repository:
  git clone https://github.com/Moulika-21/Text-to-sql-LLM.git
  cd Text-to-sql-LLM
2.Install Dependencies:
  pip install -r requirements.txt
3.Run the app
  streamlit run app.py

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6b0eba02-e69f-4e47-8b45-03e795ac135e" />
