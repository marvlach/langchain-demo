# Load environment variables
import os
from dotenv import load_dotenv, find_dotenv
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from sqlalchemy import create_engine


print(load_dotenv(find_dotenv()))
print('Creating engine')
engine = create_engine(os.environ.get("DB_URI_STRING"))


query = input("What tables should I include in my model(seperated by comma): ")
# example: "aspnet_Users, aspnet_UsersInRoles, aspnet_Membership, aspnet_Roles, aspnet_SchemaVersions, aspnet_Applications"
include_tables = [t.strip() for t in query.split(',')]

print('Creating db api')
db = SQLDatabase(engine, include_tables=include_tables)

print("Creating toolkit")
toolkit = SQLDatabaseToolkit(db=db)

print("Creating agent")
agent_executor = create_sql_agent(llm=OpenAI(temperature=0), toolkit=toolkit, verbose=True)


while True:
    query = input("Ask me something")
    agent_executor.run("query")
