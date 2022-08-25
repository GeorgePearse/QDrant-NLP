import io
import streamlit as st
from pandas.core.frame import DataFrame
import pandas as pd
import json
import os
import logging

def pick_query(saved_queries_path):
    navigation_one = os.listdir('..')
    navigation_two = os.listdir('.')
    logging.info(navigation_one)
    logging.info(navigation_two)
    examples = os.listdir(saved_queries_path)
    examples_clean = [example.replace(".json", "") for example in examples]
    return st.selectbox("Examples", examples_clean)


def save_query(
    saved_queries_path: str,
    query_results_path: str,
    query_name: str,
    data: dict,
    response_df: DataFrame,
):
    with open(
        f"./{saved_queries_path}/{query_name}.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    response_df.to_csv(f"./{query_results_path}/{query_name}.csv")


def get_json_formats_select_box():
    json_formats = ["split", "records", "index", "columns", "values", "table"]
    return st.selectbox("Json Format", json_formats)


