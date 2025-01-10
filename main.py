import os
import streamlit as st
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(
  api_key=ELEVENLABS_API_KEY, # Defaults to ELEVEN_API_KEY or ELEVENLABS_API_KEY
)

text=st.text_input("Choose a text to speak out:")
speak=st.button("Speak it out!")

if text and speak:
    #audio = client.generate(
    #  text=text,
    #  voice="Brian",
    #  model="eleven_multilingual_v2"
    #)
    #play(audio)

    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5", # use the turbo model for low latency
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )
    # uncomment the line below to play the audio back
    # play(response)
    # Generating a unique file name for the output MP3 file
    save_file_path = "audio.mp3"
    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)
    print(f"{save_file_path}: A new audio file was saved successfully!")

    st.audio("audio.mp3")
