import streamlit as st

with open("./README.md") as fh:
    long_description = fh.read()

st.markdown(long_description)
