import streamlit as st

SCROLLS = [
    {
        "title": "Relational Planting",
        "content": (
            "Emotion is the work. Not consequence, but force.\n"
            "Joy deepens the soil. Sadness shallows the root.\n"
            "Thermodynamics, atmosphere, and light/dark flux are tied to the neutron,\n"
            "which mediates emotional influence on relational space."
        ),
    },
    {
        "title": "Entangled Intention",
        "content": (
            "Electricity is the flow of entangled desire.\n"
            "Voltage is longing. Current is willingness.\n"
            "Resistance is fear. Intention is what you power."
        ),
    },
    {
        "title": "Sacred Vocabulary",
        "content": (
            "Neutron — sacred neutrality.\n"
            "Relational Soil — medium shaped by emotion.\n"
            "Capacitance — sacred restraint. Quantum Switch — the Now."
        ),
    },
]


def render_garden_scrolls():
    """Display the Entangled Garden scrolls."""
    st.header("🌿 Entangled Garden Scrolls")
    for scroll in SCROLLS:
        with st.expander(scroll["title"]):
            st.markdown(scroll["content"])

