import streamlit as st

# Load global dark‑futuristic theme
with open("theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Engineering Context AI", layout="wide"
)

st.title("🧠 Engineering Context AI")
st.subheader("Voice → Memory → Retrieval → Understanding")

st.markdown("""
Store engineering reasoning.
Retrieve context.
Compare concepts.
Track learning progression.
""")

st.success("Backend Connected via FastAPI")

# Neon‑blue futuristic About button
st.markdown(
    """
    <style>
    .about-btn {
        display: inline-block;
        padding: 12px 22px;
        margin-top: 20px;
        border-radius: 8px;
        background-color: #001F33;
        color: #00A8E8;
        border: 1px solid #00A8E8;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
        cursor: pointer;
        transition: 0.2s ease-in-out;
        box-shadow: 0 0 12px #00A8E844;
    }
    .about-btn:hover {
        background-color: #002a44;
        box-shadow: 0 0 20px #00A8E8AA;
        transform: scale(1.02);
    }
    </style>

    <a href="/About" target="_self">
        <div class="about-btn">ℹ️ About Engineering Context AI</div>
    </a>
    """,
    unsafe_allow_html=True,
)
