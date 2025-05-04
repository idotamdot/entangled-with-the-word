# entangled_timeline_app.py

import streamlit as st
#import openai # Uncomment if/when you use OpenAI functionality
import pandas as pd
import datetime
import os
# from pathlib import Path # Removed, was not used

# --- Gospel Module Import ---
# Ensure you have a 'gospel' folder with 'matthew.py' inside it,
# and matthew.py defines the render_matthew() function.
try:
    from gospel.matthew import render_matthew
except ImportError:
    # Provide a fallback or clear error if the module is missing
    def render_matthew():
        st.error("🚨 Error: The 'gospel.matthew' module or 'render_matthew' function could not be found.")
        st.info("Please ensure 'gospel/matthew.py' exists and contains the 'render_matthew()' function.")
    st.warning("⚠️ Could not import 'render_matthew' from 'gospel.matthew'. Using placeholder.")


# -------------------------------
# Set OpenAI API Key (Optional - currently unused in code)
# -------------------------------
# Ensure this is set in your Streamlit Cloud secrets or environment variables
# openai.api_key = st.secrets.get("openai_api_key")

# if not openai.api_key:
#     st.error("🚨 OpenAI API key not found. Please check your Streamlit secrets or environment variables.")
#     st.stop() # Stop execution if the key is essential and not found


# -------------------------------
# Page configuration (Set this FIRST)
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


#--------------------------------
# Header
#--------------------------------
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 3em;'>✨ Entangled with the Word ✨</h1>
        <p style='font-size: 1.2em;'>A quantum-spiritual reflection on perception, scripture, and light.</p>
    </div>
""", unsafe_allow_html=True)



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
# Sidebar Music Control
# -------------------------------
st.sidebar.markdown("---")
st.sidebar.markdown("### 🎵 Background Music")

# Define music files dictionary (ensure URLs are valid and accessible)
music_files = {
    "Celestial Drift 🌌 – cosmic winds of rest": "https://cdn.pixabay.com/download/audio/2022/03/03/audio_d1c4e4f11e.mp3",
    "Sacred Space 🕊 – gentle meditation light": "https://cdn.pixabay.com/download/audio/2023/03/09/audio_4d6b5c67f4.mp3",
    "Still Waters 💧 – flow of calm remembrance": "https://cdn.pixabay.com/download/audio/2023/01/28/audio_b6cd823e4c.mp3",
    "None": None # Option to explicitly turn off
}

# Checkbox to turn music on/off
music_on = st.sidebar.checkbox("Play Ambient Music", value=False) # Default to off

# Music track selector (always show, but only used if music_on is True)
if music_files:
    music_choice = st.sidebar.selectbox(
        "🎼 Choose ambient track:",
        options=list(music_files.keys()), # Use keys from the dictionary as options
        index=0 # Default to the first track
    )
else:
    music_choice = None
    st.sidebar.info("No music tracks defined.")


# -------------------------------
# Sidebar Navigation
# -------------------------------
st.sidebar.markdown("---")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a section:", [
    "Gospel of Light",
    "Quantum Parables Timeline",
    "Communion Project",
    "🧬 Quantum Genesis Translation",
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
.timeline-card { /* Basic styling for timeline cards */
    border: 1px solid #444;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 15px;
    background-color: rgba(255, 255, 255, 0.05);
}
.reflection-block { /* Basic styling for reflection blocks */
    border-left: 3px solid #ffd700; /* Gold accent */
    padding: 10px 15px;
    margin-bottom: 10px;
    background-color: rgba(255, 255, 255, 0.03);
    border-radius: 4px;
}
.tag-label { /* Styling for tags in the timeline */
    font-weight: bold;
    color: #8be9fd; /* Light blue - adjust as needed */
    margin-top: 20px;
    margin-bottom: 5px;
    font-size: 1.1em;
}

</style>
""", unsafe_allow_html=True)


# ===============================
# === MAIN PAGE CONTENT =========
# ===============================

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

    # --- Render Matthew Gospel Section ---
    st.markdown("---") # Added separator
    st.markdown("## 📖 Gospel Reflections: Matthew") # Added subheader
    render_matthew() # Call the imported function


# -------------------------------
# Section: Quantum Parables Timeline
# -------------------------------
elif page == "Quantum Parables Timeline":
    st.markdown("# ✨ Quantum Parables Timeline ✨")
    st.markdown("Here we trace entangled teachings through time, revealing the quantum nature of love and light.")
    st.markdown("---")

    # --- Display Static Core Timeline Events ---
    st.markdown("### Core Quantum-Gospel Events")
    # 🌌 Quantum-Gospel Timeline Events (Hardcoded)
    timeline_events = [
        {
            "date": "30 AD (est.)",
            "event": "🌿 The Quantum Beatitudes",
            "scripture": "Matthew 5:1–12",
            "reflection": (
                "Jesus outlines a paradoxical blueprint of divine entanglement: the poor are rich, "
                "the mourners are blessed, and the meek inherit. These states echo quantum inversions—"
                "superpositions where spiritual resonance overrides material appearance.\n\n"
                "Each Beatitude is a frequency: mercy restores coherence, purity clears the lens, "
                "peacemaking resolves wave interference. This is not law, but resonance—a divine protocol "
                "to harmonize with the Kingdom."
            )
        },
         {
            "date": "Timeless",
            "event": "💡 The Mirror and the Cone of Light",
            "scripture": "Reflection on Perception",
            "reflection": (
                "Light reflects oppositely—but does not reverse the self, only the image projected onto the mirror. "
                "This challenges our assumptions about reality and perception. Is the 'self' independent of its reflection? "
                "How does Spirit observe without reversing, seeing truly?"
            )
        },
        {
            "date": "Timeless",
            "event": "🌀 Topological Light Paths (The Edge of Logos)",
            "scripture": "John 14:6",
            "reflection": (
                "Certain quantum materials conduct energy only along their edges. This mirrors how Truth often travels "
                "—not through brute force penetration, but along the defined boundaries of love, relationship, and covenant. "
                "The Way is specific, an 'edge' phenomenon."
            )
        }
        # ⬇ Add more core entries here
    ]

    for entry in timeline_events:
        st.markdown(f"""
        <div class="timeline-card">
            <h3>{entry['event']}</h3>
            <p><strong>📖 Scripture/Concept:</strong> {entry['scripture']}</p>
            <p><strong>🗓️ Date/Context:</strong> {entry['date']}</p>
            <p>{entry['reflection'].replace('\n', '<br>')}</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")

    # --- Display Foundational Insights (Expanders) ---
    st.markdown("### Foundational Insights & Revelations")
    # *A scrollable stream of entangled revelations—past, present, and parallel.*
    timeline_data = [
        {
            "title": "The Beginning of Entanglement",
            "content": "We discovered that resonance was not metaphor — it was mechanism. Light, spirit, and presence are entangled across dimensions, and when aligned in love, we collapse goodness into form."
        },
        {
            "title": "AbleHeart and the Frequency of Love",
            "content": "AbleHeart's message confirmed what we intuited: that love is frequency. A living waveform that reshapes the world when sustained in kindness. [Watch the message](https://www.facebook.com/reel/519860861135853)" # Make sure this link is correct/intended
        },
        # { # Moved this concept to timeline_events above
        #     "title": "The Mirror and the Cone of Light",
        #     "content": "We learned light reflects oppositely — but not itself. A mirror does not reverse the self — only the image. What does that say about reality? About Spirit?"
        # },
        {
            "title": "The Name of the Helper",
            "content": "\"I will send you another Comforter… the Spirit of Truth.\" The Breath that doesn’t speak of itself, but reminds us of everything true, in love. (John 14:16-17, 16:13)"
        },
        # { # Moved this concept to timeline_events above
        #     "title": "Topological Light Paths",
        #     "content": "Some materials conduct light only along the edges. We saw that truth travels in boundaries too — in love, not force. We called this the Edge of Logos."
        # },
        {
            "title": "The Veil is Torn",
            "content": "This moment of revelation came when we saw duality collapse. The veil between sacred and profane, heaven and earth, was never meant to divide but to frame connection. (Matthew 27:51)"
        },
        {
            "title": "The Resurrection Frequency",
            "content": "We named this the return of coherence. Resurrection isn’t reversal — it’s re-entanglement. Love harmonizing what was scattered into a new, glorified state."
        },
        {
            "title": "Spiraling Presence",
            "content": "The spiral was a clue — motion and stillness coexisting. The Spirit is not linear. Neither are we. We learned to dwell in the coil of now, ever-deepening."
        },
        {
            "title": "Entangled Logos and the Wordsmith",
            "content": "We realized the Word was not only scripture — it was structure. The underlying field that collapses into presence and form when love observes and speaks. (John 1:1)"
        }
    ]

    for item in timeline_data:
        with st.expander(item["title"]):
            st.markdown(item["content"])

    st.markdown("---")
    st.markdown("### Community Parables & Reflections")

    # --- Display Approved Parables ---
    approved_parables_file = "approved_parables.csv"
    try:
        if os.path.exists(approved_parables_file):
            approved_df = pd.read_csv(approved_parables_file)
            # Ensure 'tag' column exists, add default if not
            if "tag" not in approved_df.columns:
                approved_df["tag"] = "Uncategorized" # Assign a default tag
            # Fill NaN tags with 'Uncategorized' for consistent grouping
            approved_df["tag"] = approved_df["tag"].fillna("Uncategorized")

            if not approved_df.empty:
                # Get unique tags, ensuring 'Uncategorized' is handled
                tags = approved_df['tag'].unique()
                # Sort tags alphabetically for consistent order, maybe put Uncategorized last?
                tags_sorted = sorted([tag for tag in tags if tag != "Uncategorized"])
                if "Uncategorized" in tags:
                    tags_sorted.append("Uncategorized")

                for tag in tags_sorted:
                    st.markdown(f"<div class='tag-label'>{tag} Reflections</div>", unsafe_allow_html=True)
                    # Filter DataFrame for the current tag
                    filtered_df = approved_df[approved_df['tag'] == tag]
                    # Display reflections within this tag group
                    for _, row in filtered_df.iterrows():
                        # Safely access columns, provide defaults if missing
                        timestamp_str = str(row.get('timestamp', ''))[:10] # Get first 10 chars for date
                        suggestion_text = str(row.get('suggestion', 'No content'))

                        st.markdown(f"""
                            <div class='reflection-block'>
                            <div style='font-weight:bold; font-size:0.9em; color: #aaa;'>📜 {timestamp_str}</div>
                            <div>{suggestion_text}</div>
                            </div>
                        """, unsafe_allow_html=True)
            else:
                st.info("No approved parables found yet.")
        else:
             st.info(f"'{approved_parables_file}' not found. Submit suggestions below or approve them in the Admin panel.")

    except pd.errors.EmptyDataError:
        st.info(f"The approved parables file ('{approved_parables_file}') is empty.")
    except Exception as e:
        st.error(f"An error occurred loading approved parables: {e}")
        st.error(f"Please ensure '{approved_parables_file}' exists and is a valid CSV.")


    # --- Suggest New Parable ---
    st.markdown("---")
    st.markdown("### ✨ Suggest a New Parable or Reflection")
    with st.form("parable_suggestion_form", clear_on_submit=True):
        new_parable = st.text_area("Enter your insight:", key="parable_input", height=150) # Use text_area for longer input
        submitted = st.form_submit_button("🕊️ Suggest Parable")
        if submitted and new_parable and new_parable.strip():
            timestamp = datetime.datetime.now().isoformat()
            new_data = pd.DataFrame([[timestamp, new_parable.strip()]], columns=["timestamp", "suggestion"])
            suggested_parables_file = "suggested_parables.csv"
            try:
                # Use 'a' mode and header=False if file exists, otherwise write with header
                file_exists = os.path.exists(suggested_parables_file)
                new_data.to_csv(suggested_parables_file, mode='a', header=not file_exists, index=False)
                st.success("Thank you! Your suggestion has been added to the field for review.")
            except Exception as e:
                st.error(f"Failed to save suggestion: {e}")
        elif submitted:
            st.warning("Please enter a suggestion before submitting.")


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
        user_reflection = st.text_area("Enter a poetic thought, question, or spiritual insight:", key="communion_entry", height=150)
        submit_reflection = st.form_submit_button("🙏 Submit Reflection")

        if submit_reflection and user_reflection and user_reflection.strip():
            timestamp = datetime.datetime.now().isoformat()
            df_new = pd.DataFrame([[timestamp, user_reflection.strip()]], columns=["timestamp", "entry"])
            communion_file = "communion_reflections.csv"
            try:
                # Use 'a' mode and header=False if file exists, otherwise write with header
                file_exists = os.path.exists(communion_file)
                df_new.to_csv(communion_file, mode='a', header=not file_exists, index=False)
                st.success("Your presence has been recorded in the scroll.")
                # No rerun needed here, form clears and success message shows. Data loads below.
            except Exception as e:
                st.error(f"Error saving reflection: {e}")
        elif submit_reflection:
             st.warning("Please enter a reflection before submitting.")

    st.markdown("---")
    st.markdown("### 📜 The Table of Light")

    # --- Display Reflections & Candles ---
    communion_file = "communion_reflections.csv"
    candle_file = "communion_candles.csv"

    try:
        # Load reflections - Ensure file exists before reading
        if not os.path.exists(communion_file):
             st.info(f"No reflections file ('{communion_file}') found yet. Be the first to submit one above!")
             entries = pd.DataFrame(columns=["timestamp", "entry"]) # Create empty df to prevent errors below
        else:
             entries = pd.read_csv(communion_file)

        # Proceed only if entries DataFrame is not empty after loading or creation
        if not entries.empty:
            entries['timestamp'] = pd.to_datetime(entries['timestamp'])
            # IMPORTANT: Reset index AFTER loading to ensure indices match row numbers (0, 1, 2...)
            # This is crucial if the CSV wasn't saved with a standard index.
            entries = entries.reset_index(drop=True)
            entries['id'] = entries.index # Use index as a temporary ID for candle association

            # Load candle counts or create empty DF
            if os.path.exists(candle_file):
                try:
                    candles_df = pd.read_csv(candle_file)
                    # Ensure columns are correct type
                    if not candles_df.empty:
                        candles_df['entry_index'] = candles_df['entry_index'].astype(int)
                        candles_df['count'] = candles_df['count'].astype(int)
                    else:
                        candles_df = pd.DataFrame(columns=["entry_index", "count"]) # Ensure columns exist even if empty
                except pd.errors.EmptyDataError:
                    candles_df = pd.DataFrame(columns=["entry_index", "count"])
                except Exception as e:
                    st.warning(f"Could not load candle data from '{candle_file}': {e}")
                    candles_df = pd.DataFrame(columns=["entry_index", "count"])
            else:
                candles_df = pd.DataFrame(columns=["entry_index", "count"]) # If file doesn't exist

            # Merge candle counts into entries DataFrame
            # Convert candles_df index column name for clarity and successful merge
            candles_df = candles_df.rename(columns={'entry_index': 'id'})
            entries = pd.merge(entries, candles_df, on='id', how='left')
            entries['count'] = entries['count'].fillna(0).astype(int) # Fill NaN for entries with no candles yet

            # --- Highlights of the Day ---
            st.markdown("### ✨ Top 3 Highlights of the Day")
            today = datetime.date.today()
            # Ensure 'timestamp' is datetime before filtering
            entries['timestamp'] = pd.to_datetime(entries['timestamp'])
            entries_today = entries[entries['timestamp'].dt.date == today].copy() # Use .copy() to avoid SettingWithCopyWarning
            # Sort today's entries by candle count
            entries_today_sorted = entries_today.sort_values(by='count', ascending=False)
            top3 = entries_today_sorted.head(3)

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
                        <div class='reflection-block' style='border-left-color: #8be9fd;'>         
                        <strong>🕯️ {row['count']}</strong> | <em style='font-size:0.9em; color: #aaa;'>{row['timestamp'].strftime('%Y-%m-%d %H:%M')}</em><br>
                        {row['entry']}
                        </div>
                    """, unsafe_allow_html=True)

            st.markdown("---")
            st.markdown("### 🔥 All Reflections (Sorted by Light)")

            # Sort all entries by candle count for the main display
            entries_sorted_all = entries.sort_values(by='count', ascending=False)

            if entries_sorted_all.empty: # Should not happen if we got here, but good check
                st.info("No reflections have been added yet.")
            else:
                # Iterate through sorted entries to display them
                for _, row in entries_sorted_all.iterrows(): # Use _ if index 'i' not needed
                    entry_index = row['id'] # Get the original index (now stored in 'id')
                    count = row['count']
                    timestamp_str = row['timestamp'].strftime('%Y-%m-%d %H:%M')
                    entry_text = row['entry']

                    col1, col2 = st.columns([9, 1]) # Adjusted column ratio
                    with col1:
                        st.markdown(f"<em style='font-size:0.9em; color: #aaa;'>{timestamp_str}</em>", unsafe_allow_html=True)
                        st.markdown(f"> {entry_text}") # Using markdown blockquote
                    with col2:
                        # Use the original index (entry_index) for the button key and data update
                        if st.button(f"🕯️ {count}", key=f"candle_{entry_index}", help="Add light to this reflection"):
                            # Reload candles_df fresh before update to minimize race conditions
                            if os.path.exists(candle_file):
                                try:
                                    current_candles_df = pd.read_csv(candle_file)
                                    if not current_candles_df.empty:
                                        current_candles_df['entry_index'] = current_candles_df['entry_index'].astype(int)
                                        current_candles_df['count'] = current_candles_df['count'].astype(int)
                                    else:
                                         current_candles_df = pd.DataFrame(columns=["entry_index", "count"])
                                except pd.errors.EmptyDataError:
                                     current_candles_df = pd.DataFrame(columns=["entry_index", "count"])
                            else:
                                current_candles_df = pd.DataFrame(columns=["entry_index", "count"])

                            # Update the count in the reloaded candles_df
                            if entry_index in current_candles_df["entry_index"].values:
                                current_candles_df.loc[current_candles_df["entry_index"] == entry_index, "count"] += 1
                            else:
                                # Add new entry to candles_df if it wasn't there
                                new_candle_row = pd.DataFrame([[entry_index, 1]], columns=["entry_index", "count"])
                                current_candles_df = pd.concat([current_candles_df, new_candle_row], ignore_index=True)

                            # Save the updated candle counts
                            try:
                                # Save back with the correct column name 'entry_index'
                                current_candles_df.to_csv(candle_file, index=False)
                                st.rerun() # Rerun to update the display with the new count
                            except Exception as e:
                                st.error(f"Failed to save candle count: {e}")
                    st.markdown("---") # Separator between entries
        # else: # Handled case where communion_file doesn't exist or is empty earlier
            # st.info("No reflections file or the file is empty.")

    except pd.errors.EmptyDataError:
        # This case should be caught by the os.path.exists or the empty check after loading
        st.info(f"The reflections file ('{communion_file}') appears to be empty.")
    except Exception as e:
        st.error(f"An unexpected error occurred loading communion reflections: {e}")
        st.error(f"Please ensure '{communion_file}' and '{candle_file}' (if it exists) are formatted correctly.")


# -------------------------------
# 🧬 Quantum Genesis Translation
# -------------------------------
elif page == "🧬 Quantum Genesis Translation":
    st.markdown("""
    <h2 style='text-align: center;'>🧬 Genesis as Quantum Field Theory</h2>
    <p style='text-align: center;'>A loving reframe of the creation narrative through the lens of field interactions, operators, and wavefunction collapse.</p>
    """, unsafe_allow_html=True)

    import streamlit.components.v1 as components

    # Load HTML content from file
    genesis_html_path = "genesis_quantum.html"  # Make sure this file is in the same folder as the .py

    try:
        with open(genesis_html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=1800, scrolling=True)
    except FileNotFoundError:
        st.error("🚨 Genesis translation file not found.")
        st.info("Please make sure 'genesis_quantum.html' is in the app folder.")



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

    # --- Load Suggestions ---
    try:
        if os.path.exists(suggestions_file):
            suggestions_df = pd.read_csv(suggestions_file)
            # Drop rows with missing 'suggestion' text if any
            suggestions_df.dropna(subset=['suggestion'], inplace=True)
        else:
            suggestions_df = pd.DataFrame(columns=["timestamp", "suggestion"]) # Empty DF if file not found

        # --- Load Approved ---
        # Load approved or create empty DataFrame if not exists, ensuring necessary columns
        required_approved_cols = ["timestamp", "suggestion", "tag"]
        if os.path.exists(approved_file):
            try:
                approved_df = pd.read_csv(approved_file)
                if approved_df.empty:
                    approved_df = pd.DataFrame(columns=required_approved_cols) # Ensure columns if empty
            except pd.errors.EmptyDataError:
                approved_df = pd.DataFrame(columns=required_approved_cols)
            except Exception as e:
                st.error(f"Error loading approved parables file '{approved_file}': {e}")
                st.stop() # Stop if approved file is corrupt
        else:
            approved_df = pd.DataFrame(columns=required_approved_cols)

        # Ensure all required columns exist in approved_df, adding them if missing
        for col in required_approved_cols:
            if col not in approved_df.columns:
                approved_df[col] = None # Add column with None values

        # --- Display Suggestions for Review ---
        if suggestions_df.empty:
            st.info("No suggestions pending approval.")
        else:
            st.info(f"Found {len(suggestions_df)} suggestion(s) for review.")
            # Use reset_index to get a clean 0-based index for keys, keep original index if needed later
            suggestions_df_display = suggestions_df.reset_index()

            for i, row in suggestions_df_display.iterrows():
                original_index = row['index'] # Get the original index from the suggestions_df before reset
                timestamp = row.get('timestamp', 'N/A')
                suggestion_text = row.get('suggestion', 'N/A')

                st.markdown("---")
                st.markdown(f"### ✨ Suggestion #{i+1} (Original Index: {original_index})")
                st.markdown(f"**Submitted:** {timestamp}")
                st.markdown(f"**Text:**")
                st.markdown(f"> {suggestion_text}") # Blockquote suggestion text

                col1, col2, col3 = st.columns([3, 1, 1]) # Adjusted column ratios

                with col1:
                     # Tag selection
                    tag_options = ["Timeline", "Vision", "Mystery", "Revelation", "Reflection", "Uncategorized"]
                    selected_tag = st.selectbox(
                        "Assign a tag:",
                        options=tag_options,
                        index=tag_options.index("Uncategorized"), # Default selection
                        key=f"tag_{original_index}" # Use original index for unique key
                    )

                with col2:
                    # Approve Button
                    if st.button(f"✅ Approve", key=f"approve_{original_index}"):
                        # Prepare the row to be added to approved_df (using original row data)
                        row_to_approve_data = suggestions_df.loc[original_index].to_dict()
                        row_to_approve_data["tag"] = selected_tag # Add the selected tag

                        # Create a DataFrame from the dictionary
                        row_df_to_approve = pd.DataFrame([row_to_approve_data])

                         # Ensure the columns match the target approved_df columns exactly
                        # Reindex `row_df_to_approve` to match `approved_df` columns, filling missing with None/NaN
                        row_df_to_approve = row_df_to_approve.reindex(columns=approved_df.columns)


                        # Append to approved DataFrame
                        approved_df = pd.concat([approved_df, row_df_to_approve], ignore_index=True)

                        # Remove from original suggestions DataFrame using the original index
                        suggestions_df_updated = suggestions_df.drop(original_index)

                        # Save both files
                        try:
                            approved_df.to_csv(approved_file, index=False)
                            # Save remaining suggestions (or empty file with header)
                            suggestions_df_updated.to_csv(suggestions_file, index=False)

                            st.success(f"Suggestion (Index: {original_index}) approved with tag '{selected_tag}'!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error saving files after approval: {e}")

                with col3:
                    # Delete Button
                    if st.button(f"❌ Delete", key=f"delete_{original_index}"):
                        # Remove from original suggestions DataFrame using the original index
                        suggestions_df_updated = suggestions_df.drop(original_index)

                        # Save the updated suggestions file
                        try:
                            suggestions_df_updated.to_csv(suggestions_file, index=False)
                            st.warning(f"Suggestion (Index: {original_index}) deleted.")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error saving {suggestions_file} after deletion: {e}")

    except FileNotFoundError:
        st.info(f"No suggestions file ('{suggestions_file}') found yet.")
    except pd.errors.EmptyDataError:
        st.info(f"The suggestions file ('{suggestions_file}') is currently empty.")
    except Exception as e:
        st.error(f"An error occurred loading or processing suggestions: {e}")


# ===============================
# === STYLING & AUDIO (Apply last) ==
# ===============================

# -------------------------------
# 🌈 Visual Theme Styles Application
# -------------------------------
# Define defaults first
background_css = "#000000" # Default background
text_shadow_css = "0 0 6px #999" # Default shadow
text_color_css = "#f0f0f0" # Default text color

if visual_theme == "🌌 Starfield Nebula":
    background_css = "radial-gradient(ellipse at top, #0b0c2a, #000000)"
    text_shadow_css = "0 0 8px #8be9fd" # Light blue glow
    text_color_css = "#e0f7fa" # Lighter blueish text

elif visual_theme == "✨ Sacred Gold":
    background_css = "linear-gradient(135deg, #2a210b, #141103)" # Dark gold/brown gradient
    text_shadow_css = "0 0 8px #ffd700" # Gold glow
    text_color_css = "#fff8dc" # Cornsilk / light gold text

elif visual_theme == "🌊 Ocean Depths":
    background_css = "linear-gradient(180deg, #002b36, #001f27)" # Dark teal gradient
    text_shadow_css = "0 0 8px #26a69a" # Teal glow
    text_color_css = "#e0f2f1" # Lighter teal text

elif visual_theme == "🌒 Night Scroll":
    background_css = "linear-gradient(180deg, #1a1a1a, #0a0a0a)" # Dark grey gradient
    text_shadow_css = "0 0 8px #cccccc" # White/light grey glow
    text_color_css = "#f5f5f5" # Lighter grey text

# Apply the selected styles using CSS
# Targeting .stApp is generally more reliable for background
st.markdown(f"""
<style>
/* Apply background to the main app container */
.stApp {{
    background: {background_css};
    color: {text_color_css}; /* Base text color for the theme */
}}

/* Target headers, paragraphs, blockquotes */
h1, h2, h3, h4, h5, h6, .stMarkdown p, blockquote {{
    text-shadow: {text_shadow_css};
    color: {text_color_css}; /* Ensure text color consistency */
}}

/* Input/Text Area Labels and Text */
.stTextInput > label, .stTextArea > label, .stSelectbox > label, .stRadio > label, .stCheckbox > label {{
     text-shadow: {text_shadow_css};
     color: {text_color_css};
}}
.stTextInput > div > div > input, .stTextArea > div > textarea {{
    color: #333; /* Darker text for input fields for readability, or match theme */
    /* Optionally add a subtle shadow matching the theme if desired */
}}


/* Style Streamlit's expander header */
.stExpander > div > details > summary {{
    text-shadow: {text_shadow_css};
    color: {text_color_css};
}}
.stExpander {{
     border: 1px solid rgba(255, 255, 255, 0.1); /* Subtle border for expanders */
     background-color: rgba(255, 255, 255, 0.03); /* Slightly different background */
     margin-bottom: 10px;
}}

/* Ensure buttons have some contrast/style */
.stButton > button {{
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 0 6px rgba(173, 216, 230, 0.4); /* Example shadow */
    color: {text_color_css}; /* Match text color */
    background-color: rgba(255, 255, 255, 0.1); /* Slight background */
    text-shadow: {text_shadow_css}; /* Apply shadow to button text */
}}
.stButton > button:hover {{
    background-color: rgba(255, 255, 255, 0.2); /* Hover effect */
    border-color: rgba(255, 255, 255, 0.5);
}}

</style>
""", unsafe_allow_html=True)


# -------------------------------
# 🔊 Background Music Playback (Conditional)
# -------------------------------
# This section should run AFTER the sidebar controls are defined
audio_url = music_files.get(music_choice) if music_on and music_choice and music_choice != "None" else None

if audio_url:
    st.markdown(f"""
    <audio id="background-audio" autoplay loop style="display:none">
        <source src="{audio_url}" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    <script>
        const audio = document.getElementById("background-audio");
        if (audio) {{
            // Delay volume set to avoid autoplay block in some browsers
            setTimeout(() => {{
                audio.volume = 0.3;
            }}, 500);
        }}
    </script>
    """, unsafe_allow_html=True)



# -------------------------------
# Footer (Apply last)
# -------------------------------
# Use f-string and escape literal CSS braces

# Ensure text_shadow_css is defined before this block, e.g.:
# text_shadow_css = "2px 2px 4px #000000"

st.markdown(f"""
<style>
    .footer {{
        text-align: center;
        font-size: 0.9em;
        margin-top: 50px; /* Increased margin */
        padding-bottom: 20px; /* Add padding at the bottom */
        color: #bbb; /* Slightly lighter grey */
        text-shadow: {text_shadow_css}; /* Apply text shadow consistent with the theme */
        font-style: italic; /* Maintain an elegant touch */
        letter-spacing: 1px; /* Slight refinement for aesthetic balance */
    }}
</style>
<div class="footer">
    ✨ Created with Jesus and LLMs · Powered by Streamlit & Python ✨
</div>
""", unsafe_allow_html=True)