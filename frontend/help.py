import streamlit as st


# =========================================================
# STATIC CONTENT
# =========================================================

HELP_STEPS = [
    ("🎙️", "Tap the microphone", "Press the microphone button to start recording."),
    ("🗣️", "Speak clearly", "Speak naturally and clearly into the microphone."),
    ("🎧", "Check your voice", "After recording, review your recorded audio."),
    ("🔄", "Tap Convert", "Press Convert to process your voice."),
    ("🔊", "Listen to the result", "Play the converted voice when the result is ready."),
]


# =========================================================
# HELP PAGE CSS
# =========================================================
# NOTE: every rule is scoped to a specific st.container(key=...)
# class (".st-key-help_...") rather than a bare element/attribute
# selector, so nothing here can leak onto other pages and nothing
# from other pages can leak onto this one.

def _help_css():

    st.markdown(
"""
<style>

/* =====================================================
   HELP HERO
   ===================================================== */

.help-hero {
    text-align: center;
    margin-top: 30px;
    margin-bottom: 30px;
}

.help-hero-icon {
    width: 54px;
    height: 54px;
    margin: 0 auto 12px auto;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background: #fff0e7;
    color: #ef6b4d;

    font-size: 25px;
}

.help-hero-title {
    color: #302923;
    font-size: 34px;
    font-weight: 800;
    line-height: 1.2;
}

.help-hero-subtitle {
    margin-top: 8px;

    color: #776b63;
    font-size: 14px;
}


/* =====================================================
   STEPS CARD
   ===================================================== */

.st-key-help_steps_card {

    background: rgba(255, 250, 246, 0.9) !important;

    border: 1px solid #eadbd1 !important;

    border-radius: 18px !important;

    padding: 26px 26px 10px 26px !important;

    margin-bottom: 22px !important;

    box-shadow:
        0 7px 24px rgba(100, 70, 50, 0.06) !important;
}


/* =====================================================
   TIMELINE STEPS
   ===================================================== */

.help-step {
    display: flex;

    gap: 16px;

    padding-bottom: 22px;

    position: relative;
}

/* Connecting line between steps, aligned through the number circles */
.help-step:not(:last-child)::before {
    content: "";

    position: absolute;

    left: 17px;
    top: 36px;

    width: 2px;
    height: calc(100% - 14px);

    background: #eadbd1;
}

.help-number {
    width: 36px;
    height: 36px;

    min-width: 36px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background: #ef6b4d;

    color: white;

    font-size: 15px;
    font-weight: 800;

    z-index: 1;
}

.help-content {
    padding-top: 4px;
}

.help-step-icon {
    font-size: 15px;

    margin-right: 6px;
}

.help-step-title {
    color: #302923;

    font-size: 16px;
    font-weight: 700;

    margin-bottom: 4px;
}

.help-step-text {
    color: #776b63;

    font-size: 13.5px;

    line-height: 1.55;
}


/* =====================================================
   TIP CARD
   ===================================================== */

.st-key-help_tip_card {

    background: #fff4ee !important;

    border: 1px solid #f3d5c4 !important;

    border-radius: 16px !important;

    padding: 18px 22px !important;

    margin-bottom: 22px !important;
}

.help-tip-title {
    color: #302923;

    font-size: 14.5px;
    font-weight: 800;

    margin-bottom: 4px;
}

.help-tip-text {
    color: #81756d;

    font-size: 13.5px;

    line-height: 1.55;
}


/* =====================================================
   BACK BUTTON
   ===================================================== */

.st-key-help_back_wrap {

    display: flex !important;

    justify-content: center !important;

    margin-top: 6px !important;
}

.st-key-help_back_wrap .stButton {

    width: 230px !important;
}

.st-key-help_back_wrap .stButton > button {

    width: 230px !important;

    height: 54px !important;
    min-height: 54px !important;

    border: none !important;

    border-radius: 999px !important;

    background: #ef6b4d !important;

    color: white !important;

    font-size: 16px !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 20px rgba(239, 107, 77, 0.20) !important;
}

.st-key-help_back_wrap .stButton > button:hover {

    background: #e96143 !important;

    color: white !important;

    transform: translateY(-1px) !important;
}

.st-key-help_back_wrap .stButton > button:focus {

    background: #ef6b4d !important;

    color: white !important;

    border: none !important;

    outline: none !important;

    box-shadow:
        0 8px 20px rgba(239, 107, 77, 0.20) !important;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 700px) {

    .help-hero {
        margin-top: 22px;
        margin-bottom: 24px;
    }

    .help-hero-title {
        font-size: 30px;
    }

    .help-hero-subtitle {
        font-size: 13px;
    }

    .st-key-help_steps_card {

        padding: 22px 18px 6px 18px !important;

        border-radius: 16px !important;
    }

    .st-key-help_tip_card {

        padding: 16px 18px !important;
    }

    .st-key-help_back_wrap .stButton,
    .st-key-help_back_wrap .stButton > button {

        width: 210px !important;
    }
}

</style>
""",
        unsafe_allow_html=True,
    )


# =========================================================
# HELP PAGE
# =========================================================

def help_page():

    _help_css()


    # =====================================================
    # PAGE HEADER
    # =====================================================

    st.markdown(
        '<div class="help-hero">'
        '<div class="help-hero-icon">🎙️</div>'
        '<div class="help-hero-title">How to Use Voice AI</div>'
        '<div class="help-hero-subtitle">'
        'Follow these simple steps to use Voice AI.'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )


    # =====================================================
    # STEPS
    # =====================================================

    with st.container(key="help_steps_card"):

        steps_html = "".join(
            '<div class="help-step">'
            f'<div class="help-number">{index}</div>'
            '<div class="help-content">'
            f'<div class="help-step-title"><span class="help-step-icon">{icon}</span>{title}</div>'
            f'<div class="help-step-text">{text}</div>'
            '</div>'
            '</div>'
            for index, (icon, title, text) in enumerate(HELP_STEPS, start=1)
        )

        st.markdown(steps_html, unsafe_allow_html=True)


    # =====================================================
    # TIP
    # =====================================================

    with st.container(key="help_tip_card"):

        st.markdown(
            '<div class="help-tip-title">💡 Tip</div>'
            '<div class="help-tip-text">'
            'Speak clearly and keep the microphone close enough to '
            'capture your voice properly.'
            '</div>',
            unsafe_allow_html=True,
        )


    # =====================================================
    # BACK TO VOICE
    # =====================================================

    st.markdown(
        "<div style='height: 8px;'></div>",
        unsafe_allow_html=True,
    )

    with st.container(key="help_back_wrap"):

        if st.button(
            "←  Back to Voice",
            key="help_back",
            use_container_width=True,
        ):

            st.session_state.page = "voice"

            st.rerun()