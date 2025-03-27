#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Create a clean config file with a hardcoded port (Azure expects port 80)
mkdir -p ~/.streamlit
echo "\
[server]
headless = true
port = 80
enableCORS = false
enableXsrfProtection = false
" > ~/.streamlit/config.toml

# Launch Streamlit app, explicitly setting host to 0.0.0.0 for external access
streamlit run entangled_timeline_app.py --server.port=80 --server.address=0.0.0.0
