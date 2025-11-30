"""Zen Mode Focus Timer - A meditative focus timer with breathing animation."""

import time
import streamlit as st

# Timer presets in minutes
TIMER_PRESETS = {
    "🌱 Quick Breath (5 min)": 5,
    "🌿 Grounded Focus (10 min)": 10,
    "🌲 Deep Roots (15 min)": 15,
    "🌳 Sacred Flow (25 min)": 25,
}


def _format_time(seconds: int) -> str:
    """Format seconds into MM:SS display."""
    mins, secs = divmod(seconds, 60)
    return f"{mins:02d}:{secs:02d}"


def _init_session_state():
    """Initialize session state variables for the timer."""
    if "zen_timer_running" not in st.session_state:
        st.session_state["zen_timer_running"] = False
    if "zen_timer_seconds" not in st.session_state:
        st.session_state["zen_timer_seconds"] = 0
    if "zen_timer_total" not in st.session_state:
        st.session_state["zen_timer_total"] = 0
    if "zen_timer_completed" not in st.session_state:
        st.session_state["zen_timer_completed"] = False


def render_zen_mode():
    """Render the Zen Mode focus timer page."""
    _init_session_state()

    # Zen Mode CSS
    st.markdown("""
    <style>
    @keyframes zen-breathe {
        0% { transform: scale(1); opacity: 0.7; box-shadow: 0 0 20px rgba(147, 112, 219, 0.3); }
        50% { transform: scale(1.15); opacity: 1; box-shadow: 0 0 60px rgba(147, 112, 219, 0.6); }
        100% { transform: scale(1); opacity: 0.7; box-shadow: 0 0 20px rgba(147, 112, 219, 0.3); }
    }
    @keyframes pulse-glow {
        0% { box-shadow: 0 0 10px rgba(147, 112, 219, 0.3); }
        50% { box-shadow: 0 0 30px rgba(147, 112, 219, 0.6); }
        100% { box-shadow: 0 0 10px rgba(147, 112, 219, 0.3); }
    }
    .zen-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 2rem;
    }
    .zen-circle {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(147, 112, 219, 0.3) 0%, rgba(30, 30, 60, 0.8) 100%);
        border: 2px solid rgba(147, 112, 219, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        animation: zen-breathe 6s infinite ease-in-out;
        margin: 2rem auto;
    }
    .zen-circle-paused {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(147, 112, 219, 0.2) 0%, rgba(30, 30, 60, 0.6) 100%);
        border: 2px solid rgba(147, 112, 219, 0.3);
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 2rem auto;
    }
    .zen-timer-display {
        font-size: 2.5em;
        font-weight: 300;
        color: #e2e8f0;
        font-family: monospace;
        letter-spacing: 4px;
    }
    .zen-quote {
        font-style: italic;
        color: #94a3b8;
        text-align: center;
        max-width: 400px;
        margin: 1.5rem auto;
        line-height: 1.8;
    }
    .zen-complete {
        background: linear-gradient(135deg, rgba(147, 112, 219, 0.2) 0%, rgba(72, 187, 120, 0.2) 100%);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        animation: pulse-glow 3s infinite ease-in-out;
    }
    .zen-complete h2 {
        color: #48bb78;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
    <div style='text-align: center;' class='fade-in'>
        <h2>🌙 Zen Mode</h2>
        <p style='color: #94a3b8; font-style: italic;'>
            "Be still, and know that I am God." — Psalm 46:10
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Timer completed state
    if st.session_state["zen_timer_completed"]:
        st.markdown("""
        <div class='zen-complete'>
            <h2>✨ Session Complete ✨</h2>
            <p style='color: #cbd5e1;'>
                You have completed your focus session.<br>
                May the stillness you cultivated carry into your next moments.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔄 Begin New Session", use_container_width=True):
            st.session_state["zen_timer_completed"] = False
            st.session_state["zen_timer_running"] = False
            st.session_state["zen_timer_seconds"] = 0
            st.rerun()
        return

    # Timer selection (only show when not running)
    if not st.session_state["zen_timer_running"]:
        st.markdown("### 🕐 Choose Your Focus Duration")

        col1, col2 = st.columns([2, 1])
        with col1:
            selected_preset = st.selectbox(
                "Timer preset:",
                options=list(TIMER_PRESETS.keys()),
                label_visibility="collapsed"
            )
            preset_minutes = TIMER_PRESETS[selected_preset]

        with col2:
            custom_minutes = st.number_input(
                "Or custom (min):",
                min_value=1,
                max_value=60,
                value=preset_minutes,
                label_visibility="collapsed"
            )

        use_custom = custom_minutes != preset_minutes
        timer_minutes = custom_minutes if use_custom else preset_minutes
        timer_seconds = timer_minutes * 60

        # Display breathing circle in idle state
        st.markdown(f"""
        <div class='zen-container'>
            <div class='zen-circle-paused'>
                <div class='zen-timer-display'>{_format_time(timer_seconds)}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p class='zen-quote'>
            Breathe deeply. Center your awareness.<br>
            When ready, begin your sacred focus time.
        </p>
        """, unsafe_allow_html=True)

        if st.button("🧘 Begin Focus Session", use_container_width=True, type="primary"):
            st.session_state["zen_timer_running"] = True
            st.session_state["zen_timer_seconds"] = timer_seconds
            st.session_state["zen_timer_total"] = timer_seconds
            st.rerun()

    # Timer running state
    else:
        remaining = st.session_state["zen_timer_seconds"]
        total = st.session_state["zen_timer_total"]

        # Progress calculation
        progress = (total - remaining) / total if total > 0 else 0

        # Breathing circle with timer
        st.markdown(f"""
        <div class='zen-container'>
            <div class='zen-circle'>
                <div class='zen-timer-display'>{_format_time(remaining)}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Progress bar
        st.progress(progress)

        st.markdown("""
        <p class='zen-quote'>
            Let go of distractions. Breathe with the rhythm.<br>
            You are present. You are enough.
        </p>
        """, unsafe_allow_html=True)

        # Control buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⏸️ Pause", use_container_width=True):
                st.session_state["zen_timer_running"] = False
                st.rerun()
        with col2:
            if st.button("🛑 End Session", use_container_width=True):
                st.session_state["zen_timer_running"] = False
                st.session_state["zen_timer_seconds"] = 0
                st.session_state["zen_timer_completed"] = False
                st.rerun()

        # Timer countdown logic
        if remaining > 0:
            # Use Streamlit's native auto-rerun capability with a time delay
            # This is the standard Streamlit pattern for countdown timers
            time.sleep(1)
            st.session_state["zen_timer_seconds"] = remaining - 1
            st.rerun()
        else:
            # Timer completed - immediately transition to completion state
            st.session_state["zen_timer_running"] = False
            st.session_state["zen_timer_completed"] = True
            st.rerun()

    # Footer wisdom
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; margin-top: 2rem;'>
        <p style='color: #64748b; font-size: 0.9em;'>
            💡 <em>Tip: Use Zen Mode to cultivate presence before journaling,
            prayer, or deep reflection.</em>
        </p>
    </div>
    """, unsafe_allow_html=True)
