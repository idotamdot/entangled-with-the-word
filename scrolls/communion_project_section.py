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
            communion_file = "data/communion_reflections.csv"
            try:
                file_exists = os.path.exists(communion_file)
                df_new.to_csv(communion_file, mode='a', header=not file_exists, index=False)
                st.success("Your presence has been recorded in the scroll.")
            except Exception as e:
                st.error(f"Error saving reflection: {e}")
        elif submit_reflection:
            st.warning("Please enter a reflection before submitting.")

    st.markdown("---")
    st.markdown("### 📜 The Table of Light")

    communion_file = "data/communion_reflections.csv"
    candle_file = "data/communion_candles.csv"

    try:
        if not os.path.exists(communion_file):
            st.info("No reflections found yet. Be the first to submit one above!")
            entries = pd.DataFrame(columns=["timestamp", "entry"])
        else:
            entries = pd.read_csv(communion_file)

        if not entries.empty:
            entries['timestamp'] = pd.to_datetime(entries['timestamp'])
            entries = entries.reset_index(drop=True)
            entries['id'] = entries.index

            if os.path.exists(candle_file):
                try:
                    candles_df = pd.read_csv(candle_file)
                    if not candles_df.empty:
                        candles_df['entry_index'] = candles_df['entry_index'].astype(int)
                        candles_df['count'] = candles_df['count'].astype(int)
                    else:
                        candles_df = pd.DataFrame(columns=["entry_index", "count"])
                except pd.errors.EmptyDataError:
                    candles_df = pd.DataFrame(columns=["entry_index", "count"])
                except Exception as e:
                    st.warning(f"Could not load candle data: {e}")
                    candles_df = pd.DataFrame(columns=["entry_index", "count"])
            else:
                candles_df = pd.DataFrame(columns=["entry_index", "count"])

            candles_df = candles_df.rename(columns={'entry_index': 'id'})
            entries = pd.merge(entries, candles_df, on='id', how='left')
            entries['count'] = entries['count'].fillna(0).astype(int)

            st.markdown("### ✨ Top 3 Highlights of the Day")
            today = datetime.date.today()
            entries_today = entries[entries['timestamp'].dt.date == today].copy()
            top3 = entries_today.sort_values(by='count', ascending=False).head(3)

            if top3.empty:
                st.markdown("""
                    <div class='fade-in' style='font-style: italic; text-align: center; padding: 1em;'>
                        No reflections yet today. Be the first to light the scroll.
                    </div>
                """, unsafe_allow_html=True)
            else:
                for _, row in top3.iterrows():
                    st.markdown(f"""
                        <div class='reflection-block' style='border-left-color: #8be9fd;'>
                        <strong>🕯️ {row['count']}</strong> | <em style='font-size:0.9em; color: #aaa;'>{row['timestamp'].strftime('%Y-%m-%d %H:%M')}</em><br>
                        {row['entry']}
                        </div>
                    """, unsafe_allow_html=True)

            st.markdown("---")
            st.markdown("### 🔥 All Reflections (Sorted by Light)")

            entries_sorted = entries.sort_values(by='count', ascending=False)

            for _, row in entries_sorted.iterrows():
                entry_index = row['id']
                count = row['count']
                timestamp_str = row['timestamp'].strftime('%Y-%m-%d %H:%M')
                entry_text = row['entry']

                col1, col2 = st.columns([9, 1])
                with col1:
                    st.markdown(f"<em style='font-size:0.9em; color: #aaa;'>{timestamp_str}</em>", unsafe_allow_html=True)
                    st.markdown(f"> {entry_text}")
                with col2:
                    if st.button(f"🕯️ {count}", key=f"candle_{entry_index}", help="Add light to this reflection"):
                        if os.path.exists(candle_file):
                            try:
                                current_df = pd.read_csv(candle_file)
                                if not current_df.empty:
                                    current_df['entry_index'] = current_df['entry_index'].astype(int)
                                    current_df['count'] = current_df['count'].astype(int)
                                else:
                                    current_df = pd.DataFrame(columns=["entry_index", "count"])
                            except pd.errors.EmptyDataError:
                                current_df = pd.DataFrame(columns=["entry_index", "count"])
                        else:
                            current_df = pd.DataFrame(columns=["entry_index", "count"])

                        if entry_index in current_df["entry_index"].values:
                            current_df.loc[current_df["entry_index"] == entry_index, "count"] += 1
                        else:
                            new_row = pd.DataFrame([[entry_index, 1]], columns=["entry_index", "count"])
                            current_df = pd.concat([current_df, new_row], ignore_index=True)

                        try:
                            current_df.to_csv(candle_file, index=False)
                            st.rerun()
                        except Exception as e:
                            st.error(f"Failed to save candle count: {e}")

                st.markdown("---")

    except pd.errors.EmptyDataError:
        st.info("The reflections file appears to be empty.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
