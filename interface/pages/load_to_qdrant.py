import streamlit as st
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance

import numpy as np

st.write('# Load to QDrant Collection')

qdrant_client = QdrantClient(host="192.168.54.124", port=6333)

batch_size = 32
collection_name = 'ag-news-collection'

vectors = np.load(f'./data/ag_news_embeddings.npy')

insert_into_collection = st.button('Insert into Collection')

if insert_into_collection:

    st.write(vectors.shape)
    st.write(len(vectors[0]))

    qdrant_client.recreate_collection(
        collection_name=collection_name,
        vector_size=len(vectors[0]),
        distance=Distance.COSINE
    )

    st.write('Recreated Collection')

    qdrant_client.upload_collection(
        collection_name=collection_name,
        vectors=vectors,  # batch_of_vectors,
        ids=None,  # Let client auto-assign sequential ids
        batch_size=batch_size,
        parallel=2,
    )
    st.write('Uploaded Collection')