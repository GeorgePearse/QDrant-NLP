import streamlit as st
from datasets import load_dataset
from sentence_transformers import SentenceTransformer

from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

# Have nice neat loading sign as you encode the data.

sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)

datasets = ['ag_news']
selected_dataset = st.selectbox('Dataset', datasets)
dataset = load_dataset(selected_dataset)

encoders = ['distilbert-base-uncased']
selected_encoder = st.selectbox('Encoders', encoders)

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling
# sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

# Normalize embeddings
sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)