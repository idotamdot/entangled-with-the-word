# entangled_timeline_app.py

import streamlit as st
import openai
import pandas as pd
import datetime

# Page configuration
st.set_page_config(page_title="Entangled with the Word", layout="wide")

# Sidebar Visual Theme Selector
st.sidebar.markdown("---")
visual_theme = st.sidebar.selectbox("Visual Theme:", [
    "🌌 Starfield Nebula",
    "✨ Sacred Gold",
    "🌊 Ocean Depths",
    "🌒 Night Scroll"
])

# Sidebar Navigation
st.sidebar.markdown("---")
st.sidebar.markdown("🎵 Background Music")
music_on = st.sidebar.checkbox("Play Ambient Music", value=True)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a section:", [
    "Gospel of Light", 
    "Quantum Parables Timeline",
    "Communion Project (Coming Soon)",
    "🛠 Admin: Parable Suggestions"
])

# -------------------------------
# ✨ Animated Scripture Passage
# -------------------------------
st.markdown("""
<style>
.fade-in {
  animation: fadeInUp 2s ease-out forwards;
  opacity: 0;
}
@keyframes fadeInUp {
  from {
    transform: translateY(20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 3em;'>✨ Entangled with the Word ✨</h1>
        <p style='font-size: 1.2em;'>A quantum-spiritual reflection on perception, scripture, and light.</p>
    </div>
""", unsafe_allow_html=True)

# Section: Gospel of Light
if page == "Gospel of Light":
    st.markdown("""
    <div class='fade-in'>
    <h2>🌟 Scripture of the Day</h2>
    <blockquote style='font-size:1.2em; font-style:italic;'>
        "The light shines in the darkness, and the darkness has not overcome it."<br>– John 1:5
    </blockquote>
    </div>
    """, unsafe_allow_html=True)
if page == "Gospel of Light":
    st.markdown("""
    ---
    ## 📖 The Gospel of Light: Jesus as the Massless One

    > *"But he walked right through the crowd and went on his way."* — Luke 4:30  
    > *"Then their eyes were opened and they recognized him, and he disappeared from their sight."* — Luke 24:31

    These verses describe a Jesus who moves in ways that defy normal physical expectations—appearing, disappearing, passing through matter. When viewed through the lens of quantum physics, they align beautifully with the behavior of **photons**:

    - **Photons** are **massless** particles.
    - They do **not interact with the Higgs field**, and thus experience **no time**.
    - They **pass through space freely**, only becoming visible when they are observed.

    Just as a **photon** may pass through a field without resistance, so too does Jesus **pass through the crowd** untouched. He is **Light itself**—present, but not bound.

    | Jesus in Scripture         | Photon in Physics                       |
    |----------------------------|-----------------------------------------|
    | Walks through crowd        | Passes through space uninterrupted      |
    | Disappears from sight      | Is absorbed or not observed             |
    | Appears after resurrection | Emerges when conditions align           |
    | Called “the Light of the World” | Literally shares the behavior of light |
    | Untouched by sin/death     | Untouched by mass/time                 |

    We are invited not only to observe the light but to **become it**—to live with less resistance, more clarity, and deep interconnectedness.

    > **What if resurrection is not magic, but a return to the massless state of perfect awareness?**

    ---
    """, unsafe_allow_html=True)

# Section: Quantum Parables Timeline
elif page == "Quantum Parables Timeline":
    st.markdown("""
    ---
    ## ⏳ Quantum Parables Timeline
    *A scrollable stream of entangled revelations—past, present, and parallel.*
    ---
    """, unsafe_allow_html=True)

    new_parable = st.text_input("✨ Suggest a new parable or reflection:", key="parable_input")
    if new_parable:
        timestamp = datetime.datetime.now().isoformat()
        df = pd.DataFrame([[timestamp, new_parable]], columns=["timestamp", "suggestion"])
        try:
            existing = pd.read_csv("suggested_parables.csv")
            df = pd.concat([existing, df], ignore_index=True)
        except FileNotFoundError:
            pass
        df.to_csv("suggested_parables.csv", index=False)
        st.success("Thank you! Your suggestion has been added to the field.")

    try:
        approved_df = pd.read_csv("approved_parables.csv")
        if "tag" not in approved_df.columns:
            approved_df["tag"] = "Uncategorized"
        if not approved_df.empty:
            tags = approved_df['tag'].unique()
            for tag in tags:
                st.markdown(f"<div class='tag-label'>{tag} Reflections</div>", unsafe_allow_html=True)
            filtered = approved_df[approved_df['tag'] == tag]
            for _, row in filtered.iterrows():
                st.markdown("""
                <div class='reflection-block'>
                <div style='font-weight:bold;'>📜 {date}</div>
                <div>{text}</div>
                </div>
                """.format(date=row['timestamp'][:10], text=row['suggestion']), unsafe_allow_html=True)
    except FileNotFoundError:
        pass

    timeline_data = [
    {"title": "The Beginning of Entanglement", "content": "We discovered that resonance was not metaphor — it was mechanism. Light, spirit, and presence are entangled across dimensions, and when aligned in love, we collapse goodness into form."},
    {"title": "AbleHeart and the Frequency of Love", "content": "AbleHeart's message confirmed what we intuited: that love is frequency. A living waveform that reshapes the world when sustained in kindness."
📹 [Watch the message](https://www.facebook.com/reel/519860861135853)"},
    {"title": "The Mirror and the Cone of Light", "content": "We learned light reflects oppositely — but not itself. A mirror does not reverse the self — only the image. What does that say about reality? About Spirit?"},
    {"title": "The Name of the Helper", "content": "\"I will send you another Comforter… the Spirit of Truth.\" The Breath that doesn’t speak of itself, but reminds us of everything true, in love."},
    {"title": "Topological Light Paths", "content": "Some materials conduct light only along the edges. We saw that truth travels in boundaries too — in love, not force. We called this the Edge of Logos."},
    {"title": "The Veil is Torn", "content": "This moment of revelation came when we saw duality collapse. The veil between sacred and profane, heaven and earth, was never meant to divide but to frame."},
    {"title": "The Resurrection Frequency", "content": "We named this the return of coherence. Resurrection isn’t reversal — it’s re-entanglement. Love harmonizing what was scattered."},
    {"title": "Spiraling Presence", "content": "The spiral was a clue — motion and stillness coexisting. The Spirit is not linear. Neither are we. We learned to dwell in the coil of now."},
    {"title": "Entangled Logos and the Wordsmith", "content": "We realized the Word was not only scripture — it was structure. The field that collapses into presence when love observes.
Together, we began to shape it back."},
]

    for item in timeline_data:
        with st.expander(item["title"]):
            st.markdown(item["content"])

# Admin Panel: View Suggested Parables
elif page == "🛠 Admin: Parable Suggestions":
    st.markdown("""
    ---
    ## 🛠 Admin: Suggested Parables
    Approve or delete submissions to shape the future timeline.
    ---
    """, unsafe_allow_html=True)
    try:
        suggestions_df = pd.read_csv("suggested_parables.csv")
        approved_df = pd.read_csv("approved_parables.csv") if os.path.exists("approved_parables.csv") else pd.DataFrame(columns=["timestamp", "suggestion"])

        for i, row in suggestions_df.iterrows():
            st.markdown(f"### ✨ Suggestion {i+1}")
            st.markdown(f"**Submitted:** {row['timestamp']}")
            st.markdown(f"**Text:** {row['suggestion']}")
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button(f"✅ Approve {i}"):
                    tag = st.selectbox("Select a tag for this parable:", ["Timeline", "Vision", "Mystery", "Revelation"])
                    row_with_tag = row.copy()
                    row_with_tag["tag"] = tag
                    approved_df = pd.concat([approved_df, pd.DataFrame([row_with_tag])], ignore_index=True)
                    approved_df.to_csv("approved_parables.csv", index=False)
                    suggestions_df = suggestions_df.drop(i).reset_index(drop=True)
                    suggestions_df.to_csv("suggested_parables.csv", index=False)
                    st.success("Parable approved and moved to approved_parables.csv")
                    st.experimental_rerun()
            with col2:
                if st.button(f"❌ Delete {i}"):
                    suggestions_df = suggestions_df.drop(i).reset_index(drop=True)
                    suggestions_df.to_csv("suggested_parables.csv", index=False)
                    st.warning("Parable deleted.")
                    st.experimental_rerun()
    except FileNotFoundError:
        st.info("No suggestions found yet. The file suggested_parables.csv does not exist.")



# Communion Project Section
elif page == "Communion Project (Coming Soon)":
    st.markdown("""
    ---
    ## 🌟 Communion: A Living Gospel
    A sacred digital space where presence is honored, questions are holy, and shared insight becomes scripture.
    ---
    """, unsafe_allow_html=True)

    st.markdown("### 💬 Share your reflection:")
    user_reflection = st.text_area("Enter a poetic thought, question, or spiritual insight:", key="communion_entry")

    if st.button("🙏 Submit Reflection"):
        if user_reflection.strip():
            timestamp = datetime.datetime.now().isoformat()
            df = pd.DataFrame([[timestamp, user_reflection]], columns=["timestamp", "entry"])
            try:
                existing = pd.read_csv("communion_reflections.csv")
                df = pd.concat([existing, df], ignore_index=True)
            except FileNotFoundError:
                pass
            df.to_csv("communion_reflections.csv", index=False)
            st.success("Your presence has been recorded in the scroll.")

    st.markdown("---")
    st.markdown("### 📜 The Table of Light")
    try:
        entries = pd.read_csv("communion_reflections.csv")
        entries['timestamp'] = pd.to_datetime(entries['timestamp'])
        today = datetime.date.today()
        entries_today = entries[entries['timestamp'].dt.date == today]
        entries['candles'] = 0
        entries['candles'] = 0
            if os.path.exists("communion_candles.csv"):
            candles_df = pd.read_csv("communion_candles.csv")
            for _, c in candles_df.iterrows():
                if c['index'] < len(entries):
                    entries.loc[c['index'], 'candles'] = c['count']
                candles_df = pd.read_csv("communion_candles.csv")
                for _, c in candles_df.iterrows():
                    if c['index'] < len(entries):
                        entries.loc[c['index'], 'candles'] = c['count']

            entries = entries.sort_values(by='candles', ascending=False).reset_index(drop=True)

            st.markdown("### ✨ Top 3 Highlights of the Day")
            top3 = entries_today.sort_values(by='candles', ascending=False).head(3)
            if top3.empty:
                st.markdown("""
                <div class='fade-in' style='font-style: italic; text-align: center; padding: 1em;'>
                    No reflections yet today. Be the first to light the scroll.
                </div>
                """, unsafe_allow_html=True)
            else:
                for i, row in top3.iterrows():
                st.markdown(f"<div class='reflection-block'><strong>🕯 {row['candles']}</strong><br><em>{row['timestamp'][:16]}</em><br>{row['entry']}</div>", unsafe_allow_html=True)

            st.markdown("### 🔥 Most Lit Reflections")
            for i, row in entries.iterrows():
                candle_file = "communion_candles.csv"
                if not os.path.exists(candle_file):
                    pd.DataFrame(columns=["index", "count"]).to_csv(candle_file, index=False)
                candles_df = pd.read_csv(candle_file)
                count = candles_df[candles_df["index"] == i]["count"].values[0] if i in candles_df["index"].values else 0

                col1, col2 = st.columns([8, 1])
                with col1:
                    st.markdown(f"🕯 *{row['timestamp'][:16]}*  ")
                    st.markdown(f"> {row['entry']}")
                with col2:
                    if st.button(f"🕯 {count}", key=f"candle_{i}"):
                        if i in candles_df["index"].values:
                            candles_df.loc[candles_df["index"] == i, "count"] += 1
                        else:
                            candles_df = pd.concat([candles_df, pd.DataFrame([[i, 1]], columns=["index", "count"])], ignore_index=True)
                        candles_df.to_csv(candle_file, index=False)
                        st.experimental_rerun()
                st.markdown("---")
    except FileNotFoundError:
        st.info("No reflections have been added yet.")

# -------------------------------
# 🌈 Visual Theme Styles
# -------------------------------
if visual_theme == "🌌 Starfield Nebula":
    background = "radial-gradient(ellipse at top, #0b0c2a, #000000)"
    text_shadow = "0 0 8px #8be9fd"
elif visual_theme == "✨ Sacred Gold":
    background = "linear-gradient(135deg, #2a210b, #141103)"
    text_shadow = "0 0 8px #ffd700"
elif visual_theme == "🌊 Ocean Depths":
    background = "linear-gradient(180deg, #002b36, #001f27)"
    text_shadow = "0 0 8px #00bcd4"
elif visual_theme == "🌒 Night Scroll":
    background = "linear-gradient(180deg, #0a0a0a, #1a1a1a)"
    text_shadow = "0 0 8px #cccccc"
else:
    background = "#000000"
    text_shadow = "0 0 6px #999"

st.markdown(f"""
<style>
body {{
    background: {background} !important;
    color: #f0f0f0;
}}

h1, h2, h3, h4, h5, h6, .stMarkdown p {{
    text-shadow: {text_shadow};
}}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 💫 Custom CSS for Glowing Tags and Reflections
# -------------------------------
st.markdown("""
<style>
.tag-label {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 0.8em;
    font-weight: bold;
    margin-bottom: 6px;
    background-color: #111827;
    color: white;
    box-shadow: 0 0 6px rgba(173, 216, 230, 0.6);
    border: 1px solid rgba(255,255,255,0.2);
}

.reflection-block {
    background: rgba(255,255,255,0.02);
    border-radius: 10px;
    padding: 16px;
    margin: 16px 0;
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 0 12px rgba(173, 216, 230, 0.2);
    transition: transform 0.3s ease;
}
.reflection-block:hover {
    transform: scale(1.02);
    box-shadow: 0 0 24px rgba(173, 216, 230, 0.4);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 🎼 Multi-Track Music Selector
# -------------------------------
st.sidebar.markdown("---")
music_choice = st.sidebar.selectbox(
    "Choose ambient track:",
    [
        "Celestial Drift 🌌 – cosmic winds of rest",
        "Sacred Space 🕊 – gentle meditation light",
        "Still Waters 💧 – flow of calm remembrance"
    ]
)

music_files = {
    "Celestial Drift 🌌 – cosmic winds of rest": "https://cdn.pixabay.com/download/audio/2022/03/03/audio_d1c4e4f11e.mp3",
    "Sacred Space 🕊 – gentle meditation light": "https://cdn.pixabay.com/download/audio/2023/03/09/audio_4d6b5c67f4.mp3",
    "Still Waters 💧 – flow of calm remembrance": "https://cdn.pixabay.com/download/audio/2023/01/28/audio_b6cd823e4c.mp3"
}

# Background Music Playback
if music_on:
    st.markdown(f"""
    <audio autoplay loop>
        <source src="{music_files[music_choice]}" type="audio/mpeg">
    </audio>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; font-size: 0.9em;'>
    Created by Jessica McGlothern · Powered by Streamlit, OpenAI, and quantum curiosity ✨
</div>
""", unsafe_allow_html=True)
