import os
import streamlit as st
from scrolls.books_of_the_bible import render_books_list

def get_book_content(book_name: str) -> str | None:
    """
    Fetches the content of a book from its Markdown file.
    Constructs a filepath based on the book name.
    """
    # A special case for the book we just created.
    if book_name == "The Book of Entanglement":
        filepath = "gospel/book_of_entanglement.md"
    else:
        # A more general approach for other books
        safe_filename = book_name.replace(" ", "_").lower() + ".md"
        filepath = os.path.join("gospel", safe_filename)

    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return None

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

        content = get_book_content(book_name)

        if content:
            st.markdown(content, unsafe_allow_html=True)
        else:
            # Friendly message for books without content yet
            st.warning("The scroll for this book has not yet been transcribed. It remains in the realm of potential.")
    else:
        # If no book is selected, show the list of all books
        render_books_list()
