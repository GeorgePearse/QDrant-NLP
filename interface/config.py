import os

# config.py is the approach that Superset takes, can't be that bad
vector_db_host = os.environ.get("VECTOR_DB_HOST")
query_results_path = "./results/"
saved_queries_path = "./queries/"
