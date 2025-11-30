import streamlit as st


def get_energy_color(level: int) -> str:
    """Return a color based on energy level (0-100)."""
    if level < 25:
        return "#ff6b6b"  # Low energy - red
    elif level < 50:
        return "#feca57"  # Medium-low energy - orange/yellow
    elif level < 75:
        return "#48dbfb"  # Medium-high energy - cyan
    else:
        return "#1dd1a1"  # High energy - green


def get_energy_message(level: int) -> str:
    """Return a spiritual message based on energy level."""
    if level < 25:
        return "🌙 *Rest is sacred. Honor your stillness.*"
    elif level < 50:
        return "🌿 *Gentle tasks only. Nurture your roots.*"
    elif level < 75:
        return "⚡ *Energy flows. Engage with purpose.*"
    else:
        return "🔥 *Full radiance! Channel your light.*"


def get_task_recommendations(level: int) -> list:
    """Return task recommendations based on energy level."""
    if level < 25:
        return [
            "📖 Light reading or reflection",
            "🧘 Meditation or breathing",
            "📝 Gentle journaling",
            "🎵 Listen to calming music",
        ]
    elif level < 50:
        return [
            "✉️ Respond to simple messages",
            "📋 Review and organize notes",
            "🌱 Light planning for tomorrow",
            "💭 Creative brainstorming",
        ]
    elif level < 75:
        return [
            "💻 Focused work sessions",
            "📊 Data analysis or research",
            "✍️ Writing and content creation",
            "🤝 Collaborative meetings",
        ]
    else:
        return [
            "🚀 Tackle challenging projects",
            "🧠 Deep learning or study",
            "🎯 High-stakes decisions",
            "🏃 Physical activity or exercise",
        ]


def render_energy_meter():
    """Render the energy meter interface for task pacing."""
    st.markdown("""
    ---
    ## ⏳ Energy Meter: Sacred Pacing
    *Align your tasks with your current energy flow.*
    ---
    """, unsafe_allow_html=True)

    # Initialize session state for energy level
    if 'energy_level' not in st.session_state:
        st.session_state['energy_level'] = 50

    # Energy level input
    st.markdown("### 🔋 Set Your Current Energy Level")
    energy_level = st.slider(
        "How is your energy right now?",
        min_value=0,
        max_value=100,
        value=st.session_state['energy_level'],
        help="0 = Completely depleted, 100 = Fully energized",
        key="energy_slider"
    )

    # Update session state
    st.session_state['energy_level'] = energy_level

    # Get dynamic values
    color = get_energy_color(energy_level)
    message = get_energy_message(energy_level)
    recommendations = get_task_recommendations(energy_level)

    # Visual energy meter display
    st.markdown(f"""
    <div style='
        background: linear-gradient(90deg, {color} {energy_level}%, rgba(255,255,255,0.1) {energy_level}%);
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        border: 1px solid rgba(255,255,255,0.2);
        text-align: center;
    '>
        <span style='font-size: 2em; font-weight: bold; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>
            {energy_level}%
        </span>
    </div>
    """, unsafe_allow_html=True)

    # Spiritual message
    st.markdown(f"<div style='text-align: center; font-size: 1.2em; padding: 10px;'>{message}</div>",
                unsafe_allow_html=True)

    st.markdown("---")

    # Task recommendations
    st.markdown("### 🎯 Recommended Tasks for Your Energy Level")
    for task in recommendations:
        st.markdown(f"- {task}")

    st.markdown("---")

    # Energy wisdom section
    st.markdown("### 🌟 Wisdom for Sacred Pacing")
    with st.expander("Understanding Energy Flow"):
        st.markdown("""
        **The Rhythm of Energy**

        Like the tides guided by the moon, our energy ebbs and flows throughout the day.
        Honoring this rhythm is not weakness—it is wisdom.

        *"There is a time for everything, and a season for every activity under the heavens."*
        — Ecclesiastes 3:1

        **Energy Conservation Principles:**
        - 🌅 Morning energy is often highest for creative work
        - 🌙 Evening may be better for reflection and rest
        - 🔄 Energy follows cycles—track your patterns
        - 💧 Hydration and movement restore flow
        """)

    with st.expander("Quick Energy Reset Techniques"):
        st.markdown("""
        **When Energy is Low:**
        - Take 3 deep breaths (4-7-8 pattern)
        - Step outside for natural light
        - Drink a glass of water
        - Do 5 minutes of gentle stretching

        **When Energy is High:**
        - Channel it into meaningful work
        - Tackle your hardest task first
        - Share your energy with others
        - Create something new
        """)
