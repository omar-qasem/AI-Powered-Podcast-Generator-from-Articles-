
from gtts import gTTS
from pydub import AudioSegment
import os

def text_to_speech(text: str, output_filename: str, lang="en"):
    """
    Converts text to speech using gTTS and saves it as an MP3 file.
    """
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(output_filename)
        return True
    except Exception as e:
        print(f"Error during TTS conversion: {e}")
        return False

def add_audio_intro_outro(main_audio_path: str, intro_text: str, outro_text: str, output_path: str):
    """
    Adds an intro and outro to the main audio and saves the combined audio.
    """
    try:
        # Generate intro and outro audio
        intro_audio_path = "intro.mp3"
        outro_audio_path = "outro.mp3"

        if not text_to_speech(intro_text, intro_audio_path):
            print("Could not generate intro audio. Skipping intro.")
            intro_audio = AudioSegment.empty()
        else:
            intro_audio = AudioSegment.from_mp3(intro_audio_path)

        if not text_to_speech(outro_text, outro_audio_path):
            print("Could not generate outro audio. Skipping outro.")
            outro_audio = AudioSegment.empty()
        else:
            outro_audio = AudioSegment.from_mp3(outro_audio_path)

        main_audio = AudioSegment.from_mp3(main_audio_path)

        # Concatenate audio segments
        final_audio = intro_audio + main_audio + outro_audio

        final_audio.export(output_path, format="mp3")

        # Clean up temporary files
        if os.path.exists(intro_audio_path):
            os.remove(intro_audio_path)
        if os.path.exists(outro_audio_path):
            os.remove(outro_audio_path)

        return True
    except Exception as e:
        print(f"Error adding intro/outro: {e}")
        return False

def add_background_music(main_audio_path: str, music_path: str, output_path: str, volume_reduction=6):
    """
    Adds background music to the main audio.
    """
    try:
        main_audio = AudioSegment.from_mp3(main_audio_path)
        background_music = AudioSegment.from_mp3(music_path)

        # Ensure background music is at least as long as the main audio
        if len(background_music) < len(main_audio):
            background_music = background_music * (len(main_audio) // len(background_music) + 1)
        background_music = background_music[:len(main_audio)]

        # Reduce volume of background music
        background_music = background_music - volume_reduction

        # Overlay background music
        combined_audio = main_audio.overlay(background_music)

        combined_audio.export(output_path, format="mp3")
        return True
    except Exception as e:
        print(f"Error adding background music: {e}")
        return False

if __name__ == '__main__':
    # Example Usage:
    sample_text = "This is a test of the text to speech function. It should convert this sentence into an audio file."
    output_file = "sample_audio.mp3"
    if text_to_speech(sample_text, output_file):
        print(f"Successfully created {output_file}")

    # Example with intro/outro
    intro_text = "Welcome to the AI podcast!"
    outro_text = "Thanks for listening. See you next time!"
    final_podcast_path = "final_podcast.mp3"
    if add_audio_intro_outro(output_file, intro_text, outro_text, final_podcast_path):
        print(f"Successfully created {final_podcast_path} with intro and outro.")

    # Example with background music (requires a music.mp3 file in the same directory)
    # For testing, you might need to manually place a royalty-free music file named 'music.mp3'
    # You can download one from sites like https://www.bensound.com/royalty-free-music/acoustic-folk
    music_file = "music.mp3" # Placeholder - user needs to provide this
    if os.path.exists(music_file):
        podcast_with_music_path = "podcast_with_music.mp3"
        if add_background_music(final_podcast_path, music_file, podcast_with_music_path):
            print(f"Successfully created {podcast_with_music_path} with background music.")
    else:
        print(f"Skipping background music test: {music_file} not found.")

    # Clean up test files
    if os.path.exists(output_file):
        os.remove(output_file)
    if os.path.exists(final_podcast_path):
        os.remove(final_podcast_path)
    if os.path.exists("podcast_with_music.mp3"):
        os.remove("podcast_with_music.mp3")



