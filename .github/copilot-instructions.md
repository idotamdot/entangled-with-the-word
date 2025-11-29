# Copilot Instructions for Entangled with the Word

## Project Overview

Entangled with the Word is a quantum-spiritual web application built with Streamlit that bridges ancient scripture with quantum curiosity. It features sacred dialogue, poetic reflections, and community contributions through an interactive interface with themes of resonance, perception, and divine coherence.

## Technology Stack

- **Framework**: Streamlit (Python web framework)
- **Language**: Python 3.x
- **AI Integration**: OpenAI API
- **Data Processing**: pandas
- **Data Storage**: CSV files in the `data/` directory
- **Styling**: Custom CSS embedded in Streamlit markdown

## Project Structure

```
├── entangled_timeline_app.py    # Main Streamlit application entry point
├── scrolls/                      # Feature modules
│   ├── all_books_section.py     # Books of the Bible navigation
│   ├── timeline_section.py      # Quantum Parables Timeline
│   ├── communion_project_section.py  # Community reflections
│   ├── admin_parables.py        # Admin panel for parable management
│   ├── books_of_the_bible.py    # Bible book data
│   ├── parables_of_jesus.py     # Parables data
│   └── categories.py            # Category definitions
├── data/                         # CSV data storage
├── style/                        # Additional style assets
├── images/                       # Image assets
├── gospel/                       # Gospel content
├── EntangledGardenScrolls        # Garden scrolls content file
├── .streamlit/                   # Streamlit configuration
└── requirements.txt             # Python dependencies
```

## Code Style Guidelines

### Python Conventions
- Use type hints for function parameters and return values (e.g., `list[str] | None`)
- Follow PEP 8 style guidelines
- Use descriptive variable names that reflect the spiritual/quantum theme when appropriate
- Keep functions focused and single-purpose

### Streamlit Patterns
- Always call `st.set_page_config()` as the first Streamlit command
- Use `st.session_state` for maintaining state across reruns
- Prefer `st.markdown()` with `unsafe_allow_html=True` for custom HTML/CSS
- Use Streamlit columns (`st.columns()`) for layout

### CSS/Styling
- Use CSS animations (keyframes) for visual effects like breathing circles
- Apply the `.fade-in` class for entrance animations
- Use `.scroll-card` class for card-style content containers
- Support multiple visual themes (Nebula, Gold, Ocean, Scroll)

## Data Handling

- Use `read_csv_safe()` and `write_csv_safe()` helper functions for CSV operations
- Always handle file not found gracefully
- Store user-generated content in CSV files under `data/`

## Environment and Configuration

- Sensitive configuration goes in `.streamlit/secrets.toml` (never commit)
- Environment variables stored in `.env` files (never commit)
- The `.gitignore` already excludes sensitive files

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run entangled_timeline_app.py
```

## Module Guidelines

When creating new scrolls/modules:
1. Create a new Python file in the `scrolls/` directory
2. Define a main render function (e.g., `render_new_section()`)
3. Import and add the function to `entangled_timeline_app.py`
4. Add navigation entry in the sidebar radio options

## Content Tone

- Maintain a reverent, contemplative tone in user-facing text
- Use metaphors connecting quantum physics concepts with spiritual themes
- Include relevant scripture references where appropriate
- Use emoji icons consistently with existing patterns (✨, 🌌, 📜, etc.)

## Constraints

- Do not commit secrets, API keys, or `.env` files
- Do not modify CSV data files unless implementing data-related features
- Preserve the existing visual theme system
- Maintain backward compatibility with existing data structures
