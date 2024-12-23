import os
from dotenv import load_dotenv
import pandas as pd
import asyncpg
import asyncio
from sqlalchemy import create_engine

#load enviromental variable from dot env file
load_dotenv()

#fetching database connection parametrs from enviroment variable
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# def load_data_from_postgres(query):
#     '''
#     connect to postgresql database 
#     and loaded the data based on the query

#     param query:sql query to execute
#     return:dataframe containing the result of query
#     '''
#     try:
#         #creat connection
#         conn = asyncpg.connect(user='DB_USER', password='DB_PASSWORD', database='DB_NAME', host='DB_HOST')

#         #loade data
#         df = pd.read_sql_query(query, conn)

#         return df
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None

async def load_data_from_postgres(query):
    """
    Connect to PostgreSQL database 
    and load the data based on the query.

    param query: SQL query to execute
    return: DataFrame containing the result of the query
    """
    try:
        # Create connection pool
        conn = await asyncpg.connect(user='DB_USER', password='DB_PASSWORD', database='DB_NAME', host='DB_HOST')

        # Execute the query
        records = await conn.fetch(query)

        # Convert records to a DataFrame
        df = pd.DataFrame(records)

        await conn.close()
        
        return df
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    
def load_data_using_sqlalchemy(query):
# Replace the placeholders with your database credentials
    try :
        DATABASE_URI = "postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create an engine
        engine = create_engine(DATABASE_URI)

# load data to panda dataframe
        df = pd.read_sql_query(query, engine)
        return df
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None    