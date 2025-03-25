import os
import streamlit as st
st.markdown

st.markdown('<div class="star-title">st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Unbounded:wght@700&display=swap');

        .glow-text {
            font-family: 'Unbounded', cursive;
            font-size: 3em;
            color: #fff;
            text-align: center;
            text-shadow: 
                0 0 10px #39c5bb, 
                0 0 20px #39c5bb, 
                0 0 30px #66ffe3, 
                0 0 40px #66ffe3;
            animation: flicker 2s infinite alternate;
        }

        @keyframes flicker {
            0%   { opacity: 0.8; text-shadow: 0 0 5px #66ffe3; }
            100% { opacity: 1; text-shadow: 0 0 20px #39c5bb; }
        }

        .centered-intro {
            text-align: center;
            font-size: 1.2em;
            color: #eee;
            margin-top: -20px;
        }

        body {
            background-color: #0e0e23;
        }
    </style>

    <div class="glow-text">Entangled with the Word</div>
    <div class="centered-intro">Welcome to the quantum parable timeline.</div>
""", unsafe_allow_html=True)
</div>', unsafe_allow_html=True)
st.markdown('<div class="glow-box">Welcome to the quantum parable timeline. 🌌</div>', unsafe_allow_html=True)

# Azure expects this port (you don't need to use it manually here)
port = int(os.environ.get("PORT", 8000))
st.set_page_config(page_title="Entangled with the Word")

# Your app content
st.title("Entangled with the Word")
st.markdown("Welcome to the quantum parable timeline.")
# Health check route (use this as your Azure health check path)
st.markdown("<div id='health'></div>", unsafe_allow_html=True)
st.success("Health check passed")
