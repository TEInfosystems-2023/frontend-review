import streamlit as st


def speech_to_text():

    # ========================================================
    # SPEECH TO TEXT — LOCAL STYLING
    # ========================================================

    st.markdown(
        """
        <style>

        /* Speech-to-Text title */
        .stt-page-title {
            color: #24242b !important;
            font-size: 22px;
            font-weight: 600;
            text-align: center;
            margin: 10px 0 4px 0;
        }

        /* Speech-to-Text subtitle */
        .stt-page-subtitle {
            color: #77747a !important;
            font-size: 12px;
            text-align: center;
            margin: 0 0 18px 0;
        }

        /* Microphone circle */
        .stt-record-circle {
            width: 64px;
            height: 64px;
            border-radius: 50%;
            margin: 0 auto 8px auto;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #f6e7e4;
        }

        .stt-record-icon {
            font-size: 25px;
        }

        /* Recorder label */
        div[data-testid="stAudioInput"] label {
            color: #77747a !important;
        }

        div[data-testid="stAudioInput"] label p {
            color: #77747a !important;
        }

        /* Recognized Text label */
        .stt-field-label {
            color: #4d4a50 !important;
            font-size: 11px;
            font-weight: 500;
            margin: 12px 0 5px 0;
        }

        /* Language label */
        .stt-language-label {
            color: #4d4a50 !important;
            font-size: 11px;
            font-weight: 500;
            margin: 12px 0 5px 0;
        }

        /* Small recording message */
        .stt-small-note {
            color: #77747a !important;
            text-align: center;
            font-size: 10px;
            margin: 8px 0;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # RECORDING HEADER
    # ========================================================

    st.markdown(
        """
        <div class="stt-record-circle">
            <div class="stt-record-icon">🎙️</div>
        </div>

        <p class="stt-page-title">
            Start Recording
        </p>

        <p class="stt-page-subtitle">
            Record your voice and convert it into text
        </p>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # AUDIO RECORDING
    # ========================================================

    audio = st.audio_input(
        "Record your voice",
        sample_rate=16000,
        key="stt_audio",
    )

    # ========================================================
    # RECOGNIZED TEXT
    # ========================================================

    st.markdown(
        '<div class="stt-field-label">Recognized Text</div>',
        unsafe_allow_html=True,
    )

    recognized_text = st.text_area(
        "Recognized Text",
        value="I was wrong, hey ma'am",
        height=105,
        label_visibility="collapsed",
        key="recognized_text",
    )

    # ========================================================
    # LANGUAGE
    # ========================================================

    st.markdown(
        '<div class="stt-language-label">Language</div>',
        unsafe_allow_html=True,
    )

    st.selectbox(
        "Language",
        [
            "English",
            "Odia",
            "Hindi",
            "Bengali",
        ],
        label_visibility="collapsed",
        key="stt_language",
    )

    # ========================================================
    # AUDIO RESULT
    # ========================================================

    if audio is not None:

        st.markdown(
            """
            <div class="stt-small-note">
                Audio recorded successfully.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.audio(audio)