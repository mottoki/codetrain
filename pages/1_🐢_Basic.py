import streamlit as st
import pandas as pd
from random import randint, shuffle
from input_function import display_output
from questions_basic import basic_questions

# ------------- CONFIG ---------------------------
title = "Basic"

st.set_page_config(page_title=title, layout="wide")

hide_table_row_index = """
    <style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """

st.markdown(hide_table_row_index, unsafe_allow_html=True)

# -------------- INITIALISE ----------------------
col1, col2, col3, col4 = st.columns([1,1,1,1])
with col1:
    st.subheader(title)
with col2:
    # Initialisation
    if 'i' not in st.session_state:
        # Randomly take the number and remove it from list
        st.session_state['mylist'] = list(range(10))
        shuffle(st.session_state['mylist'])
        selectedi = st.session_state['mylist'].pop()
        # Store the variables
        st.session_state['i'] = selectedi # selected random number
        st.session_state['cnt'] = 1 # count of question
        st.session_state['correct'] = 0 # count of correct answer

    # When the button for next problem clicked
    increment = st.button("次の問題")
    if increment:
        # Randomly take the number and remove it from list
        shuffle(st.session_state['mylist'])
        selectedi = st.session_state['mylist'].pop()
        # Store the variables
        st.session_state.i = selectedi # selected random number
        st.session_state['cnt'] += 1 # count of question

#  ----------------- QUESTIONS ----------------------
dfq = basic_questions()

# Main code
if st.session_state['cnt'] < 6:
    # Get Question, Hint, Answer
    question = dfq.iloc[st.session_state['i']-1]["Question"]
    hint = dfq.iloc[st.session_state['i']-1]["Hint"]
    answer = dfq.iloc[st.session_state['i']-1]["Answer"]
    acode = dfq.iloc[st.session_state['i']-1]["Code"]

    # Question and Hint
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown(" ")
        st.markdown(f"問題 {st.session_state.cnt}")
        st.code(question, language="markdown")
    with col2:
        if st.button('ヒント', key=f"{title}_hint_{st.session_state['i']}"):
            st.code(hint, language="markdown")

    # Write your own code
    st.markdown(" ")
    key=f"{title}_q_{st.session_state['i']}"
    display_output(key)

    myanswer = None

    # Answer
    col1, col2, col3 = st.columns([2,1,1])
    with col1:
        myanswer = st.text_input('答え', key=f"{title}_ans_{st.session_state['i']}")
    with col2:
        st.markdown(" ")
        st.markdown(" ")
        if st.button('提出', key=f"{title}_submit_{st.session_state['i']}"):
            with col3:
                # if myanswer:
                st.markdown(" ")
                if myanswer==answer:
                    st.success('正解!', icon="✅")
                    st.session_state['correct'] += 1
                else:
                    st.warning('残念！', icon="⚠️")

    st.markdown(" ")
    if st.button('正解をみる', key=f"{title}_giveup_{st.session_state['i']}"):
        st.code(acode, language="markdown")

else:
    st.write("Complete")
    st.write("You got ", st.session_state['correct'], " out of 5 correct!")
    # Initialise
    st.session_state['mylist'] = list(range(10))
    shuffle(st.session_state['mylist'])
    selectedi = st.session_state['mylist'].pop()
    st.session_state['i'] = selectedi
    st.session_state['cnt'] = 1
    st.session_state['correct'] = 0

# i = i + 1
