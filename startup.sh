#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Create a clean config file with the correct port
mkdir -p ~/.streamlit
echo "\
[server]
headless = true
port = $PORT
enableCORS = false
enableXsrfProtection = false
" > ~/.streamlit/config.toml

# Launch Streamlit app
streamlit run entangled_with_the_Word_app.py
