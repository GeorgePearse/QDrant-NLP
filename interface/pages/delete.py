import os

import streamlit as st

from config import (
    saved_queries_path,
    query_results_path,
 )

st.write("# Delete Queries")

examples = os.listdir(saved_queries_path)
file_to_delete = st.selectbox("Examples", examples)

delete = st.button("Delete")

if delete:
    try:
        os.remove(f"{saved_queries_path}/{file_to_delete}")
        os.remove(f"{query_results_path}/{file_to_delete.replace('json','csv')}")
        st.write("Query and results deleted successfully.")
    except Exception as e:
        st.error("Files were not successfully deleted.")
