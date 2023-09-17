# SqlAgent
Chat with sql database present in our device. usually retrieving data from sql database requires sql querying but with this we can get our required data from the data with natural language question.

# Project_setup

## Step 1 -- environment setup:
1. open vscode

```   
python -m venv myenv
```
2. myenv can be any name u want to give to ur virtual environment

3. myenv in above code is virtual environment name we give
   
## Step 2 -- Activating virtual environment setup:

```
.\myenv\scripts\activate
```

4. To activate vitual environment created

## Step 3 -- Installing required libraries: 

5. Now we have to install required library packages

```
pip install langchain
pip install openai
pip install streamlit
pip install tabulate
```
## step 4 -- upload the .db sqlit database into the directoryof the project

## database: 
https://database.guide/2-sample-databases-sqlite/ this contains instruction to load database

## Script of databasehttps:
//raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sql

6. Create a folder open its location in cmd
   
7. Then create database by connecting to SQLite with the following command:

```
sqlite3 Chinook.db
```

8. Now you can run the script. To run it from the file, use the following command:

```   
.read Chinook_Sqlite.sql
```

9. Once the script has finished running, you can verify that it created the database by selecting some data from a table. For example, you could run the following:

```
SELECT * FROM Artist LIMIT 10;
```

## Step 5 -- Streamlit file for Chatbot on sql database

7. Run sql.py file to build chatbot interface .

```
streamlit run sql.py
```

# References:
https://python.langchain.com/docs/modules/agents/toolkits/sql_database.html


# Collab Notebook:
Sql_Agent.ipynb
It is the model code for question answering with sql database


# Utility:
1. people who are not having knowledge of sql query language can have a greate use of this

   
