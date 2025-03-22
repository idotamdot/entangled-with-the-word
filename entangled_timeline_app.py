import os
import streamlit as st
import subprocess

port = int(os.environ.get("PORT", 8000))  # Azure expects port 8000
st.set_page_config(page_title="Entangled with the Word")

# Your app content here...
st.title("Entangled with the Word")

# Optional: lightweight health check support
if st.experimental_get_query_params().get("ping") == ["true"]:
    st.write("OK")
