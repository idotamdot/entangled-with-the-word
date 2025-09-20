import streamlit as st

BOOKS_OLD_TESTAMENT = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
    "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
    "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles",
    "Ezra", "Nehemiah", "Esther", "Job", "Psalms",
    "Proverbs", "Ecclesiastes", "Song of Solomon", "Isaiah",
    "Jeremiah", "Lamentations", "Ezekiel", "Daniel",
    "Hosea", "Joel", "Amos", "Obadiah", "Jonah",
    "Micah", "Nahum", "Habakkuk", "Zephaniah",
    "Haggai", "Zechariah", "Malachi",
]

BOOKS_NEW_TESTAMENT = [
    "Matthew", "Mark", "Luke", "John", "Acts",
    "Romans", "1 Corinthians", "2 Corinthians",
    "Galatians", "Ephesians", "Philippians", "Colossians",
    "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy",
    "Titus", "Philemon", "Hebrews", "James",
    "1 Peter", "2 Peter", "1 John", "2 John", "3 John",
    "Jude", "Revelation",
]


BOOKS_QUANTUM_TESTAMENT = [
    "The Book of Entanglement",
]


def render_books_list():
    """Display all books of the Bible as clickable links."""
    st.header("📚 Books of the Bible")

    # Using columns to create a more compact layout
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Old Testament")
        for book in BOOKS_OLD_TESTAMENT:
            st.markdown(f"- <a href='?book={book.replace(' ', '+')}' target='_self'>{book}</a>", unsafe_allow_html=True)

    with col2:
        st.subheader("New Testament")
        for book in BOOKS_NEW_TESTAMENT:
            st.markdown(f"- <a href='?book={book.replace(' ', '+')}' target='_self'>{book}</a>", unsafe_allow_html=True)

    with col3:
        st.subheader("Quantum Testament")
        for book in BOOKS_QUANTUM_TESTAMENT:
            st.markdown(f"- <a href='?book={book.replace(' ', '+')}' target='_self'>{book}</a>", unsafe_allow_html=True)

