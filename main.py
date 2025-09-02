import streamlit as st
from Helper import Yt_video_summarizer

st.set_page_config(page_title="YouTube Video Summarizer", page_icon="🎬", layout="centered")

# Sidebar for info and style
with st.sidebar:
    st.title("🎬 YouTube Summarizer")
    st.markdown(
        """
        Enter a YouTube video URL and select your preferred summary style.
        - **Language**: Select the language for the summary
        - **In Bullet Points**: Key points only
        - **In Short**: Brief summary
        - **In Detailed**: Comprehensive summary
        - **In Conversational**: Friendly, chat-like summary
        """
    )
    st.info("Powered by LLMs and Streamlit")

st.header("YouTube Video Summarizer")
st.write("Paste a YouTube video link below and get a summary in your chosen style.")

url = st.text_input("🔗 Enter YouTube Video URL:")
language = st.selectbox(
    "🌐 Select Language:",
    ["English", "Hindi", "Marathi", "Gujarati", "Malayalam", "Kannada", "Telugu"],
    index=0
)
style = st.selectbox(
    "📝 Select Summary Style:",
    ["In Bullet Points", "In Short", "In Detailed", "In Conversational"],
    index=1
)

if st.button("Summarize"):
    if url:
        with st.spinner("Fetching and summarizing transcript..."):
            try:
                summary = Yt_video_summarizer(url, style, language)
                if summary.strip():
                    st.success("Summary generated successfully!")
                    st.subheader("Summary:")
                    st.write(summary)
                else:
                    st.warning("No summary was generated. Please check the video URL or try another video.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube video URL.")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit and LLMs.")