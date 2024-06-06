import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px
from datetime import datetime
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.grid import grid

st.title('Python - Dashboard')

#Definição da função para a SideBar 
def build_sidebar():
  st.image("images\logo-250-100-transparente.png")
  ticker_list = pd.read_csv("tickers_ibra.csv", index_col=0)
  tickers = st.multiselect(label="Selecione as Empresas", options=ticker_list,placeholder='Códigos')
  start_date = st.date_input("De", format="DD/MM/YYYY",value=datetime(2023,1,2))
  start_end = st.date_input("Até", format="DD/MM/YYYY",value="today")
#Definição da função para o corpo 
def build_main(): 
  pass

with st.sidebar:
  build_sidebar()


