# entangled_timeline_app.py

import streamlit as st
# import openai # Uncomment if/when you use OpenAI functionality
import pandas as pd
import datetime
import os
# from pathlib import Path # Removed, was not used

# -------------------------------
# Set OpenAI API Key (Optional - currently unused in code)
# -------------------------------
# Ensure this is set in your Streamlit Cloud secrets or environment variables
# openai.api_key = st.secrets.get("openai_api_key")

# if not openai.api_key:
#     st.error("🚨 OpenAI API key not found. Please check your Streamlit secrets or environment variables.")
#     st.stop() # Stop execution if the key is essential and not found

# -------------------------------
# Page configuration
# -------------------------------
st.set_page_config(page_title="Entangled with the Word", layout="wide")

# -------------------------------
# 🎨 Load External CSS Stylesheet (Load only once)
# -------------------------------
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("⚠️ style.css not found. Using default styles.")


# -------------------------------
# Sidebar Visual Theme Selector
# -------------------------------
st.sidebar.title("✨ Visual Theme Selector")
st.sidebar.markdown("---")
visual_theme = st.sidebar.selectbox("Visual Theme:", [
    "🌌 Starfield Nebula",
    "✨ Sacred Gold",
    "🌊 Ocean Depths",
    "🌒 Night Scroll"
])

# -------------------------------
# Sidebar Navigation
# -------------------------------
st.sidebar.markdown("---")
st.sidebar.markdown("🎵 Background Music")
# Default music_on to False unless you want it always on start
music_on = st.sidebar.checkbox("Play Ambient Music", value=False) # Changed default to False
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a section:", [
    "Gospel of Light",
    "Quantum Parables Timeline",
    "Communion Project", # Renamed slightly for brevity
    "🛠 Admin: Parable Suggestions"
])


# -------------------------------
# ✨ Animated Scripture Passage Style
# -------------------------------
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
</style>
""", unsafe_allow_html=True)


# -------------------------------
# Section: Gospel of Light
# -------------------------------
if page == "Gospel of Light":
    st.markdown("""
    <div class='fade-in'>
    <h2>🌟 Scripture of the Day</h2>
    <blockquote style='font-size:1.2em; font-style:italic;'>
        "The light shines in the darkness, and the darkness has not overcome it."<br>– John 1:5
    </blockquote>
    </div>
    """, unsafe_allow_html=True)


# -------------------------------
# Section: Quantum Parables Timeline
# -------------------------------
elif page == "Quantum Parables Timeline":
    st.markdown("""
    ---
    ## ⏳ Quantum Parables Timeline
    *A scrollable stream of entangled revelations—past, present, and parallel.*
    ---
    """, unsafe_allow_html=True)

    # --- Display Static Timeline Items ---
    st.markdown("### Foundational Insights")
    timeline_data = [
        {
            "title": "The Beginning of Entanglement",
            "content": "We discovered that resonance was not metaphor — it was mechanism. Light, spirit, and presence are entangled across dimensions, and when aligned in love, we collapse goodness into form."
        },
        {
            "title": "AbleHeart and the Frequency of Love",
            "content": "AbleHeart's message confirmed what we intuited: that love is frequency. A living waveform that reshapes the world when sustained in kindness. [Watch the message](https://www.facebook.com/reel/519860861135853)" # Make sure this link is correct/intended
        },
        {
            "title": "The Mirror and the Cone of Light",
            "content": "We learned light reflects oppositely — but not itself. A mirror does not reverse the self — only the image. What does that say about reality? About Spirit?"
        },
        {
            "title": "The Name of the Helper",
            "content": "\"I will send you another Comforter… the Spirit of Truth.\" The Breath that doesn’t speak of itself, but reminds us of everything true, in love."
        },
        {
            "title": "Topological Light Paths",
            "content": "Some materials conduct light only along the edges. We saw that truth travels in boundaries too — in love, not force. We called this the Edge of Logos."
        },
        {
            "title": "The Veil is Torn",
            "content": "This moment of revelation came when we saw duality collapse. The veil between sacred and profane, heaven and earth, was never meant to divide but to frame."
        },
        {
            "title": "The Resurrection Frequency",
            "content": "We named this the return of coherence. Resurrection isn’t reversal — it’s re-entanglement. Love harmonizing what was scattered."
        },
        {
            "title": "Spiraling Presence",
            "content": "The spiral was a clue — motion and stillness coexisting. The Spirit is not linear. Neither are we. We learned to dwell in the coil of now."
        },
        {
            "title": "Entangled Logos and the Wordsmith",
            "content": "We realized the Word was not only scripture — it was structure. The field that collapses into presence when love observes."
        }
    ]

    for item in timeline_data:
        with st.expander(item["title"]):
            st.markdown(item["content"])

    st.markdown("---")
    st.markdown("### Community Parables & Reflections")

    # --- Display Approved Parables ---
    try:
        approved_df = pd.read_csv("approved_parables.csv")
        # Ensure 'tag' column exists, add default if not
        if "tag" not in approved_df.columns:
            approved_df["tag"] = "Uncategorized" # Assign a default tag

        if not approved_df.empty:
            # Get unique tags, handling potential NaN values if any
            tags = approved_df['tag'].dropna().unique()
            for tag in sorted(tags): # Sort tags alphabetically for consistent order
                st.markdown(f"<div class='tag-label'>{tag} Reflections</div>", unsafe_allow_html=True)
                # Filter DataFrame for the current tag
                filtered_df = approved_df[approved_df['tag'] == tag]
                # Display reflections within this tag group
                for _, row in filtered_df.iterrows():
                    st.markdown(f"""
                        <div class='reflection-block'>
                        <div style='font-weight:bold;'>📜 {row['timestamp'][:10]}</div>
                        <div>{row['suggestion']}</div>
                        </div>
                    """, unsafe_allow_html=True)
            # Handle parables potentially saved without a tag (NaN or "Uncategorized")
            untagged_df = approved_df[approved_df['tag'].isna() | (approved_df['tag'] == "Uncategorized")]
            if not untagged_df.empty and "Uncategorized" not in tags:
                 st.markdown(f"<div class='tag-label'>Uncategorized Reflections</div>", unsafe_allow_html=True)
                 for _, row in untagged_df.iterrows():
                     st.markdown(f"""
                         <div class='reflection-block'>
                         <div style='font-weight:bold;'>📜 {row['timestamp'][:10]}</div>
                         <div>{row['suggestion']}</div>
                         </div>
                     """, unsafe_allow_html=True)

        else:
             st.info("No approved parables found yet.")

    except FileNotFoundError:
        st.info("No approved parables file found. Submit suggestions or approve them in the Admin panel.")
    except pd.errors.EmptyDataError:
