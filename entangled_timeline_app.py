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


#--------------------------------
# Header
#--------------------------------
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 3em;'>✨ Entangled with the Word ✨</h1>
        <p style='font-size: 1.2em;'>A quantum-spiritual reflection on perception, scripture, and light.</p>
    </div>
""", unsafe_allow_html=True)


#---------------------------------
# Inject custom CSS
#---------------------------------
st.markdown("""
    <style>
    /* ✨ Custom Expander Box Style */
    div.streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.05);
        color: #f0f0f0;
        font-size: 1.2rem;
        border: 1px solid #ffffff20;
        border-radius: 12px;
        padding: 10px;
        box-shadow: 0 0 15px rgba(173, 216, 230, 0.4);
        backdrop-filter: blur(6px);
    }

    details[open] > summary {
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.3) !important;
    }

    /* 🌌 Starry Background */
    body::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url("https://i.ibb.co/0j1yZ9k/stars-bg.gif") repeat;
        background-size: cover;
        opacity: 0.1;
        z-index: -1;
        pointer-events: none;
    }
    </style>
""", unsafe_allow_html=True)


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
        st.info("The approved parables file is empty.")
    except Exception as e:
        st.error(f"An error occurred loading approved parables: {e}")


    # --- Suggest New Parable ---
    st.markdown("---")
    with st.form("parable_suggestion_form", clear_on_submit=True):
        new_parable = st.text_input("✨ Suggest a new parable or reflection:", key="parable_input")
        submitted = st.form_submit_button("Suggest Parable")
        if submitted and new_parable:
            timestamp = datetime.datetime.now().isoformat()
            new_data = pd.DataFrame([[timestamp, new_parable]], columns=["timestamp", "suggestion"])
            try:
                # Use 'a' mode and header=False if file exists, otherwise write with header
                if os.path.exists("suggested_parables.csv"):
                    new_data.to_csv("suggested_parables.csv", mode='a', header=False, index=False)
                else:
                    new_data.to_csv("suggested_parables.csv", index=False)
                st.success("Thank you! Your suggestion has been added to the field for review.")
            except Exception as e:
                st.error(f"Failed to save suggestion: {e}")

# -------------------------------
# Communion Project Section (Integrated Code)
# -------------------------------
elif page == "Communion Project": # Matched updated name
    st.markdown("""
    ---
    ## 🌟 Communion: A Living Gospel
    A sacred digital space where presence is honored, questions are holy, and shared insight becomes scripture.
    ---
    """, unsafe_allow_html=True)

    # --- Submit Reflection ---
    st.markdown("### 💬 Share your reflection:")
    with st.form("communion_form", clear_on_submit=True):
        user_reflection = st.text_area("Enter a poetic thought, question, or spiritual insight:", key="communion_entry")
        submit_reflection = st.form_submit_button("🙏 Submit Reflection")

        if submit_reflection and user_reflection.strip():
            timestamp = datetime.datetime.now().isoformat()
            df_new = pd.DataFrame([[timestamp, user_reflection]], columns=["timestamp", "entry"])
            try:
                 # Use 'a' mode and header=False if file exists, otherwise write with header
                if os.path.exists("communion_reflections.csv"):
                    df_new.to_csv("communion_reflections.csv", mode='a', header=False, index=False)
                else:
                    df_new.to_csv("communion_reflections.csv", index=False)
                st.success("Your presence has been recorded in the scroll.")
                # No rerun needed here, form clears and success message shows. Data loads below.
            except Exception as e:
                 st.error(f"Error saving reflection: {e}")

    st.markdown("---")
    st.markdown("### 📜 The Table of Light")

    # --- Display Reflections & Candles ---
    communion_file = "communion_reflections.csv"
    candle_file = "communion_candles.csv"

    try:
        # Load reflections
        entries = pd.read_csv(communion_file)
        entries['timestamp'] = pd.to_datetime(entries['timestamp'])
        # IMPORTANT: Reset index AFTER loading to ensure indices match row numbers (0, 1, 2...)
        # This is crucial if the CSV wasn't saved with a standard index.
        entries = entries.reset_index(drop=True)
        entries['id'] = entries.index # Use index as a temporary ID for candle association

        # Load candle counts
        if os.path.exists(candle_file):
            try:
                candles_df = pd.read_csv(candle_file)
                # Ensure columns are correct type
                candles_df['entry_index'] = candles_df['entry_index'].astype(int)
                candles_df['count'] = candles_df['count'].astype(int)
            except (FileNotFoundError, pd.errors.EmptyDataError):
                candles_df = pd.DataFrame(columns=["entry_index", "count"])
            except Exception as e:
                 st.warning(f"Could not load candle data: {e}")
                 candles_df = pd.DataFrame(columns=["entry_index", "count"])
        else:
            candles_df = pd.DataFrame(columns=["entry_index", "count"])

        # Merge candle counts into entries DataFrame
        # Convert candles_df index column name for clarity
        candles_df = candles_df.rename(columns={'entry_index': 'id'})
        entries = pd.merge(entries, candles_df, on='id', how='left')
        entries['count'] = entries['count'].fillna(0).astype(int) # Fill NaN for entries with no candles yet

        # --- Highlights of the Day ---
        st.markdown("### ✨ Top 3 Highlights of the Day")
        today = datetime.date.today()
        entries_today = entries[entries['timestamp'].dt.date == today].copy() # Use .copy() to avoid SettingWithCopyWarning
        # Sort today's entries by candle count
        entries_today = entries_today.sort_values(by='count', ascending=False)
        top3 = entries_today.head(3)

        if top3.empty:
            st.markdown("""
                <div class='fade-in' style='font-style: italic; text-align: center; padding: 1em;'>
                    No reflections yet today. Be the first to light the scroll.
                </div>
            """, unsafe_allow_html=True)
        else:
            for _, row in top3.iterrows():
                 # Display with timestamp, candle count, and entry text
                 st.markdown(f"""
                     <div class='reflection-block'>
                     <strong>🕯️ {row['count']}</strong> | <em>{row['timestamp'].strftime('%Y-%m-%d %H:%M')}</em><br>
                     {row['entry']}
                     </div>
                 """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 🔥 All Reflections (Sorted by Light)")

        # Sort all entries by candle count for the main display
        entries_sorted = entries.sort_values(by='count', ascending=False)

        if entries_sorted.empty:
            st.info("No reflections have been added yet.")
        else:
            # Iterate through sorted entries to display them
            for i, row in entries_sorted.iterrows():
                entry_index = row['id'] # Get the original index (now stored in 'id')
                count = row['count']

                col1, col2 = st.columns([8, 1])
                with col1:
                    st.markdown(f"🕯️ *{row['timestamp'].strftime('%Y-%m-%d %H:%M')}*")
                    st.markdown(f"> {row['entry']}")
                with col2:
                    # Use the original index (entry_index) for the button key and data update
                    if st.button(f"🕯️ {count}", key=f"candle_{entry_index}"):
                        # Update the count in the candles_df
                        if entry_index in candles_df["id"].values:
                             candles_df.loc[candles_df["id"] == entry_index, "count"] += 1
                        else:
                            # Add new entry to candles_df if it wasn't there
                            new_candle_row = pd.DataFrame([[entry_index, 1]], columns=["id", "count"])
                            candles_df = pd.concat([candles_df, new_candle_row], ignore_index=True)

                        # Save the updated candle counts
                        try:
                            # Save back with the correct column name
                            candles_df.rename(columns={'id': 'entry_index'}).to_csv(candle_file, index=False)
                            st.rerun() # Rerun to update the display with the new count
                        except Exception as e:
                            st.error(f"Failed to save candle count: {e}")
                st.markdown("---") # Separator between entries

    except FileNotFoundError:
        st.info("No reflections file (communion_reflections.csv) found yet. Submit one above!")
    except pd.errors.EmptyDataError:
         st.info("The reflections file is empty.")
    except Exception as e:
        st.error(f"An error occurred loading communion reflections: {e}")
        st.error("Please ensure 'communion_reflections.csv' and 'communion_candles.csv' are formatted correctly.")


# -------------------------------
# Admin Panel: View Suggested Parables
# -------------------------------
elif page == "🛠 Admin: Parable Suggestions":
    st.markdown("""
    ---
    ## 🛠 Admin: Suggested Parables
    Approve or delete submissions to shape the future timeline.
    ---
    """, unsafe_allow_html=True)

    suggestions_file = "suggested_parables.csv"
    approved_file = "approved_parables.csv"

    try:
        # Load suggestions
        suggestions_df = pd.read_csv(suggestions_file)

        # Load approved or create empty DataFrame if not exists
        if os.path.exists(approved_file):
            try:
                 approved_df = pd.read_csv(approved_file)
                 # Ensure required columns exist in approved_df
                 if "timestamp" not in approved_df.columns: approved_df["timestamp"] = None
                 if "suggestion" not in approved_df.columns: approved_df["suggestion"] = None
                 if "tag" not in approved_df.columns: approved_df["tag"] = None

            except pd.errors.EmptyDataError:
                 approved_df = pd.DataFrame(columns=["timestamp", "suggestion", "tag"])
            except Exception as e:
                 st.error(f"Error loading {approved_file}: {e}")
                 st.stop() # Stop if approved file is corrupt
        else:
            approved_df = pd.DataFrame(columns=["timestamp", "suggestion", "tag"])

        if suggestions_df.empty:
            st.info("No suggestions pending approval.")
        else:
             st.info(f"Found {len(suggestions_df)} suggestion(s) for review.")
             # Display suggestions one by one
             for i, row in suggestions_df.iterrows():
                 st.markdown("---")
                 st.markdown(f"### ✨ Suggestion #{i+1}")
                 st.markdown(f"**Submitted:** {row['timestamp']}")
                 st.markdown(f"**Text:**")
                 st.markdown(f"> {row['suggestion']}") # Blockquote suggestion text

                 col1, col2, col3 = st.columns([2, 1, 1]) # Make space for tag selector

                 with col1:
                      # CORRECTED LOGIC: Selectbox appears BEFORE the button
                      tag_options = ["Timeline", "Vision", "Mystery", "Revelation", "Uncategorized"]
                      # Default tag can be the first option or "Uncategorized"
                      selected_tag = st.selectbox(
                          "Assign a tag:",
                          options=tag_options,
                          index=tag_options.index("Uncategorized"), # Default selection
                          key=f"tag_{i}" # Unique key for each selectbox
                      )

                 with col2:
                      # Approve Button
                      if st.button(f"✅ Approve #{i+1}", key=f"approve_{i}"):
                          # Prepare the row to be added to approved_df
                          row_to_approve = row.copy()
                          row_to_approve["tag"] = selected_tag # Use the selected tag

                          # Append to approved DataFrame (ensure columns match)
                          approved_df = pd.concat([approved_df, pd.DataFrame([row_to_approve])], ignore_index=True)

                          # Remove from suggestions DataFrame
                          suggestions_df = suggestions_df.drop(i) # Keep original index for now

                          # Save both files
                          try:
                              approved_df.to_csv(approved_file, index=False)
                              # If suggestions is empty, save empty file, else save remaining
                              if suggestions_df.empty:
                                  # Create an empty file or overwrite with header only
                                  pd.DataFrame(columns=suggestions_df.columns).to_csv(suggestions_file, index=False)
                              else:
                                  suggestions_df.to_csv(suggestions_file, index=False)

                              st.success(f"Suggestion #{i+1} approved with tag '{selected_tag}'!")
                              st.rerun() # Use st.rerun()
                          except Exception as e:
                              st.error(f"Error saving files after approval: {e}")


                 with col3:
                      # Delete Button
                      if st.button(f"❌ Delete #{i+1}", key=f"delete_{i}"):
                          # Remove from suggestions DataFrame
                          suggestions_df = suggestions_df.drop(i) # Drop by index

                           # Save the updated suggestions file
                          try:
                               # If suggestions is empty, save empty file, else save remaining
                              if suggestions_df.empty:
                                  pd.DataFrame(columns=suggestions_df.columns).to_csv(suggestions_file, index=False)
                              else:
                                  suggestions_df.to_csv(suggestions_file, index=False)

                              st.warning(f"Suggestion #{i+1} deleted.")
                              st.rerun() # Use st.rerun()
                          except Exception as e:
                              st.error(f"Error saving {suggestions_file} after deletion: {e}")


    except FileNotFoundError:
        st.info(f"No suggestions file ({suggestions_file}) found yet.")
    except pd.errors.EmptyDataError:
         st.info("The suggestions file is currently empty.")
    except Exception as e:
        st.error(f"An error occurred loading suggestions: {e}")


# -------------------------------
# 🌈 Visual Theme Styles Application
# -------------------------------
# Define defaults first
background = "#000000" # Default background
text_shadow = "0 0 6px #999" # Default shadow

if visual_theme == "🌌 Starfield Nebula":
    background = "radial-gradient(ellipse at top, #0b0c2a, #000000)"
    text_shadow = "0 0 8px #8be9fd" # Light blue glow

elif visual_theme == "✨ Sacred Gold":
    background = "linear-gradient(135deg, #2a210b, #141103)" # Dark gold/brown gradient
    text_shadow = "0 0 8px #ffd700" # Gold glow

elif visual_theme == "🌊 Ocean Depths":
    background = "linear-gradient(180deg, #002b36, #001f27)" # Dark teal gradient
    text_shadow = "0 0 8px #26a69a" # Teal glow (adjusted from cyan)

elif visual_theme == "🌒 Night Scroll":
    background = "linear-gradient(180deg, #1a1a1a, #0a0a0a)" # Dark grey gradient
    text_shadow = "0 0 8px #cccccc" # White/light grey glow

# Apply the selected styles using CSS
st.markdown(f"""
<style>
/* Apply to the main app container for better compatibility */
.stApp {{
    background: {background};
    color: #f0f0f0; /* Base text color */
}}

/* Target headers and paragraphs more specifically */
h1, h2, h3, h4, h5, h6, .stMarkdown p, blockquote, .stTextInput > div > div > input, .stTextArea > label, .stTextArea > div > textarea {{
    text-shadow: {text_shadow};
    color: #f0f0f0; /* Ensure text color is consistent */
}}

/* Ensure buttons and other elements inherit or have appropriate contrast */
.stButton > button {{
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 0 6px rgba(173, 216, 230, 0.4); /* Example shadow */
}}
.stRadio > label, .stSelectbox > label, .stCheckbox > label {{
     text-shadow: {text_shadow}; /* Apply shadow to labels */
}}

/* Style Streamlit's expander header */
.stExpander > div > details > summary {{
     text-shadow: {text_shadow};
}}

</style>
""", unsafe_allow_html=True)


# -------------------------------
# 💫 Custom CSS for Glowing Tags and Reflections (Loaded via style.css or here)
# -------------------------------
# This section assumes styles are either in style.css OR defined here.
# If style.css contains these, this block can be simplified or removed.
st.markdown("""
<style>
/* Tag Styles */
.tag-label {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 16px;
    font-size: 0.85em;
    font-weight: bold;
    margin-bottom: 8px;
    margin-right: 6px;
    background-color: #111827; /* Dark blue-grey */
    color: #ffffff;
    box-shadow: 0 0 8px rgba(173, 216, 230, 0.7); /* Light blue glow */
    border: 1px solid rgba(255,255,255,0.2);
    transition: all 0.3s ease;
}
.tag-label:hover {
    background-color: #1f2937; /* Slightly lighter blue-grey */
    box-shadow: 0 0 12px rgba(173, 216, 230, 0.9); /* Brighter glow on hover */
}

/* Reflection Block */
.reflection-block {
    background: rgba(255,255,255,0.03); /* Very subtle background */
    border-radius: 12px;
    padding: 18px;
    margin: 20px 0;
    border: 1px solid rgba(255,255,255,0.07); /* Faint border */
    box-shadow: 0 0 12px rgba(173, 216, 230, 0.3); /* Subtle glow */
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.reflection-block:hover {
    transform: scale(1.015); /* Slight scale up on hover */
    box-shadow: 0 0 24px rgba(173, 216, 230, 0.5); /* More prominent glow */
}

/* Optional scroll glow for entire page */
body::-webkit-scrollbar {
     width: 8px;
}
body::-webkit-scrollbar-track {
     background: rgba(0, 0, 0, 0.1);
}
body::-webkit-scrollbar-thumb {
    background-color: rgba(173, 216, 230, 0.3); /* Scrollbar color matches glow */
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 10px rgba(173, 216, 230, 0.4); /* Glow on scrollbar */
}
</style>
""", unsafe_allow_html=True)


# -------------------------------
# 🎼 Multi-Track Music Selector
# -------------------------------
# Define music files dictionary (ensure URLs are valid and accessible)
music_files = {
    "Celestial Drift 🌌 – cosmic winds of rest": "https://cdn.pixabay.com/download/audio/2022/03/03/audio_d1c4e4f11e.mp3",
    "Sacred Space 🕊 – gentle meditation light": "https://cdn.pixabay.com/download/audio/2023/03/09/audio_4d6b5c67f4.mp3",
    "Still Waters 💧 – flow of calm remembrance": "https://cdn.pixabay.com/download/audio/2023/01/28/audio_b6cd823e4c.mp3"
}

# Display music selector only if there are tracks defined
if music_files:
    st.sidebar.markdown("---")
    music_choice = st.sidebar.selectbox(
        "🎼 Choose ambient track:",
        options=list(music_files.keys()) # Use keys from the dictionary as options
    )

    # -------------------------------
    # 🔊 Background Music Playback
    # -------------------------------
    if music_on and music_choice in music_files:
        # Ensure the selected choice is valid before trying to play
        audio_url = music_files[music_choice]
        st.markdown(f"""
        <audio id="background-audio" autoplay loop>
            <source src="{audio_url}" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        <script>
          // Optional: Control volume (e.g., set to 50%)
          var audio = document.getElementById("background-audio");
          audio.volume = 0.5;
        </script>
        """, unsafe_allow_html=True)
    elif music_on:
        st.sidebar.warning("Selected music track not found.")

 
#-------------------------------
# Footer
# -------------------------------
st.markdown(
    """
    <style>
    .footer {
        text-align: center;
        font-size: 0.9em;
        margin-top: 50px; /* Increased margin */
        padding-bottom: 20px; /* Add padding at the bottom */
        color: #bbb; /* Slightly lighter grey */
        text-shadow: 0 0 6px rgba(173, 216, 230, 0.5);
    }
    </style>
    <div class="footer">
        Created with curiosity · Powered by Streamlit & Python ✨
    </div>
    """,
    unsafe_allow_html=True,
)

# Optional: Fixed position footer (if you want a separate one)
# st.markdown(
#     """
#     <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #f0f2f6; color: gray; text-align: center; padding: 5px;">
#         Created with curiosity · Powered by Streamlit & Python ✨ (Fixed)
#     </div>
#     """,
#     unsafe_allow_html=True,
# )
