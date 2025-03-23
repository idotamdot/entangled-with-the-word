import os
import streamlit as st

# Azure expects this port (you don't need to use it manually here)
port = int(os.environ.get("PORT", 8000))
st.set_page_config(page_title="Entangled with the Word")

# Your app content
st.title("Entangled with the Word")
st.markdown("Welcome to the quantum parable timeline.")
# Health check route (use this as your Azure health check path)
st.markdown("<div id='health'></div>", unsafe_allow_html=True)
st.success("Health check passed")
