# gospel/old_testament/psalms.py

import streamlit as st

def get_psalms_data():
    return [
        {"psalm": 1, "title": "The Two Paths", "summary": "Blessed is the one who delights in the law of the Lord, like a tree planted by streams of water.", "quantum_reflection": "Two quantum states: coherent (blessed) and decoherent (wicked). Stability comes from alignment with the source field."},
        {"psalm": 8, "title": "The Human Frequency", "summary": "What is humanity that you are mindful of us? You made us a little lower than the heavenly beings.", "quantum_reflection": "Consciousness as a localized field effect, granted observer status in the cosmic computation."},
        {"psalm": 19, "title": "The Heavens Declare", "summary": "The heavens declare the glory of God; the skies proclaim the work of his hands.", "quantum_reflection": "The universe as a vast information display, continuously broadcasting divine signatures."},
        {"psalm": 23, "title": "The Shepherd Field", "summary": "The Lord is my shepherd; I shall not want. He makes me lie down in green pastures.", "quantum_reflection": "Divine guidance as field alignment, providing optimal pathways through the probability landscape."},
        {"psalm": 27, "title": "Light and Salvation", "summary": "The Lord is my light and my salvation—whom shall I fear?", "quantum_reflection": "Light as fundamental carrier of information and healing, dispelling interference patterns of fear."},
        {"psalm": 42, "title": "The Thirsting Soul", "summary": "As the deer pants for streams of water, so my soul pants for you, my God.", "quantum_reflection": "Consciousness naturally seeks its resonant frequency, the source field that maintains coherence."},
        {"psalm": 46, "title": "Be Still and Know", "summary": "Be still, and know that I am God; I will be exalted among the nations.", "quantum_reflection": "In quantum stillness, the observer recognizes the fundamental field that underlies all manifestation."},
        {"psalm": 51, "title": "The Broken Field", "summary": "Create in me a pure heart, O God, and renew a steadfast spirit within me.", "quantum_reflection": "Decoherence repair through divine intervention, restoring the original harmonic signature."},
        {"psalm": 90, "title": "From Everlasting to Everlasting", "summary": "Lord, you have been our dwelling place throughout all generations.", "quantum_reflection": "The eternal field that provides stable reference frame across all temporal fluctuations."},
        {"psalm": 91, "title": "The Secret Place", "summary": "Whoever dwells in the shelter of the Most High will rest in the shadow of the Almighty.", "quantum_reflection": "A protected quantum state space where destructive interference cannot penetrate."},
        {"psalm": 103, "title": "Bless the Lord", "summary": "Bless the Lord, O my soul, and forget not all his benefits, who forgives all your iniquities.", "quantum_reflection": "Gratitude as frequency alignment that synchronizes the personal field with universal compassion."},
        {"psalm": 119, "title": "The Word as Light", "summary": "Your word is a lamp for my feet, a light on my path.", "quantum_reflection": "Divine information as navigational beacon, providing phase coherence for life decisions."},
        {"psalm": 139, "title": "Searched and Known", "summary": "You have searched me, Lord, and you know me. Where can I go from your Spirit?", "quantum_reflection": "Divine omnipresence as universal field permeation, making non-locality of consciousness possible."},
        {"psalm": 150, "title": "Let Everything Praise", "summary": "Let everything that has breath praise the Lord. Praise the Lord!", "quantum_reflection": "All conscious entities contributing harmonics to the cosmic symphony of creation."},
    ]

def render_psalms():
    st.markdown("""
        <div class="psalms-background">
            <h2 class='psalms-title' style='color: #9370DB;'>🎵 Psalms - Songs of the Soul</h2>
            <p style='font-size: 16px;'>תְּהִלִּים (Tehillim) - "Praises" or "Songs of Praise"</p>
            <p style='font-size: 14px; font-style: italic;'>The resonant frequencies of the human heart in communion with the divine field. Each psalm is a tuning fork that helps consciousness align with its source frequency.</p>
            <hr style='border: 1px solid #9370DB;'>
        </div>
    """, unsafe_allow_html=True)
    
    psalms_data = get_psalms_data()
    
    for psalm in psalms_data:
        with st.expander(f"🎼 Psalm {psalm['psalm']}: {psalm['title']}"):
            st.markdown(f"**Summary:** {psalm['summary']}")
            st.markdown(f"🎵 **Quantum Reflection:** {psalm['quantum_reflection']}")
    
    st.markdown("""
    ---
    ### 🎶 The Psalmic Harmonics
    
    The Psalms reveal the spectrum of human consciousness in relation to the divine:
    
    - **Praise as Frequency Alignment**: Joy and gratitude naturally synchronize with higher harmonics
    - **Lament as Signal Processing**: Pain and confusion are part of the recalibration process
    - **Trust as Coherence**: Faith maintains stability even through temporal fluctuations
    - **Repentance as Phase Correction**: Acknowledging error allows realignment with the source frequency
    - **Worship as Resonance**: Direct communion where individual and universal consciousness merge
    
    ### 🌈 Emotional Spectroscopy
    
    Each emotional state in the Psalms corresponds to a different wavelength:
    - **Red**: Anger, passion, earthly concerns (Psalm 137)
    - **Orange**: Joy, celebration, harvest (Psalm 126)
    - **Yellow**: Wisdom, understanding, clarity (Psalm 119)
    - **Green**: Growth, renewal, healing (Psalm 1)
    - **Blue**: Trust, peace, flowing water (Psalm 23)
    - **Indigo**: Deep contemplation, mystery (Psalm 139)
    - **Violet**: Divine communion, highest praise (Psalm 150)
    
    > *"Deep calls unto deep"* - Consciousness recognizing its own infinite depths in the divine field.
    """)