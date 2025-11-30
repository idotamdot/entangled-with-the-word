import os
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
from scrolls.categories import PROJECT_CATEGORIES

SUGGEST_FILE = os.path.join("data", "suggested_parables.csv")
APPROVED_FILE = os.path.join("gospel", "approved_parables.csv")


def _load_df(path, columns):
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            if not df.empty:
                return df
        except Exception as e:
            st.error(f"Could not load {path}: {e}")
    return pd.DataFrame(columns=columns)


def _save_df(df, path):
    df.to_csv(path, index=False)


def _filter_by_date_range(df, start_date, end_date):
    """Filter dataframe by date range."""
    if df.empty or 'timestamp' not in df.columns:
        return df
    df = df.copy()
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    # Convert dates to datetime for comparison
    start_dt = pd.to_datetime(start_date)
    end_dt = pd.to_datetime(end_date) + timedelta(days=1) - timedelta(seconds=1)
    return df[(df['timestamp'] >= start_dt) & (df['timestamp'] <= end_dt)]


def render_admin_panel():
    """Simple moderation panel for parable suggestions."""
    st.header("🛠 Parable Suggestions")
    suggestions = _load_df(SUGGEST_FILE, ['timestamp', 'suggestion', 'tag'])

    # Date range filter for admin panel
    st.markdown("##### 📅 Filter by Due Date Range")
    col1, col2 = st.columns(2)
    
    today = datetime.now().date()
    default_start = today - timedelta(days=365)
    
    with col1:
        start_date = st.date_input("Start Date", value=default_start, key="admin_start_date")
    with col2:
        end_date = st.date_input("End Date", value=today, key="admin_end_date")
    
    if start_date > end_date:
        st.warning("Start date must be before or equal to end date.")
        return

    if suggestions.empty:
        st.info("No suggestions pending.")
    else:
        # Apply date filter
        filtered_suggestions = _filter_by_date_range(suggestions, start_date, end_date)
        
        if filtered_suggestions.empty:
            st.info("No suggestions found in the selected date range.")
        else:
            filtered_suggestions = filtered_suggestions.reset_index(drop=True)
            for i, row in filtered_suggestions.iterrows():
                st.markdown(f"**{row.get('timestamp','')}** - {row.get('tag','')}")
                st.markdown(row.get('suggestion',''))
                col1, col2 = st.columns(2)
                # Use original index for operations
                orig_idx = suggestions[suggestions['suggestion'] == row['suggestion']].index[0]
                if col1.button('Approve', key=f'app_{i}'):
                    approved = _load_df(APPROVED_FILE, ['timestamp', 'suggestion', 'tag'])
                    approved = pd.concat([approved, pd.DataFrame([row])], ignore_index=True)
                    _save_df(approved, APPROVED_FILE)
                    suggestions = suggestions.drop(orig_idx)
                    _save_df(suggestions, SUGGEST_FILE)
                    st.rerun()
                if col2.button('Delete', key=f'del_{i}'):
                    suggestions = suggestions.drop(orig_idx)
                    _save_df(suggestions, SUGGEST_FILE)
                    st.rerun()

    st.markdown('---')
    st.subheader('Add New Suggestion')
    with st.form('new_suggestion', clear_on_submit=True):
        text = st.text_area('Suggestion')
        tag = st.selectbox('Category', options=PROJECT_CATEGORIES, index=PROJECT_CATEGORIES.index('#Timeline'))
        if st.form_submit_button('Submit') and text.strip():
            new_row = pd.DataFrame([[datetime.now().isoformat(), text.strip(), tag]],
                                   columns=['timestamp', 'suggestion', 'tag'])
            suggestions = pd.concat([suggestions, new_row], ignore_index=True)
            _save_df(suggestions, SUGGEST_FILE)
            st.success('Suggestion added.')

