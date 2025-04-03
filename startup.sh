#!/bin/bash
set -e  # Fail fast on error

# Set PORT default
export PORT=${PORT:-8000}

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "⚙️ Writing Streamlit config to ~/.streamlit/config.toml..."
mkdir -p ~/.streamlit
cat << EOF > ~/.streamlit/config.toml
[server]
headless = true
enableCORS = false
enableXsrfProtection = false
port = $PORT

[theme]
base = "light"
EOF


echo "🗝️ Writing secrets to ~/.streamlit/secrets.toml..."
cat << EOF > ~/.streamlit/secrets.toml
[openai]
api_key = "your-openai-api-key-here"
EOF


echo "🚀 Launching app on port $PORT..."
streamlit run entangled_timeline_app.py --server.port=$PORT
