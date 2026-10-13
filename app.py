import base64

import streamlit as st



from frontend.styles import load_styles

from frontend.voice_to_voice import voice_to_voice

from frontend.settings import settings_page

from frontend.about import about_page

from frontend.help import help_page





# =====================================================

# PAGE CONFIGURATION

# =====================================================



st.set_page_config(

    page_title="Voice AI",

    page_icon="🎙️",

    layout="centered",

    initial_sidebar_state="collapsed",

)





load_styles()





# =====================================================

# SESSION STATE

# =====================================================



if "show_menu" not in st.session_state:

    st.session_state.show_menu = False



if "page" not in st.session_state:

    st.session_state.page = "voice"





# =====================================================

# HEADER / MENU CSS

# =====================================================

# NOTE: every HTML/CSS string below is flush-left (no leading indentation)

# before it reaches st.markdown(). Indented HTML inside a triple-quoted

# string gets treated as a literal code block by the markdown renderer,

# which is why the old menu HTML showed up as raw text on screen.



st.markdown(

"""

<style>



/* =================================================

   TOP HEADER ROW (hamburger / title / help)

   Force a single row on all screen sizes so the "?"

   button can never drop below the title on mobile.



   NOTE: the old unscoped "MENU BUTTON" rule that used to

   live here (div[data-testid="stHorizontalBlock"] >

   div:first-child div[data-testid="stButton"] > button)

   has been removed. It matched the first column of EVERY

   st.columns() row in the app, not just the header, which

   was forcing Settings-page buttons like "Light" and

   "Default" down to a 40px width. The hamburger button is

   now styled only by the .st-key-voice_header-scoped rule

   below (and its counterpart in styles.py).

   ================================================= */



.st-key-voice_header {

position: relative !important;

}



.st-key-voice_header div[data-testid="stHorizontalBlock"] {

flex-wrap: nowrap !important;

align-items: center !important;

}



.st-key-voice_header div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {

min-width: 0 !important;

width: auto !important;

}



/* Hamburger (menu) button */

.st-key-voice_header div[data-testid="stHorizontalBlock"] > div:first-child div[data-testid="stButton"] > button {

background: transparent !important;

background-color: transparent !important;

border: none !important;

box-shadow: none !important;

color: #3c332d !important;

width: 40px !important;

height: 35px !important;

min-height: 35px !important;

padding: 0 !important;

font-size: 21px !important;

font-weight: 400 !important;

}



.st-key-voice_header div[data-testid="stHorizontalBlock"] > div:first-child div[data-testid="stButton"] > button:hover {

background: transparent !important;

background-color: transparent !important;

border: none !important;

box-shadow: none !important;

color: #7f4d38 !important;

}



.st-key-voice_header div[data-testid="stHorizontalBlock"] > div:first-child div[data-testid="stButton"] > button:focus {

background: transparent !important;

background-color: transparent !important;

border: none !important;

box-shadow: none !important;

outline: none !important;

}



/* Help ("?") button

   FIX: instead of relying on Streamlit's internal column/flex/grid

   sizing (which broke unpredictably in earlier attempts), this

   button is taken out of that layout system entirely with

   position: absolute, anchored directly to .st-key-voice_header

   (set to position: relative above). "right: 0" pins it flush to

   the header container's own right edge -- which is guaranteed to

   be exactly as far from the browser edge as the header's left

   edge is (both come from the same centered .block-container

   padding), mirroring the hamburger button with a simple, robust

   geometric guarantee rather than fighting column internals. */

.st-key-voice_header .st-key-help_button {

position: absolute !important;

right: 0 !important;

top: 50% !important;

transform: translateY(-50%) !important;

}



.st-key-voice_header .st-key-help_button > div[data-testid="stButton"] > button {

background: transparent !important;

background-color: transparent !important;

border: none !important;

box-shadow: none !important;

color: #3c332d !important;

width: 32px !important;

height: 32px !important;

min-height: 32px !important;

padding: 0 !important;

margin: 0 !important;

font-size: 19px !important;

font-weight: 400 !important;

}



.st-key-voice_header .st-key-help_button > div[data-testid="stButton"] > button:hover {

background: transparent !important;

background-color: transparent !important;

color: #7f4d38 !important;

}



.st-key-voice_header .st-key-help_button > div[data-testid="stButton"] > button:focus {

background: transparent !important;

background-color: transparent !important;

outline: none !important;

box-shadow: none !important;

}



/* =================================================

   LEFT NAVIGATION DRAWER

   This targets the real Streamlit container that holds

   the drawer's header + nav buttons (st.container(key="voice_side_menu")),

   so nothing can render outside of it.

   ================================================= */



.st-key-voice_side_menu {

position: fixed !important;

top: 0 !important;

left: 0 !important;

width: 265px !important;

height: 100vh !important;

background: #fffaf6 !important;

border-right: 1px solid #ead8cb !important;

box-shadow: 8px 0 30px rgba(80, 55, 40, 0.12) !important;

z-index: 9999 !important;

padding: 22px 20px 20px 26px !important;

box-sizing: border-box !important;

overflow-y: auto !important;

}



.voice-side-title {

font-size: 21px;

font-weight: 800;

color: #302923;

padding-top: 6px;

}



.voice-side-divider {

border-bottom: 1px solid #eadfd7;

margin: 16px -20px 8px -26px;

}



/* Close (x) button: small, top-right of the drawer */

.st-key-voice_side_menu .st-key-close_side_menu > div[data-testid="stButton"] > button {

width: 32px !important;

height: 32px !important;

min-height: 32px !important;

padding: 0 !important;

margin: 0 0 0 auto !important;

display: flex !important;

background: transparent !important;

background-color: transparent !important;

border: none !important;

box-shadow: none !important;

color: #5b4b42 !important;

font-size: 22px !important;

justify-content: center !important;

}



.st-key-voice_side_menu .st-key-close_side_menu > div[data-testid="stButton"] > button:hover {

background: transparent !important;

color: #7f4d38 !important;

}



/* Nav item buttons (Voice / Settings / About / Help) */

.st-key-voice_side_menu div[data-testid="stButton"] > button {

width: 100% !important;

height: 54px !important;

min-height: 54px !important;

padding: 0 10px !important;

margin: 0 !important;

background: transparent !important;

background-color: transparent !important;

border: none !important;

border-radius: 8px !important;

box-shadow: none !important;

color: #302923 !important;

font-size: 16px !important;

text-align: left !important;

justify-content: flex-start !important;

}



.st-key-voice_side_menu div[data-testid="stButton"] > button:hover {

background: #fff1e8 !important;

color: #7f4d38 !important;

}



/* Re-apply the close-button sizing after the generic nav rule above

   (kept last on purpose so it wins) */

.st-key-voice_side_menu .st-key-close_side_menu > div[data-testid="stButton"] > button {

width: 32px !important;

height: 32px !important;

min-height: 32px !important;

}



/* Dimmed overlay to the right of the drawer */

.voice-side-overlay {

position: fixed;

top: 0;

left: 265px;

right: 0;

bottom: 0;

background: rgba(48, 41, 35, 0.08);

z-index: 9990;

}



/* =================================================

   MOBILE

   ================================================= */



@media (max-width: 700px) {



.st-key-voice_header div[data-testid="stHorizontalBlock"] > div:first-child div[data-testid="stButton"] > button {

width: 36px !important;

}



.st-key-voice_side_menu {

width: 240px !important;

padding: 22px 16px 20px 20px !important;

}



.voice-side-overlay {

left: 240px;

}



}



</style>

""",

unsafe_allow_html=True,

)





# =====================================================

# LEFT SIDE MENU (real Streamlit drawer)

# =====================================================



if st.session_state.show_menu:



    # Dimmed backdrop over the main content (drawer sits on top of it)

    st.markdown('<div class="voice-side-overlay"></div>', unsafe_allow_html=True)



    with st.container(key="voice_side_menu"):



        header_col, close_col = st.columns([4, 1])



        with header_col:

            st.markdown('<div class="voice-side-title">VOICE AI</div>', unsafe_allow_html=True)



        with close_col:

            if st.button("×", key="close_side_menu"):

                st.session_state.show_menu = False

                st.rerun()



        st.markdown('<div class="voice-side-divider"></div>', unsafe_allow_html=True)



        if st.button("🎙️  Voice", key="side_voice", use_container_width=True):

            st.session_state.page = "voice"

            st.session_state.show_menu = False

            st.rerun()



        if st.button("⚙️  Settings", key="side_settings", use_container_width=True):

            st.session_state.page = "settings"

            st.session_state.show_menu = False

            st.rerun()



        if st.button("ℹ️  About", key="side_about", use_container_width=True):

            st.session_state.page = "about"

            st.session_state.show_menu = False

            st.rerun()



        if st.button("❓  Help", key="side_help", use_container_width=True):

            st.session_state.page = "help"

            st.session_state.show_menu = False

            st.rerun()





# =====================================================

# HEADER

# =====================================================



with st.container(key="voice_header"):



    left, center, right = st.columns([1, 2, 1])



    with left:



        if st.button("☰", key="menu_button"):



            st.session_state.show_menu = True



            st.rerun()



    with center:



        with open("frontend/tekvaani.png", "rb") as _logo_file:

            _logo_b64 = base64.b64encode(_logo_file.read()).decode()



        st.markdown(

            f'<div style="display:flex;justify-content:center;align-items:center;width:100%;">'

            f'<img src="data:image/png;base64,{_logo_b64}" '

            f'style="width:220px;max-width:100%;height:auto;display:block;" alt="Tekvaani">'

            f'</div>',

            unsafe_allow_html=True,

        )



    with right:



        if st.button("?", key="help_button"):



            st.session_state.page = "help"

            st.session_state.show_menu = False



            st.rerun()





# =====================================================

# PAGE ROUTING

# =====================================================



if st.session_state.page == "settings":



    settings_page()



elif st.session_state.page == "about":



    about_page()



elif st.session_state.page == "help":



    help_page()



else:



    voice_to_voice()