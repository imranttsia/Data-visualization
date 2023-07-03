import streamlit as st
import pandas as pd
import numpy as np

df=pd.DataFrame({
    "column1":[1,2,3,4,5],
    "column2":[6,7,8,9,10]
})

st.write("My first streamlit application")
st.write(df)
