import streamlit as st
#import pandas as pd
#import numpy as np


st.header('Welcome to Ikeja Electric BI Portal')
st.subheader(''' This portal is created and maintained by DRIM ''')

options = st.selectbox('Please Select', ['Technical Dashboard', 'Commercial Dashboard'])

if options == 'Technical Dashboard':

    st.markdown('<iframe title="IE-TECHNICAL DASHBOARD" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=8fadb882-f320-4a52-86a0-7ef914fcfc65&autoAuth=true&ctid=581816b2-c0be-4eaa-80e3-29e5f2486494" frameborder="0" allowFullScreen="true"></iframe>',unsafe_allow_html=True)
