import pandas as pd
import re

# Load dataset
df = pd.read_csv("ds_salaries.csv")

# Clean 'experience_level' field
def clean_experience(exp):
    mapping = {'EN': 'Entry-Level', 'MI': 'Mid-Level', 'SE': 'Senior', 'EX': 'Executive'}
    return mapping.get(exp, exp)

df['experience_level'] = df['experience_level'].apply(clean_experience)

# Clean 'salary' column from USD to INR (for demo, multiply by 83)
df['salary_in_inr'] = df['salary_in_usd'] * 83

# Save cleaned data
df.to_csv("cleaned_jobs.csv", index=False)
print("✅ Cleaned data saved to 'cleaned_jobs.csv'")