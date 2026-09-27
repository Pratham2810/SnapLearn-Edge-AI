from pathlib import Path
import tempfile
import streamlit as st

from src.transcribe import transcribe_audio
from src.summarize import build_study_notes, answer_question

st.set_page_config(page_title="SnapLearn Edge", page_icon="⚡", layout="wide")
st.title("⚡ SnapLearn Edge")
st.caption("Private, on-device AI study and meeting copilot designed for Snapdragon-powered HP PCs")

with st.sidebar:
    st.subheader("Edge AI target")
    st.write("Speech: Qualcomm AI Hub Whisper")
    st.write("Reasoning: Qualcomm AI Hub Llama 3.2 3B Instruct")
    st.info("Prototype UI works without bundled model weights. Snapdragon NPU adapters are documented in /docs.")

uploaded = st.file_uploader("Upload a lecture or meeting audio file", type=["wav", "mp3", "m4a", "flac"])

if uploaded:
    suffix = Path(uploaded.name).suffix
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as f:
        f.write(uploaded.getbuffer())
        audio_path = f.name

    if st.button("Generate private smart notes", type="primary"):
        with st.spinner("Processing locally..."):
            transcript = transcribe_audio(audio_path)
            notes = build_study_notes(transcript)
            st.session_state["transcript"] = transcript
            st.session_state["notes"] = notes

if "transcript" in st.session_state:
    left, right = st.columns(2)
    with left:
        st.subheader("Transcript")
        st.write(st.session_state["transcript"])
    with right:
        st.subheader("Smart Notes")
        st.markdown(st.session_state["notes"])

    st.divider()
    q = st.text_input("Ask a question about this session")
    if q:
        st.write(answer_question(q, st.session_state["transcript"]))
