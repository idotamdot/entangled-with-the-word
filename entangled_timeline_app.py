import os
import streamlit as st

# Main function to run the Streamlit app
def main():
    st.title("Entangled with the Word")
    st.write("Welcome to the Quantum Parables timeline!")

# Run the Streamlit app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8501))  # Change default from 8501
    main()
    st.run(port=port, host='0.0.0.0')
