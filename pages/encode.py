import streamlit as st
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

st.write('# Encoding Dataset')

run_encoding = st.button('Encode')

# dataset = load_dataset('ag_news')
# dataset_df = pd.DataFrame(dataset['train'])

sample_size = st.text_input('Sample Size')
sample_size = 6000

if run_encoding: 
    ag_news_df = pd.read_csv('./ag_news.csv')
    sentences = list(ag_news_df['text'])
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    sentences_sampled = sentences[:sample_size]

    with st.spinner("One second.."):
        embeddings = model.encode(sentences_sampled)
        np.save(f'ag_news_embeddings.npy', embeddings)
