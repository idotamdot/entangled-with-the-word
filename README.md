# ✨ Entangled with the Word

> A quantum-spiritual scroll of reflections, built with Streamlit, OpenAI, and the light of love.

**Entangled with the Word** is a living web app for sacred dialogue, poetic reflection, and community contribution. It bridges ancient scripture with quantum curiosity, empowering users to submit insights, light digital candles, and experience themes of resonance, perception, and divine coherence.

---

## 🌈 Features

- 🧬 **Quantum Parables Timeline** – scroll through entries exploring light, consciousness, and scripture.
- 📚 **Books of the Bible** – view every book from Genesis to Revelation.
- 📕 **Parables of Jesus** – a complete list of Christ's parables.
- 🌿 **Entangled Garden Scrolls** – meditations on intention and connection.
- 📜 **Communion Project** – share reflections and light digital candles.
- 🌌 **Visual Theme Selector** – switch between Nebula, Gold, Ocean, or Scroll aesthetics.
- 🎶 **Ambient Music Playback** – optional meditative background tracks.
- 🔧 **Admin Panel for Parables** – curate, approve, and tag community insights.
- 🔐 **User Authentication** – secure login and session handling for admin features.

---

## 🚀 How to Run Locally

1. **Clone this repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/entangled-with-the-word.git
   cd entangled-with-the-word
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up authentication (optional)**
   ```bash
   # Copy the example config and customize it
   cp config/auth_config.yaml.example config/auth_config.yaml
   # Edit config/auth_config.yaml with your credentials
   ```
4. **Launch the app**
   ```bash
   streamlit run entangled_timeline_app.py
   ```

---

## 🔐 Authentication Setup

The app includes user authentication for admin features. To configure:

1. Copy `config/auth_config.yaml.example` to `config/auth_config.yaml`
2. Generate a password hash using bcrypt:
   ```python
   import bcrypt
   password = 'your_password'
   hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
   print(hashed)
   ```
   Or using streamlit-authenticator (if available):
   ```python
   import streamlit_authenticator as stauth
   hashed = stauth.Hasher.hash('your_password')
   print(hashed)
   ```
3. Update the `password` field in `auth_config.yaml` with the generated hash
4. Change the `cookie.key` to a secure random string for production

**Default credentials** (for development only):
- Username: `admin`
- Password: `admin123`

⚠️ **Important**: Never commit `config/auth_config.yaml` with real credentials to the repository!

---

> "Write the vision; make it plain on tablets, that he may run who reads it." – Habakkuk 2:2
