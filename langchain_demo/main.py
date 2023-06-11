# Load environment variables
import os
from dotenv import load_dotenv, find_dotenv
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor


print(load_dotenv(find_dotenv()))


db = SQLDatabase.from_uri(os.environ.get("DB_URI_STRING"))
print('Creating toolkit')

toolkit = SQLDatabaseToolkit(db=db)
print('Creating agent')
agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True
)

agent_executor.run("Get all asp net applications")
