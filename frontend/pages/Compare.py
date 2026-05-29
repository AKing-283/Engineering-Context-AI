import requests
import streamlit as st

# Load global dark‑futuristic theme
with open("theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

API = "http://127.0.0.1:8000"

st.title("⚔ Engineering Compare")

# Layout concepts side-by-side using columns
col1, col2 = st.columns(2)

with col1:
    a = st.text_input("Concept A", placeholder="e.g., Dijkstra")

with col2:
    b = st.text_input("Concept B", placeholder="e.g., Bellman-Ford")

if st.button("Compare Concepts", type="primary"):
    if not a or not b:
        st.warning("Please provide both Concept A and Concept B to compare.")
    else:
        try:
            response = requests.post(f"{API}/compare", json={"a": a, "b": b})

            if response.status_code == 200:
                comparison_text = response.json().get("comparison", "No comparison text returned.")

                st.subheader("Comparison Evaluation")
                # Render inside an info block or container for clean presentation
                st.info(comparison_text)
            else:
                st.error(f"Backend error: Received status code {response.status_code}")

        except requests.RequestException as e:
            st.error(f"❌ Error connecting to the backend engineering service engine: {e}")