import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Data Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("All-in-One Data Summary Tool")
upload_files = st.file_uploader("Upload CSV files", type=["csv"])
if upload_files is not None:
     df =  pd.read_csv(upload_files)
     st.subheader("Data preview")
     st.write(df.head())
     st.subheader("Data description")
     st.write(df.describe())
     st.subheader("Data visualization")
     columns = st.text_input("Enter your column name to visulaize")
     if columns:
          st.line_chart(df[columns])
          st.bar_chart(df[columns])
          st.subheader("Data distribution")
          st.write(df[columns].value_counts())
          st.subheader("Data missing values")
          st.write(df.isnull().sum())
else:
     st.info("make sure your file is not empty or in csv format")