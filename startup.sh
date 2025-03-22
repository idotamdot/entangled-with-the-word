#!/bin/bash
pip install --upgrade pip
pip install -r requirements.txt
streamlit run entangled_timeline_app.py --server.port=$PORT --server.address=0.0.0.0
