# From https://gist.github.com/robwalton/d985ffd0b3f319919f3d79da7873d762

import json
import logging
import os

import pandas as pd

from utils import (
    pick_query,
    save_query,
)

LOG_LEVEL = logging.DEBUG
LOGFORMAT = (
    "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
)
from colorlog import ColoredFormatter
from config import (
    vector_db_host,
    saved_queries_path,
    query_results_path,
 )

logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT)
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
logger = logging.getLogger("pythonConfig")
logger.setLevel(LOG_LEVEL)
logger.addHandler(stream)

import requests
import streamlit as st


st.markdown("# Run and Save Queries")

collections = [
    record["name"]
    for record in requests.get(f"{vector_db_host}/collections").json()["result"][
        "collections"
    ]
]

collection_name = st.selectbox("Collection", collections)
query_name = st.text_input("Query Name (For Saving)")

choice = pick_query(saved_queries_path)

with open(f"{saved_queries_path}/{choice}.json") as f:
    selected_query = json.load(f)
    logger.info(f"{selected_query} worked")

col1, col2 = st.columns(2)
with col1:
    # load example
    st.write(selected_query)
with col2:
    # edit as wanted
    string_query = st.text_area(label="query", height=400)

request = f"collections/{collection_name}/points/recommend"
url = f"{vector_db_host}/{request}"

save_query_button = st.checkbox("Save Query")
if st.button("Run Query"):
    # if outside of this button it will execute on initial load
    # have no string content, and error.
    data = json.loads(string_query)

    try:
        response = requests.post(url, json=data).json()

        code = f"""
data = {data}
url = '{url}'
response = requests.post(url, json=data).json()
    """
        st.code(code, language="python")

        with st.expander("JSON Response"):
            st.json(response)

        response_df = pd.json_normalize(response["result"])
        st.dataframe(response_df)

        if save_query_button:
            save_query(
                saved_queries_path,
                query_results_path,
                query_name,
                data,
                response_df,
            )

        st.download_button(
            label="Download data as CSV",
            data=response_df.to_csv().encode("utf-8"),
            file_name=f"{query_name}.csv",
        )
    except Exception as e:
        st.write(f"Please complete the form \n Exception = {e}")
