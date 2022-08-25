import os

# config.py is the approach that Superset takes, can't be that bad
vector_db_host = os.environ.get("VECTOR_DB_HOST", "http://192.168.54.124:6333")
fast_api_host = os.environ.get("FAST_API_HOST", "http://192.168.54.124:8000")
query_results_path = "./results/"
saved_queries_path = "./queries/"
