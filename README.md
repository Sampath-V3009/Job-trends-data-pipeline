# 📊 Job Trends Data Pipeline

This project demonstrates a simple **ETL (Extract, Transform, Load)** pipeline built using **Python**, **Pandas**, and **SQLite**. The goal is to extract job salary data, clean and transform it, and store the refined data in a local database for future querying and analysis.

---

## 🏗️ Project Structure

job-trends-data-pipeline/ │ ├── ds_salaries.csv # 📥 Raw dataset ├── etl_pipeline.py # 🧹 Extracts and cleans data ├── store_to_db.py # 🗄️ Loads data into SQLite DB ├── cleaned_jobs.csv # 📄 Cleaned output data ├── jobs_data.db # 🛢️ SQLite database file └── README.md # 📘 Project documentation

---

## 🚀 Features

- Clean and map experience levels from codes to readable text
- Convert salaries from USD to INR
- Save the cleaned dataset to a `.csv` file
- Load data into a SQLite database for efficient storage
- Modular code for easy maintenance

---

## 📥 Dataset Info

The raw dataset `ds_salaries.csv` contains job listing information with fields like:

- `work_year`
- `experience_level` (e.g., EN, MI, SE, EX)
- `employment_type`
- `job_title`
- `salary_in_usd`
- `employee_residence`
- `company_location`
- and more...

---

## 🧼 ETL Process

### Step 1: Extract & Transform (`etl_pipeline.py`)

- Reads the dataset from `ds_salaries.csv`
- Maps `experience_level` codes to human-readable text
- Converts salary from USD to INR using a sample conversion (×83)
- Outputs cleaned data to `cleaned_jobs.csv`

### Step 2: Load (`store_to_db.py`)

- Reads the cleaned data from CSV
- Stores it into an SQLite database `jobs_data.db`
- Creates a table named `job_data`

---

## ▶️ How to Run the Project

1. **Run ETL Pipeline**

```bash
python etl_pipeline.py

2. Load Cleaned Data to SQLite



python store_to_db.py

3. Verify SQLite Data (Optional)



You can use tools like DB Browser for SQLite or Python scripts to inspect the database.


---

🧪 Sample Output

Cleaned CSV: cleaned_jobs.csv

SQLite DB Table: job_data



---

💡 Optional Enhancements

Add logging and exception handling

Convert pipeline into an Airflow DAG or Prefect flow

Add Jupyter Notebook for data exploration and visualization

Visualize top job trends using Matplotlib/Seaborn or Power BI

Add configuration via .env or .yaml file



---

🚀 Future Improvements

Load data to cloud-based data warehouses (e.g., Amazon Redshift, Google BigQuery)

Use REST APIs for data extraction from live job boards

Automate the pipeline using Apache Airflow

Implement unit tests and CI/CD integration



---

👤 Author

Sampath V
Aspiring Data Engineer
🌐 LinkedIn Profile
## 🔗 Connect with Me
[![LinkedIn](www.linkedin.com/in/sampath3009
)



---

📄 License

This project is licensed for personal and educational use. For commercial usage, please contact the author.

---

Let me know if you want this saved directly to a file (`README.md`) for you!
```
