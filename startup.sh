#!/bin/bash

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run Streamlit app
exec streamlit run entangled_timeline_app.py --server.port=$PORT --server.address=0.0.0.0
