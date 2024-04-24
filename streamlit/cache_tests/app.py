import streamlit as st
from time import time, sleep


@st.cache_data(ttl=10)
def get_time():
    t = time()
    print("Calculating time:", t)
    return t


st.title("Cache test")

req_time = st.button("Request time")
if req_time:
    t = get_time()
    st.info(t)


