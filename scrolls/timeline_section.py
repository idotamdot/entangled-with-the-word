import os
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st
import pandas as pd
from scrolls.categories import PROJECT_CATEGORIES
from backend import ParablesAPI


# Initialize API
_parables_api = ParablesAPI()
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


def filter_by_date_range(df, start_date, end_date):
    """Filter dataframe by date range."""
    if df.empty:
        return df
    # Convert dates to datetime for comparison
    start_dt = pd.to_datetime(start_date)
    end_dt = pd.to_datetime(end_date) + timedelta(days=1) - timedelta(seconds=1)
    return df[(df['timestamp'] >= start_dt) & (df['timestamp'] <= end_dt)]


def render_timeline():
    """Display approved parables as a timeline."""
    st.header("🧬 Quantum Parables Timeline")
    
    # Category filter
    all_tags = ["All"] + PROJECT_CATEGORIES
    selected_category = st.selectbox("Filter by category:", options=all_tags)

    # Date range filter
    st.markdown("##### 📅 Filter by Date Range")
    col1, col2 = st.columns(2)
    
    # Set default date range
    today = datetime.now().date()
    default_start = today - timedelta(days=365)  # Default to last year
    
    with col1:
        start_date = st.date_input("Start Date", value=default_start, key="timeline_start_date")
    with col2:
        end_date = st.date_input("End Date", value=today, key="timeline_end_date")
    
    # Validate date range
    if start_date > end_date:
        st.warning("Start date must be before or equal to end date.")
        return

    # Filter dataframe if a specific category is selected
    if selected_category != "All":
        df = df[df['tag'] == selected_category]

    # Apply date range filter
    df = filter_by_date_range(df, start_date, end_date)

    if df.empty:
        st.info(f"No parables found for the selected filters.")
        return

    # Apply sorting based on selection
    if sort_option == "Importance (High to Low)":
        df = df.sort_values('importance', ascending=False)
    elif sort_option == "Energy (High to Low)":
        df = df.sort_values('energy_score', ascending=False)
    else:
        df = df.sort_values('timestamp')

    for _, row in df.iterrows():
        date_str = row['timestamp'].strftime('%Y-%m-%d') if pd.notna(row['timestamp']) else ''
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

