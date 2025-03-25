import streamlit as st
import pandas as pd
from datetime import datetime

# This must be the first Streamlit command!
st.set_page_config(
    page_title="Entangled with the Word",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'mailto:jessica.elizabeth.mcglothern@gmail.com',
        'Report a bug': 'https://github.com/idotamdot/entangled-with-the-word/issues',
        'About': "### Entangled with the Word\nAn AI-enhanced timeline of spiritual and scientific entanglement. Built with ❤️ by Jessica McGlothern."
    }
)

# Custom CSS for a glowing, mystical look
# Custom CSS for a glowing, mystical look with readable text
st.markdown("""
    <style>
    body {
        background-color: #0e0e1a;
        color: #f5f5ff;
    }
    .title-glow {
        font-size: 3em;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        text-shadow: 0 0 5px #88f, 0 0 15px #aaf, 0 0 25px #66f;
        margin-top: 30px;
        margin-bottom: 30px;
    }
    .timeline-box {
        background-color: #1c1c2e;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 25px rgba(120, 120, 255, 0.3);
        margin-bottom: 20px;
    }
    .timeline-box h4 {
        color: #cce6ff;
        text-shadow: 0 0 4px #88f;
    }
    .timeline-box p {
        color: #eeeeff;
        text-shadow: 0 0 3px #6699ff;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


# Glowing Title
st.markdown('<div class="title-glow">✨ Entangled with the Word ✨</div>', unsafe_allow_html=True)

# Example Timeline Data
def load_timeline():
    return pd.DataFrame({
        "Date": [
            "2023-01-01",
            "2023-03-15",
            "2023-06-21",
            "2023-09-10",
            "2024-01-01"
        ],
        "Event": [
            "Initial Concept Inspired",
            "Mirrored Sphere Hypothesis Named",
            "Shared Online for the First Time",
            "Spiritual + Scientific Merge Drafted",
            "Entangled with the Word App Deployed"
        ]
    })

# Load data
timeline_df = load_timeline()

# Render Timeline
for i, row in timeline_df.iterrows():
    with st.container():
        st.markdown(f"""
            <div class="timeline-box">
                <h4>{row['Date']}</h4>
                <p>{row['Event']}</p>
            </div>
        """, unsafe_allow_html=True)

# Optional footer or expansion
st.markdown("---")
st.info("More features like search, animations, and OpenAI-enhanced content are coming soon!")

