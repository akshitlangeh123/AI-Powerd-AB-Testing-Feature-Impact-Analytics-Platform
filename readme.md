# 📊 A/B Testing & Feature Impact Analytics Platform

An end-to-end analytics system to design, analyze, and query A/B experiments using modern data stack tools and GenAI.

---

## 🚀 Project Overview

This project simulates a real-world experimentation platform used by product and data teams to evaluate feature impact.

It includes:

* Data pipeline (Databricks + dbt)
* Statistical analysis (Python)
* Business dashboard (Power BI)
* GenAI-powered NL2SQL interface (LLaMA via Ollama)

---

## 🏗️ Architecture

```
Data Generation → Databricks (Bronze)
                    ↓
                dbt (Silver → Gold)
                    ↓
        Python (A/B Testing Stats)
                    ↓
     Power BI Dashboard + NL2SQL App
```

---

## 🧱 Tech Stack

* Databricks (Delta Lake, SQL Warehouse)
* dbt (Data transformations)
* Python (Pandas, Statsmodels)
* Power BI (Dashboard + DAX)
* Ollama (LLaMA - local LLM)
* Streamlit (NL2SQL UI)

---

## 📊 Key Features

### 🔹 A/B Testing Analytics

* Conversion rate calculation
* Lift analysis (absolute & relative)
* Statistical significance testing (Z-test)

### 🔹 Data Modeling

* Medallion architecture (Bronze → Silver → Gold)
* Cleaned and aggregated experiment data using dbt

### 🔹 Dashboard (Power BI)

* KPI tracking (CR, Lift, Users)
* Variant comparison
* Time-series trends
* Segmentation support

### 🔹 NL2SQL (GenAI)

* Natural language → SQL query generation
* Runs queries directly on Databricks
* Built using local LLaMA model (Ollama)

---

## 🧪 Sample Questions (NL2SQL)

* "conversion rate by variant"
* "daily trend for variant B"
* "which variant performed better?"
* "total users and conversions"

---

## 📂 Project Structure

```
├── dbt_project/
├── analysis/
│   └── ab_test.py
├── nl2sql_app/
│   ├── app.py
│   ├── llm.py
│   ├── db.py
│   └── prompt.py
├── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone repo

```
git clone <your-repo-link>
cd ab-testing-analytics-platform
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Setup environment variables

```
DATABRICKS_HOST=...
DATABRICKS_HTTP_PATH=...
DATABRICKS_TOKEN=...
```

### 4. Run NL2SQL app

```
streamlit run nl2sql_app/app.py
```

---

## 📈 Results

* Variant B achieved ~22% lift over control
* Statistically significant improvement (p < 0.05)
* Consistent performance across time

---

## 🎯 Key Learnings

* End-to-end experimentation pipeline design
* Statistical validation of product features
* Prompt engineering for NL2SQL systems
* Building business-ready dashboards

---

## 📌 Future Improvements

* Multi-experiment tracking
* Automated pipeline orchestration (Airflow)
* Advanced statistical methods (Bayesian A/B testing)
* Query validation & optimization layer

---

## 👤 Author

Akshit Langeh
