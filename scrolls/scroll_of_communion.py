import streamlit as st
import pandas as pd
import datetime
import os


def render_communion_scroll():
    
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



