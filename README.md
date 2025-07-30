# 🧠 Job Trends Data Pipeline (ETL Project)

This project demonstrates a complete **ETL (Extract, Transform, Load)** pipeline for analyzing job listing data. It focuses on cleaning raw job data, transforming key features like experience, and storing the processed data into a **SQLite database**.

---

## 🔧 Technologies Used

- Python 🐍
- Pandas 🐼
- SQLite3 💾
- VS Code 💻

---

## 🛠️ Pipeline Overview

### 1. Extract

- Read job listing data from a raw CSV file.

### 2. Transform

- Clean and normalize the "Experience" field (e.g., "1-3 years", "2 yrs", "Fresher").
- Handle missing values and inconsistent formatting.

### 3. Load

- Store cleaned data into a SQLite database named `job_trends.db`.
- Table: `job_data`

---

## 📁 Files Included

| File               | Description                                      |
| ------------------ | ------------------------------------------------ |
| `etl_pipeline.py`  | Main script for data cleaning and transformation |
| `store-to-db.py`   | Script to load cleaned data into SQLite          |
| `cleaned_jobs.csv` | Final cleaned dataset                            |
| `job_trends.db`    | SQLite database file                             |
| `README.md`        | This project documentation                       |

---

## 📌 How to Run

1. Clone the repo or download files
2. Run `etl_pipeline.py` to clean the data
3. Run `store-to-db.py` to store it into the SQLite database
4. Open `job_trends.db` with any SQLite browser or query using Python

---

## 💡 What I Learned

- Data cleaning with Pandas
- Creating custom transformation functions
- Loading structured data into SQL databases
- Structuring a real-world mini ETL pipeline

---

## 🔗 Author

**Sampath V**  
_Aspiring Data Engineer_  
[LinkedIn](https://www.linkedin.com) ← (Update with your real profile)

---

## ⭐ Future Improvements

- Add job skill extraction using NLP
- Automate pipeline with Airflow or Prefect
