import streamlit as st
from streamlit_ace import st_ace

from contextlib import contextmanager
from io import StringIO
from streamlit.runtime.scriptrunner.script_run_context import SCRIPT_RUN_CONTEXT_ATTR_NAME
from threading import current_thread
import subprocess
import sys

# --------------- FUNCTION ------------------

# def user_input(key):
#     # return st.text_area('text to analyse', key='userinput')
#     return st_ace(language='python', theme="nord_dark", font_size=18, key=key)

def execute_input(codes):
    output = exec(codes)
    return output

# Write output
@contextmanager
def st_redirect(src, dst):
    placeholder = st.empty()
    output_func = getattr(placeholder, dst)

    with StringIO() as buffer:
        old_write = src.write

        def new_write(b):
            if getattr(current_thread(), SCRIPT_RUN_CONTEXT_ATTR_NAME, None):
                buffer.write(b)
                output_func(buffer.getvalue())
            else:
                old_write(b)

        try:
            src.write = new_write
            yield
        finally:
            src.write = old_write

@contextmanager
def st_stdout(dst):
    with st_redirect(sys.stdout, dst):
        yield

@contextmanager
def st_stderr(dst):
    with st_redirect(sys.stderr, dst):
        yield

def display_output(codes):
    myanswer = None
    # ------------- CODE part --------------------
    # col1, col2 = st.columns([1,1])
    # with col1:
        # st.write('コードを書く')
        # codes = user_input(key)

    # ------------ OUTPUT ------------------------
    # if st.button('Execute'):
    # if codes:
    # with col2:
    st.write('アウトプット')
    with st_stdout("code"):
        exec(codes)
            # Answer
            # myanswer = st.number_input('Your answer')

    # return myanswer
