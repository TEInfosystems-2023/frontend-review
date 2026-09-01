import streamlit as st


def voice_to_voice():

    # =========================================================
    # TITLE
    # =========================================================

    st.markdown(
        """
<h2 class="v2v-title">Voice to Voice</h2>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<p class="v2v-subtitle">
Speak in one language and hear the translated voice
</p>
""",
        unsafe_allow_html=True,
    )

    # =========================================================
    # LANGUAGE SELECTION
    # =========================================================

    col1, col2 = st.columns(2)

    with col1:
        source = st.selectbox(
            "Source Language",
            ["English", "Odia", "Hindi", "Bengali"],
            key="v2v_source_language",
        )

    with col2:
        target = st.selectbox(
            "Target Language",
            ["Odia", "English", "Hindi", "Bengali"],
            key="v2v_target_language",
        )

    # =========================================================
    # VOICE FLOW
    # =========================================================

    left, middle, right = st.columns([2, 1, 2])

    with left:
        st.markdown(
            f"""
<div class="voice-card">
<div class="voice-circle">🎙️</div>
<div class="voice-title">YOUR VOICE</div>
<div class="voice-language">{source}</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with middle:
        st.markdown(
            """
<div class="voice-arrow">→</div>
""",
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            f"""
<div class="voice-card">
<div class="voice-circle">🔊</div>
<div class="voice-title">TRANSLATED VOICE</div>
<div class="voice-language">{target}</div>
</div>
""",
            unsafe_allow_html=True,
        )

    # =========================================================
    # RECORD VOICE
    # =========================================================

    conversation_audio = st.audio_input(
        "Record your voice",
        sample_rate=16000,
        key="v2v_recorder",
    )

    # =========================================================
    # AUDIO PREVIEW
    # =========================================================

    if conversation_audio is not None:
        st.audio(conversation_audio)

    # =========================================================
    # START CONVERSATION
    # =========================================================

    if st.button(
        "🎙️  Start Conversation",
        key="conversation_button",
        use_container_width=True,
    ):

        if conversation_audio is None:

            st.markdown(
                """
<div class="v2v-warning">
<span class="v2v-warning-icon">⚠</span>
<span>Please record your voice first.</span>
</div>
""",
                unsafe_allow_html=True,
            )

        else:

            st.success(
                f"Voice captured: {source} → {target}"
            )

            st.info(
                "Voice translation will be connected to the backend next."
            )

    # =========================================================
    # DESCRIPTION
    # =========================================================

    st.markdown(
        """
<p class="small-note">
Speak naturally — your voice will be translated and spoken back.
</p>
""",
        unsafe_allow_html=True,
    )