import pandas as pd
import sqlite3

# Load cleaned CSV
df = pd.read_csv("cleaned_jobs.csv")

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("jobs_data.db")

# Store into DB
df.to_sql("job_data", conn, if_exists="replace", index=False)

conn.close()
print("✅ Data saved to SQLite DB 'jobs_data.db'")