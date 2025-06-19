import os
import pandas as pd
import streamlit as st

APPROVED_FILE = os.path.join("gospel", "approved_parables.csv")


def load_entries():
    if os.path.exists(APPROVED_FILE):
        try:
            df = pd.read_csv(APPROVED_FILE)
            if not df.empty:
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df = df.sort_values('timestamp')
            return df
        except Exception as e:
            st.error(f"Failed to load timeline: {e}")
    return pd.DataFrame(columns=['timestamp', 'suggestion', 'tag'])


def render_timeline():
    """Display approved parables as a timeline."""
    st.header("🧬 Quantum Parables Timeline")
    df = load_entries()
    if df.empty:
        st.info("No parables have been approved yet.")
        return

    for _, row in df.iterrows():
        date_str = row['timestamp'].strftime('%Y-%m-%d') if not pd.isna(row['timestamp']) else ''
        tag = row.get('tag', '')
        with st.container():
            st.markdown(
                f"<div class='timeline-card'><h3>{date_str}</h3><p>{row['suggestion']}</p></div>",
                unsafe_allow_html=True,
            )
            if tag:
                st.markdown(f"<span class='tag-label'>{tag}</span>", unsafe_allow_html=True)

