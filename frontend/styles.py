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


/* =====================================================
   MAIN CONTAINER
   ===================================================== */

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
   SPEAK TITLE
   ===================================================== */

.speak-title {

    text-align: center;

    margin-top: 42px;

    margin-bottom: 0;

    font-size: 36px;

    font-weight: 800;

    color: #302923 !important;

    line-height: 1.2;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 700px) {

    .block-container {

        padding-left: 18px;

        padding-right: 18px;
    }


    .speak-title {

        margin-top: 30px;

        font-size: 28px;
    }
}

</style>
""",
        unsafe_allow_html=True,
    )