import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #5865F2 !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 2.5rem !important;
                border-radius: 4rem !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #E0E3FF !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            /* Hide top Streamlit chrome */
            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top: 1.5rem !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 1.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0 !important;
                color: #2B2D42 !important;
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 1.5rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0 !important;
                color: #2B2D42 !important;
            }

            h3, h4, p {
                font-family: 'Outfit', sans-serif !important;
                color: #1E293B !important;
            }

            label, .stMarkdown, .stTextInput label, .stSelectbox label, .stFileUploader label {
                color: #1E293B !important;
                font-family: 'Outfit', sans-serif !important;
            }

            input, textarea, div[data-baseweb="input"], div[data-baseweb="select"] > div {
                background-color: #F8FAFC !important;
                color: #1E293B !important;
                border-color: #CBD5E1 !important;
            }

            input::placeholder, textarea::placeholder {
                color: #64748B !important;
                opacity: 1 !important;
            }

            button {
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button:hover {
                transform: scale(1.05);
            }
        </style>
    """, unsafe_allow_html=True)
