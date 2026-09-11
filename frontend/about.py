import streamlit as st


# =========================================================
# STATIC CONTENT
# =========================================================

HOW_IT_WORKS_STEPS = [
    ("🎙️", "Speak", "Record your voice using the microphone."),
    ("⚙️", "Process", "Your voice is processed by the AI system."),
    ("🔄", "Convert", "The system converts the spoken input."),
    ("🔊", "Listen", "Listen to the generated voice response."),
]

TECHNOLOGIES = [
    "Python",
    "Streamlit",
    "FastAPI",
    "AI / ML",
    "Speech Processing",
]


# =========================================================
# ABOUT PAGE CSS
# =========================================================
# NOTE: every selector below is scoped to a specific
# st.container(key=...) class (".st-key-about_...") rather
# than a bare element/attribute selector. Unscoped selectors
# like "div[data-testid='stHorizontalBlock'] > div:first-child"
# match EVERY st.columns() row in the whole app, not just the
# one they were written for -- that caused real layout bugs
# elsewhere in this project. Scoping keeps this page's styles
# fully self-contained.

def _about_css():

    st.markdown(
"""
<style>

/* =====================================================
   ABOUT HERO
   ===================================================== */

.about-hero {
    text-align: center;
    margin-top: 30px;
    margin-bottom: 30px;
}

.about-hero-icon {
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

.about-hero-title {
    color: #302923;
    font-size: 34px;
    font-weight: 800;
    line-height: 1.2;
}

.about-hero-subtitle {
    margin-top: 8px;
    margin-left: auto;
    margin-right: auto;

    max-width: 480px;

    color: #776b63;
    font-size: 14px;
    line-height: 1.5;
}


/* =====================================================
   CARDS (shared shell)
   ===================================================== */

.st-key-about_intro_card,
.st-key-about_how_card,
.st-key-about_tech_card,
.st-key-about_dev_card {

    background: rgba(255, 250, 246, 0.9) !important;

    border: 1px solid #eadbd1 !important;

    border-radius: 18px !important;

    padding: 24px 26px 26px 26px !important;

    margin-bottom: 22px !important;

    box-shadow:
        0 7px 24px rgba(100, 70, 50, 0.06) !important;
}


/* =====================================================
   CARD TITLE / TEXT
   ===================================================== */

.about-card-title {
    color: #302923;

    font-size: 20px;

    font-weight: 800;

    line-height: 1.2;

    margin-bottom: 14px;
}

.about-card-text {
    color: #776b63;

    font-size: 14.5px;

    line-height: 1.65;
}

.about-card-text + .about-card-text {
    margin-top: 12px;
}


/* =====================================================
   HOW IT WORKS -- STEPS
   ===================================================== */

.st-key-about_how_card div[data-testid="stHorizontalBlock"] {
    align-items: stretch !important;
    gap: 4px;
}

.about-step {
    height: 100%;

    text-align: center;

    padding: 6px 8px;
}

.about-step-icon {
    width: 46px;
    height: 46px;
    margin: 0 auto 10px auto;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background: #fff0e7;

    font-size: 20px;
}

.about-step-title {
    color: #302923;

    font-size: 15px;
    font-weight: 700;

    margin-bottom: 4px;
}

.about-step-text {
    color: #81756d;

    font-size: 12.5px;

    line-height: 1.5;
}


/* =====================================================
   TECHNOLOGY PILLS
   ===================================================== */

.about-tech-pills {
    display: flex;
    flex-wrap: wrap;

    gap: 10px;
}

.about-tech-pill {
    padding: 9px 16px;

    border-radius: 999px;

    border: 1px solid #eadbd1;

    background: #fffaf7;

    color: #5b4b42;

    font-size: 13.5px;
    font-weight: 650;

    white-space: nowrap;
}


/* =====================================================
   BACK BUTTON
   ===================================================== */

.st-key-about_back_wrap {

    display: flex !important;

    justify-content: center !important;

    margin-top: 6px !important;
}

.st-key-about_back_wrap .stButton {

    width: 230px !important;
}

.st-key-about_back_wrap .stButton > button {

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

.st-key-about_back_wrap .stButton > button:hover {

    background: #e96143 !important;

    color: white !important;

    transform: translateY(-1px) !important;
}

.st-key-about_back_wrap .stButton > button:focus {

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

    .about-hero {
        margin-top: 22px;
        margin-bottom: 24px;
    }

    .about-hero-title {
        font-size: 30px;
    }

    .about-hero-subtitle {
        font-size: 13px;
    }

    .st-key-about_intro_card,
    .st-key-about_how_card,
    .st-key-about_tech_card,
    .st-key-about_dev_card {

        padding: 20px 16px 22px 16px !important;

        border-radius: 16px !important;
    }

    .about-card-title {
        font-size: 19px;
    }

    /* Stack the 4 "How it works" steps vertically on mobile,
       each with a divider instead of a border-radius card. */
    .st-key-about_how_card div[data-testid="stHorizontalBlock"] {
        flex-direction: column !important;
    }

    .st-key-about_how_card div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
        width: 100% !important;
    }

    .about-step {
        display: flex;
        align-items: center;

        text-align: left;

        gap: 14px;

        padding: 14px 4px;

        border-bottom: 1px solid #f0e4da;
    }

    .about-step-icon {
        margin: 0;

        flex-shrink: 0;
    }

    .st-key-about_back_wrap .stButton,
    .st-key-about_back_wrap .stButton > button {

        width: 210px !important;
    }
}

</style>
""",
        unsafe_allow_html=True,
    )


# =========================================================
# HOW IT WORKS STEP
# =========================================================

def _how_it_works_step(icon, title, text):

    st.markdown(
        '<div class="about-step">'
        f'<div class="about-step-icon">{icon}</div>'
        f'<div class="about-step-title">{title}</div>'
        f'<div class="about-step-text">{text}</div>'
        '</div>',
        unsafe_allow_html=True,
    )


# =========================================================
# ABOUT PAGE
# =========================================================

def about_page():

    _about_css()


    # =====================================================
    # PAGE HEADER
    # =====================================================

    st.markdown(
        '<div class="about-hero">'
        '<div class="about-hero-icon">🎙️</div>'
        '<div class="about-hero-title">About Voice AI</div>'
        '<div class="about-hero-subtitle">'
        'A simple voice-based AI application designed to make '
        'spoken communication easier.'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )


    # =====================================================
    # ABOUT THE PROJECT
    # =====================================================

    with st.container(key="about_intro_card"):

        st.markdown(
            '<div class="about-card-title">About the Project</div>'
            '<div class="about-card-text">'
            'Voice AI is a voice-based application that allows users '
            'to speak naturally and process their voice through an '
            'easy-to-use interface.'
            '</div>'
            '<div class="about-card-text">'
            'The application is designed with a simple user experience '
            'so that users can record or upload their voice, select the '
            'required option, and receive a processed voice response.'
            '</div>',
            unsafe_allow_html=True,
        )


    # =====================================================
    # HOW IT WORKS
    # =====================================================

    with st.container(key="about_how_card"):

        st.markdown(
            '<div class="about-card-title">How It Works</div>',
            unsafe_allow_html=True,
        )

        step_columns = st.columns(4, gap="small")

        for column, (icon, title, text) in zip(step_columns, HOW_IT_WORKS_STEPS):

            with column:

                _how_it_works_step(icon, title, text)


    # =====================================================
    # TECHNOLOGY
    # =====================================================

    with st.container(key="about_tech_card"):

        pills_html = "".join(
            f'<div class="about-tech-pill">{tech}</div>'
            for tech in TECHNOLOGIES
        )

        st.markdown(
            '<div class="about-card-title">Technology</div>'
            f'<div class="about-tech-pills">{pills_html}</div>',
            unsafe_allow_html=True,
        )


    # =====================================================
    # FRONTEND DEVELOPMENT
    # =====================================================

    with st.container(key="about_dev_card"):

        st.markdown(
            '<div class="about-card-title">Frontend Development</div>'
            '<div class="about-card-text">'
            'The frontend is built using Streamlit with a focus on a '
            'simple, accessible, and user-friendly voice interface.'
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

    with st.container(key="about_back_wrap"):

        if st.button(
            "←  Back to Voice",
            key="about_back",
            use_container_width=True,
        ):

            st.session_state.page = "voice"

            st.rerun()