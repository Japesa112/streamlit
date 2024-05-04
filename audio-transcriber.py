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
result = model.transcribe("https://firebasestorage.googleapis.com/v0/b/daily-devotion-72b13.appspot.com/o/devotion_preaching%2F13TH%20APRIL%202024_daily_devotion.mp4?alt=media&token=108722cf-3c27-41ed-966d-f0c60044d2fd")
        
st.sidebar.success("Transcription Complete")
st.markdown(result['text'])
