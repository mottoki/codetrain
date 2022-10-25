import streamlit as st

# ------------ CONFIG -------------------
st.set_page_config(page_title='Coder', page_icon=None, layout="wide")

hide_table_row_index = """
    <style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """

st.markdown(hide_table_row_index, unsafe_allow_html=True)


st.markdown("Home")

