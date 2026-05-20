import streamlit as st

def footer_home():
    logo_url = ""
    st.markdown(f"""
        <div style="margin-top:2rem;display:flex;gap:6px;justify-content:center;align-items:center;">
            <p style="color:white;margin:0;">Created with 💖 by Shaikh Raheem</p>
            <img src="{logo_url}" style="max-height:25px;object-fit:contain;" />
        </div>
    """, unsafe_allow_html=True)
