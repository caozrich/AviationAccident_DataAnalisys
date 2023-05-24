#CSS styles---------
import streamlit as st
import base64

def set_bg_hack(main_bg):

        main_bg_ext = "png"
       
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    set_bg_hack('/img/background.png')
