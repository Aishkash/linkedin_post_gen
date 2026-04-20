import streamlit as st


def load_css():
    with open("styles.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


def page_header():
    st.markdown(
        """
        <div class="header-container">
            <h1 class="main-title">LinkedIn Post Generator</h1>
            <p class="sub-title">
                Create high-engagement LinkedIn posts in seconds 
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def output_box(post):
    st.markdown(
        f"""
        <div class="output-box">
            {post}
        </div>
        """,
        unsafe_allow_html=True
    )


def section_card_start():
    st.markdown(
        """
        <div class="custom-card">
        """,
        unsafe_allow_html=True
    )


def section_card_end():
    st.markdown(
        """
        </div>
        """,
        unsafe_allow_html=True
    )


def generate_button():
    return st.button("✨ Generate Post", use_container_width=True)


def loading_spinner():
    return st.spinner("Generating your LinkedIn post...")


def footer():
    st.markdown(
        """
        <hr style="margin-top:40px; border:1px solid rgba(0,0,0,0.08);">

        <p style="
            text-align:center;
            color:#444;
            font-size:14px;
            margin-top:10px;
        ">
        I am here to help
        </p>
        """,
        unsafe_allow_html=True
    )