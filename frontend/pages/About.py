import streamlit as st

st.set_page_config(layout="wide")

# Neon blue accent
ACCENT = "#00A8E8"

st.markdown(f"""
<style>
.about-title {{
    font-size: 38px;
    font-weight: 800;
    color: {ACCENT};
    text-shadow: 0 0 20px {ACCENT};
}}
.section-header {{
    font-size: 26px;
    font-weight: 700;
    margin-top: 30px;
    color: white;
    border-left: 4px solid {ACCENT};
    padding-left: 12px;
}}
.section-box {{
    background-color: #0A0F1F;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid {ACCENT}33;
    margin-top: 10px;
}}
</style>
""", unsafe_allow_html=True)

st.markdown(f"<div class='about-title'>⚡ About Engineering Context AI</div>", unsafe_allow_html=True)

# Mission Section
st.markdown("<div class='section-header'>🚀 Mission</div>", unsafe_allow_html=True)
st.markdown(f"""
<div class='section-box'>
Engineering Context AI enhances technical learning by converting raw audio explanations into 
structured engineering memory — enabling retrieval, reasoning, and comparison for deeper understanding.
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("<div class='section-header'>💡 Key Features</div>", unsafe_allow_html=True)
st.markdown(f"""
<div class='section-box'>
<ul>
<li><b>Voice → Memory Conversion</b>: Speak engineering concepts, store them as structured knowledge.</li>
<li><b>Automated Transcription</b>: Powered by Groq Whisper (whisper-large-v3).</li>
<li><b>Smart Subject Extraction</b>: Lyzr-powered classification converts text into clean engineering subjects.</li>
<li><b>Context Retrieval</b>: Retrieve memories using similarity search from Qdrant.</li>
<li><b>Concept Comparison</b>: Compare engineering concepts with Lyzr normalization + curated knowledge.</li>
<li><b>Analytics Dashboard</b>: Track learning progression across engineering domains.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Architecture Diagram
st.markdown("<div class='section-header'>🏗️ System Architecture</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class='section-box'>
<pre style="color:{ACCENT}; font-size:15px;">
Speak → Audio Upload  
        ↓  
Groq Whisper (Transcription)  
        ↓  
Lyzr Classification (Concept + Subject Normalization)  
        ↓  
Chunking → Embeddings → Qdrant Vector Store  
        ↓  
Retrieval → Ranking → Context Agents  
        ↓  
Understanding, Comparison, Timeline, Analytics
</pre>
</div>
""", unsafe_allow_html=True)

# Pipeline Section
st.markdown("<div class='section-header'>🔁 Processing Pipeline</div>", unsafe_allow_html=True)
st.markdown(f"""
<div class='section-box'>
<b>1. Audio Input</b> — User speaks engineering concepts  
<b>2. Transcription</b> — Groq Whisper converts speech to text  
<b>3. Subject Extraction</b> — Lyzr classifies the topic  
<b>4. Storage</b> — Qdrant stores embeddings + metadata  
<b>5. Retrieval</b> — Relevant memories fetched based on queries  
<b>6. Comparison</b> — Concepts normalized + evaluated side-by-side  
<b>7. Visualization</b> — Timeline, Analytics, and Progress Tracking  
</div>
""", unsafe_allow_html=True)

# Tech Stack
st.markdown("<div class='section-header'>🛠️ Tech Stack</div>", unsafe_allow_html=True)
st.markdown(f"""
<div class='section-box'>
<ul>
<li><b>Backend:</b> FastAPI, Python</li>
<li><b>Transcription:</b> Groq Whisper (whisper-large-v3)</li>
<li><b>Concept Intelligence:</b> Lyzr Agent API</li>
<li><b>Vector Store:</b> Qdrant</li>
<li><b>Frontend:</b> Streamlit Multipage App</li>
<li><b>Agents:</b> Context Agent, Comparison Agent, Explanation Agent</li>
</ul>
</div>
""", unsafe_allow_html=True)
