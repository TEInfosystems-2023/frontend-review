import streamlit as st


def text_to_speech():

    # ========================================================
    # TTS HERO
    # ========================================================

    st.markdown(
        """<div class="tts-hero">
<div class="tts-icon-circle">
<div class="tts-icon">🔊</div>
</div>

<h2 class="tts-title">Text to Speech</h2>

<p class="tts-subtitle">
Type your text and convert it into speech
</p>
</div>""",
        unsafe_allow_html=True,
    )

    # ========================================================
    # TEXT INPUT
    # ========================================================

    st.markdown(
        """<div class="tts-field-label">Enter your text</div>""",
        unsafe_allow_html=True,
    )

    text = st.text_area(
        "Text",
        placeholder="Type something to speak...",
        height=125,
        label_visibility="collapsed",
        key="tts_text",
    )

    # ========================================================
    # LANGUAGE + VOICE
    # ========================================================

    language_col, voice_col = st.columns(
        2,
        gap="small",
    )

    with language_col:

        st.markdown(
            """<div class="tts-field-label">Language</div>""",
            unsafe_allow_html=True,
        )

        language = st.selectbox(
            "Language",
            [
                "English",
                "Odia",
                "Hindi",
                "Bengali",
            ],
            key="tts_language",
            label_visibility="collapsed",
        )

    with voice_col:

        st.markdown(
            """<div class="tts-field-label">Voice</div>""",
            unsafe_allow_html=True,
        )

        voice = st.selectbox(
            "Voice",
            [
                "Default Voice",
                "Voice 1",
                "Voice 2",
            ],
            key="tts_voice",
            label_visibility="collapsed",
        )

    # ========================================================
    # SPEAK BUTTON
    # ========================================================

    speak_clicked = st.button(
        "🔊  Speak",
        key="speak_button",
        type="primary",
        use_container_width=True,
    )

    # ========================================================
    # BUTTON RESPONSE
    # ========================================================

    if speak_clicked:

        if text.strip():

            st.success(
                f"Text is ready for speech generation. "
                f"Language: {language} | Voice: {voice}"
            )

        else:

            st.warning(
                "Please type something first."
            )

    # ========================================================
    # DESCRIPTION
    # ========================================================

    st.markdown(
        """<div class="tts-bottom-note">
Enter your text, choose a language and voice,
then generate speech.
</div>""",
        unsafe_allow_html=True,
    )