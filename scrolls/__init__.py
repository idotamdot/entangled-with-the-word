"""Scroll rendering modules for the app."""

from .communion_project_section import render_communion_scroll
from .scroll_of_cleansing import render_cleansing_scroll

try:
    from .timeline_section import render_timeline
except Exception:  # Module may not exist yet
    def render_timeline():
        import streamlit as st
        st.warning("Timeline module not available.")

try:
    from .admin_parables import render_admin_panel
except Exception:
    def render_admin_panel():
        import streamlit as st
        st.warning("Admin panel module not available.")
