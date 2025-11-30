# Copilot Instructions for Entangled with the Word

## Project Overview

**Entangled with the Word** is a Streamlit-based web application that bridges quantum physics concepts with spiritual reflection. The app provides sacred dialogue, poetic reflection, and community contribution features.

## Technology Stack

- **Framework:** Streamlit (Python)
- **Dependencies:** streamlit, openai, pandas
- **Styling:** Custom CSS with animations
- **Data Storage:** CSV files in the `data/` directory
- **Deployment:** GitHub Pages (Jekyll) and Streamlit Cloud

## Repository Structure

```
├── entangled_timeline_app.py    # Main Streamlit application
├── scrolls/                      # Feature modules
│   ├── all_books_section.py
│   ├── timeline_section.py
│   ├── communion_project_section.py
│   ├── admin_parables.py
│   └── ...
├── data/                         # CSV data files
├── style/                        # CSS stylesheets
├── .streamlit/                   # Streamlit configuration
├── gospel/                       # Content markdown files
└── images/                       # Static images
```

## Coding Standards

### Python

- Use Python 3.9+ type hints for function signatures (e.g., `list[str]`)
- Follow PEP 8 style guidelines
- Use descriptive variable names that reflect the spiritual/quantum theme
- Keep functions focused and modular
- Handle exceptions gracefully with fallback behaviors

### Streamlit Patterns

- `st.set_page_config()` must be the first Streamlit command
- Use session state (`st.session_state`) for persistence across reruns
- Organize UI sections with clear markdown headers
- Use columns (`st.columns`) for responsive layouts
- Embed custom CSS with `st.markdown(unsafe_allow_html=True)`

### CSS/Styling

- Follow the existing animation patterns (breathe, fadeInUp)
- Maintain the spiritual aesthetic with gradients and glowing effects
- Support multiple visual themes (Nebula, Gold, Ocean, Scroll)
- Use RGBA colors for transparency effects

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run entangled_timeline_app.py
```

## Data Handling

- CSV files are stored in the `data/` directory
- Use the `read_csv_safe()` and `write_csv_safe()` utility functions defined in `entangled_timeline_app.py`
- Always handle missing files gracefully with empty DataFrames
- Sensitive data (API keys, secrets) goes in `.streamlit/secrets.toml` (gitignored)

## Content Guidelines

- Maintain the reverent, contemplative tone of the project
- Content should bridge scientific concepts with spiritual themes
- Use metaphorical language that connects quantum physics to faith
- Scripture references should be accurate and properly attributed

## Testing

- Test UI changes by running the Streamlit app locally
- Verify CSV data operations don't corrupt existing data
- Check that all navigation routes render correctly
- Test visual themes for consistent styling

## Security Considerations

- Never commit secrets or API keys
- `.env` and `.streamlit/secrets.toml` are gitignored
- Validate user inputs in the communion/submission features
- Sanitize any user-generated content before display

## Pull Request Guidelines

- Keep changes focused and minimal
- Update the ROADMAP.md if adding major features
- Include screenshots for UI changes
- Test all affected navigation pages
