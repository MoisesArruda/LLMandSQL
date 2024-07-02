import streamlit as st
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

path = "data/Screenshot_207.png"
st.set_page_config(page_title="Database Q/A App", page_icon=":bookmark_tabs:")
st.image(path,width=900)

st.title('Conector com Banco de Dados :red[Q/A App] 	:open_book:')


db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.table_info)
from config_gpt import GPTConfig, Prompt
llm = GPTConfig().create_chat()
question = st.text_input(":violet[Pergunta: ]")
submit=st.button("Enviar")

if question and submit:
    chain=SQLDatabaseChain.from_llm(llm, db, verbose=True)
    response=chain.run(question)
    st.header("Enviar")
    st.write(response)