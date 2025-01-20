import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import ta
import base64
import plotly.graph_objects as go
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler
from keras.models import MinMaxScaler
from keras.layers import Sequential
from keras.layers import LSTM, Dense
from datetime import datetime, timedelta
# streamlit page configuration 
st.set_page_config(page_title= "Stock Analysis Dashboard",layout = "wide")

st.tilte("Stock Analysis Dashboard")

ticker = st.text_input("Enter ticker symbol(eg. Nestle): ")
period = st.selectbox("Select period:",['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'])
interval = st.selectbox("select interval :" , ['1m','2m','5m','15m','30m','60m','90m','1d','5d','1wk','1mo','3mo'])

if(st.button )("Get Data"):
    if ticker and period and interval :
        data = yf.download(ticker,period= period,interval = interval)
        data.index = pd.to_datetime(data.index)

        #candelstick chart with volume 

        fig = go.Figure(data=[go.Candlestick(x=data.index,
                                             open=data['Open'],
                                             high=data['High'],
                                             low=data['Low'],
                                             close=data['Close'],
                                             name='Candlestick')])
        
        





