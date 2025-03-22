import streamlit as st
import os

st.set_page_config(page_title="Entangled with the Word")

# Main app
st.title("Entangled with the Word")

# Health check support
if st.experimental_get_query_params().get("ping") == ["true"]:
    st.write("OK")
