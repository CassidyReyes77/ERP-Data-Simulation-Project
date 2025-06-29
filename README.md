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

   git clone https://github.com/CassidyReyes77/ERP-Data-Simulation-Project.git
   cd ERP-Data-Simulation-Project

2. Install dependencies:

   pip install -r requirements.txt

3. Generate and load data:

   python Scripts/generate_data.py
   python Scripts/load_data_to_db.py

4. Run data audit:

   python Scripts/audit_clean.py

5. Launch dashboard:

   streamlit run Scripts/dashboard.py
