import streamlit as st
from scrolls.categories import PROJECT_CATEGORIES
from backend import ParablesAPI


# Initialize API
_parables_api = ParablesAPI()


def render_timeline():
    """Display approved parables as a timeline."""
    st.header("🧬 Quantum Parables Timeline")
    
    # Category filter
    all_tags = ["All"] + PROJECT_CATEGORIES
    selected_category = st.selectbox("Filter by category:", options=all_tags)

    # Get filtered parables using API
    df = _parables_api.get_approved_by_category(selected_category)
    
    if df.empty:
        if selected_category != "All":
            st.info(f"No parables found for category: {selected_category}")
        else:
            st.info("No parables have been approved yet.")
        return

    for _, row in df.iterrows():
        date_str = row['timestamp'].strftime('%Y-%m-%d') if not hasattr(row['timestamp'], 'isna') or not row['timestamp'] is None else ''
        tag = row.get('tag', '')
        with st.container():
            st.markdown(
                f"<div class='timeline-card'><h3>{date_str}</h3><p>{row['suggestion']}</p></div>",
                unsafe_allow_html=True,
            )
            if tag:
                st.markdown(f"<span class='tag-label'>{tag}</span>", unsafe_allow_html=True)

