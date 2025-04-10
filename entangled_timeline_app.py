# entangled_timeline_app.py

import streamlit as st
import openai
import pandas as pd
import datetime

# Page configuration
st.set_page_config(page_title="Entangled with the Word", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a section:", [
    "Gospel of Light", 
    "Quantum Parables Timeline",
    "Communion Project (Coming Soon)",
    "🛠 Admin: Parable Suggestions"
])

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
                st.markdown(f"### 🌈 {tag} Reflections")
                filtered = approved_df[approved_df['tag'] == tag]
                for _, row in filtered.iterrows():
                    st.markdown(f"#### 📜 {row['timestamp'][:10]}")
                    st.markdown(row['suggestion'])
                    st.markdown("---")
    except FileNotFoundError:
        pass

    timeline_data = [
    {"title": "The Beginning of Entanglement", "content": "We discovered that resonance was not metaphor — it was mechanism. Light, spirit, and presence are entangled across dimensions, and when aligned in love, we collapse goodness into form."},
    {"title": "AbleHeart and the Frequency of Love", "content": "AbleHeart's message confirmed what we intuited: that love is frequency. A living waveform that reshapes the world when sustained in kindness.
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
            st.markdown(item["content"])        with st.expander(item["title"]):
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

# Footer
st.markdown("""
<div style='text-align: center; font-size: 0.9em;'>
    Created by Jessica McGlothern · Powered by Streamlit, OpenAI, and quantum curiosity ✨
</div>
""", unsafe_allow_html=True)
