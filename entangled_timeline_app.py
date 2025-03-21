# Streamlit app file - previously created
# if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8501))  # Change default from 8501
    st.run(port=port, host='0.0.0.0')

