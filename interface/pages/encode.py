import streamlit as st
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

st.write('# Encoding Dataset')

run_encoding = st.button('Encode')

dataset_options = ['ag_news']
selected_dataset = st.selectbox('Selected Dataset', dataset_options)
dataset = load_dataset(selected_dataset)
dataset_df = pd.DataFrame(dataset['train'])

st.write('I suggest ~ 10K for the timebeing.')
sample_size = st.text_input('Sample Size')

file_path = './data/{selected_dataset}.csv'

dataset_df = dataset_df.iloc[0:sample_size]
dataset_df.to_csv(file_path)

if run_encoding: 
    sentences = list(dataset_df['text'])
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    sentences_sampled = sentences[:sample_size]

    with st.spinner("One second.."):
        embeddings = model.encode(sentences_sampled)
        np.save(f'{selected_dataset}.npy', embeddings)
