# entangled_timeline_app.py
import os
import datetime as dt
import pandas as pd
import streamlit as st

# --- Page config (must be the first Streamlit call) ---
st.set_page_config(page_title="Entangled with the Word", layout="wide")

# =============== Small utils for CSV storage ===============
DATA_DIR = "."
def _path(name: str) -> str:
    return os.path.join(DATA_DIR, name)

def read_csv_safe(name: str, cols: list[str] | None = None) -> pd.DataFrame:
    p = _path(name)
    if not os.path.exists(p):
        return pd.DataFrame(columns=cols or [])
    try:
        df = pd.read_csv(p)
        if cols:
            for c in cols:
                if c not in df.columns:
                    df[c] = "" if c != "candles" else 0
            # keep only expected columns to avoid surprises
            df = df[[c for c in cols]]
        return df
    except Exception:
        return pd.DataFrame(columns=cols or [])

def write_csv_safe(name: str, df: pd.DataFrame) -> None:
    df.to_csv(_path(name), index=False)

# =============== Sidebar ===============
st.sidebar.markdown("---")
visual_theme = st.sidebar.selectbox(
    "Visual Theme:",
    ["🌌 Starfield Nebula", "✨ Sacred Gold", "🌊 Ocean Depths", "🌒 Night Scroll"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("🎵 Background Music")
music_on = st.sidebar.checkbox("Play Ambient Music", value=True)

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a section:",
    ["Gospel of Light", "All Books", "Quantum Parables Timeline", "Communion Project (Coming Soon)", "🛠 Admin: Parable Suggestions"]
)

# =============== Global CSS ===============
st.markdown("""
<style>
.fade-in { animation: fadeInUp 2s ease-out forwards; opacity: 0; }
@keyframes fadeInUp {
  from { transform: translateY(20px); opacity: 0; }
  to   { transform: translateY(0); opacity: 1; }
}
.tag-label {
  display:inline-block; padding:4px 10px; border-radius:12px; font-size:.8em; font-weight:bold; margin:8px 8px 0 0;
  background:#111827; color:white; box-shadow:0 0 6px rgba(173,216,230,.6); border:1px solid rgba(255,255,255,.2);
}
.reflection-block {
  background:rgba(255,255,255,.02); border-radius:10px; padding:16px; margin:16px 0;
  border:1px solid rgba(255,255,255,.05); box-shadow:0 0 12px rgba(173,216,230,.2); transition:transform .3s ease;
}
.reflection-block:hover { transform:scale(1.02); box-shadow:0 0 24px rgba(173,216,230,.4); }
blockquote { border-left:4px solid rgba(255,255,255,.2); padding-left:12px; color:#eaeaea; }
</style>
""", unsafe_allow_html=True)

from scrolls.all_books_section import render_all_books_page


# Header
st.markdown("""
<div style='text-align:center;'>
  <h1 style='font-size:3em;'>✨ Entangled with the Word ✨</h1>
  <p style='font-size:1.2em;'>A quantum-spiritual reflection on perception, scripture, and light.</p>
</div>
""", unsafe_allow_html=True)


# =============== Page Content ===============
if page == "All Books":
    render_all_books_page()
elif page == "Gospel of Light":
    st.markdown("""
    <div class='fade-in'>
      <h2>🌟 Scripture of the Day</h2>
      <blockquote style='font-size:1.2em; font-style:italic;'>
        "The light shines in the darkness, and the darkness has not overcome it."<br>– John 1:5
      </blockquote>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ---
    ## 📖 The Gospel of Light: Jesus as the Massless One

    > *"But he walked*
