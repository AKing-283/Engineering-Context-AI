import requests
import pandas as pd
import streamlit as st

API = "http://127.0.0.1:8000"

st.set_page_config(page_title="Engineering Context AI", layout="wide")
st.title("🧠 Engineering Context AI")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Store Memory",
    "Ask AI",
    "Timeline",
    "Analytics",
    "Voice"
])

# ==========================================
# STORE MEMORY
# ==========================================
with tab1:
    st.header("Store Engineering Reasoning")
    
    subject = st.selectbox(
        "Subject", 
        ["DSA", "Signals", "Electronics", "Mechanical", "General"],
        key="store_subject"
    )
    text = st.text_area("Reasoning", key="store_text")

    if st.button("Store Memory", key="btn_store"):
        if not text.strip():
            st.error("Please enter some reasoning text before storing.")
        else:
            payload = {"subject": subject, "text": text}
            try:
                r = requests.post(f"{API}/store-reasoning", json=payload)
                r.raise_for_status()
                st.json(r.json())
            except requests.exceptions.RequestException as e:
                st.error(f"Backend connection error: {e}")

# ==========================================
# ASK AI
# ==========================================
with tab2:
    st.header("Ask Engineering AI")
    question = st.text_input("Question", key="ask_question")

    if st.button("Ask", key="btn_ask"):
        if not question.strip():
            st.error("Please enter a question.")
        else:
            try:
                r = requests.post(f"{API}/answer", json={"query": question})
                r.raise_for_status()
                data = r.json()
                
                st.success(data.get("response", "No response field found."))
                st.metric("Confidence", data.get("confidence", "N/A"))
            except requests.exceptions.RequestException as e:
                st.error(f"Backend connection error: {e}")

# ==========================================
# TIMELINE
# ==========================================
with tab3:
    st.header("Memory Timeline")

    if st.button("Load Timeline", key="btn_timeline"):
        try:
            r = requests.get(f"{API}/timeline")
            r.raise_for_status()
            data = r.json()
            
            timeline_data = data.get("timeline", [])
            if timeline_data:
                df = pd.DataFrame(timeline_data)
                st.dataframe(df, use_container_width=True)
            else:
                st.info("No timeline events found.")
        except requests.exceptions.RequestException as e:
            st.error(f"Backend connection error: {e}")

# ==========================================
# ANALYTICS
# ==========================================
with tab4:
    st.header("Engineering Analytics")

    if st.button("Load Analytics", key="btn_analytics"):
        try:
            r = requests.get(f"{API}/analytics")
            r.raise_for_status()
            data = r.json()

            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Subjects")
                st.json(data.get("subjects", {}))
            with col2:
                st.subheader("Concepts")
                st.json(data.get("concepts", {}))

            st.metric("Total Memory", data.get("total_memories", 0))
        except requests.exceptions.RequestException as e:
            st.error(f"Backend connection error: {e}")

# ==========================================
# VOICE SIMULATION
# ==========================================
with tab5:
    st.header("Omi Voice Simulation")
    transcript = st.text_area("Voice Transcript", key="voice_transcript")
    subject = st.selectbox(
        "Voice Subject", 
        ["DSA", "Signals", "Electronics", "Mechanical"],
        key="voice_subject"
    )

    if st.button("Send Voice", key="btn_voice"):
        if not transcript.strip():
            st.error("Please enter a voice transcript text.")
        else:
            payload = {"subject": subject, "transcript": transcript}
            try:
                r = requests.post(f"{API}/omi-webhook", json=payload)
                r.raise_for_status()
                st.json(r.json())
            except requests.exceptions.RequestException as e:
                st.error(f"Backend connection error: {e}")