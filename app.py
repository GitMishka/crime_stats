import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import config
df = pd.read_csv('Crime_Data_from_2020_to_Present.csv')

df.columns = df.columns.str.replace(' ', '')

engine = create_engine(f'postgresql://{config.pg_user}:{config.pg_password}@{config.pg_host}/{config.pg_database}')

df.to_sql("crime_data", engine, if_exists='replace', index=False)

print("Data has been successfully loaded to the database")
