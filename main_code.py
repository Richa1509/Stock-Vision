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
        fig.update_layout(title=f'{ticker} Candlestick Chart', xaxis_title='Date', yaxis_title='Price', xaxis_rangeslider_visible=False)

        fig.add_trace(go.Bar(x=data.index, y=data['Volume'], name='Volume', marker_color='blue', opacity=0.3, yaxis='y2'))

        fig.update_layout(yaxis2=dict(overlaying='y', side='right', title='Volume'), height=700)
        st.plotly_chart(fig, use_container_width=True)

        #technical indicators 
        data['rsi'] = ta.momentum.RSIIndicator(data['Close'].rsi)
        macd = ta.trend.MACD(data['Close'])
        data['macd'] = macd.macd()
        data['macd_signal'] = macd.macd_signal()
        data['macd_diff'] = macd.macd_diff()

        stoch = ta.momentum.StochasticOscillator(data['High'],data['low'],data['close'])
        data['stoch_k'] =stoch.stoch()
        data['stoch_d'] =stoch.stoch_signal()

        bbands = ta.volatility.BollingerBands(data['CLose'])
        data['bbands_upper'] = bbands.bollinger_hband()
        data['bbands_middle'] =bbands.bollinger_mavg()
        data['bbands_lower'] = bbands.bollinger_lband()

        data['dpo'] = ta.trend.DPOIndicator(data['Close'].dpo())
        dmi = ta.trend.ADXIndicator(high=data['High'],low =data['low'],close=data['close'],window=14)

        data['adx'] = dmi.adx
        data['dmi_pos'] = dmi.adx_pos()
        data['dmi_neg'] = dmi.adx_neg()

        data['cci'] =ta.trend.CCIIndicator(data['High'],low=data['Low'],close=data['Close'],window=14)
        data['roc']=ta.momentum.ROCIndicator(data['Close'].roc())
        






        
        





