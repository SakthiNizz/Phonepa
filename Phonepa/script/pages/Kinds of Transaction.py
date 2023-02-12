import streamlit as st
import json
import pandas as pd
import plotly.express as px

st.markdown("# kinds of Transaction 🎉")
st.sidebar.header("Kinds of Transaction 🎉")

def dataset(file):
    a = open(file, 'r')
    b = json.loads(a.read())
    c = []
    d = []
    for i in range(len(b['data']['transactionData'])):
        c.append(b['data']['transactionData'][i]['name'])
        df1 = pd.DataFrame()
    for i in range(len(b['data']['transactionData'])):
        d.append(b['data']['transactionData'][i]['paymentInstruments'])
    for i in range(len(d)):
        if i>len(d):
            break
        df = pd.DataFrame(d[i])
        df1 = df1.append(df)
    df1['Payment name']=c
    df1.reset_index()
    del df1['type']
    del df1['amount']
    return df1

yr = st.selectbox('Select the Year!',('2018','2019','2020','2021','2022'))

if yr == '2018':
    a = dataset('2018_ag.json')
    fig = px.pie(a['count'], names=a['Payment name'], title = 'kind of Transaction of 2018 in percent')
    st.plotly_chart(fig)

elif yr == '2019':
    a = dataset('2019_ag.json')
    fig = px.pie(a['count'], names=a['Payment name'], title = 'kind of Transaction of 2019 in percent')
    st.plotly_chart(fig)

elif yr == '2020':
    a = dataset('2020_ag.json')
    fig = px.pie(a['count'], names=a['Payment name'], title = 'kind of Transaction of 2020 in percent')
    st.plotly_chart(fig)

elif yr == '2021':
    a = dataset('2021_ag.json')
    fig = px.pie(a['count'], names=a['Payment name'], title = 'kind of Transaction of 2021 in percent')
    st.plotly_chart(fig)

else:
    a = dataset('2022_ag.json')
    fig = px.pie(a['count'], names=a['Payment name'], title = 'kind of Transaction of 2022 in percent')
    st.plotly_chart(fig)