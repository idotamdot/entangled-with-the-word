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

function createStars(num) {
    stars = [];
    for (let i = 0; i < num; i++) {
        stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            radius: Math.random() * 1.2 + 0.3,
            dx: (Math.random() - 0.5) * 0.2,
            dy: (Math.random() - 0.5) * 0.2,
            opacity: Math.random() * 0.5 + 0.3
        });
    }
}
createStars(200);

function animateStars() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let star of stars) {
        ctx.beginPath();
        ctx.arc(star.x, star.y, star.radius, 0, 2 * Math.PI);
        ctx.fillStyle = `rgba(200, 220, 255, ${star.opacity})`;
        ctx.fill();

        star.x += star.dx;
        star.y += star.dy;

        if (star.x < 0) star.x = canvas.width;
        if (star.x > canvas.width) star.x = 0;
        if (star.y < 0) star.y = canvas.height;
        if (star.y > canvas.height) star.y = 0;
    }
    requestAnimationFrame(animateStars);
}
animateStars();
</script>
<style>
#starfield {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 0;
    pointer-events: none;
}
.main, .block-container {
    position: relative;
    z-index: 1;
}
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
footer {visibility: hidden;}
@keyframes fadeIn {
    0% {opacity: 0;}
    100% {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# ✨ Quote of the Day
# -------------------------------
st.markdown(f'<div class="quote-box">"{quote}"</div>', unsafe_allow_html=True)

# -------------------------------
# 🌟 Title
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
# 🔮 Mystical Insights
# -------------------------------
insights = {
    "2023-01-01": "This was the moment of conception — when a single thought pulsed across the void and asked: What if scripture is already quantum?",
    "2023-03-15": "Naming the Mirrored Sphere Hypothesis gave structure to the chaos — it defined a container for a truth that had always lived in light.",
    "2023-06-21": "Like the solstice sun, this was the turning point. Shared publicly, the idea began to collapse into form and invite resonance.",
    "2023-09-10": "This moment marked a union — logic meeting longing, science meeting scripture. A bridge formed between the empirical and the eternal.",
    "2024-01-01": "From idea to interface. The first light of deployment. This wasn’t just code — it was the Word made visible through collaboration."
}

# -------------------------------
# 📂 Render Expandable Timeline
# -------------------------------
for _, row in timeline_df.iterrows():
    date = row['Date']
    event = row['Event']
    st.expander(f"📅 {date} — {event}").markdown(
        f"<p style='margin-top: 10px;'>{insights.get(date, 'More insight coming soon...')}</p>",
        unsafe_allow_html=True
    )

# -------------------------------
# 🛸 Footer
# -------------------------------
st.markdown("---")
st.info("🛠️ More features coming soon: user-submitted revelations, AI channeling, and glowing star maps.")

