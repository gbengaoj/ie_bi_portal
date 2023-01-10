import streamlit as st
import pandas as pd
import numpy as np

source_dir = "C:/Users/GOojo/Desktop/TECHNICAL PERFORMANCE MONITORING ANALYST/EXCEL/Daily Report/Support Files/DAILTY TECHNICAL REPORT - DECENTRALIZED DATA/"

source_file = "BU FAULT LOG_daily.xlsx"

st.title('Technical Performance Report')

# A function to load data
@st.cache
def load_data(file_name, file_path):
    df = pd.read_excel(
                        io="{}/{}".format(file_path, file_name),
                        engine='openpyxl',
                        sheet_name='fault_metrics'
    )

    return df


# Create a text element and let the reader know the data is loading
data_load_state = st.text('Loading data...')
# Load actual data
data = load_data(source_file, source_dir)
# Notify the reader that the data was successfully loaded
data_load_state.text('Done! (using st.cache)')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)