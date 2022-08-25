# From https://gist.github.com/robwalton/d985ffd0b3f319919f3d79da7873d762

import logging

import pandas as pd

LOG_LEVEL = logging.DEBUG
LOGFORMAT = (
    "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
)
from colorlog import ColoredFormatter
from config import (
    vector_db_host,
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
st.write("""
The scroll endpoint enables you to browse through raw data,
it is only in this app for the sake of occasional debuggin wrt the 
data structure.
""")

collections = [
    record["name"]
    for record in requests.get(f"{vector_db_host}/collections").json()["result"][
        "collections"
    ]
]

collection_name = st.selectbox("Collection", collections)


request = f"collections/{collection_name}/points/scroll"
url = f"{vector_db_host}/{request}"

data = {
    "limit": 10,
    "with_payload": True,
    "with_vector": False
}

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

except Exception as e:
    st.error(e)