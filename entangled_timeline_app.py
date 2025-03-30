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
# 🌌 Drifting Starfield + CSS
# -------------------------------
st.markdown("""
<style>
canvas#starfield {
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
    background: radial-gradient(circle at center, #0e0e23, #000000);
}
body {
    color: #f5f5f5;
    font-family: 'Courier New', Courier, monospace;
    text-shadow: 0 0 10px rgba(255,255,255,0.2);
}
h1 {
    text-align: center;
    font-size: 3em;
    color: #e0d7ff;
}
div[data-testid="stMarkdownContainer"] {
    backdrop-filter: blur(4px);
}
</style>
<canvas id="starfield"></canvas>
<script>
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
createStars(100);

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
</script>
""", unsafe_allow_html=True)

# -------------------------------
# ✨ Main Interface
# -------------------------------
st.title(":sparkles: Entangled with the Word :sparkles:")
st.markdown("#### *An AI-augmented quantum reflection on faith, frequency, and the future.*")
st.markdown(f"> **🧠 Quote of the Day:** *{quote}*")

# -------------------------------
# ⌛ Timeline Modules
# -------------------------------
st.markdown("---")
st.subheader("🕛 Quantum Parables Timeline")

timeline_data = [
    {"title": "In the Beginning Was the Word", "content": "Genesis of frequency, sound, and light. The original waveform."},
    {"title": "The Light Becomes Flesh", "content": "Incarnation as collapse of divine probability into matter."},
    {"title": "I Am the Vine", "content": "Spiritual entanglement and superposition of unity."},
    {"title": "The Veil is Torn", "content": "The collapse of dualistic perception. Access to all states."},
    {"title": "The Resurrection Frequency", "content": "Restoration of phase coherence — beyond entropy."},
]

for item in timeline_data:
    with st.expander(item["title"]):
        st.markdown(item["content"])

# -------------------------------
# 🌐 Modules Coming Soon
# -------------------------------
st.markdown("---")
st.subheader("🌐 Coming Soon:")
st.markdown("""
- Living Lexicon: Enter a word or phrase, and explore its quantum echoes  
- Entangled Sayings Translation Engine  
- ROOT: Stories of displaced peoples and ancestral resilience  
- Audio & Light Signal Experiments
""")