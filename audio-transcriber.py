import streamlit as st
import whisper 
import json

st.title("Podcast Transcriber")

st.sidebar.header("Transcription section")

url_input = st.sidebar.text_input("Enter audio URL")

process_button = st.sidebar.button("Transcribe Episode")
st.sidebar.markdown("**Note**: Processing can take up to 5 mins, please be patient.")

model = whisper.load_model("base")
st.text("Whisper Model Loaded")

if process_button and url_input:
    st.sidebar.info("Transcribing audio...")        
    result = model.transcribe(url_input)
    st.sidebar.success("Transcription Complete")
    
    # Convert the result to JSON format
    json_result = json.dumps(result)
    st.json(json_result)
