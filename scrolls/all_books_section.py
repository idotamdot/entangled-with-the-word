import os
import streamlit as st
from scrolls.books_of_the_bible import render_books_list

def render_book_content(book_name: str) -> bool:
    """
    Renders a book's content by calling its render function.
    Returns True if successful, False if not found.
    """
    # Handle New Testament books
    if book_name == "Matthew":
        from gospel.new_testament.matthew import render_matthew
        render_matthew()
        return True
    elif book_name == "John":
        from gospel.new_testament.john import render_john
        render_john()
        return True
    elif book_name == "Hebrews":
        from gospel.new_testament.hebrews import render_hebrews
        render_hebrews()
        return True
    
    # Handle Old Testament books
    elif book_name == "Genesis":
        from gospel.old_testament.genesis import render_genesis
        render_genesis()
        return True
    elif book_name == "Psalms":
        from gospel.old_testament.psalms import render_psalms
        render_psalms()
        return True
    elif book_name == "Ecclesiastes":
        from gospel.old_testament.ecclesiastes import render_ecclesiastes
        render_ecclesiastes()
        return True
    elif book_name == "Isaiah":
        from gospel.old_testament.isaiah import render_isaiah
        render_isaiah()
        return True
    elif book_name == "Daniel":
        from gospel.old_testament.daniel import render_daniel
        render_daniel()
        return True
    
    # Handle Quantum Testament
    elif book_name == "The Book of Entanglement":
        filepath = "gospel/book_of_entanglement.md"
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            st.markdown(content, unsafe_allow_html=True)
            return True
    
    return False

def render_all_books_page():
    """
    Renders the 'All Books' page.
    If a 'book' is specified in the query params, it displays the book's content.
    Otherwise, it displays the list of all books.
    """
    # Get the book from query params, if it exists.
    book_name_param = st.query_params.get("book")

    if book_name_param:
        # Decode the book name from URL format (e.g., 'The+Book' -> 'The Book')
        book_name = book_name_param.replace('+', ' ')

        # Provide a link to go back to the main library view
        st.markdown(f"<a href='?page=All+Books' target='_self'>&larr; Back to Full Library</a>", unsafe_allow_html=True)
        st.title(f"📖 {book_name}")

        # Try to render the book content
        if render_book_content(book_name):
            pass  # Content was successfully rendered
        else:
            # Friendly message for books without content yet
            st.warning("The scroll for this book has not yet been transcribed. It remains in the realm of potential.")
    else:
        # If no book is selected, show the list of all books
        render_books_list()
