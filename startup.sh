#!/bin/bash
export PORT=${PORT:-8000}

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

python -m streamlit run entangled_timeline_app.py
