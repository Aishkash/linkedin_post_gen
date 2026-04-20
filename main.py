import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
from ui import load_css, page_header, output_box, footer

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


# Main app layout
def main():
    st.set_page_config(

        page_title="LinkedIn Post Generator",

        page_icon="✨",

        layout="centered"

    )

    load_css()

    page_header()
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("Language", options=language_options)
    
    custom_prompt = st.text_area(
        "Additional Context (Optional)",
        placeholder="e.g., Focus on AI trends, Make it motivational, Include implementation tips...",
        height=100
    )

    # Generate Button
    if st.button("✨ Generate"):

        with st.spinner("Generating post..."):

            post = generate_post(

                selected_length,

                selected_language,

                selected_tag,

                custom_prompt

            )

        output_box(post)

    footer()


# Run the app
if __name__ == "__main__":
    main()