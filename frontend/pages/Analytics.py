import pandas as pd
import plotly.express as px
import requests
import streamlit as st

# Load global dark‑futuristic theme
with open("theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

API = "http://127.0.0.1:8000"

st.title("📊 Analytics")

try:
    response = requests.get(f"{API}/analytics")
    data = response.json()

    subjects = data.get("subjects", {})
    concepts = data.get("concepts", {})

    # Create layout layout columns
    col1, col2 = st.columns([2, 1])

    with col1:
        if subjects:
            df = pd.DataFrame(
                {"subject": list(subjects.keys()), "count": list(subjects.values())}
            )

            fig = px.bar(
                df,
                x="subject",
                y="count",
                title="Subject Distribution",
                labels={"subject": "Engineering Domain", "count": "Memory Count"},
                color="subject",
                template="plotly_white",
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No subject distribution metrics tracked yet.")

    with col2:
        st.subheader("Top Extracted Concepts")
        if concepts:
            # Render as a clean metric or dataframe list instead of raw JSON
            concepts_df = pd.DataFrame(
                {"Concept": list(concepts.keys()), "Mentions": list(concepts.values())}
            ).sort_values(by="Mentions", ascending=False)

            st.dataframe(concepts_df, use_container_width=True, hide_index=True)
        else:
            st.info("No analytics insights compiled yet.")

except requests.RequestException as e:
    st.error(f"Error fetching analytics data: {e}")