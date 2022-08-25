import os

import pandas as pd
import requests
import streamlit as st

from utils import get_json_formats_select_box, pick_query
from config import fast_api_host, saved_queries_path

st.write("# API Interface")

selected_query = pick_query(saved_queries_path)
selected_json_format = get_json_formats_select_box()

url = f"{fast_api_host}/query/{selected_query}/{selected_json_format}"

code = f"""
url = '{url}'
response = requests.get(url).json()
"""
st.code(code, language="python")

if st.button("Hit API"):
    response = requests.get(url).json()
    st.json(response)
