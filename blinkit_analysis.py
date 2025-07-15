import sqlite3
import pandas as pd

# Connect to your DB file
conn = sqlite3.connect("blinkit_db.db")

# Read your query from the file
with open("queries.sql", "r") as file:
    query = file.read()

# Run the query
df = pd.read_sql_query(query, conn)
print(df.head())

conn.close()