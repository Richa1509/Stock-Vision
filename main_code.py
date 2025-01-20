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


