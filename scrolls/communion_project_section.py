import streamlit as st
import datetime
from backend import CommunionAPI


# Initialize API
_communion_api = CommunionAPI()


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
            if _communion_api.submit_reflection(user_reflection):
                st.success("Your presence has been recorded in the scroll.")
            else:
                st.error("Error saving reflection.")
        elif submit_reflection:
            st.warning("Please enter a reflection before submitting.")

    st.markdown("---")
    st.markdown("### 📜 The Table of Light")

    entries = _communion_api.get_reflections()

    if entries.empty:
        st.info("No reflections found yet. Be the first to submit one above!")
    else:
        st.markdown("### ✨ Top 3 Highlights of the Day")
        today = datetime.date.today()
        top3 = _communion_api.get_top_reflections(date=datetime.datetime.now(), limit=3)

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
                    if _communion_api.add_candle(entry_index):
                        st.rerun()
                    else:
                        st.error("Failed to add candle.")

            st.markdown("---")
