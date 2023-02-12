import streamlit as st

def main_page():
    st.markdown("# Overview 🎈")
    st.sidebar.markdown("# Overview 🎈")

def page2():
    st.markdown("# Brand User ❄️")
    st.sidebar.markdown("# Brand User ❄️")

def page3():
    st.markdown("# Kinds of Transaction 🎉")
    st.sidebar.markdown("# Kinds of Transaction 🎉")

page_names_to_funcs = {
    "Overview": main_page,
    "Brand User": page2,
    "Kinds of Transaction": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()