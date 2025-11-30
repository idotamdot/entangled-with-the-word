"""Dashboard section with daily and weekly summaries."""
import os
from datetime import datetime, timedelta

import pandas as pd
import streamlit as st


def _load_reflections() -> pd.DataFrame:
    """Load reflections data."""
    path = "data/communion_reflections.csv"
    if not os.path.exists(path):
        return pd.DataFrame(columns=["timestamp", "entry"])
    try:
        df = pd.read_csv(path)
        if not df.empty:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df
    except Exception:
        return pd.DataFrame(columns=["timestamp", "entry"])


def _load_candles() -> pd.DataFrame:
    """Load candle data."""
    path = "data/communion_candles.csv"
    if not os.path.exists(path):
        return pd.DataFrame(columns=["entry_index", "count"])
    try:
        df = pd.read_csv(path)
        if not df.empty:
            df["entry_index"] = df["entry_index"].astype(int)
            df["count"] = df["count"].astype(int)
        return df
    except Exception:
        return pd.DataFrame(columns=["entry_index", "count"])


def _load_approved_parables() -> pd.DataFrame:
    """Load approved parables data."""
    path = "gospel/approved_parables.csv"
    if not os.path.exists(path):
        return pd.DataFrame(columns=["timestamp", "suggestion", "tag"])
    try:
        df = pd.read_csv(path)
        if not df.empty:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df
    except Exception:
        return pd.DataFrame(columns=["timestamp", "suggestion", "tag"])


def render_dashboard():
    """Render the dashboard with daily and weekly summaries."""
    st.markdown("""
    ---
    ## 📊 Sacred Dashboard
    A glimpse into the collective spiritual activity of our community.
    ---
    """, unsafe_allow_html=True)

    # Load data
    reflections = _load_reflections()
    candles = _load_candles()
    parables = _load_approved_parables()

    # Calculate dates
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)

    # Create tabs for daily and weekly views
    tab_daily, tab_weekly = st.tabs(["📅 Daily Summary", "📆 Weekly Summary"])

    with tab_daily:
        _render_daily_summary(reflections, candles, parables, today)

    with tab_weekly:
        _render_weekly_summary(reflections, candles, parables, today, week_ago)


def _render_daily_summary(
    reflections: pd.DataFrame,
    candles: pd.DataFrame,
    parables: pd.DataFrame,
    today,
):
    """Render daily summary statistics."""
    st.markdown("### ✨ Today's Spiritual Activity")

    # Filter data for today
    if not reflections.empty:
        today_reflections = reflections[reflections["timestamp"].dt.date == today]
        reflection_count = len(today_reflections)
    else:
        today_reflections = pd.DataFrame()
        reflection_count = 0

    # Calculate total candles lit today
    total_candles = candles["count"].sum() if not candles.empty else 0

    # Parables added today
    if not parables.empty:
        today_parables = parables[parables["timestamp"].dt.date == today]
        parable_count = len(today_parables)
    else:
        parable_count = 0

    # Display metrics in columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="🙏 Reflections Today",
            value=reflection_count,
            help="Number of reflections shared today",
        )

    with col2:
        st.metric(
            label="🕯️ Total Candles Lit",
            value=total_candles,
            help="Total candles lit across all reflections",
        )

    with col3:
        st.metric(
            label="📜 Parables Approved",
            value=parable_count,
            help="Number of parables approved today",
        )

    st.markdown("---")

    # Top reflections today
    st.markdown("### 🔥 Today's Most Illuminated Reflections")

    if today_reflections.empty:
        st.info("No reflections shared today yet. Be the first to light the scroll!")
    else:
        # Merge with candles to get counts
        today_reflections = today_reflections.reset_index(drop=True)
        today_reflections["id"] = today_reflections.index

        if not candles.empty:
            candles_renamed = candles.rename(columns={"entry_index": "id"})
            today_reflections = pd.merge(
                today_reflections, candles_renamed, on="id", how="left"
            )
            today_reflections["count"] = today_reflections["count"].fillna(0).astype(int)
        else:
            today_reflections["count"] = 0

        # Sort by candle count and show top 3
        top_reflections = today_reflections.sort_values(by="count", ascending=False).head(3)

        for _, row in top_reflections.iterrows():
            time_str = row["timestamp"].strftime("%H:%M")
            st.markdown(f"""
            <div style='background: rgba(255,255,255,0.05); border-radius: 10px; padding: 15px; margin: 10px 0; border-left: 3px solid #ffd700;'>
                <strong>🕯️ {row['count']}</strong> | <em style='color: #aaa;'>{time_str}</em><br>
                {row['entry']}
            </div>
            """, unsafe_allow_html=True)


def _render_weekly_summary(
    reflections: pd.DataFrame,
    candles: pd.DataFrame,
    parables: pd.DataFrame,
    today,
    week_ago,
):
    """Render weekly summary statistics."""
    st.markdown("### 📈 This Week's Spiritual Journey")

    # Filter data for the week
    if not reflections.empty:
        week_reflections = reflections[
            (reflections["timestamp"].dt.date >= week_ago)
            & (reflections["timestamp"].dt.date <= today)
        ]
        weekly_reflection_count = len(week_reflections)
    else:
        week_reflections = pd.DataFrame()
        weekly_reflection_count = 0

    # Calculate total candles
    total_candles = candles["count"].sum() if not candles.empty else 0

    # Parables this week
    if not parables.empty:
        week_parables = parables[
            (parables["timestamp"].dt.date >= week_ago)
            & (parables["timestamp"].dt.date <= today)
        ]
        weekly_parable_count = len(week_parables)
    else:
        weekly_parable_count = 0

    # Display weekly metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="🙏 Reflections This Week",
            value=weekly_reflection_count,
            help="Number of reflections shared in the last 7 days",
        )

    with col2:
        st.metric(
            label="🕯️ Total Candles Lit",
            value=total_candles,
            help="Total candles lit across all reflections",
        )

    with col3:
        st.metric(
            label="📜 Parables This Week",
            value=weekly_parable_count,
            help="Number of parables approved in the last 7 days",
        )

    st.markdown("---")

    # Daily breakdown chart
    st.markdown("### 📊 Daily Reflection Activity")

    if not week_reflections.empty:
        # Group by date
        daily_counts = (
            week_reflections.groupby(week_reflections["timestamp"].dt.date)
            .size()
            .reset_index(name="reflections")
        )
        daily_counts.columns = ["date", "reflections"]
        daily_counts["date"] = pd.to_datetime(daily_counts["date"])

        # Create a complete date range
        date_range = pd.date_range(start=week_ago, end=today, freq="D")
        complete_df = pd.DataFrame({"date": date_range})
        complete_df = pd.merge(complete_df, daily_counts, on="date", how="left")
        complete_df["reflections"] = complete_df["reflections"].fillna(0).astype(int)

        # Display as bar chart
        st.bar_chart(complete_df.set_index("date")["reflections"])
    else:
        st.info("No reflections recorded this week yet.")

    st.markdown("---")

    # Category breakdown for parables
    st.markdown("### 🏷️ Parable Categories This Week")

    if not parables.empty and "tag" in parables.columns:
        week_parables = parables[
            (parables["timestamp"].dt.date >= week_ago)
            & (parables["timestamp"].dt.date <= today)
        ]
        if not week_parables.empty:
            category_counts = week_parables["tag"].value_counts()
            for tag, count in category_counts.items():
                st.markdown(f"**{tag}**: {count} parable(s)")
        else:
            st.info("No parables approved this week.")
    else:
        st.info("No parable data available.")
