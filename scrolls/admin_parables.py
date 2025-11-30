import streamlit as st
from scrolls.categories import PROJECT_CATEGORIES
from backend import ParablesAPI


# Initialize API
_parables_api = ParablesAPI()


def render_admin_panel():
    """Simple moderation panel for parable suggestions."""
    st.header("🛠 Parable Suggestions")
    suggestions = _parables_api.get_suggestions()

    if suggestions.empty:
        st.info("No suggestions pending.")
    else:
        suggestions = suggestions.reset_index(drop=True)
        for i, row in suggestions.iterrows():
            st.markdown(f"**{row.get('timestamp','')}** - {row.get('tag','')}")
            st.markdown(row.get('suggestion',''))
            col1, col2 = st.columns(2)
            if col1.button('Approve', key=f'app_{i}'):
                if _parables_api.approve_suggestion(i):
                    st.rerun()
                else:
                    st.error("Failed to approve suggestion.")
            if col2.button('Delete', key=f'del_{i}'):
                if _parables_api.delete_suggestion(i):
                    st.rerun()
                else:
                    st.error("Failed to delete suggestion.")

    st.markdown('---')
    st.subheader('Add New Suggestion')
    with st.form('new_suggestion', clear_on_submit=True):
        text = st.text_area('Suggestion')
        tag = st.selectbox('Category', options=PROJECT_CATEGORIES, index=PROJECT_CATEGORIES.index('#Timeline'))
        if st.form_submit_button('Submit') and text.strip():
            if _parables_api.submit_suggestion(text, tag):
                st.success('Suggestion added.')
            else:
                st.error('Failed to add suggestion.')

