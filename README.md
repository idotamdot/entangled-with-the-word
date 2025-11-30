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
- 🔐 **User Authentication** – secure login system with role-based access control.
- 🔧 **Admin Panel for Parables** – curate, approve, and tag community insights (admin only).

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
3. **Set up authentication** (optional but recommended for admin features)
   ```bash
   cp config/auth_config.yaml.example config/auth_config.yaml
   # Edit config/auth_config.yaml with your own credentials
   ```
4. **Launch the app**
   ```bash
   streamlit run entangled_timeline_app.py
   ```

---

## 🔐 Authentication Setup

The app includes a built-in authentication system using `streamlit-authenticator`. To configure:

1. Copy the example config: `cp config/auth_config.yaml.example config/auth_config.yaml`
2. Generate password hashes:
   ```python
   import bcrypt
   print(bcrypt.hashpw('YOUR_PASSWORD'.encode(), bcrypt.gensalt()).decode())
   ```
3. Update `config/auth_config.yaml` with your hashed passwords
4. Change the cookie key to a secure random string

**User Roles:**
- `admin` – Full access including the Admin panel for managing parable suggestions
- `user` – Standard access to all public features

---

> "Write the vision; make it plain on tablets, that he may run who reads it." – Habakkuk 2:2
