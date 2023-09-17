import os
import streamlit as st
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

os.environ["OPENAI_API_KEY"] = "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"

# Create the database connection
db = SQLDatabase.from_uri("sqlite:///chinook.db")

# Create the SQL database toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))

# Create the agent executor
agent_executor = create_sql_agent(
    llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS
)

# Set the title of the app
st.title("Chatbot")

# Function to display messages in a conversational format
def show_messages(messages):
    for message in messages:
        role = message["role"]
        content = message["content"]
        if role == "user":
            st.text_input("User:", value=content, key=content, disabled=True)
        elif role == "system":
            st.text_area("Agent:", value=content, key=content, disabled=True)

st.session_state.setdefault("messages", [])

prompt = st.text_input("User:", "")

if prompt:
    with st.spinner("Generating response..."):
        st.session_state["messages"] += [{"role": "user", "content": prompt}]
        response = agent_executor.run(prompt)
        message_response = response
        st.session_state["messages"] += [
            {"role": "system", "content": message_response}
        ]
        show_messages(st.session_state["messages"])
