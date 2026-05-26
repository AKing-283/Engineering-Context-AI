import requests
import streamlit as st

API = "http://127.0.0.1:8000"

st.title("🎙 Engineering Memory")

subject = st.selectbox("Subject", ["DSA", "Electronics", "Signals", "Mechanical"])
text = st.text_area("Engineering reasoning")

if st.button("Store Memory"):
    payload = {"subject": subject, "text": text}
    response = requests.post(f"{API}/store-reasoning", json=payload)
    st.json(response.json())

st.divider()

query = st.text_input("Retrieve Context")

if st.button("Search"):
    result = requests.post(f"{API}/retrieve", json={"query": query})
    data = result.json()

    for memory in data.get("memory", []):
        # Using st.container with a border to replicate a clean "card" interface
        with st.container(border=True):
            st.markdown(f"### {memory.get('concept', 'Unknown Concept')}")
            st.write(memory.get("reason", "No reasoning details available."))

            col1, col2 = st.columns([1, 1])
            with col1:
                st.caption(f"**Subject:** {memory.get('subject')}")
            with col2:
                if "score" in memory:
                    st.caption(f"**Match Score:** {memory['score']}")