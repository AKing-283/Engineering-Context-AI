import pandas as pd
import requests
import streamlit as st

API = "http://127.0.0.1:8000"

st.title("🕒 Learning Timeline")

try:
    response = requests.get(f"{API}/timeline")
    data = response.json()
    timeline = data.get("timeline", [])

    if timeline:
        df = pd.DataFrame(timeline)

        # Reordering columns gracefully for better visual scanning
        desired_order = ["timestamp", "subject", "concept", "reason"]
        existing_order = [col for col in desired_order if col in df.columns]
        remaining_cols = [col for col in df.columns if col not in existing_order]
        df = df[existing_order + remaining_cols]

        # Render timeline items inside an interactive data table with hidden indexes
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "timestamp": st.column_config.TextColumn("Time Recorded"),
                "subject": st.column_config.TextColumn("Domain"),
                "concept": st.column_config.TextColumn("Core Concept"),
                "reason": st.column_config.TextColumn("Engineering Context"),
            },
        )
    else:
        st.info("Your engineering timeline is currently empty. Record some insights to get started!")

except requests.exceptions.ConnectionError:
    st.error("❌ Unable to reach the backend service timeline registry.")