from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
# from langchain.agents.agent_toolkits import create_sql_agent,SQLDatabaseToolkit
# from langchain.chat_models import AzureChatOpenAI
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from config_gpt import GPTConfig, Prompt

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.dialect)
print(db.get_usable_table_names())
select = db.run("SELECT * FROM Artist LIMIT 10;")
print(select)


llm = GPTConfig().create_chat()
# agent_executor = create_sql_agent(llm,toolkit=SQLDatabaseToolkit(db=db, llm=llm), agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# sql_awnser = agent_executor.invoke(
#     "List the total sales per country. Which country's customers spent the most?"
# )

# print(sql_awnser)


chain = SQLDatabaseChain.from_llm(llm,db,verbose=True)
response = chain.run("List the total sales per country. Which country's customers spent the most?")
print(response)