#!/bin/bash

# Fail fast if something goes wrong
set -e

# Install Python dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Create Streamlit config
echo "⚙️ Creating Streamlit config..."
mkdir -p ~/.streamlit
cat <<EOF > ~/.streamlit/config.toml
[server]
headless = true
port = $PORT
enableCORS = false
enableXsrfProtection = false
EOF

# Run the app
echo "🚀 Starting Streamlit app..."
streamlit run entangled_timeline_app.py --server.port=$PORT
