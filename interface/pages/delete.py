import os

import streamlit as st

st.write("# Delete Queries")

saved_queries = "./pages/saved_queries/"
query_results = "./pages/results/"
examples = os.listdir(saved_queries)
file_to_delete = st.selectbox("Examples", examples)

delete = st.button("Delete")

if delete:
    try:
        os.remove(f"{saved_queries}/{file_to_delete}")
        os.remove(f"{query_results}/{file_to_delete.replace('json','csv')}")
        st.write("Query and results deleted successfully.")
    except Exception as e:
        st.error("Files were not successfully deleted.")
