"""Scroll rendering modules for the app."""

from .communion_project_section import render_communion_scroll
from .scroll_of_cleansing import render_cleansing_scroll
from .books_of_the_bible import render_books_list
from .parables_of_jesus import render_parables_list
from .garden_scrolls_section import render_garden_scrolls
from .categories import PROJECT_CATEGORIES

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

try:
    from .task_parser import (
        parse_task,
        parse_tags,
        parse_due_date,
        parse_and_save_task,
        save_task,
        get_task,
        get_all_tasks,
        get_tasks_by_tag,
        mark_task_completed,
        delete_task,
        init_database,
        ParsedTask,
    )
except Exception:
    pass  # Task parser module may not be available
