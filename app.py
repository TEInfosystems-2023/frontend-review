import streamlit as st

from frontend.styles import load_styles
from frontend.voice_to_voice import voice_to_voice


st.set_page_config(
    page_title="Voice AI",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="collapsed",
)


load_styles()


# =====================================================
# HEADER
# =====================================================

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


# =====================================================
# VOICE AI
# =====================================================

voice_to_voice()