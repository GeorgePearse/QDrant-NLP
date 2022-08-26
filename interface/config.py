import os
import logging

# config.py is the approach that Superset takes, can't be that bad
try:
  vector_db_host = os.environ["VECTOR_DB_HOST"]
except Exception as e:
  logging.error(f'Please specify IP of host machine. Exception is {e}")
                
query_results_path = "./results/"
saved_queries_path = "./queries/"
