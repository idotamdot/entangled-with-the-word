# -------------------------------
# Communion Project Section
# -------------------------------


    st.markdown("""
    ---
    ## 🌟 Communion: A Living Gospel
    A sacred digital space where presence is honored, questions are holy, and shared insight becomes scripture.
    ---
    """, unsafe_allow_html=True)

    st.markdown("### 💬 Share your reflection:")
    user_reflection = st.text_area("Enter a poetic thought, question, or spiritual insight:", key="communion_entry")

    if st.button("🙏 Submit Reflection"):
        if user_reflection.strip():
            timestamp = datetime.datetime.now().isoformat()
            df = pd.DataFrame([[timestamp, user_reflection]], columns=["timestamp", "entry"])
            try:
                existing = pd.read_csv("communion_reflections.csv")
                df = pd.concat([existing, df], ignore_index=True)
            except FileNotFoundError:
                pass
            df.to_csv("communion_reflections.csv", index=False)
            st.success("Your presence has been recorded in the scroll.")

    st.markdown("---")
    st.markdown("### 📜 The Table of Light")

    try:
        entries = pd.read_csv("communion_reflections.csv")
        entries['timestamp'] = pd.to_datetime(entries['timestamp'])
        today = datetime.date.today()
        entries_today = entries[entries['timestamp'].dt.date == today]
        entries['candles'] = 0

        candle_file = "communion_candles.csv"
        if os.path.exists(candle_file):
            candles_df = pd.read_csv(candle_file)
            for _, c in candles_df.iterrows():
                if c['index'] < len(entries):
                    entries.loc[c['index'], 'candles'] = c['count']
        else:
            candles_df = pd.DataFrame(columns=["index", "count"])

        entries = entries.sort_values(by='candles', ascending=False).reset_index(drop=True)

        st.markdown("### ✨ Top 3 Highlights of the Day")
        top3 = entries_today.sort_values(by='candles', ascending=False).head(3)
        if top3.empty:
            st.markdown("""
                <div class='fade-in' style='font-style: italic; text-align: center; padding: 1em;'>
                    No reflections yet today. Be the first to light the scroll.
                </div>
            """, unsafe_allow_html=True)
        else:
            for i, row in top3.iterrows():
                st.markdown(f"<div class='reflection-block'><strong>🕯 {row['candles']}</strong><br><em>{row['timestamp'][:16]}</em><br>{row['entry']}</div>", unsafe_allow_html=True)

        st.markdown("### 🔥 Most Lit Reflections")
        for i, row in entries.iterrows():
            count = candles_df[candles_df["index"] == i]["count"].values[0] if i in candles_df["index"].values else 0

            col1, col2 = st.columns([8, 1])
            with col1:
                st.markdown(f"🕯 *{row['timestamp'][:16]}*")
                st.markdown(f"> {row['entry']}")
            with col2:
                if st.button(f"🕯 {count}", key=f"candle_{i}"):
                    if i in candles_df["index"].values:
                        candles_df.loc[candles_df["index"] == i, "count"] += 1
                    else:
                        candles_df = pd.concat([candles_df, pd.DataFrame([[i, 1]], columns=["index", "count"])], ignore_index=True)
                    candles_df.to_csv(candle_file, index=False)
                    st.experimental_rerun()

        st.markdown("---")

    except FileNotFoundError:
        st.info("No reflections have been added yet.")
