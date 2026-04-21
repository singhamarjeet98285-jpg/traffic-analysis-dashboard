import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🚦 Traffic Analysis Dashboard")

data = pd.read_csv("data.csv")

st.subheader("Dataset Preview")
st.write(data)

st.subheader("Traffic Level Count")
fig, ax = plt.subplots()
data['traffic_level'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

st.subheader("Vehicle vs Speed")
fig2, ax2 = plt.subplots()
ax2.scatter(data['vehicle_count'], data['speed'])
st.pyplot(fig2)