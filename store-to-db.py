import pandas as pd
import sqlite3

# Load the cleaned CSV
df = pd.read_csv('cleaned_jobs.csv')

# Connect to SQLite database (will be created if it doesn't exist)
conn = sqlite3.connect('job_trends.db')

# Store DataFrame into table
df.to_sql('job_data', conn, if_exists='replace', index=False)

print("Data stored in SQLite database: job_trends.db → Table: job_data")

# View first 5 rows
cursor = conn.cursor()
for row in cursor.execute("SELECT * FROM job_data LIMIT 5"):
    print(row)

conn.close()