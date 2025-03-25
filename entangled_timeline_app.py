import os
import streamlit as st
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Raleway', sans-serif;
        background: linear-gradient(135deg, #0f0f1c, #1b1b38);
        color: #f0f8ff;
    }

    h1, h2, h3 {
        color: #ffffff;
        text-shadow: 0 0 8px #8be9fd, 0 0 12px #8be9fd;
    }

    .glow-box {
        border: 2px solid #8be9fd;
        border-radius: 12px;
        padding: 1.5em;
        margin-bottom: 2em;
        background-color: rgba(255, 255, 255, 0.05);
        box-shadow: 0 0 20px #8be9fd88;
    }

    .star-title {
        font-size: 2.2em;
        text-align: center;
        color: #f0f8ff;
        text-shadow: 0 0 6px #ffffff, 0 0 20px #8be9fd;
        animation: glow 3s infinite alternate;
    }

    @keyframes glow {
        from {
            text-shadow: 0 0 6px #ffffff, 0 0 20px #8be9fd;
        }
        to {
            text-shadow: 0 0 12px #ffffff, 0 0 30px #8be9fd;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="star-title">Entangled with the Word</div>', unsafe_allow_html=True)
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
