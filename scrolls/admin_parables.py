import streamlit as st
from datetime import datetime, timedelta
from scrolls.categories import PROJECT_CATEGORIES
from backend import ParablesAPI


# Initialize API
_parables_api = ParablesAPI()
# Define column schema with importance and energy_score
SUGGESTION_COLUMNS = ['timestamp', 'suggestion', 'tag', 'importance', 'energy_score']
APPROVED_COLUMNS = ['timestamp', 'suggestion', 'tag', 'importance', 'energy_score']


def _load_df(path, columns):
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            if not df.empty:
                # Ensure new columns exist with defaults
                if 'importance' not in df.columns:
                    df['importance'] = 3
                if 'energy_score' not in df.columns:
                    df['energy_score'] = 5
                return df
        except Exception as e:
            st.error(f"Could not load {path}: {e}")
    return pd.DataFrame(columns=columns)


def _save_df(df, path):
    df.to_csv(path, index=False)


def _filter_by_date_range(df, start_date, end_date):
    """Filter dataframe by date range.
    
    Returns a filtered copy of the dataframe with rows within the date range.
    Preserves the original index for reliable row identification.
    """
    if df.empty or 'timestamp' not in df.columns:
        return df
    result = df.copy()
    result['timestamp'] = pd.to_datetime(result['timestamp'], errors='coerce')
    # Convert dates to datetime for comparison
    start_dt = pd.to_datetime(start_date)
    end_dt = pd.to_datetime(end_date) + timedelta(days=1) - timedelta(seconds=1)
    return result[(result['timestamp'] >= start_dt) & (result['timestamp'] <= end_dt)]


def render_admin_panel():
    """Simple moderation panel for parable suggestions."""
    st.header("🛠 Parable Suggestions")
    suggestions = _parables_api.get_suggestions()

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
        # Apply date filter (preserves original index)
        filtered_suggestions = _filter_by_date_range(suggestions, start_date, end_date)
        
        if filtered_suggestions.empty:
            st.info("No suggestions found in the selected date range.")
        else:
            # Store original indices before resetting for iteration
            for orig_idx in filtered_suggestions.index:
                row = filtered_suggestions.loc[orig_idx]
                st.markdown(f"**{row.get('timestamp','')}** - {row.get('tag','')}")
                st.markdown(row.get('suggestion',''))
                col1, col2 = st.columns(2)
                # Use original index for unique key and operations
                if col1.button('Approve', key=f'app_{orig_idx}'):
                    approved = _load_df(APPROVED_FILE, ['timestamp', 'suggestion', 'tag'])
                    approved = pd.concat([approved, pd.DataFrame([row])], ignore_index=True)
                    _save_df(approved, APPROVED_FILE)
                    suggestions = suggestions.drop(orig_idx)
                    _save_df(suggestions, SUGGEST_FILE)
                    st.rerun()
                if col2.button('Delete', key=f'del_{orig_idx}'):
                    suggestions = suggestions.drop(orig_idx)
                    _save_df(suggestions, SUGGEST_FILE)
                    st.rerun()

    st.markdown('---')
    st.subheader('Add New Suggestion')
    with st.form('new_suggestion', clear_on_submit=True):
        text = st.text_area('Suggestion')
        tag = st.selectbox('Category', options=PROJECT_CATEGORIES, index=PROJECT_CATEGORIES.index('#Timeline'))
        
        # Add importance and energy score inputs
        st.markdown("#### 💡 Task Importance & Energy")
        col_imp, col_eng = st.columns(2)
        with col_imp:
            importance = st.slider('⭐ Importance (1-5)', min_value=1, max_value=5, value=3, 
                                   help='How important is this task? 1=Low, 5=Critical')
        with col_eng:
            energy_score = st.slider('⚡ Energy Score (1-10)', min_value=1, max_value=10, value=5,
                                     help='How much energy/effort does this require? 1=Minimal, 10=Maximum')
        
        if st.form_submit_button('Submit') and text.strip():
            if _parables_api.submit_suggestion(text, tag):
                st.success('Suggestion added.')
            else:
                st.error('Failed to add suggestion.')
            new_row = pd.DataFrame([[datetime.now().isoformat(), text.strip(), tag, importance, energy_score]],
                                   columns=SUGGESTION_COLUMNS)
            suggestions = pd.concat([suggestions, new_row], ignore_index=True)
            _save_df(suggestions, SUGGEST_FILE)
            st.success('Suggestion added.')

