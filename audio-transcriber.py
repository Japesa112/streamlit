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
result = model.transcribe("https://firebasestorage.googleapis.com/v0/b/daily-devotion-72b13.appspot.com/o/devotion_preaching%2Foutput2.mp3?alt=media&token=3a035a32-8475-4357-9ad8-815d7981240f")
        
st.sidebar.success("Transcription Complete")
st.markdown(result['text'])
