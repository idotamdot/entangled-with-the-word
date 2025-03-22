import os
import streamlit as st

port = int(os.environ.get("PORT", 8000))  # Azure expects port 8000
st.set_page_config(page_title="Entangled with the Word")

# Your app content here...
st.title("Entangled with the Word")
