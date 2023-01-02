import streamlit as st
import pandas as pd
import numpy as np

st.title('Testing free host streamlit')
st.header('This is a header')
option = st.selectbox(
    'Testing dropdown',
    ('test1', 'test2', 'test3'))

st.write('You selected:', option)
