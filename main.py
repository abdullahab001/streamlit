import pandas as pd
import yfinance as yf
import streamlit as st

msft = yf.Ticker('MSFT')

hist= msft.history(period='1mo')
st.title('Hello Abdullah')
st.text('Calculate Square')

num = st.number_input('Enter a number:')

if(st.button('Calculate')):
    res = num**2
    st.text(res)

st.write(hist)

