# TO RUN:
# 1. Open terminal on the same location
# 2. streamlit run myapp.py


import streamlit as st
import json


st.set_page_config(page_title="Test", page_icon=":tada:", layout="wide")
st.subheader("Hi")

with open('data/data.json', 'r') as file:
    data = json.load(file)
    
st.markdown(data["Contest Collections"]["International Contests"]["imo"]["2023imo"]["items"][0]["post_rendered"], unsafe_allow_html=True)
st.markdown(data["Contest Collections"]["International Contests"]["imo"]["2023imo"]["items"][1]["post_rendered"], unsafe_allow_html=True)
st.markdown(data["Contest Collections"]["International Contests"]["imo"]["2023imo"]["items"][2]["post_rendered"], unsafe_allow_html=True)
st.markdown(data["Contest Collections"]["International Contests"]["imo"]["2023imo"]["items"][3]["post_rendered"], unsafe_allow_html=True)
st.markdown(data["Contest Collections"]["International Contests"]["imo"]["2023imo"]["items"][4]["post_rendered"], unsafe_allow_html=True)
st.markdown(data["Contest Collections"]["International Contests"]["imo"]["2023imo"]["items"][5]["post_rendered"], unsafe_allow_html=True)
