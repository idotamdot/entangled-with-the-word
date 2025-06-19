import os
import pandas as pd
import streamlit as st
from datetime import datetime

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


def render_admin_panel():
    """Simple moderation panel for parable suggestions."""
    st.header("🛠 Parable Suggestions")
    suggestions = _load_df(SUGGEST_FILE, ['timestamp', 'suggestion', 'tag'])

    if suggestions.empty:
        st.info("No suggestions pending.")
    else:
        suggestions = suggestions.reset_index(drop=True)
        for i, row in suggestions.iterrows():
            st.markdown(f"**{row.get('timestamp','')}** - {row.get('tag','')}")
            st.markdown(row.get('suggestion',''))
            col1, col2 = st.columns(2)
            if col1.button('Approve', key=f'app_{i}'):
                approved = _load_df(APPROVED_FILE, ['timestamp', 'suggestion', 'tag'])
                approved = pd.concat([approved, pd.DataFrame([row])], ignore_index=True)
                _save_df(approved, APPROVED_FILE)
                suggestions = suggestions.drop(i)
                _save_df(suggestions, SUGGEST_FILE)
                st.experimental_rerun()
            if col2.button('Delete', key=f'del_{i}'):
                suggestions = suggestions.drop(i)
                _save_df(suggestions, SUGGEST_FILE)
                st.experimental_rerun()

    st.markdown('---')
    st.subheader('Add New Suggestion')
    with st.form('new_suggestion', clear_on_submit=True):
        text = st.text_area('Suggestion')
        tag = st.text_input('Tag', value='Timeline')
        if st.form_submit_button('Submit') and text.strip():
            new_row = pd.DataFrame([[datetime.now().isoformat(), text.strip(), tag]],
                                   columns=['timestamp', 'suggestion', 'tag'])
            suggestions = pd.concat([suggestions, new_row], ignore_index=True)
            _save_df(suggestions, SUGGEST_FILE)
            st.success('Suggestion added.')

