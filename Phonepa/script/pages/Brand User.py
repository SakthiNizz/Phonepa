import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("# App User Count ❄️")
st.sidebar.header("App User Count ❄️")

df = pd.read_csv('user.csv')
del df['AppOpens']
del df['No of Registered User']
del df['Percentage']
del df['State']
del df['Unnamed: 0']
yr = st.selectbox('Select the Year!',('2018','2019','2020','2021','2022'))

if yr == '2018':
    df.query('Year == 2018')
    fig = px.bar(df, x="Brand", y="Count", title="App User Count 2018")
    st.plotly_chart(fig)

elif yr == '2019':
    df.query('Year == 2019')
    fig = px.bar(df, x="Brand", y="Count", title="App User Count 2019")
    st.plotly_chart(fig)

elif yr == '2020':
    df.query('Year == 2020')
    fig = px.bar(df, x="Brand", y="Count", title="App User Count 2020")
    st.plotly_chart(fig)

elif yr == '2021':
    df.query('Year == 2021')
    fig = px.bar(df, x="Brand", y="Count", title="App User Count 2021")
    st.plotly_chart(fig)

else:
    df.query('Year == 2022')
    fig = px.bar(df, x="Brand", y="Count", title="App User Count 2022")
    st.plotly_chart(fig)