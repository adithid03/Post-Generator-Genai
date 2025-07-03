import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Post Generator",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def styled_copy_to_clipboard(text):
    with open("styles.css", "r") as f:
        css = f.read()
    escaped_text = text.replace('"', '&quot;').replace("'", "&#39;").replace("\n", "<br>")
    components.html(f"""
        <style>{css}</style>
        <div class="post-container" id="postText">{escaped_text}</div>
        <button class="copy-btn" onclick="navigator.clipboard.writeText(document.getElementById('postText').innerText).then(() => alert('Copied!'));">
            📋 Copy to Clipboard
        </button>
    """, height=600)


length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


# Main app layout
def main():
    st.subheader("GEN-AI Post Generator")
    st.markdown("""
    Welcome to the **Post Generator Tool**!  
    This app helps you generate **LinkedIn-style posts** based on selected topics, length, and language preferences.  
    Ideal for content creators, marketers, or students looking to craft posts effortlessly using Generative AI.
    """)

    st.subheader("Customize Your Post")
    
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        
        selected_language = st.selectbox("Language", options=language_options)

    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)
        styled_copy_to_clipboard(post)


if __name__ == "__main__":
    main()
