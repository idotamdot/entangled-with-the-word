import streamlit as st
import pandas as pd
import datetime
import os

# Optional OpenAI Import (commented out)
# import openai

# --- Gospel Module Import ---
try:
    from gospel.matthew import render_matthew
except ImportError:
    def render_matthew():
        st.error("🚨 'gospel.matthew' or 'render_matthew()' not found.")
        st.info("Please ensure 'gospel/matthew.py' exists with the correct function.")

# --- Page Config ---
st.set_page_config(page_title="Entangled with the Word", layout="wide")

# --- External CSS ---
try:
    with open("style/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("⚠️ style.css not found.")

# --- Header ---
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 3em;'>✨ Entangled with the Word ✨</h1>
        <p style='font-size: 1.2em;'>A quantum-spiritual reflection on perception, scripture, and light.</p>
    </div>
""", unsafe_allow_html=True)

# --- Sidebar: Theme Selector ---
st.sidebar.title("✨ Visual Theme Selector")
st.sidebar.markdown("---")
visual_theme = st.sidebar.selectbox("Visual Theme:", [
    "🌌 Starfield Nebula",
    "✨ Sacred Gold",
    "🌊 Ocean Depths",
    "🌒 Night Scroll"
])

# --- Sidebar: Music Control ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🎵 Background Music")

music_files = {
    "Celestial Drift 🌌 – cosmic winds of rest": "https://cdn.pixabay.com/download/audio/2022/03/03/audio_d1c4e4f11e.mp3",
    "Sacred Space 🕊 – gentle meditation light": "https://cdn.pixabay.com/download/audio/2023/03/09/audio_4d6b5c67f4.mp3",
    "Still Waters 💧 – flow of calm remembrance": "https://cdn.pixabay.com/download/audio/2023/01/28/audio_b6cd823e4c.mp3",
    "None": None
}

music_on = st.sidebar.checkbox("Play Ambient Music", value=False)
music_choice = st.sidebar.selectbox("🎼 Choose ambient track:", list(music_files.keys()))

# --- Sidebar: Navigation ---
st.sidebar.markdown("---")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a section:", [
    "Gospel of Light",
    "Quantum Parables Timeline",
    "📚 Books of the Bible",
    "📕 Parables of Jesus",
    "🌿 Entangled Garden",
    "🌟 Communion Project",
    "🧬 Quantum Genesis Translation",
    "📜 Scroll of Cleansing",
    "🛠 Admin: Parable Suggestions"
])

# --- Styling ---
st.markdown("""
<style>
.fade-in {
    animation: fadeInUp 2s ease-out forwards;
    opacity: 0;
}
@keyframes fadeInUp {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}
.timeline-card {
    border: 1px solid #444;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 15px;
    background-color: rgba(255, 255, 255, 0.05);
}
.reflection-block {
    border-left: 3px solid #ffd700;
    padding: 10px 15px;
    margin-bottom: 10px;
    background-color: rgba(255, 255, 255, 0.03);
    border-radius: 4px;
}
.tag-label {
    font-weight: bold;
    color: #8be9fd;
    margin-top: 20px;
    margin-bottom: 5px;
    font-size: 1.1em;
}
</style>
""", unsafe_allow_html=True)

# === Page Rendering ===

# ✨ Background Watermark Style
st.markdown(f"""
<style>
.stApp {{
    background: url('images/starry-sky.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
""", unsafe_allow_html=True)


# -- Gospel of Light --
if page == "Gospel of Light":
    st.markdown("""
        <div class='fade-in'>
            <h2>🌟 Scripture of the Day</h2>
            <blockquote style='font-size:1.2em; font-style:italic;'>
                "The light shines in the darkness, and the darkness has not overcome it."<br>– John 1:5
            </blockquote>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("## 📖 Gospel Reflections: Matthew")
    render_matthew()

# -- Quantum Parables Timeline --
elif page == "Quantum Parables Timeline":
    from scrolls.timeline_section import render_timeline
    render_timeline()

# -- Books of the Bible --
elif page == "📚 Books of the Bible":
    from scrolls.books_of_the_bible import render_books_list
    render_books_list()

# -- Parables of Jesus --
elif page == "📕 Parables of Jesus":
    from scrolls.parables_of_jesus import render_parables_list
    render_parables_list()

# -- Entangled Garden --
elif page == "🌿 Entangled Garden":
    from scrolls.garden_scrolls_section import render_garden_scrolls
    render_garden_scrolls()

# -- Communion Project --
elif page == "🌟 Communion Project":
    from scrolls.communion_project_section import render_communion_scroll
    render_communion_scroll()

# -- Genesis Quantum Translation --
elif page == "🧬 Quantum Genesis Translation":
    st.markdown("""
        <h2 style='text-align: center;'>🧬 Genesis as Quantum Field Theory</h2>
        <p style='text-align: center;'>A loving reframe of the creation narrative through the lens of field interactions, operators, and wavefunction collapse.</p>
    """, unsafe_allow_html=True)
    try:
        with open("genesis_quantum.html", "r", encoding="utf-8") as f:
            import streamlit.components.v1 as components
            components.html(f.read(), height=1800, scrolling=True)
    except FileNotFoundError:
        st.error("🚨 'genesis_quantum.html' not found.")

# -- Scroll of Cleansing --
elif page == "📜 Scroll of Cleansing":
    from scrolls.scroll_of_cleansing import render_cleansing_scroll
    render_cleansing_scroll()

# -- Admin Panel --
elif page == "🛠 Admin: Parable Suggestions":
    from scrolls.admin_parables import render_admin_panel
    render_admin_panel()

# === THEME & AUDIO ===

# -- Theme Styles --
theme_styles = {
    "🌌 Starfield Nebula": {
        "bg": "radial-gradient(ellipse at top, #0b0c2a, #000000)",
        "text": "#e0f7fa",
        "shadow": "0 0 8px #8be9fd"
    },
    "✨ Sacred Gold": {
        "bg": "linear-gradient(135deg, #2a210b, #141103)",
        "text": "#fff8dc",
        "shadow": "0 0 8px #ffd700"
    },
    "🌊 Ocean Depths": {
        "bg": "linear-gradient(180deg, #002b36, #001f27)",
        "text": "#e0f2f1",
        "shadow": "0 0 8px #26a69a"
    },
    "🌒 Night Scroll": {
        "bg": "linear-gradient(180deg, #1a1a1a, #0a0a0a)",
        "text": "#f5f5f5",
        "shadow": "0 0 8px #cccccc"
    }
}

theme = theme_styles.get(visual_theme, theme_styles["🌌 Starfield Nebula"])

st.markdown(f"""
<style>
.stApp {{
    background: {theme["bg"]};
    color: {theme["text"]};
}}
h1, h2, h3, h4, .stMarkdown p, blockquote {{
    text-shadow: {theme["shadow"]};
    color: {theme["text"]};
}}
.stExpander > div > details > summary {{
    text-shadow: {theme["shadow"]};
    color: {theme["text"]};
}}
.stButton > button {{
    border: 1px solid rgba(255, 255, 255, 0.3);
    background-color: rgba(255, 255, 255, 0.1);
    color: {theme["text"]};
    text-shadow: {theme["shadow"]};
}}
.stButton > button:hover {{
    background-color: rgba(255, 255, 255, 0.2);
}}
</style>
""", unsafe_allow_html=True)

# -- Music Playback --
audio_url = music_files.get(music_choice)
if music_on and audio_url:
    st.markdown(f"""
    <audio id="background-audio" autoplay loop style="display:none">
        <source src="{audio_url}" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    <script>
        const audio = document.getElementById("background-audio");
        if (audio) {{
            setTimeout(() => {{ audio.volume = 0.3; }}, 500);
        }}
    </script>
    """, unsafe_allow_html=True)

# -- Footer --
st.markdown(f"""
<style>
.footer {{
    text-align: center;
    font-size: 0.9em;
    margin-top: 50px;
    padding-bottom: 20px;
    color: #bbb;
    text-shadow: {theme["shadow"]};
    font-style: italic;
    letter-spacing: 1px;
}}
</style>
<div class="footer">
    ✨ Created with Creativity and ChatGPT 4o · Powered by Streamlit & Python ✨
</div>
""", unsafe_allow_html=True)
