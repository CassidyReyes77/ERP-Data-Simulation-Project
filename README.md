# ERP Data Simulation Project

## Purpose
This project simulates a basic ERP (Enterprise Resource Planning) system using synthetic data. It includes automated auditing of potential data issues and a Streamlit dashboard for visual reporting. It demonstrates skills in data generation, validation, and dashboarding using Python.

## Project Structure
Data/ - CSV data files (customers, vendors, items, pricebook)
Database/ - SQLite database with loaded tables and audit log
Scripts/ - Python scripts for data generation, loading, cleaning, and dashboarding
requirements.txt - Python dependencies
README.md - Project overview and instructions

bash
Copy code

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/CassidyReyes77/ERP-Data-Simulation-Project.git
   cd ERP-Data-Simulation-Project
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Generate and load data:

bash
Copy code
python Scripts/generate_data.py
python Scripts/load_data_to_db.py
Run data audit:

bash
Copy code
python Scripts/audit_clean.py
Launch dashboard:

bash
Copy code
streamlit run Scripts/dashboard.py
