import streamlit as st
import pandas as pd
import numpy as numpy
st.title("Uber Pickups in NYC")
DATA_URL = ('DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')')

         DATE_COLUMN="date/time"
def load_data(nrows):
            data=pd.read_csv(DATA_URL,nrows=nrows)
            lowercase=lambda x:str(x).lower()
            data.rename(lowercase, axis="columns", inplace=True)
            data[Date_Column]=pd.to_datetime[DATE_COLUMN]
            return data

data_load_state = st.text ("Loading Data...")
data=load_data (1000)
data_load_state = st.text("Loading Data...Done!")

st.subheader ("Raw Data")
st.write (data)

st.subheader ("Number of Pickups per hour")
hist_values=np.histogram(data[DATE_COLUMN]).dt.hour, bins=24, range=(0,24)
st.bar_chart(hist_values)

