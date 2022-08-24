import streamlit as st
from qdrant_client import QdrantClient
import numpy as np

st.write('Load to QDrant Collection')

qdrant_client = QdrantClient(host="localhost", port=6333)

batch_size = 100

vectors = np.load('ag_news_embeddings.npy')

qdrant_client.upload_collection(
    collection_name="ag-news-mini-lm",
    vectors=vectors,  # batch_of_vectors,
    batch_size=batch_size,
    parallel=4,
)