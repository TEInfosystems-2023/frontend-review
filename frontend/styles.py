import streamlit as st


def load_styles():

    st.markdown(
        """
        <style>

        /* =====================================================
           GLOBAL
        ===================================================== */

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        .stApp {
            min-height: 100vh;

            background:
                radial-gradient(
                    circle at 8% 18%,
                    rgba(245, 205, 177, 0.22),
                    transparent 27%
                ),
                radial-gradient(
                    circle at 92% 20%,
                    rgba(242, 190, 169, 0.20),
                    transparent 27%
                ),
                radial-gradient(
                    circle at 50% 100%,
                    rgba(247, 220, 197, 0.18),
                    transparent 35%
                ),
                linear-gradient(
                    135deg,
                    #fffaf6 0%,
                    #fff8f4 45%,
                    #fffaf7 100%
                );

            color: #302923;
        }

        .block-container {
            max-width: 760px;

            padding-top: 2rem;
            padding-bottom: 3rem;
        }


        /* =====================================================
           HEADER
        ===================================================== */

        .menu-icon {
            font-size: 20px;
            color: #3c332d;
            text-align: left;
            padding-top: 4px;
        }

        .brand {
            text-align: center;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 4px;
            color: #302923;
            padding-top: 5px;
        }

        .profile-icon {
            text-align: right;
            font-size: 17px;
            color: #6d625a;
            padding-top: 4px;
        }


        /* =====================================================
           MODE BUTTONS
        ===================================================== */

        div[data-testid="stHorizontalBlock"] {
            gap: 10px;
        }

        .stButton > button {

            height: 48px;

            border-radius: 13px;

            border: 1px solid #ded5ce;

            background: rgba(255, 253, 250, 0.96);

            color: #302923;

            font-size: 13px;

            font-weight: 600;

            box-shadow:
                0 5px 15px rgba(75, 55, 45, 0.06);

            transition:
                all 0.15s ease;
        }

        .stButton > button:hover {

            border-color: #e8a27d;

            background: #fffaf6;

            color: #302923;

            transform: translateY(-1px);

            box-shadow:
                0 8px 20px rgba(130, 82, 55, 0.10);
        }

        .stButton > button:active {
            transform: scale(0.98);
        }


        /* =====================================================
           ACTIVE MODE BUTTON
        ===================================================== */

        .stButton > button[kind="primary"] {

            background:
                linear-gradient(
                    100deg,
                    #f3b18d 0%,
                    #efa47c 50%,
                    #e98f6b 100%
                ) !important;

            border: none !important;

            color: #302720 !important;

            font-weight: 700 !important;

            box-shadow:
                0 9px 24px rgba(190, 122, 83, 0.22) !important;
        }

        .stButton > button[kind="primary"]:hover {

            background:
                linear-gradient(
                    100deg,
                    #efa681 0%,
                    #e99870 50%,
                    #df835f 100%
                ) !important;

            color: #2d241f !important;

            box-shadow:
                0 12px 28px rgba(190, 122, 83, 0.28) !important;
        }


        /* =====================================================
           GENERAL PAGE TITLES
        ===================================================== */

        .page-title {

            text-align: center;

            margin-top: 10px;

            margin-bottom: 0;

            font-size: 23px;

            font-weight: 800;

            color: #302923 !important;
        }

        .page-subtitle {

            text-align: center;

            margin-top: 8px;

            margin-bottom: 30px;

            font-size: 14px;

            color: #766960 !important;
        }


        /* =====================================================
           RECORD CIRCLE
        ===================================================== */

        .record-circle {

            width: 112px;

            height: 112px;

            margin: 28px auto 18px auto;

            border-radius: 50%;

            display: flex;

            align-items: center;

            justify-content: center;

            background:
                radial-gradient(
                    circle at 50% 45%,
                    #fffdf9 0%,
                    #fff7ed 45%,
                    #f8e4d2 100%
                );

            border: 2px solid #f0d2bb;

            box-shadow:
                0 0 0 7px rgba(244, 207, 178, 0.18),
                0 0 0 14px rgba(244, 207, 178, 0.08),
                0 12px 30px rgba(102, 76, 58, 0.12);
        }

        .record-icon {

            width: 72px;

            height: 72px;

            border-radius: 50%;

            display: flex;

            align-items: center;

            justify-content: center;

            background:
                linear-gradient(
                    135deg,
                    #f6c7a8,
                    #f0a676
                );

            color: #3b3029;

            font-size: 34px;

            box-shadow:
                inset 0 1px 4px rgba(255, 255, 255, 0.75),
                0 8px 18px rgba(192, 128, 84, 0.18);
        }


        /* =====================================================
           VOICE TO VOICE TITLES
        ===================================================== */

        .v2v-title {

            text-align: center;

            margin-top: 28px;

            margin-bottom: 0;

            font-size: 23px;

            font-weight: 800;

            color: #302923 !important;
        }

        .v2v-subtitle {

            text-align: center;

            margin-top: 8px;

            margin-bottom: 30px;

            font-size: 14px;

            color: #766960 !important;
        }


        /* =====================================================
           VOICE CARDS
        ===================================================== */

        .voice-card {

            text-align: center;

            padding: 10px 5px;
        }

        .voice-circle {

            width: 120px;

            height: 120px;

            margin: 0 auto 18px auto;

            border-radius: 50%;

            background:
                radial-gradient(
                    circle at center,
                    #ffffff 0%,
                    #fffaf5 70%,
                    #f9eee5 100%
                );

            border: 1px solid #ead9cd;

            box-shadow:
                0 0 0 8px rgba(244, 207, 178, 0.10),
                0 10px 25px rgba(70, 55, 50, 0.08);

            display: flex;

            align-items: center;

            justify-content: center;

            font-size: 30px;
        }

        .voice-title {

            font-size: 13px;

            font-weight: 800;

            color: #302923 !important;

            letter-spacing: 0.6px;
        }

        .voice-language {

            margin-top: 5px;

            font-size: 11px;

            color: #8c7e75 !important;
        }

        .voice-arrow {

            height: 150px;

            display: flex;

            align-items: center;

            justify-content: center;

            font-size: 24px;

            color: #a18f84 !important;
        }


        /* =====================================================
           AUDIO INPUT
        ===================================================== */

        .stAudioInput {
            margin-top: 10px;
        }

        audio {
            border-radius: 12px;
        }


        /* =====================================================
           SELECTBOX
        ===================================================== */

        div[data-baseweb="select"] > div {

            min-height: 48px;

            border-radius: 13px;

            border: 1px solid #ded5ce;

            background: #fffdfa;

            box-shadow:
                0 5px 18px rgba(90, 70, 55, 0.06);
        }

        div[data-baseweb="select"] span {

            font-size: 14px;

            color: #3b332e !important;
        }


        /* =====================================================
           TEXT AREA
        ===================================================== */

        textarea {

            border-radius: 14px !important;

            border: 1px solid #ded5ce !important;

            background: #fffdfa !important;

            color: #332c27 !important;

            font-size: 15px !important;

            box-shadow:
                0 5px 18px rgba(90, 70, 55, 0.07) !important;
        }

        textarea:focus {

            border-color: #e9aa83 !important;

            box-shadow:
                0 0 0 3px rgba(233, 170, 131, 0.15),
                0 8px 22px rgba(100, 75, 60, 0.08) !important;
        }


        /* =====================================================
           FIELD LABEL
        ===================================================== */

        .field-label {

            margin-top: 16px;

            margin-bottom: 7px;

            font-size: 13px;

            font-weight: 700;

            color: #3d332d !important;
        }


        /* =====================================================
           SMALL NOTE
        ===================================================== */

        .small-note {

            text-align: center;

            margin-top: 18px;

            font-size: 11px;

            color: #897c74 !important;

            line-height: 1.5;
        }


        /* =====================================================
           WAVEFORM
        ===================================================== */

        .waveform {

            height: 45px;

            margin-top: 18px;

            display: flex;

            justify-content: center;

            align-items: center;

            gap: 4px;
        }

        .waveform span {

            width: 3px;

            border-radius: 5px;

            background: #d5a68a;
        }

        .waveform span:nth-child(1) {
            height: 10px;
        }

        .waveform span:nth-child(2) {
            height: 18px;
        }

        .waveform span:nth-child(3) {
            height: 28px;
        }

        .waveform span:nth-child(4) {
            height: 17px;
        }

        .waveform span:nth-child(5) {
            height: 35px;
        }

        .waveform span:nth-child(6) {
            height: 22px;
        }

        .waveform span:nth-child(7) {
            height: 30px;
        }

        .waveform span:nth-child(8) {
            height: 15px;
        }

        .waveform span:nth-child(9) {
            height: 25px;
        }


        /* =====================================================
           V2V WARNING
        ===================================================== */

        .v2v-warning {

            width: 100%;

            box-sizing: border-box;

            margin-top: 14px;

            padding: 14px 18px;

            border-radius: 12px;

            background: #fff5c9 !important;

            border: 1px solid #efd77b !important;

            color: #42391d !important;

            font-size: 14px !important;

            font-weight: 600 !important;

            display: flex;

            align-items: center;

            gap: 10px;

            opacity: 1 !important;

            visibility: visible !important;
        }

        .v2v-warning * {

            color: #42391d !important;

            opacity: 1 !important;

            visibility: visible !important;
        }

        .v2v-warning-icon {

            font-size: 17px !important;

            font-weight: 700 !important;

            color: #8a6c00 !important;
        }


        /* =====================================================
           STREAMLIT ALERTS
        ===================================================== */

        div[data-testid="stAlert"] {

            opacity: 1 !important;

            visibility: visible !important;

            border-radius: 12px !important;
        }

        div[data-testid="stAlert"] p,
        div[data-testid="stAlert"] span {

            opacity: 1 !important;

            visibility: visible !important;
        }


        /* =====================================================
           TEXT TO SPEECH
        ===================================================== */

        .tts-hero {

            text-align: center;

            margin-top: 28px;
        }

        .tts-icon-circle {

            width: 112px;

            height: 112px;

            margin: 24px auto 18px auto;

            border-radius: 50%;

            display: flex;

            align-items: center;

            justify-content: center;

            background:
                radial-gradient(
                    circle at 50% 45%,
                    #fffdf9 0%,
                    #fff7ec 45%,
                    #f8e5d4 100%
                );

            border: 2px solid #f2d5bd;

            box-shadow:
                0 0 0 7px rgba(244, 207, 178, 0.18),
                0 0 0 14px rgba(244, 207, 178, 0.08),
                0 12px 30px rgba(102, 76, 58, 0.12);
        }

        .tts-icon {

            width: 72px;

            height: 72px;

            border-radius: 50%;

            display: flex;

            align-items: center;

            justify-content: center;

            background:
                linear-gradient(
                    135deg,
                    #f6c7a8,
                    #f2a875
                );

            color: #3b3029;

            font-size: 34px;

            box-shadow:
                inset 0 1px 4px rgba(255, 255, 255, 0.75),
                0 8px 18px rgba(192, 128, 84, 0.18);
        }

        .tts-title {

            text-align: center;

            margin: 0;

            font-size: 23px;

            font-weight: 800;

            color: #302923 !important;
        }

        .tts-subtitle {

            text-align: center;

            margin-top: 8px;

            margin-bottom: 30px;

            font-size: 14px;

            color: #766960 !important;
        }


        /* =====================================================
           TTS FIELD LABEL
        ===================================================== */

        .tts-field-label {

            margin-top: 16px;

            margin-bottom: 7px;

            font-size: 13px;

            font-weight: 700;

            color: #3d332d !important;
        }


        /* =====================================================
           TTS TEXT AREA
        ===================================================== */

        div[data-testid="stTextArea"] textarea {

            min-height: 125px !important;

            border-radius: 14px !important;

            border: 1px solid #ded5ce !important;

            background: #fffdfa !important;

            color: #332c27 !important;

            font-size: 15px !important;

            box-shadow:
                0 5px 18px rgba(90, 70, 55, 0.07) !important;
        }

        div[data-testid="stTextArea"] textarea:focus {

            border-color: #e9aa83 !important;

            box-shadow:
                0 0 0 3px rgba(233, 170, 131, 0.15),
                0 8px 22px rgba(100, 75, 60, 0.08) !important;
        }


        /* =====================================================
           TTS LANGUAGE + VOICE
           KEEP IN SAME ROW
        ===================================================== */

        div[data-testid="stHorizontalBlock"] {

            align-items: flex-end !important;
        }


        /* =====================================================
           TTS SELECTBOX
        ===================================================== */

        div[data-testid="stSelectbox"]
        div[data-baseweb="select"] > div {

            min-height: 48px !important;

            border-radius: 13px !important;

            border: 1px solid #ded5ce !important;

            background: #fffdfa !important;

            box-shadow:
                0 5px 18px rgba(90, 70, 55, 0.06);
        }

        div[data-testid="stSelectbox"]
        div[data-baseweb="select"] span {

            color: #3b332e !important;

            font-size: 14px !important;

            font-weight: 500 !important;
        }


        /* =====================================================
           TTS SPEAK BUTTON
        ===================================================== */

        div[data-testid="stButton"]
        button[kind="primary"] {

            min-height: 50px !important;

            margin-top: 22px !important;

            border-radius: 14px !important;

            border: none !important;

            background:
                linear-gradient(
                    100deg,
                    #f3b18d 0%,
                    #efa47c 50%,
                    #e88f68 100%
                ) !important;

            color: #302720 !important;

            font-size: 14px !important;

            font-weight: 700 !important;

            box-shadow:
                0 9px 24px rgba(190, 122, 83, 0.20) !important;

            transition:
                transform 0.15s ease,
                box-shadow 0.15s ease;
        }

        div[data-testid="stButton"]
        button[kind="primary"]:hover {

            background:
                linear-gradient(
                    100deg,
                    #efa681 0%,
                    #e99870 50%,
                    #df835f 100%
                ) !important;

            color: #2d241f !important;

            transform: translateY(-1px);

            box-shadow:
                0 12px 28px rgba(190, 122, 83, 0.27) !important;
        }


        /* =====================================================
           TTS BOTTOM NOTE
        ===================================================== */

        .tts-bottom-note {

            text-align: center;

            margin-top: 17px;

            font-size: 11px;

            color: #897c74 !important;

            line-height: 1.5;
        }


        /* =====================================================
           MOBILE / TABLET
        ===================================================== */

        @media (max-width: 700px) {

            .block-container {

                padding-left: 18px;

                padding-right: 18px;
            }

            .voice-circle {

                width: 100px;

                height: 100px;
            }

            .voice-arrow {

                height: 120px;
            }

            .record-circle {

                width: 95px;

                height: 95px;
            }

            .record-icon {

                width: 62px;

                height: 62px;

                font-size: 29px;
            }

            .tts-icon-circle {

                width: 95px;

                height: 95px;
            }

            .tts-icon {

                width: 62px;

                height: 62px;

                font-size: 29px;
            }

            .page-title,
            .tts-title,
            .v2v-title {

                font-size: 20px;
            }

            .page-subtitle,
            .tts-subtitle,
            .v2v-subtitle {

                font-size: 13px;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )