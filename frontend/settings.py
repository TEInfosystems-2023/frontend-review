import streamlit as st


# =========================================================
# SETTINGS OPTIONS
# =========================================================

THEME_CHOICES = [
    ("☀️", "Light", "Light"),
    ("🌙", "Dark", "Dark"),
]

VOICE_CHOICES = [
    ("👤", "Default", "Default"),
    ("👨", "Male", "Male"),
    ("👩", "Female", "Female"),
]

DEFAULT_THEME = "Light"
DEFAULT_VOICE = "Default"


# =========================================================
# SESSION STATE
# =========================================================

def _init_settings_state():
    if "settings_theme" not in st.session_state:
        st.session_state.settings_theme = DEFAULT_THEME

    if "settings_voice" not in st.session_state:
        st.session_state.settings_voice = DEFAULT_VOICE


# =========================================================
# SETTINGS CSS
# =========================================================

def _settings_css():

    st.markdown(
        """
        <style>

        /* =====================================================
           SETTINGS HEADER
           ===================================================== */

        .settings-hero {
            text-align: center;
            margin-top: 30px;
            margin-bottom: 30px;
        }

        .settings-hero-icon {
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

        .settings-hero-title {
            color: #302923;
            font-size: 34px;
            font-weight: 800;
            line-height: 1.2;
        }

        .settings-hero-subtitle {
            margin-top: 8px;

            color: #776b63;
            font-size: 14px;
        }


        /* =====================================================
           CARDS
           ===================================================== */

        .st-key-appearance_card,
        .st-key-voice_card {

            background: rgba(255, 250, 246, 0.9) !important;

            border: 1px solid #eadbd1 !important;

            border-radius: 18px !important;

            padding: 24px 26px 26px 26px !important;

            margin-bottom: 22px !important;

            box-shadow:
                0 7px 24px rgba(100, 70, 50, 0.06) !important;
        }


        /* =====================================================
           CARD HEADER
           ===================================================== */

        .settings-header-row {
            display: flex;
            align-items: center;
            gap: 14px;

            margin-bottom: 20px;
        }

        .settings-header-icon {
            width: 44px;
            height: 44px;

            min-width: 44px;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 50%;

            background: #fff0e7;

            font-size: 20px;
        }

        .settings-header-title {
            color: #302923;

            font-size: 20px;

            font-weight: 800;

            line-height: 1.2;
        }

        .settings-header-description {
            color: #81756d;

            font-size: 13.5px;

            margin-top: 4px;
        }


        /* =====================================================
           OPTION BUTTONS (unselected)
           -----------------------------------------------------
           NOTE: _option_button() wraps each button in
           st.container(key=f"normal_{key_name}"), which Streamlit
           renders as a container carrying the class
           "st-key-normal_<key_name>" (NOT "settings-option-button").
           The key_name suffix changes per option (theme_light,
           theme_dark, voice_male, ...), so we match on the
           "st-key-normal_" prefix with a substring selector.
           ===================================================== */

        div[class*="st-key-normal_"] .stButton > button {

            width: 100% !important;

            height: 62px !important;
            min-height: 62px !important;

            padding: 0 18px !important;

            border-radius: 13px !important;

            border: 1px solid #eadbd1 !important;

            background: #fffaf7 !important;

            color: #302923 !important;

            font-size: 15px !important;

            font-weight: 650 !important;

            box-shadow: none !important;

            text-align: left !important;

            transition:
                all 0.18s ease !important;
        }

        div[class*="st-key-normal_"] .stButton > button:hover {

            border: 1.5px solid #ef9a80 !important;

            background: #fff4ee !important;

            color: #302923 !important;

            transform: translateY(-1px);
        }


        /* =====================================================
           SELECTED OPTION
           -----------------------------------------------------
           Same fix as above: the container key is
           f"selected_{key_name}", which becomes the class
           "st-key-selected_<key_name>".
           ===================================================== */

        div[class*="st-key-selected_"] .stButton > button {

            width: 100% !important;

            height: 62px !important;
            min-height: 62px !important;

            padding: 0 18px !important;

            border-radius: 13px !important;

            border: 1.5px solid #ef6b4d !important;

            background: #fff3ed !important;

            color: #302923 !important;

            font-size: 15px !important;

            font-weight: 700 !important;

            box-shadow:
                0 4px 12px rgba(239, 107, 77, 0.08) !important;

            text-align: left !important;
        }


        /* =====================================================
           BACK BUTTON
           ===================================================== */

        .st-key-settings_back_wrap {

            display: flex !important;

            justify-content: center !important;

            margin-top: 26px !important;
        }

        .st-key-settings_back_wrap .stButton {

            width: 230px !important;
        }

        .st-key-settings_back_wrap .stButton > button {

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

        .st-key-settings_back_wrap .stButton > button:hover {

            background: #e96143 !important;

            color: white !important;

            transform: translateY(-1px) !important;
        }

        .st-key-settings_back_wrap .stButton > button:focus {

            background: #ef6b4d !important;

            color: white !important;

            border: none !important;

            outline: none !important;

            box-shadow:
                0 8px 20px rgba(239, 107, 77, 0.20) !important;
        }


        /* =====================================================
           SAVE MESSAGE
           ===================================================== */

        .settings-save-text {

            text-align: center;

            margin-top: 12px;

            color: #887a71;

            font-size: 13px;
        }


        /* =====================================================
           MOBILE
           ===================================================== */

        @media (max-width: 700px) {

            .settings-hero {
                margin-top: 22px;
                margin-bottom: 24px;
            }

            .settings-hero-title {
                font-size: 30px;
            }

            .settings-hero-subtitle {
                font-size: 13px;
            }

            .st-key-appearance_card,
            .st-key-voice_card {

                padding: 20px 16px 22px 16px !important;

                border-radius: 16px !important;
            }

            .settings-header-title {
                font-size: 19px;
            }

            .settings-header-description {
                font-size: 13px;
            }

            div[class*="st-key-normal_"] .stButton > button,
            div[class*="st-key-selected_"] .stButton > button {

                height: 58px !important;
                min-height: 58px !important;
            }

            .st-key-settings_back_wrap .stButton,
            .st-key-settings_back_wrap .stButton > button {

                width: 210px !important;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# OPTION BUTTON
# =========================================================

def _option_button(icon, label, value, state_key, key_name):

    selected = st.session_state[state_key] == value

    if selected:

        with st.container(
            key=f"selected_{key_name}"
        ):

            st.button(
                f"{icon}   {label}                         ●",
                key=f"selected_button_{key_name}",
                use_container_width=True,
            )

    else:

        with st.container(
            key=f"normal_{key_name}"
        ):

            if st.button(
                f"{icon}   {label}",
                key=f"normal_button_{key_name}",
                use_container_width=True,
            ):

                st.session_state[state_key] = value

                st.rerun()


# =========================================================
# SETTINGS PAGE
# =========================================================

def settings_page():

    _init_settings_state()

    _settings_css()


    # =====================================================
    # PAGE HEADER
    # =====================================================

    st.markdown(
        '<div class="settings-hero">'
        '<div class="settings-hero-icon">⚙️</div>'
        '<div class="settings-hero-title">Settings</div>'
        '<div class="settings-hero-subtitle">'
        'Customize your experience. Changes are saved automatically.'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )


    # =====================================================
    # APPEARANCE
    # =====================================================

    with st.container(key="appearance_card"):

        st.markdown(
            '<div class="settings-header-row">'
            '<div class="settings-header-icon">☀️</div>'
            '<div>'
            '<div class="settings-header-title">Appearance</div>'
            '<div class="settings-header-description">'
            'Choose how the app looks. You can change this anytime.'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True,
        )

        theme_columns = st.columns(2, gap="small")

        with theme_columns[0]:

            _option_button(
                "☀️",
                "Light",
                "Light",
                "settings_theme",
                "theme_light",
            )

        with theme_columns[1]:

            _option_button(
                "🌙",
                "Dark",
                "Dark",
                "settings_theme",
                "theme_dark",
            )


    # =====================================================
    # VOICE
    # =====================================================

    with st.container(key="voice_card"):

        st.markdown(
            '<div class="settings-header-row">'
            '<div class="settings-header-icon">🔊</div>'
            '<div>'
            '<div class="settings-header-title">Voice</div>'
            '<div class="settings-header-description">'
            'Select the voice you want to use for AI responses.'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True,
        )

        voice_columns = st.columns(3, gap="small")

        with voice_columns[0]:

            _option_button(
                "👤",
                "Default",
                "Default",
                "settings_voice",
                "voice_default",
            )

        with voice_columns[1]:

            _option_button(
                "👨",
                "Male",
                "Male",
                "settings_voice",
                "voice_male",
            )

        with voice_columns[2]:

            _option_button(
                "👩",
                "Female",
                "Female",
                "settings_voice",
                "voice_female",
            )


    # =====================================================
    # BACK TO VOICE
    # =====================================================

    st.markdown(
        "<div style='height: 8px;'></div>",
        unsafe_allow_html=True,
    )

    with st.container(key="settings_back_wrap"):

        if st.button(
            "←  Back to Voice",
            key="settings_back",
            use_container_width=True,
        ):

            st.session_state.page = "voice"

            st.rerun()


    # =====================================================
    # AUTO SAVE MESSAGE
    # =====================================================

    st.markdown(
        '<div class="settings-save-text">'
        'Your preferences are saved automatically.'
        '</div>',
        unsafe_allow_html=True,
    )