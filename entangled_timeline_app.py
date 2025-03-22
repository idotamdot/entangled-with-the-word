import os
import streamlit as st

port = int(os.environ.get("PORT", 8000))  # Azure expects port 8000
st.set_page_config(page_title="Entangled with the Word")

# Your app content here...
st.title("Entangled with the Word")

# Run the app if using CLI (but Azure handles this via startup command or gunicorn)
    import subprocess
    subprocess.run(["streamlit", "run", "entangled_timeline_app.py", "--server.port", str(port), "--server.address", "0.0.0.0"])
