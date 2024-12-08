# Load file wit name of CSV file
import sqlite3
import pandas as pd
import os
import re

# Load file wit name of CSV file
csvfile = os.path.join(os.getcwd(), 'Data.csv')

# Read CSV file
df = pd.read_csv(csvfile)
# find columns names in CSV file
df.columns

print(df.columns)

# Create database
conn = sqlite3.connect('Data.db')
print("Opened database successfully")

# Export pandas dataframe to sqlite database
df.to_sql('Data', conn, if_exists='replace', index=False)
print("Table created successfully")

# Close database connection
conn.close()
print("Closed database successfully")
