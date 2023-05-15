import streamlit as st
import pickle
from pathlib import Path

#import streamlit_authenticator as stauth
#import pandas as pd
#import numpy as np


#page_bg = 
#"""
#<style>
#[data-testid="stAppViewContainer"] {
 #   background-color: #fffff7;
#}
#</style>
#"""

logo_url = "Ikeja-Electric-Logo2.png"
logo_url2 = "IKEJA-ELECTRIC.png"
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
#st.image(logo_url, width=100)
st.set_page_config(page_title="IE BI Dashboard", page_icon=logo_url, layout="wide")
#st.markdown(page_bg, unsafe_allow_html=True)


# --- USER AUTHENTICATION ---
#names = ["drim_portal", "Sunny Okonkwo", "Feyisayo Adebiyi"]
#usernames = ["", "SOkonkwo", "FAAdebiyi"]

# Load hashed passwords
#file_path = Path(__file__).parent / "hashed_pw.pkl"
#with file_path.open("rb") as file:
#    hashed_passwords = pickle.load(file)


#credentials = {
#    "usernames":{
#        usernames[0]:{
#            "name":names[0],
#            "password":hashed_passwords[0]
#        },
#    usernames[1]:{
#        "name":names[1],
#        "password":hashed_passwords[1]
#    },
#    usernames[1]:{
#        "name":names[2],
#        "password":hashed_passwords[2]
#    }
#    }
#}

#authenticator = stauth.Authenticate(credentials,"bi_dashboard","abcdef",cookie_expiry_days=30)

#name, authentication_status, username = authenticator.login("Login", "main")







#if authentication_status == False:
#    st.error("Username/password is incorrect")

#if authentication_status == None:
#    st.warning("Please enter your username and password")

#if authentication_status:

col1, col2 = st.columns([2,20])
col1.image(logo_url2, width=80)
col2.header('Welcome to DRIM Portal')

#authenticator.logout("Logout", "main")

#st.subheader(''' This portal is created and maintained by DRIM ''')
#st.write(f"Welcome {name}")

options = st.selectbox('Please select a report:', ['Technical Dashboard', 'Commercial&Technical Dashboard'])

if options == 'Technical Dashboard':
    st.markdown('<iframe title="IE-TECHNICAL DASHBOARD" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=8fadb882-f320-4a52-86a0-7ef914fcfc65&autoAuth=true&ctid=581816b2-c0be-4eaa-80e3-29e5f2486494" frameborder="0" allowFullScreen="true"></iframe>',unsafe_allow_html=True)
elif options == 'Commercial Dashboard':
    st.markdown('<iframe title="Companywide Commercial Performance vdashboard UPDATED" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiMWQ4MjJiMmItNmYwZS00ZGFiLWIxYWYtZjMzMzg3Y2MwMjNlIiwidCI6IjBjYTU1ZWIwLWVjYzItNGYwYS1hMTcxLWQ0ZTVlNmI1NzlkMyJ9" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)




hide_streamlit_style = """
            <style>
            #MainMenu {visibility: visible;}
            footer {visibility: hidden;}
            footer:before {
                content:'Data Refining and Information Management (DRIM)'; 
                visibility: visible;
                display: block;
                position: relative;
                #background-color: white;
                padding: 5px;
                top: 2px;
                bottom: 10px;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
