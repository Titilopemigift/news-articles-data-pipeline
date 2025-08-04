# Tech News ETL Pipeline

## Project Overview
This project is an **ETL (Extract, Transform, Load)** pipeline that collects **technology news** from the [NewsAPI](https://newsapi.org/), stores it in an **AWS RDS PostgreSQL** instance, and then transfers it to **AWS Redshift** for analytics.

The pipeline is **orchestrated using Apache Airflow**, making it easy to schedule and automate.

---

##  Tech Stack
- **Python** — Data extraction & transformation
- **Pandas** — Data cleaning and manipulation
- **Requests** — API data fetching
- **PostgreSQL (AWS RDS)** — Staging database
- **Amazon Redshift** — Data warehouse for analytics
- **Terraform** — Infrastructure as Code (IaC)
- **Apache Airflow** — Workflow orchestration

---

##  Architecture
1. **Extract**: Fetch technology news articles using NewsAPI.
2. **Transform**: Clean and standardize article fields (source, author, title, date, etc.).
3. **Load (Stage)**: Insert cleaned data into AWS RDS PostgreSQL.
4. **Load (Warehouse)**: Move data from RDS to AWS Redshift.
5. **Automate**: Schedule the workflow using Apache Airflow.


