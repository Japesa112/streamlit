import streamlit as st
import whisper 

st.title("Podcast Transcriber")

st.sidebar.header("Transcription section")

#audio_file = st.file_uploader("Upload audio", type=["wav", "mp3", "m4a"])

process_button = st.sidebar.button("Transcribe Episode")
st.sidebar.markdown("**Note**: Processing can take up to 5 mins, please be patient.")

model = whisper.load_model("base")
st.text("Whisper Model Loaded")
st.sidebar.info("Transcribing audio...")        
result = model.transcribe("https://firebasestorage.googleapis.com/v0/b/daily-devotion-72b13.appspot.com/o/devotion_preaching%2Foutput4.mp3?alt=media&token=f68e59d2-eecc-4b2b-85f1-6e4eb44f707b")
        
st.sidebar.success("Transcription Complete")
st.markdown(result['text'])
