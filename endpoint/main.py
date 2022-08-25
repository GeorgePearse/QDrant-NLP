import json
import os

import pandas as pd
import requests
from fastapi import FastAPI
import os
import logging

vector_db_host = os.environ.get("VECTOR_DB_HOST", "http://192.168.54.124:6333")

app = FastAPI()

@app.get("{collection_name}/query/{query_name}/{json_format}")
async def root(
    collection_name: str,
    query_name: str,
    json_format: str,
):
    """
    The whole point is that you would be checking whether the datapoint of
    interest was in this set. Where this set is a recently discovered subclass
    known to underperform, or where you want the data flow to be different,

    e.g. a filter to move them straight to a labelling backlog

    Args:
        query_name (str): Name of the QDrant query you want to execute
        json_format (str): Json format of the response
    """
    saved_queries = "../queries"
    with open(f"{saved_queries}/{query_name}.json") as f:
        selected_query = json.load(f)

    collection_name = 'ag-news-collection'
    request = f"collections/{collection_name}/points/recommend"
    url = f"{vector_db_host}/{request}"
    response = requests.post(url, json=selected_query).json()
    logging.info('LOGGING TEST')
    print('ARRRGGHHHH')
    logging.info(response)
    logging.error('ERRRROOOTTTT')
    response_df = pd.json_normalize(response["result"])
    return response_df.to_json(orient=json_format)
