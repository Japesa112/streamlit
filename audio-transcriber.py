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
result = model.transcribe("https://firebasestorage.googleapis.com/v0/b/daily-devotion-72b13.appspot.com/o/devotion_preaching%2FDEVOTION%20FOR%20FRIDAY%2026TH%20APRIL%202024%20WITH%20FR%20EUSTACE%20SIAME%20SDB!.mp4?alt=media&token=b5e28a04-5e5f-45d4-b864-a12f9c20c81a")
        
st.sidebar.success("Transcription Complete")
st.markdown(result['text'])
