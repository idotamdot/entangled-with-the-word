"""
Constellation View Module.

Visualizes relationships between spiritual and quantum concepts as a glowing constellation.
"""
import streamlit as st


# Configuration constants
CONSTELLATION_CONTAINER_HEIGHT = 500  # Height of the constellation container in pixels
CONSTELLATION_IFRAME_HEIGHT = 620  # Height of the iframe (container + padding)
BACKGROUND_STARS_COUNT = 50  # Number of twinkling background stars

# Constellation nodes representing key concepts from the project
CONSTELLATION_NODES = [
    {"id": "logos", "label": "The Logos", "x": 50, "y": 20, "size": 12, "color": "#FFD700"},
    {"id": "quantum", "label": "Quantum Field", "x": 25, "y": 40, "size": 10, "color": "#8be9fd"},
    {"id": "spirit", "label": "Spirit", "x": 75, "y": 40, "size": 10, "color": "#bd93f9"},
    {"id": "light", "label": "Light", "x": 15, "y": 60, "size": 8, "color": "#f1fa8c"},
    {"id": "love", "label": "Love", "x": 85, "y": 60, "size": 8, "color": "#ff79c6"},
    {"id": "garden", "label": "Garden", "x": 35, "y": 75, "size": 9, "color": "#50fa7b"},
    {"id": "communion", "label": "Communion", "x": 65, "y": 75, "size": 9, "color": "#ffb86c"},
    {"id": "neutron", "label": "Neutron", "x": 20, "y": 85, "size": 7, "color": "#6272a4"},
    {"id": "soul", "label": "Soul", "x": 50, "y": 55, "size": 11, "color": "#f8f8f2"},
    {"id": "word", "label": "The Word", "x": 80, "y": 85, "size": 7, "color": "#ff5555"},
]

# Connections between nodes representing relationships
CONSTELLATION_EDGES = [
    {"from": "logos", "to": "quantum"},
    {"from": "logos", "to": "spirit"},
    {"from": "logos", "to": "soul"},
    {"from": "quantum", "to": "light"},
    {"from": "quantum", "to": "neutron"},
    {"from": "quantum", "to": "soul"},
    {"from": "spirit", "to": "love"},
    {"from": "spirit", "to": "soul"},
    {"from": "light", "to": "garden"},
    {"from": "love", "to": "communion"},
    {"from": "garden", "to": "neutron"},
    {"from": "garden", "to": "soul"},
    {"from": "communion", "to": "word"},
    {"from": "communion", "to": "soul"},
    {"from": "soul", "to": "word"},
]


def _generate_constellation_html() -> str:
    """Generate HTML/CSS/JS for the interactive constellation visualization."""
    nodes_js = "[\n"
    for node in CONSTELLATION_NODES:
        nodes_js += f'        {{id: "{node["id"]}", label: "{node["label"]}", x: {node["x"]}, y: {node["y"]}, size: {node["size"]}, color: "{node["color"]}"}},\n'
    nodes_js += "    ]"

    edges_js = "[\n"
    for edge in CONSTELLATION_EDGES:
        edges_js += f'        {{from: "{edge["from"]}", to: "{edge["to"]}"}},\n'
    edges_js += "    ]"

    return f"""
    <style>
        .constellation-container {{
            position: relative;
            width: 100%;
            height: {CONSTELLATION_CONTAINER_HEIGHT}px;
            background: radial-gradient(ellipse at center, #1a1a2e 0%, #0f0f23 50%, #000000 100%);
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 0 40px rgba(99, 102, 241, 0.2);
        }}

        .constellation-canvas {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }}

        .constellation-node {{
            position: absolute;
            border-radius: 50%;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .constellation-node:hover {{
            transform: scale(1.5);
            z-index: 100;
        }}

        .constellation-label {{
            position: absolute;
            color: #e0f7fa;
            font-size: 11px;
            font-family: 'Georgia', serif;
            white-space: nowrap;
            pointer-events: none;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
            opacity: 0;
            transition: opacity 0.3s ease;
            transform: translateX(-50%);
            left: 50%;
            top: calc(100% + 8px);
        }}

        .constellation-node:hover .constellation-label {{
            opacity: 1;
        }}

        @keyframes twinkle {{
            0%, 100% {{ opacity: 0.7; box-shadow: 0 0 10px currentColor; }}
            50% {{ opacity: 1; box-shadow: 0 0 20px currentColor, 0 0 30px currentColor; }}
        }}

        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.1); }}
        }}

        .star-glow {{
            animation: twinkle 3s ease-in-out infinite;
        }}

        .constellation-title {{
            text-align: center;
            color: #e0f7fa;
            font-family: 'Georgia', serif;
            font-size: 1.5em;
            margin-bottom: 10px;
            text-shadow: 0 0 20px rgba(139, 233, 253, 0.5);
        }}

        .constellation-subtitle {{
            text-align: center;
            color: #94a3b8;
            font-family: 'Georgia', serif;
            font-style: italic;
            font-size: 0.95em;
            margin-bottom: 20px;
        }}

        /* Twinkling background stars */
        .bg-star {{
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: twinkle 4s ease-in-out infinite;
        }}
    </style>

    <div class="constellation-title">✨ The Constellation of Entanglement ✨</div>
    <div class="constellation-subtitle">"Where quantum threads weave sacred connections"</div>

    <div class="constellation-container" id="constellation">
        <svg class="constellation-canvas" id="constellationSvg"></svg>
    </div>

    <script>
        (function() {{
            const nodes = {nodes_js};
            const edges = {edges_js};

            const container = document.getElementById('constellation');
            const svg = document.getElementById('constellationSvg');
            const containerRect = container.getBoundingClientRect();

            // Add background stars
            for (let i = 0; i < {BACKGROUND_STARS_COUNT}; i++) {{
                const star = document.createElement('div');
                star.className = 'bg-star';
                star.style.left = Math.random() * 100 + '%';
                star.style.top = Math.random() * 100 + '%';
                star.style.width = (Math.random() * 2 + 1) + 'px';
                star.style.height = star.style.width;
                star.style.animationDelay = Math.random() * 4 + 's';
                star.style.opacity = Math.random() * 0.5 + 0.2;
                container.appendChild(star);
            }}

            // Create node lookup
            const nodeMap = {{}};
            nodes.forEach(n => nodeMap[n.id] = n);

            // Draw edges
            edges.forEach((edge, idx) => {{
                const fromNode = nodeMap[edge.from];
                const toNode = nodeMap[edge.to];
                if (fromNode && toNode) {{
                    const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                    line.setAttribute('x1', fromNode.x + '%');
                    line.setAttribute('y1', fromNode.y + '%');
                    line.setAttribute('x2', toNode.x + '%');
                    line.setAttribute('y2', toNode.y + '%');
                    line.setAttribute('stroke', 'rgba(139, 233, 253, 0.3)');
                    line.setAttribute('stroke-width', '1');
                    line.style.filter = 'drop-shadow(0 0 3px rgba(139, 233, 253, 0.5))';
                    svg.appendChild(line);
                }}
            }});

            // Create nodes
            nodes.forEach((node, idx) => {{
                const el = document.createElement('div');
                el.className = 'constellation-node star-glow';
                el.style.left = 'calc(' + node.x + '% - ' + (node.size / 2) + 'px)';
                el.style.top = 'calc(' + node.y + '% - ' + (node.size / 2) + 'px)';
                el.style.width = node.size + 'px';
                el.style.height = node.size + 'px';
                el.style.backgroundColor = node.color;
                el.style.color = node.color;
                el.style.boxShadow = '0 0 ' + (node.size * 2) + 'px ' + node.color;
                el.style.animationDelay = (idx * 0.3) + 's';

                const label = document.createElement('span');
                label.className = 'constellation-label';
                label.textContent = node.label;
                el.appendChild(label);

                container.appendChild(el);
            }});
        }})();
    </script>
    """


def render_constellation():
    """Render the constellation view showing relationships between concepts."""
    st.header("🌌 Constellation View")
    st.markdown("""
    *Behold the sacred web of interconnected truths—where quantum physics and spirituality 
    dance together in eternal entanglement.*
    
    **Hover over each star** to reveal its name. The glowing threads between them represent 
    the relationships that bind these concepts together in the tapestry of understanding.
    """)

    # Render the interactive constellation
    st.components.v1.html(_generate_constellation_html(), height=CONSTELLATION_IFRAME_HEIGHT, scrolling=False)

    # Legend section
    st.markdown("---")
    st.markdown("### 📖 The Stars Explained")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **🌟 The Logos** — The divine Word, the cosmic blueprint  
        **💠 Quantum Field** — The fabric of possibility  
        **💜 Spirit** — The breath of the sacred  
        **💛 Light** — The messenger between realms  
        **💗 Love** — The force that entangles all
        """)

    with col2:
        st.markdown("""
        **🌿 Garden** — Where intention takes root  
        **🍊 Communion** — The shared table of souls  
        **🔵 Neutron** — Sacred neutrality in balance  
        **⚪ Soul** — The center of all connection  
        **❤️ The Word** — Scripture made manifest
        """)

    st.markdown("---")
    st.info("""
    *"As above, so below. As within, so without. The constellation reveals that all 
    things are connected—quantum entanglement is but the scientific name for what 
    mystics have always known: we are all One."*
    """)
