import os
import pandas as pd
import streamlit as st
from scrolls.categories import PROJECT_CATEGORIES

APPROVED_FILE = os.path.join("gospel", "approved_parables.csv")

# Define column schema with importance and energy_score
APPROVED_COLUMNS = ['timestamp', 'suggestion', 'tag', 'importance', 'energy_score']


def load_entries():
    if os.path.exists(APPROVED_FILE):
        try:
            df = pd.read_csv(APPROVED_FILE)
            if not df.empty:
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df = df.sort_values('timestamp')
                # Ensure new columns exist with defaults
                if 'importance' not in df.columns:
                    df['importance'] = 3
                if 'energy_score' not in df.columns:
                    df['energy_score'] = 5
            return df
        except Exception as e:
            st.error(f"Failed to load timeline: {e}")
    return pd.DataFrame(columns=APPROVED_COLUMNS)


def render_timeline():
    """Display approved parables as a timeline."""
    st.header("🧬 Quantum Parables Timeline")
    df = load_entries()
    if df.empty:
        st.info("No parables have been approved yet.")
        return

    # Category filter
    all_tags = ["All"] + PROJECT_CATEGORIES
    selected_category = st.selectbox("Filter by category:", options=all_tags)

    # Sort options including importance and energy
    sort_option = st.selectbox("Sort by:", options=["Date", "Importance (High to Low)", "Energy (High to Low)"])

    # Filter dataframe if a specific category is selected
    if selected_category != "All":
        df = df[df['tag'] == selected_category]

    if df.empty:
        st.info(f"No parables found for category: {selected_category}")
        return

    # Apply sorting based on selection
    if sort_option == "Importance (High to Low)":
        df = df.sort_values('importance', ascending=False)
    elif sort_option == "Energy (High to Low)":
        df = df.sort_values('energy_score', ascending=False)
    else:
        df = df.sort_values('timestamp')

    for _, row in df.iterrows():
        date_str = row['timestamp'].strftime('%Y-%m-%d') if not pd.isna(row['timestamp']) else ''
        tag = row.get('tag', '')
        importance = int(row.get('importance', 3)) if pd.notna(row.get('importance')) else 3
        energy = int(row.get('energy_score', 5)) if pd.notna(row.get('energy_score')) else 5
        
        with st.container():
            st.markdown(
                f"<div class='timeline-card'><h3>{date_str}</h3><p>{row['suggestion']}</p></div>",
                unsafe_allow_html=True,
            )
            # Display importance and energy indicators
            col1, col2, col3 = st.columns([2, 2, 6])
            with col1:
                st.markdown(f"⭐ **{importance}/5**")
            with col2:
                st.markdown(f"⚡ **{energy}/10**")
            with col3:
                if tag:
                    st.markdown(f"<span class='tag-label'>{tag}</span>", unsafe_allow_html=True)

