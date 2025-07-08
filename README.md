# ERP Data Simulation Project

## Purpose
This project simulates a basic ERP (Enterprise Resource Planning) system using synthetic data. It includes automated auditing of potential data issues and a Streamlit dashboard for visual reporting.

## Project Structure
Data/ - CSV data files (customers, vendors, items, pricebook)

Database/ - SQLite database with loaded tables and audit log

Scripts/ - Python scripts for data generation, loading, cleaning, and dashboarding

requirements.txt - Python dependencies

README.md - Project overview and instructions


## How to Run

1. Clone the repository:

   git clone https://github.com/CassidyReyes77/ERP-Data-Simulation-Project.git
   
   cd ERP-Data-Simulation-Project

3. Install dependencies:

   pip install -r requirements.txt

4. Generate and load data:

   python Scripts/generate_data.py
   
   python Scripts/load_data_to_db.py

5. Run data audit:

   python Scripts/audit_clean.py

6. Launch dashboard:

   streamlit run Scripts/dashboard.py

7. Dashboard
   
    http://localhost:8501/
