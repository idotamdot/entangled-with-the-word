import os
import pandas as pd
import streamlit as st
from datetime import datetime
from scrolls.categories import PROJECT_CATEGORIES

SUGGEST_FILE = os.path.join("data", "suggested_parables.csv")
APPROVED_FILE = os.path.join("gospel", "approved_parables.csv")

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


def render_admin_panel():
    """Simple moderation panel for parable suggestions."""
    st.header("🛠 Parable Suggestions")
    suggestions = _load_df(SUGGEST_FILE, SUGGESTION_COLUMNS)

    if suggestions.empty:
        st.info("No suggestions pending.")
    else:
        suggestions = suggestions.reset_index(drop=True)
        for i, row in suggestions.iterrows():
            st.markdown(f"**{row.get('timestamp','')}** - {row.get('tag','')}")
            st.markdown(row.get('suggestion',''))
            
            # Display importance and energy score indicators
            importance = int(row.get('importance', 3))
            energy = int(row.get('energy_score', 5))
            st.markdown(f"⭐ **Importance:** {'🔥' * importance} ({importance}/5) | ⚡ **Energy:** {'💫' * (energy // 2)} ({energy}/10)")
            
            col1, col2 = st.columns(2)
            if col1.button('Approve', key=f'app_{i}'):
                approved = _load_df(APPROVED_FILE, APPROVED_COLUMNS)
                approved = pd.concat([approved, pd.DataFrame([row])], ignore_index=True)
                _save_df(approved, APPROVED_FILE)
                suggestions = suggestions.drop(i)
                _save_df(suggestions, SUGGEST_FILE)
                st.rerun()
            if col2.button('Delete', key=f'del_{i}'):
                suggestions = suggestions.drop(i)
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
            new_row = pd.DataFrame([[datetime.now().isoformat(), text.strip(), tag, importance, energy_score]],
                                   columns=SUGGESTION_COLUMNS)
            suggestions = pd.concat([suggestions, new_row], ignore_index=True)
            _save_df(suggestions, SUGGEST_FILE)
            st.success('Suggestion added.')

