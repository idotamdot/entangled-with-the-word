import os
import pandas as pd
import streamlit as st
from datetime import datetime
from scrolls.categories import PROJECT_CATEGORIES

TASKS_FILE = os.path.join("data", "tasks.csv")
TASK_COLUMNS = ["id", "timestamp", "title", "description", "category", "completed"]


def _load_tasks() -> pd.DataFrame:
    """Load tasks from CSV file."""
    if os.path.exists(TASKS_FILE):
        try:
            df = pd.read_csv(TASKS_FILE)
            if not df.empty:
                # Ensure all columns exist
                for col in TASK_COLUMNS:
                    if col not in df.columns:
                        df[col] = "" if col != "completed" else False
                return df
        except Exception as e:
            st.error(f"Could not load tasks: {e}")
    return pd.DataFrame(columns=TASK_COLUMNS)


def _save_tasks(df: pd.DataFrame) -> None:
    """Save tasks to CSV file."""
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
    df.to_csv(TASKS_FILE, index=False)


def _get_next_id(df: pd.DataFrame) -> int:
    """Get the next available task ID."""
    if df.empty:
        return 1
    return int(df["id"].max()) + 1


def render_task_list():
    """Render the task list display interface."""
    st.markdown("""
    ---
    ## 📋 Sacred Task List
    *Align your intentions with purposeful action.*
    ---
    """, unsafe_allow_html=True)

    # Load existing tasks
    tasks_df = _load_tasks()

    # --- Add New Task Section ---
    st.markdown("### ✨ Add a New Task")
    with st.form("new_task_form", clear_on_submit=True):
        task_title = st.text_input("Task Title", placeholder="Enter your sacred intention...")
        task_description = st.text_area(
            "Description (optional)",
            placeholder="Add details about this task...",
            height=100
        )
        task_category = st.selectbox("Category", options=PROJECT_CATEGORIES)
        submit_task = st.form_submit_button("🙏 Add Task")

        if submit_task and task_title.strip():
            new_id = _get_next_id(tasks_df)
            new_task = pd.DataFrame([[
                new_id,
                datetime.now().isoformat(),
                task_title.strip(),
                task_description.strip() if task_description else "",
                task_category,
                False
            ]], columns=TASK_COLUMNS)
            tasks_df = pd.concat([tasks_df, new_task], ignore_index=True)
            _save_tasks(tasks_df)
            st.success("✨ Task added to your sacred list!")
            st.rerun()
        elif submit_task:
            st.warning("Please enter a task title.")

    st.markdown("---")

    # --- Filter Section ---
    st.markdown("### 🔍 Filter Tasks")
    col_filter1, col_filter2 = st.columns(2)
    with col_filter1:
        filter_category = st.selectbox(
            "Category",
            options=["All"] + PROJECT_CATEGORIES,
            key="filter_category"
        )
    with col_filter2:
        filter_status = st.selectbox(
            "Status",
            options=["All", "Pending", "Completed"],
            key="filter_status"
        )

    # Apply filters
    filtered_df = tasks_df.copy()
    if filter_category != "All":
        filtered_df = filtered_df[filtered_df["category"] == filter_category]
    if filter_status == "Pending":
        filtered_df = filtered_df[~filtered_df["completed"]]
    elif filter_status == "Completed":
        filtered_df = filtered_df[filtered_df["completed"]]

    st.markdown("---")

    # --- Task Display Section ---
    st.markdown("### 📜 Your Tasks")

    if filtered_df.empty:
        st.info("🌟 No tasks found. Add your first sacred intention above!")
    else:
        # Display task counts
        total = len(tasks_df)
        completed = len(tasks_df[tasks_df["completed"]])
        pending = total - completed

        col_stats1, col_stats2, col_stats3 = st.columns(3)
        with col_stats1:
            st.metric("Total Tasks", total)
        with col_stats2:
            st.metric("Completed", completed)
        with col_stats3:
            st.metric("Pending", pending)

        st.markdown("---")

        # Display each task as a card
        for _, task in filtered_df.iterrows():
            task_id = int(task["id"])
            is_completed = task["completed"]
            title = task["title"]
            description = task.get("description", "")
            category = task.get("category", "")
            timestamp = task.get("timestamp", "")

            # Format timestamp for display
            try:
                dt = datetime.fromisoformat(timestamp)
                date_str = dt.strftime("%Y-%m-%d %H:%M")
            except (ValueError, TypeError):
                date_str = timestamp

            # Card styling based on completion status
            status_icon = "✅" if is_completed else "⏳"
            border_color = "rgba(29, 209, 161, 0.5)" if is_completed else "rgba(99, 102, 241, 0.5)"
            bg_opacity = "0.03" if is_completed else "0.05"

            st.markdown(f"""
            <div class="scroll-card" style="
                border-color: {border_color};
                background: rgba(255, 255, 255, {bg_opacity});
                margin-bottom: 10px;
            ">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <div class="scroll-title" style="{'text-decoration: line-through; opacity: 0.7;' if is_completed else ''}">
                            {status_icon} {title}
                        </div>
                        {f'<div class="scroll-content">{description}</div>' if description else ''}
                    </div>
                </div>
                <div style="margin-top: 10px; font-size: 0.85em; color: #64748b;">
                    <span style="background: rgba(99, 102, 241, 0.2); padding: 2px 8px; border-radius: 10px;">{category}</span>
                    <span style="margin-left: 10px;">📅 {date_str}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Action buttons
            col_action1, col_action2, col_action3 = st.columns([2, 2, 6])
            with col_action1:
                if is_completed:
                    if st.button("↩️ Reopen", key=f"reopen_{task_id}"):
                        tasks_df.loc[tasks_df["id"] == task_id, "completed"] = False
                        _save_tasks(tasks_df)
                        st.rerun()
                else:
                    if st.button("✅ Complete", key=f"complete_{task_id}"):
                        tasks_df.loc[tasks_df["id"] == task_id, "completed"] = True
                        _save_tasks(tasks_df)
                        st.rerun()
            with col_action2:
                if st.button("🗑️ Delete", key=f"delete_{task_id}"):
                    tasks_df = tasks_df[tasks_df["id"] != task_id]
                    _save_tasks(tasks_df)
                    st.rerun()

            st.markdown("")

    # --- Wisdom Section ---
    st.markdown("---")
    st.markdown("### 🌟 Sacred Productivity Wisdom")
    with st.expander("Guidance for Task Alignment"):
        st.markdown("""
        **The Art of Sacred Tasking**

        Tasks are not burdens—they are opportunities to manifest intention.
        Each completed task is a prayer answered through action.

        *"Whatever you do, work at it with all your heart, as working for the Lord."*
        — Colossians 3:23

        **Principles of Sacred Productivity:**
        - 🎯 **Intention First**: Align tasks with your higher purpose
        - 🌱 **Small Steps**: Break large intentions into sacred moments
        - ⏰ **Divine Timing**: Honor the rhythm of when to act and when to rest
        - 🙏 **Gratitude**: Celebrate each completion as a blessing
        """)
