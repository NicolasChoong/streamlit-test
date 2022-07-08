from operator import mod
import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

with header:
    st.title('Welcome to my streamlit test')
    st.text('In this project I look into the transactions of taxis in NYC...')

with dataset:
    st.header('NYC taxi dataset')
    st.text('This is the dataset I found')

    covid_data = pd.read_csv('data/Covid Dataset.csv')
    st.write(covid_data.head())

with features:
    st.header('The features I created')

with modelTraining:
    st.header('Time to train the model')
    st.text('Miao')