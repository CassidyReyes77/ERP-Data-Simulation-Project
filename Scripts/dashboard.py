import sqlite3
import streamlit as st
import sqlite3
import pandas as pd

st.title("ERP Data Audit Dashboard")

# Connect to the database
conn = sqlite3.connect('business_data.db')
cursor = conn.cursor()

# Load audit log 
audit_log = pd.read_sql_query('SELECT * FROM audit_log', conn)

# SHow full audit log 
audit_log = pd.read_sql_query('SELECT * FROM audit_log', conn)

# Show the audit log in a table
st.subheader("Audit Log")
st.dataframe(audit_log)

# Show summary statistics
st.subheader("Issue summary by Table")

# Show summary by table
st.subheader("📊 Issue Summary by Table")
summary = audit_log.groupby('table_name').size().reset_index(name='issue_count')
st.bar_chart(summary.set_index('table_name'))

# Show summary by issue type
st.subheader("📊 Issue Summary by Type")
type_summary = audit_log.groupby('issue_type').size().reset_index(name='count')
st.bar_chart(type_summary.set_index('issue_type'))

conn.close()