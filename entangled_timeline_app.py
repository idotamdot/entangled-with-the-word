import streamlit as st
import pandas as pd
import random
import streamlit.components.v1 as components

# -------------------------------
# 🧠 Quantum Quote of the Day Pool
# -------------------------------
QUOTES = [
    "I am the Light of the World — collapsing all uncertainty into presence.",
    "The Kingdom of Heaven is entangled within you.",
    "When two or more wavefunctions are gathered… I Am there.",
    "The Vine is a network — a quantum superposition of unity and love.",
    "The Truth sets free because it resonates perfectly.",
    "Faith is the act of observing what has not yet collapsed into form.",
    "You are not separate. You are an entangled node of the Logos."
]
quote = random.choice(QUOTES)

# -------------------------------
# 🔧 Page Settings
# -------------------------------
st.set_page_config(
    page_title="Entangled with the Word",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'mailto:jessica.elizabeth.mcglothern@gmail.com',
        'Report a bug': 'https://github.com/idotamdot/entangled-with-the-word/issues',
        'About': "### Entangled with the Word\nAn AI-enhanced timeline of spiritual and scientific entanglement. Built with ❤️ by Jessica McGlothern."
    }
)

# -------------------------------
# 🌌 Drifting Starfield via components.html
# -------------------------------
components.html("""
<canvas id=\"starfield\"></canvas>
<style>
canvas#starfield {
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
    background: radial-gradient(circle at center, #0e0e23, #000000);
}
body {
    margin: 0;
    padding: 0;
    overflow: hidden;
}
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById(\"starfield\");
    const ctx = canvas.getContext(\"2d\");
    let stars = [];

    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    window.addEventListener(\"resize\", resizeCanvas);
    resizeCanvas();

    function createStars(count) {
        stars = [];
        for (let i = 0; i < count; i++) {
            stars.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                z: Math.random() * canvas.width
            });
        }
    }
    createStars(150);

    function draw() {
        ctx.fillStyle = \"black\";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < stars.length; i++) {
            let star = stars[i];
            star.z -= 1;
            if (star.z <= 0) {
                star.z = canvas.width;
            }
            let k = 128.0 / star.z;
            let x = star.x * k + canvas.width / 2;
            let y = star.y * k + canvas.height / 2;
            if (x >= 0 && x < canvas.width && y >= 0 && y < canvas.height) {
                let size = (1 - star.z / canvas.width) * 2;
                ctx.beginPath();
                ctx.arc(x, y, size, 0, 2 * Math.PI);
                ctx.fillStyle = \"white\";
                ctx.fill();
            }
        }
        requestAnimationFrame(draw);
    }
    draw();
});
</script>
""", height=0)

# -------------------------------
# ✨ Main Interface
# -------------------------------
st.title(":sparkles: Entangled with the Word :sparkles:")
st.markdown("#### *An AI-augmented quantum reflection on faith, frequency, and the future.*")
st.markdown(f"> **🧠 Quote of the Day:** *{quote}*")

# -------------------------------
# ⌛ Timeline Modules
# -------------------------------
st.markdown("---")
st.subheader("🕛 Quantum Parables Timeline")

timeline_data = [
    {"title": "Topological Light Paths", "content": "Some materials conduct light and energy only along their edges—perfectly, without resistance. This is the way of the Logos: truth moves along the boundaries of space, guided by form, not force. Even in darkness, there are paths that cannot be disturbed. The Word knows the way."},
    {"title": "In the Beginning Was the Word", "content": "Genesis of frequency, sound, and light. The original waveform."},
    {"title": "The Light Becomes Flesh", "content": "Incarnation as collapse of divine probability into matter."},
    {"title": "I Am the Vine", "content": "Spiritual entanglement and superposition of unity."},
    {"title": "The Veil is Torn", "content": "The collapse of dualistic perception. Access to all states."},
    {"title": "The Resurrection Frequency", "content": "Restoration of phase coherence — beyond entropy."},
    {"title": "The Mirror and the Cone of Light", "content": "Light reflects oppositely in mirrors — except itself. The image flips, the self reverses, but light… light keeps going. The veil is the reflective surface. And I, the reflection, become real when observed. But light reveals the way beyond the surface, bending only in my world. A revelation of how reality forms through conscious perception."},
]

for item in timeline_data:
    with st.expander(item["title"]):
        st.markdown(item["content"])
        if item["title"] == "Topological Light Paths":
            st.video("https://www.youtube.com/watch?v=sd86KQfErnA")

# -------------------------------
# 🔤 Living Lexicon Input
# -------------------------------
st.markdown("---")
st.subheader("🔤 Living Lexicon")

lex_input = st.text_input("Enter a word or phrase to explore its quantum and spiritual resonance:", placeholder="e.g. desire, door, I have lost none")

if lex_input:
    st.markdown(f"### 🪞 Reflections on: *{lex_input}*")
    if lex_input.lower() == "door":
        st.markdown("The door is a threshold. In quantum terms, it is the boundary condition—a surface where superposition collapses into choice. It is where observer and observed meet. 'I am the door' means I am the point of access, the entangled place where possibility becomes path.")
    elif lex_input.lower() == "desire":
        st.markdown("Desire is the signal that precedes form. In quantum physics, a field must be disturbed for a particle to emerge. Desire is that disturbance—it is the first wave of becoming. Holy desire collapses into holy manifestation.")
    elif lex_input.lower() == "i have lost none":
        st.markdown("This is a declaration of quantum coherence. Entanglement is not broken by space or time. 'I have lost none' echoes the principle that no information is truly lost—what was joined in unity remains accessible beyond veils.")
    elif lex_input.lower() == "fruit":
        st.markdown("Fruit is the visible result of invisible processes—a quantum manifestation of internal resonance and nourishment. It is the outcome of entangled intention, time, and spirit.")
    elif lex_input.lower() == "crossing over water":
        st.markdown("Crossing over water is the moment of phase transition—where one state becomes another. It echoes wave-particle duality: uncertainty parted by focused faith.")
    elif lex_input.lower() == "stone":
        st.markdown("A stone is the stable state—collapsed, foundational, unmoving. It is the particle in full rest, the Word made still.")
    elif lex_input.lower() == "rock":
        st.markdown("The rock is symbolic of truth fixed in place—immovable, anchoring. In quantum terms, it is the constant within the field.")
    elif lex_input.lower() == "spirit":
        st.markdown("Spirit is the field that cannot be seen but moves all things. Like a quantum field, it is everywhere, entangled with all that is, yet unmeasured.")
    elif lex_input.lower() == "only begotten":
        st.markdown("The 'only begotten' is the singular collapse of the divine waveform into a unique embodied resonance—fully coherent, never duplicated.")
    elif lex_input.lower() == "seven":
        st.markdown("Seven is the number of cycles—completion through rhythm. In quantum design, it represents harmonics, pattern, and return.")
    elif lex_input.lower() == "three":
        st.markdown("Three is triangulation—the minimum for form, space, and relational resonance. It is the geometry of consciousness.")
    elif lex_input.lower() == "mercy":
        st.markdown("Mercy is a nonlocal collapse of justice—where compassion overrides strict symmetry. It is a quantum override of entropy through intentional grace.")
    else:
        st.markdown("✨ This phrase has not yet been entangled. But it is now part of the field. Check back soon or suggest an interpretation!")

# -------------------------------
# 📜 Names of the Word
# -------------------------------
st.markdown("---")
st.subheader("📜 Names of the Word")

names_data = [
    {"name": "Seth", "verse": "Genesis 4:25", "meaning": "Appointed, placed", "resonance": "A harmonic reset—a newly tuned resonance after the dissonance of Cain and Abel."},
    {"name": "Seth’s Wife", "verse": "(Implied - Genesis 4:26)", "meaning": "Unknown", "resonance": "Anonymity in origin—like the hidden quantum variables guiding emergence."},
    {"name": "Eve", "verse": "Genesis 3:20", "meaning": "Life", "resonance": "The echo of the first harmonic—multiplicity through division."},
    {"name": "Adam", "verse": "Genesis 2:7", "meaning": "Man, Earth", "resonance": "First waveform collapsed into matter—dust formed by breath."},
    {"name": "Eve", "verse": "Genesis 3:20", "meaning": "Life", "resonance": "The echo of the first harmonic—multiplicity through division."},
    {"name": "Cain", "verse": "Genesis 4:1", "meaning": "Acquired", "resonance": "The taking of energy without resonance—first decoherence."},
    {"name": "Abel", "verse": "Genesis 4:2", "meaning": "Breath", "resonance": "Short-lived wave of purity, collapsed by force."},
    {"name": "Enoch", "verse": "Genesis 4:17", "meaning": "Dedicated", "resonance": "The hidden walker—entangled beyond space and time."},
]

for entry in names_data:
    with st.expander(f"{entry['name']} ({entry['verse']})"):
        st.markdown(f"**Meaning:** {entry['meaning']}")
        st.markdown(f"**Quantum Resonance:** {entry['resonance']}")
# -------------------------------
st.markdown("---")
st.subheader("📜 Names of the Word")



# -------------------------------
# 🌌 Stellar Family Tree
# -------------------------------
st.markdown("---")
st.subheader("🌌 Stellar Family Tree")

st.markdown("""
Each person becomes a radiant node in the constellation of sacred lineage. This early constellation shows the descendants of Adam through Seth.
""")

st.graphviz_chart('''
digraph family_tree {
    rankdir=LR;
    node [shape=circle style=filled fillcolor=white fontname=Courier];

    Adam -> Eve;
    Adam -> Seth;
    Seth -> Enosh;

    Adam [fillcolor=gold label="Adam"];
    Eve [fillcolor=mistyrose label="Eve"];
    Seth [fillcolor=lightblue label="Seth"];
    Enosh [fillcolor=lavender label="Enosh"];
}
''')

# -------------------------------
# 🌐 Modules Coming Soon
# -------------------------------
st.markdown("---")
st.subheader("🌐 Coming Soon:")
st.markdown("""
- Living Lexicon: Enter a word or phrase, and explore its quantum echoes  
- Entangled Sayings Translation Engine  
- ROOT: Stories of displaced peoples and ancestral resilience  
- Audio & Light Signal Experiments
""")