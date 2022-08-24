import streamlit as st
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

st.write('# Encoding Dataset')

run_encoding = st.button('Encode')

if run_encoding: 
    ag_news_df = pd.read_csv('./ag_news.csv')
    sentences = list(ag_news_df['text'])
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    sample_size = 6000
    sentences_sampled = sentences[:sample_size]

    embeddings = model.encode(sentences_sampled)
    np.save(f'ag_news_embeddings.npy', embeddings)