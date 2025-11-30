# scrolls/task_list_section.py
import os
import pandas as pd
import streamlit as st
from datetime import datetime

TASK_FILE = os.path.join("data", "tasks.csv")
TASK_COLUMNS = ['id', 'timestamp', 'task', 'completed', 'priority']


def _load_tasks() -> pd.DataFrame:
    """Load tasks from CSV file."""
    if os.path.exists(TASK_FILE):
        try:
            df = pd.read_csv(TASK_FILE)
            if not df.empty:
                # Ensure all expected columns exist
                for col in TASK_COLUMNS:
                    if col not in df.columns:
                        if col == 'completed':
                            df[col] = False
                        elif col == 'priority':
                            df[col] = 'Medium'
                        else:
                            df[col] = ''
                return df
        except pd.errors.EmptyDataError:
            pass
        except Exception as e:
            st.error(f"Could not load tasks: {e}")
    return pd.DataFrame(columns=TASK_COLUMNS)


def _save_tasks(df: pd.DataFrame) -> None:
    """Save tasks to CSV file."""
    try:
        df.to_csv(TASK_FILE, index=False)
    except Exception as e:
        st.error(f"Failed to save tasks: {e}")


def _generate_id(df: pd.DataFrame) -> int:
    """Generate a unique ID for a new task."""
    if df.empty or 'id' not in df.columns:
        return 1
    return int(df['id'].max()) + 1


def render_task_list():
    """Render the task list UI component."""
    st.markdown("""
    ---
    ## 📋 Sacred Task List
    *Organize your intentions and manifest your goals through mindful action.*
    ---
    """, unsafe_allow_html=True)

    # Load existing tasks
    tasks = _load_tasks()

    # --- Add New Task Section ---
    st.markdown("### ✨ Add a New Task")
    with st.form("new_task_form", clear_on_submit=True):
        task_text = st.text_input(
            "What would you like to accomplish?",
            placeholder="Enter your task here...",
            key="new_task_input"
        )
        col1, col2 = st.columns([3, 1])
        with col1:
            priority = st.selectbox(
                "Priority",
                options=["High", "Medium", "Low"],
                index=1,
                key="task_priority"
            )
        with col2:
            submit_btn = st.form_submit_button("➕ Add Task", use_container_width=True)

        if submit_btn and task_text and task_text.strip():
            new_task = pd.DataFrame([{
                'id': _generate_id(tasks),
                'timestamp': datetime.now().isoformat(),
                'task': task_text.strip(),
                'completed': False,
                'priority': priority
            }])
            tasks = pd.concat([tasks, new_task], ignore_index=True)
            _save_tasks(tasks)
            st.success("Task added to your sacred list!")
            st.rerun()
        elif submit_btn:
            st.warning("Please enter a task before submitting.")

    st.markdown("---")

    # --- Display Tasks Section ---
    if tasks.empty:
        st.markdown("""
        <div class='fade-in' style='text-align: center; padding: 2em; font-style: italic; color: #94a3b8;'>
            Your task list is empty. Begin your journey by adding your first intention above.
        </div>
        """, unsafe_allow_html=True)
    else:
        # Calculate task statistics
        total_tasks = len(tasks)
        completed_tasks = len(tasks[tasks['completed'] == True])
        pending_tasks = total_tasks - completed_tasks

        # Display statistics
        st.markdown("### 📊 Task Overview")
        stat_cols = st.columns(3)
        with stat_cols[0]:
            st.metric("Total Tasks", total_tasks)
        with stat_cols[1]:
            st.metric("Completed", completed_tasks)
        with stat_cols[2]:
            st.metric("Pending", pending_tasks)

        st.markdown("---")

        # --- Pending Tasks ---
        st.markdown("### 🔥 Pending Tasks")
        pending_df = tasks[tasks['completed'] == False].copy()

        if pending_df.empty:
            st.markdown("""
            <div style='text-align: center; padding: 1em; font-style: italic; color: #94a3b8;'>
                All tasks completed! Well done.
            </div>
            """, unsafe_allow_html=True)
        else:
            # Sort by priority
            priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
            pending_df['priority_order'] = pending_df['priority'].map(priority_order)
            pending_df = pending_df.sort_values('priority_order')

            for _, row in pending_df.iterrows():
                task_id = row['id']
                priority_emoji = {'High': '🔴', 'Medium': '🟡', 'Low': '🟢'}.get(row['priority'], '🟡')

                col1, col2, col3 = st.columns([7, 1, 1])
                with col1:
                    st.markdown(f"""
                    <div class='scroll-card' style='padding: 12px; margin-bottom: 8px;'>
                        <span style='font-size: 1.1em;'>{priority_emoji} {row['task']}</span>
                        <br><small style='color: #64748b;'>Priority: {row['priority']}</small>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    if st.button("✅", key=f"complete_{task_id}", help="Mark as complete"):
                        tasks.loc[tasks['id'] == task_id, 'completed'] = True
                        _save_tasks(tasks)
                        st.rerun()
                with col3:
                    if st.button("🗑️", key=f"delete_{task_id}", help="Delete task"):
                        tasks = tasks[tasks['id'] != task_id]
                        _save_tasks(tasks)
                        st.rerun()

        st.markdown("---")

        # --- Completed Tasks ---
        st.markdown("### ✨ Completed Tasks")
        completed_df = tasks[tasks['completed'] == True].copy()

        if completed_df.empty:
            st.markdown("""
            <div style='text-align: center; padding: 1em; font-style: italic; color: #94a3b8;'>
                No completed tasks yet. Keep going!
            </div>
            """, unsafe_allow_html=True)
        else:
            for _, row in completed_df.iterrows():
                task_id = row['id']

                col1, col2, col3 = st.columns([7, 1, 1])
                with col1:
                    st.markdown(f"""
                    <div style='padding: 12px; margin-bottom: 8px; background: rgba(34, 197, 94, 0.1); 
                                border-radius: 8px; border-left: 3px solid #22c55e;'>
                        <span style='text-decoration: line-through; color: #64748b;'>{row['task']}</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    if st.button("↩️", key=f"undo_{task_id}", help="Mark as incomplete"):
                        tasks.loc[tasks['id'] == task_id, 'completed'] = False
                        _save_tasks(tasks)
                        st.rerun()
                with col3:
                    if st.button("🗑️", key=f"delete_done_{task_id}", help="Delete task"):
                        tasks = tasks[tasks['id'] != task_id]
                        _save_tasks(tasks)
                        st.rerun()

        # --- Clear Completed Button ---
        st.markdown("---")
        if not completed_df.empty:
            if st.button("🧹 Clear All Completed Tasks", help="Remove all completed tasks"):
                tasks = tasks[tasks['completed'] == False]
                _save_tasks(tasks)
                st.success("Completed tasks cleared!")
                st.rerun()
