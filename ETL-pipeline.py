import pandas as pd

df = pd.read_csv('job-listing.csv')
print(df.head())

# --- Clean Salary column ---
# Remove ₹ and 'LPA', then split range and take average
def clean_salary(s):
    if pd.isnull(s):
        return None
    s = s.replace('₹', '').replace('LPA', '').strip()
    if '-' in s:
        low, high = s.split('-')
        return (float(low) + float(high)) / 2
    return float(s)

df['Salary Cleaned (LPA)'] = df['Salary'].apply(clean_salary)

# --- Clean Experience column ---
# Extract average years from strings like "2-4 yrs"
def clean_experience(exp):
    if pd.isnull(exp):
        return None
    exp = exp.lower().replace('yrs', '').replace('yr', '').strip()
    if '-' in exp:
        low, high = exp.split('-')
        return (float(low) + float(high)) / 2
    return float(exp)

df['Experience (Years)'] = df['Experience'].apply(clean_experience)

# --- Convert Posted Date to datetime ---
df['Posted Date'] = pd.to_datetime(df['Posted Date'])

# --- Print cleaned data ---
print(df[['Job Title', 'Salary', 'Salary Cleaned (LPA)', 'Experience', 'Experience (Years)', 'Posted Date']].head())

# Save the cleaned DataFrame to CSV
df.to_csv('cleaned_jobs.csv', index=False)
print("✅ Cleaned data saved to 'cleaned_jobs.csv'")