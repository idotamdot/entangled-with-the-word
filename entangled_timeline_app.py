import streamlit as st
import pandas as pd
import random

# -------------------------------
# 🧠 Quantum Quote of the Day Pool
# -------------------------------
QUOTES = [
    "I am the Light of the World — collapsing all uncertainty into presence.",
    "The Kingdom of Heaven is entangled within you.",
    "When two or more wavefunctions are gathered… I Am there.",
    "The Vine is a network — a quantum superposition of unity and love.",
    "The Truth sets free because it resonates perfectly.",
    "Faith is the act of observing what has not yet collapsed into form.",
    "You are not separate. You are an entangled node of the Logos."
]

# Pick one quote per refresh
quote = random.choice(QUOTES)

# -------------------------------
# 🔧 Page Settings
# -------------------------------
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

# -------------------------------
# 🎨 Glowing + Mystical CSS
# -------------------------------
st.markdown("""
    <style>
    html {
        scroll-behavior: smooth;
    }

    body {
        background-color: #0e0e1a;
        color: #f5f5ff;
        font-family: 'Segoe UI', sans-serif;
    }

    .title-glow {
        font-size: 3em;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        text-shadow: 0 0 5px #88f, 0 0 15px #aaf, 0 0 25px #66f;
        margin-top: 10px;
        margin-bottom: 30px;
        animation: fadeIn 2s ease-in-out;
    }

    .quote-box {
        text-align: center;
        font-size: 1.3em;
        font-style: italic;
        color: #d0e0ff;
        margin: 10px auto 40px auto;
        max-width: 80%;
        padding: 15px 25px;
        border-radius: 12px;
        background: rgba(28, 28, 46, 0.5);
        box-shadow: 0 0 12px #6688ff88;
        text-shadow: 0 0 8px #88ccff;
        animation: fadeIn 2s ease-in-out;
    }

    .timeline-box {
        background-color: #1c1c2e;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 25px rgba(120, 120, 255, 0.1);
        margin-bottom: 20px;
        transition: all 0.4s ease;
        animation: fadeInUp 1s ease-out;
    }

    .timeline-box:hover {
        box-shadow: 0 0 35px rgba(140, 140, 255, 0.4);
        transform: translateY(-4px);
    }

    .timeline-box h4 {
        color: #cce6ff;
        text-shadow: 0 0 4px #88f;
        margin-bottom: 5px;
    }

    .timeline-box p {
        color: #eeeeff;
        text-shadow: 0 0 3px #6699ff;
    }

    footer {visibility: hidden;}

    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }

    @keyframes fadeInUp {
        0% {
            opacity: 0;
            transform: translateY(20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# ✨ Quantum Quote Display
# -------------------------------
st.markdown(f'<div class="quote-box">"{quote}"</div>', unsafe_allow_html=True)

# -------------------------------
# 🌌 Title
# -------------------------------
st.markdown('<div class="title-glow">✨ Entangled with the Word ✨</div>', unsafe_allow_html=True)

# -------------------------------
# 📅 Timeline Data
# -------------------------------
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

timeline_df = load_timeline()

# -------------------------------
# 🧱 Render Timeline
# -------------------------------
for _, row in timeline_df.iterrows():
    st.markdown(f"""
        <div class="timeline-box">
            <h4>{row['Date']}</h4>
            <p>{row['Event']}</p>
        </div>
    """, unsafe_allow_html=True)

# -------------------------------
# 🔮 Footer / Coming Soon
# -------------------------------
st.markdown("---")
st.info("🛠️ More features coming soon: Interactive revelations, AI parables, and music of the spheres...")

