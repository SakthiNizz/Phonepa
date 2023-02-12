import streamlit as st
import plotly as px
import pandas as pd
import plotly.express as px
import json

def graph():
    state = json.load(open('Indian_States.json','r'))
    state_id_map = {}
    for feature in state['features']:
        feature['id'] = feature['properties']['ID_1']
        state_id_map[feature['properties']['NAME_1']] = feature['id']
    df = pd.read_csv('count.csv')
    df['id'] = df['state'].apply(lambda x: state_id_map[x])
    fig = px.choropleth(df, locations = 'id', geojson = state, color = 'User_count', hover_name = 'state',hover_data = ['Amount'])
    fig.update_geos(fitbounds='locations', visible = False)
    st.plotly_chart(fig)

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
    return df1

st.markdown("# PhonePe Transcation")
st.header('Overview 🎈')
st.sidebar.header("Overview🎈")
graph()
yr = st.selectbox('Select the Year!',('2018','2019','2020','2021','2022'))

tab1, tab2 = st.tabs(["📈 Transaction", "🗃 Data"])

if yr == '2018':
    tab1.subheader('Transaction')
    tab1.write('All PhonePe transaction(UPI+Cards+wallets)')
    tab1.write('2,33,12,35,819')
    tab1.write('Total Payment value')
    tab1.write('Rs: 18,91,497 Cr')
    tab2.header('Categories:')
    a = dataset('2018_ag.json')
    tab2.write(a)

elif yr == '2019':
    tab1.subheader('Transaction')
    tab1.write('All PhonePe transaction(UPI+Cards+wallets)')
    tab1.write('6,33,12,35,819')
    tab1.write('Total Payment value')
    tab1.write('Rs: 20,91,497 Cr')
    tab2.header('Categories:')
    a = dataset('2019_ag.json')
    tab2.write(a)

elif yr == '2020':
    tab1.subheader('Transaction')
    tab1.write('All PhonePe transaction(UPI+Cards+wallets)')
    tab1.write('12,33,12,35,819')
    tab1.write('Total Payment value')
    tab1.write('Rs: 32,91,497 Cr')
    tab2.header('Categories:')
    a = dataset('2020_ag.json')
    tab2.write(a)

elif yr == '2021':
    tab1.subheader('Transaction')
    tab1.write('All PhonePe transaction(UPI+Cards+wallets)')
    tab1.write('34,33,12,35,819')
    tab1.write('Total Payment value')
    tab1.write('Rs: 50,91,497 Cr')
    tab2.header('Categories:')
    a = dataset('2021_ag.json')
    tab2.write(a)

else:
    tab1.subheader('Transaction')
    tab1.write('All PhonePe transaction(UPI+Cards+wallets)')
    tab1.write('78,33,12,35,819')
    tab1.write('Total Payment value')
    tab1.write('Rs: 98,91,497 Cr')
    tab2.header('Categories:')
    a = dataset('2022_ag.json')
    tab2.write(a)