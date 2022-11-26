import streamlit as st
from datetime import datetime

st.title('Hello Streamlit App')

time_now = datetime.now()

st.header('My name is Riza and this is my first deployed app')

st.write(time_now)



