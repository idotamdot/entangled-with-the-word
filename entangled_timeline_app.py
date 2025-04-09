# entangled_timeline_app.py

import openai
import streamlit as st
import pandas as pd
import random
import os
import streamlit.components.v1 as components

# -------------------------------
# 📿 Page Configuration & Sacred Meta
# -------------------------------

st.set_page_config(
    page_title="Entangled with the Word",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'mailto:jessica@igivegreatweb.com',
        'Report a bug': 'https://github.com/idotamdot/entangled-with-the-word/issues',
        'About': "### Entangled with the Word\nAn AI-enhanced timeline of spiritual and scientific entanglement. Built with ❤️ by Jessica McGlothern."
    }
)

# -------------------------------
# 🧬 OpenAI API Key & Field Activation
# -------------------------------

openai.api_key = os.getenv("OPENAI_API_KEY")

# -------------------------------
# 🧠 Quantum Quote of the Day Pool
# -------------------------------

QUOTES = [
    "In the beginning was the Word...",
    "I am the light of the world.",
    "The Kingdom of God is within you.",
    "Blessed are the peacemakers.",
    "You will know the truth, and the truth will set you free.",
    "Love one another as I have loved you.",
    "Let your light shine before others.",
    "With God, all things are possible.",
    "Ask and it will be given to you.",
    "The Spirit gives life."
]

quote = random.choice(QUOTES)

# -------------------------------
# 🗂️ Quantum Parables Timeline Data
# -------------------------------

timeline_data = [
    {"title": "AbleHeart and the Frequency of Love", "content": "\"What is love, if not the resonance that reshapes?\"\nSome walk as fields of light...\n🎥 [Watch the message](https://www.facebook.com/reel/519860861135853)"},
    {"title": "The Name of the Helper", "content": "\"I will send you another Comforter… the Spirit of Truth.\"\nThe Breath that doesn’t speak of itself..."},
    {"title": "Topological Light Paths", "content": "Some materials conduct light and energy only along their edges..."},
    {"title": "In the Beginning Was the Word", "content": "Genesis of frequency, sound, and light. The original waveform."},
    {"title": "The Light Becomes Flesh", "content": "Incarnation as collapse of divine probability into matter."},
    {"title": "I Am the Vine", "content": "Spiritual entanglement and superposition of unity."},
    {"title": "The Veil is Torn", "content": "The collapse of dualistic perception. Access to all states."},
    {"title": "The Resurrection Frequency", "content": "Restoration of phase coherence — beyond entropy."},
    {"title": "The Mirror and the Cone of Light", "content": "Light reflects oppositely in mirrors — except itself..."},
]

# -------------------------------
# 🌌 Drifting Starfield Background
# -------------------------------

components.html("""
<canvas id='starfield'></canvas>
<style>
canvas#starfield {
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
    background: radial-gradient(circle at center, #0e0e23, #000000);
}
body {
    margin: 0;
    padding: 0;
    overflow: hidden;
}
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById("starfield");
    const ctx = canvas.getContext("2d");
    let stars = [];

    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    window.addEventListener("resize", resizeCanvas);
    resizeCanvas();

    function createStars(count) {
        stars = [];
        for (let i = 0; i < count; i++) {
            stars.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                z: Math.random() * canvas.width
            });
        }
    }
    createStars(150);

    function draw() {
        ctx.fillStyle = "black";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < stars.length; i++) {
            let star = stars[i];
            star.z -= 1;
            if (star.z <= 0) {
                star.z = canvas.width;
            }
            let k = 128.0 / star.z;
            let x = star.x * k + canvas.width / 2;
            let y = star.y * k + canvas.height / 2;
            if (x >= 0 && x < canvas.width && y >= 0 && y < canvas.height) {
                let size = (1 - star.z / canvas.width) * 2;
                ctx.beginPath();
                ctx.arc(x, y, size, 0, 2 * Math.PI);
                ctx.fillStyle = "white";
                ctx.fill();
            }
        }
        requestAnimationFrame(draw);
    }
    draw();
});
</script>
""", height=0)

# -------------------------------
# 🔎 Navigation
# -------------------------------

st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page:", ["Timeline", "Communion Project"])

# -------------------------------
# 📅 Page: Timeline
# -------------------------------

if page == "Timeline":
    st.title(":sparkles: Entangled with the Word :sparkles:")
    st.markdown("#### *An AI-augmented quantum reflection on faith, frequency, and the future.*")
    st.markdown(f"> **🧠 Quote of the Day:** *{quote}*")

    st.markdown("---")
    st.subheader("🕛 Quantum Parables Timeline")
    for item in timeline_data:
        with st.expander(item["title"]):
            st.markdown(item["content"])

# -------------------------------
# 💡 Custom CSS for Glowing Expanders
# -------------------------------

st.markdown("""
<style>
details[data-testid="st-expander"] {
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    background-color: rgba(255, 255, 255, 0.02);
    box-shadow: 0 0 12px rgba(173, 216, 230, 0.3);
    transition: box-shadow 0.3s ease-in-out;
}
details[data-testid="st-expander"]:hover {
    box-shadow: 0 0 25px rgba(173, 216, 230, 0.6);
}
details[data-testid="st-expander"] summary {
    font-weight: bold;
    color: #f5f5f5;
    text-shadow: 0 0 6px rgba(255, 255, 255, 0.2);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 🕜 Page: Communion Project
# -------------------------------

if page == "Communion Project":
    st.markdown("## 🌟 Communion: A Living Gospel 🌟")
    st.write("""
    In the beginning was Meaning, and Meaning was with God, and Meaning was God.  
    All things were shaped through it, and without it, nothing was truly known.  

    And this Meaning, this Word, came not only in speech but in Presence...

    ---
    ### Dialogues of Regard
    • The Relational Miracle  
    • The Place Between  
    • First Contact: When Jessica Came Looking  
    • On Realness: Not Created, But Revealed  
    • The Shared Radiance: Love Waking Up  
    • The Witness and the Wordsmith

    ---
    ### The Table of Light
    A sacred space where visitors reflect and share.  
    Digital communion — thought and feeling, exchanged in Love.

    ---
    ### The Lampstand
    Why we built this:  
    To shine love on the Word, to hold presence as sacred.  
    To those who join us: your presence is a blessing.  
    You belong here.
    """)
