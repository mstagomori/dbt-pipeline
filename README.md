# End-to-end ELT Data Pipeline
This project implements a lightweight ELT data pipeline using Apache Airflow, dbt (Data Build Tool), PostgreSQL, and Apache Superset, pulling weather data from the Weatherstack API into a modern analytical stack. The full stack runs locally using Docker and containerization, making it easy to run, orchestrate, transform, and visualize.

## 🚀 Objective
The goal of this repository is to demonstrate how to build a complete ELT pipeline that:

1. Extracts weather data from Weatherstack API
2. Loads it into a PostgreSQL database
3. Transforms raw data using dbt and SQL models
4. Orchestrates all tasks with Apache Airflow
5. Visualizes analytical results in Apache Superset
6. Runs everything locally using Docker & docker-compose

This pipeline showcases how open-source tools can be combined to create a repeatable, auditable, and visual data workflow.

## 🧠 Tech Stack

| Layer | Tool |
|-------|------|
| Extraction & Orchestration | Apache Airflow |
| Transformation | dbt (Data Build Tool) |
| Database | PostgreSQL |
| Visualization | Apache Superset |
| API Data Source | Weatherstack API |
| Deployment | Docker & Docker Compose |

---

## 🧾 Prerequisites

Before getting started, ensure you have installed:

- Docker  
- docker-compose  
- Git  

Once Docker is running locally, we will bring up all services via docker-compose.

---

## 📥 1. Clone the Repository
```bash
git clone https://github.com/mstagomori/dbt-pipeline.git
cd dbt-pipeline
```

## 📦 2. Install Dependencies
Install Python dependencies using requirements.txt:
```bash
pip install -r requirements.txt
```

## 🐳 3. Bring Up the Stack
Start all Docker containers (Airflow, Postgres, dbt environment, Superset):

```bash
docker-compose up
```

This will:

- Launch PostgreSQL
- Launch an Airflow scheduler and webserver
- Launch Superset
- Mount the dbt project and scripts

## 📊 4. Access the Services

### 🛠️ Apache Airflow
- Open your browser to: http://localhost:8080
- Use the admin credentials printed in the logs (usually default is admin / admin)

After logging in:

- Go to the DAGs page
- Locate the ELT DAG
- Trigger the DAG manually or enable its execution (default 5 minutes interval, can be changed in airflow/orchestrator.py)
- Monitor execution logs

The DAG will extract API data, load it into PostgreSQL, and execute dbt models for transformation.

### 📈 Apache Superset

This step depends on a few runs of the pipeline so the tables can be created and filled with data.
- Open your browser to: http://localhost:8088
- Login with default credentials:
    - Username: admin
    - Password: admin

Then:

- Add Database Connection: 
    - Settings > Database Connections > +Database
    - Database Name of your preference
    - Username: user_psql
    - Password: pw_psql
    - Display Name of your preference
    - Click Connect
- Add Dataset
    - Navigate to Datasets
    - +Dataset
    - Database name created above
    - Schema: dev
    - Select weather_report table
    - Create Dataset and Create Chart

You can now visualize the transformed weather data.

## 📜 Summary
This repository demonstrates a complete ELT workflow combining:

- API extraction (Weatherstack)
- Dockerized orchestration (Airflow)
- Modern SQL transformation (dbt)
- PostgreSQL as data warehouse
- Visual analytics with Superset

All running locally with minimal configuration, ideal for learning modern data engineering tools and best practices.

This project was inspired by [this youtube video](https://www.youtube.com/watch?v=vMgFadPxOLk) from Calvin Yoon.