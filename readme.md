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

## Output Screenshots

<img width="367" height="438" alt="Screenshot 2026-04-27 011914" src="https://github.com/user-attachments/assets/bb4f31e5-8a30-453a-8741-252425a13e76" />

<img width="2531" height="1569" alt="Screenshot 2026-04-27 011857" src="https://github.com/user-attachments/assets/f5248380-d30a-4918-935a-88ae2cd9610d" />

<img width="2545" height="1533" alt="Screenshot 2026-04-27 010746" src="https://github.com/user-attachments/assets/8217cc6d-7a7e-4133-b80a-fff058cbba5e" />

<img width="2528" height="1478" alt="Screenshot 2026-04-27 010501" src="https://github.com/user-attachments/assets/e6f7a11e-6970-4249-8e06-bf8733854215" />

<img width="2559" height="1368" alt="Screenshot 2026-04-27 003531" src="https://github.com/user-attachments/assets/b0a12824-d2ca-4df9-8f80-0b11d6f11767" />




## 👤 Author

Akshit Langeh
