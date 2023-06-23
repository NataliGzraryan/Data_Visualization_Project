import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv("FINANCE_Credit_Scoring.csv")

st.title("Credit Data Dashboard")

# Sidebar filters
st.sidebar.title("Filters")

# Filter by default status
default_status = st.sidebar.selectbox("Default Status", options=["All", "Default", "No Default"])
if default_status == "Default":
    data = data[data['default'] == 1]
elif default_status == "No Default":
    data = data[data['default'] == 0]

# Filter by credit history
credit_history = st.sidebar.multiselect("Credit History", options=data['credit_history'].unique())
if credit_history:
    data = data[data['credit_history'].isin(credit_history)]

# Filter by purpose
purpose = st.sidebar.multiselect("Purpose", options=data['purpose'].unique())
if purpose:
    data = data[data['purpose'].isin(purpose)]

# Display data table
st.subheader("Credit Data")
st.dataframe(data)

# Default Column
st.subheader("Default Column")
default_counts = data['default'].value_counts()
st.bar_chart(default_counts)

# Account Check Status Column
st.subheader("Account Check Status Column")
account_check_status_counts = data['account_check_status'].value_counts()
st.bar_chart(account_check_status_counts)

# Duration in Month Column
st.subheader("Duration in Month Column")
fig, ax = plt.subplots()
ax.hist(data['duration_in_month'], bins='auto')
ax.set_xlabel("Duration in Month")
ax.set_ylabel("Count")
st.pyplot(fig)

# Credit History Column
st.subheader("Credit History Column")
credit_history_counts = data['credit_history'].value_counts()
fig = px.pie(credit_history_counts, values=credit_history_counts.values, names=credit_history_counts.index)
st.plotly_chart(fig)

# Purpose Column
st.subheader("Purpose Column")
purpose_counts = data['purpose'].value_counts()
fig = px.bar(purpose_counts, x=purpose_counts.index, y=purpose_counts.values)
st.plotly_chart(fig)


