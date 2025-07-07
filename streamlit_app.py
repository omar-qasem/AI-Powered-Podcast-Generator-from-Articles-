import streamlit as st
import os
import tempfile
from text_processing import extract_article_text, summarize_text, rewrite_to_podcast_style
from audio_processing import text_to_speech, add_audio_intro_outro, add_background_music

# Set page configuration
st.set_page_config(
    page_title="AI Podcast Generator",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🎙️ AI Podcast Generator")
st.markdown("""
Transform AI articles into engaging podcast-style audio content!

This tool:
1. Extracts text from URLs or accepts raw text input
2. Summarizes the content using AI
3. Rewrites it in a conversational podcast tone
4. Converts it to high-quality speech
5. Adds intro/outro and optional background music
""")

# Sidebar for configuration
st.sidebar.header("Configuration")
add_intro_outro = st.sidebar.checkbox("Add intro/outro", value=True)
add_bg_music = st.sidebar.checkbox("Add background music", value=True)

# Main interface
col1, col2 = st.columns([1, 1])

with col1:
    st.header("Input")
    
    # Input method selection
    input_method = st.radio("Choose input method:", ["URL", "Raw Text"])
    
    if input_method == "URL":
        url_input = st.text_input("Enter article URL:", placeholder="https://example.com/article")
        if st.button("Extract Text from URL") and url_input:
            with st.spinner("Extracting text from URL..."):
                extracted_text = extract_article_text(url_input)
                if extracted_text.startswith("Error"):
                    st.error(extracted_text)
                else:
                    st.session_state.raw_text = extracted_text
                    st.success("Text extracted successfully!")
    else:
        raw_text = st.text_area("Enter article text:", height=300, placeholder="Paste your article text here...")
        if raw_text:
            st.session_state.raw_text = raw_text

    # Process button
    if st.button("Generate Podcast", type="primary") and hasattr(st.session_state, 'raw_text'):
        with st.spinner("Processing..."):
            try:
                # Step 1: Summarize
                st.info("Step 1: Summarizing text...")
                summary = summarize_text(st.session_state.raw_text)
                st.session_state.summary = summary
                
                # Step 2: Rewrite to podcast style
                st.info("Step 2: Converting to podcast style...")
                podcast_text = rewrite_to_podcast_style(summary)
                st.session_state.podcast_text = podcast_text
                
                # Step 3: Generate audio
                st.info("Step 3: Generating audio...")
                
                # Create temporary files
                main_audio_path = "main_podcast.mp3"
                final_audio_path = "final_podcast.mp3"
                
                # Generate main audio
                if text_to_speech(podcast_text, main_audio_path):
                    st.session_state.main_audio_path = main_audio_path
                    
                    if add_intro_outro:
                        intro_text = "Welcome to the AI Podcast! Today we're diving into some fascinating insights from the world of artificial intelligence."
                        outro_text = "Thanks for listening to the AI Podcast! Stay curious and keep exploring the amazing world of AI."
                        
                        if add_audio_intro_outro(main_audio_path, intro_text, outro_text, final_audio_path):
                            st.session_state.final_audio_path = final_audio_path
                        else:
                            st.session_state.final_audio_path = main_audio_path
                    else:
                        st.session_state.final_audio_path = main_audio_path
                    
                    # Add background music if requested and available
                    if add_bg_music and os.path.exists("music.mp3"):
                        music_audio_path = "podcast_with_music.mp3"
                        if add_background_music(st.session_state.final_audio_path, "music.mp3", music_audio_path):
                            st.session_state.final_audio_path = music_audio_path
                    
                    st.success("Podcast generated successfully!")
                else:
                    st.error("Failed to generate audio")
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

with col2:
    st.header("Output")
    
    # Display summary
    if hasattr(st.session_state, 'summary'):
        st.subheader("📝 Summary")
        st.write(st.session_state.summary)
    
    # Display podcast text
    if hasattr(st.session_state, 'podcast_text'):
        st.subheader("🎙️ Podcast Script")
        st.write(st.session_state.podcast_text)
    
    # Display audio player and download
    if hasattr(st.session_state, 'final_audio_path') and os.path.exists(st.session_state.final_audio_path):
        st.subheader("🔊 Generated Podcast")
        
        # Audio player
        with open(st.session_state.final_audio_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
        
        # Download button
        st.download_button(
            label="📥 Download Podcast",
            data=audio_bytes,
            file_name="ai_podcast.mp3",
            mime="audio/mp3"
        )

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit, Transformers, and gTTS")

# Clean up temporary files on app restart
if st.button("🗑️ Clear Cache"):
    for file in ["main_podcast.mp3", "final_podcast.mp3", "podcast_with_music.mp3"]:
        if os.path.exists(file):
            os.remove(file)
    
    # Clear session state
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    
    st.success("Cache cleared!")
    st.rerun()


