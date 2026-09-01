import streamlit as st

from frontend.styles import load_styles
from frontend.speech_to_text import speech_to_text
from frontend.text_to_speech import text_to_speech
from frontend.voice_to_voice import voice_to_voice


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Voice AI",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

load_styles()


# ============================================================
# SESSION STATE
# ============================================================

if "mode" not in st.session_state:
    st.session_state.mode = "Speech to Text"


# ============================================================
# HEADER
# ============================================================

left, center, right = st.columns([1, 2, 1])

with left:
    st.markdown(
        '<div class="menu-icon">☰</div>',
        unsafe_allow_html=True,
    )

with center:
    st.markdown(
        '<div class="brand">VOICE AI</div>',
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        '<div class="profile-icon">♙</div>',
        unsafe_allow_html=True,
    )

# ============================================================
# MODE SELECTOR
# ============================================================

col1, col2, col3 = st.columns(3, gap="small")


with col1:
    if st.button(
        "Speech to Text",
        key="mode_stt",
        use_container_width=True,
        type="primary"
        if st.session_state.mode == "Speech to Text"
        else "secondary",
    ):
        st.session_state.mode = "Speech to Text"
        st.rerun()


with col2:
    if st.button(
        "Text to Speech",
        key="mode_tts",
        use_container_width=True,
        type="primary"
        if st.session_state.mode == "Text to Speech"
        else "secondary",
    ):
        st.session_state.mode = "Text to Speech"
        st.rerun()


with col3:
    if st.button(
        "Voice to Voice",
        key="mode_v2v",
        use_container_width=True,
        type="primary"
        if st.session_state.mode == "Voice to Voice"
        else "secondary",
    ):
        st.session_state.mode = "Voice to Voice"
        st.rerun()


# ============================================================
# DISPLAY SELECTED MODE
# ============================================================

if st.session_state.mode == "Speech to Text":

    speech_to_text()


elif st.session_state.mode == "Text to Speech":

    text_to_speech()


elif st.session_state.mode == "Voice to Voice":

    voice_to_voice()