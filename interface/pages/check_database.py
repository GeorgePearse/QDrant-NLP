import os

import requests
import streamlit as st
from config import vector_db_host

st.write("Check DB State")

request = st.text_input("request")
response = requests.get(f"{vector_db_host}/{request}").json()
st.json(response)
