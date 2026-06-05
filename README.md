# Synthetic-Data--Generator
Synthetic-Data- Generator
AI Synthetic Data Generator
An AI-powered platform that converts natural language business requirements into relational database schemas and synthetic datasets.

Features
Requirement Collection Agent
Planning Agent
Schema Generation Agent
Relationship Mapping
Dependency Resolution
Synthetic Data Generation
CSV Export
Primary Key Validation
Foreign Key Validation
Streamlit UI
Architecture
User Requirement ↓ Requirement Agent ↓ Planning Agent ↓ Schema Generator ↓ Relationship Mapper ↓ Dependency Resolver ↓ Synthetic Data Generator ↓ CSV Exporter ↓ Validation Agent

Example
Input:

I want to build a Netflix-like platform.

Need synthetic data for QA testing.

Output:

users.csv
subscriptions.csv
programs.csv
devices.csv
payments.csv
Tech Stack
Python
OpenAI API
Pydantic
Faker
Pandas
Streamlit
Installation
pip install -r requirements.txt

Run CLI
python main.py

Run UI
streamlit run app.py

Future Improvements
Business Rules Engine
Domain-specific Data Generators
Docker Support
PostgreSQL Export
JSON Export
Multi-Agent Memory
User Requirement │ ▼ Requirement Agent │ ▼ Planning Agent │ ▼ Schema Generator │ ▼ Relationship Mapper │ ▼ Dependency Resolver │ ▼ Synthetic Data Generator │ ▼ CSV Exporter │ ▼ Validation Agent
