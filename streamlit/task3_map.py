import streamlit as st
import pandas as pd

df=pd.DataFrame({"lat":[24.925410388280735,24.93879748360024,24.95903102950317],
                 "lon":[67.10328565812229,67.08852277946879,67.05865369940241]})
st.map(df)