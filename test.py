import streamlit as st
import pandas as pd
import numpy as np

st.title('Gay percentage test')
st.header('Are u gay?')
option = st.selectbox(
    'Select 1',
    ('yes', 'definitely', 'YES but in capital'))

st.write('You selected:', option)
