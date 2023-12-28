import os
import streamlit as st
import textwrap
import requests
from io import BytesIO
from PIL import Image
from pytube import YouTube
import create_vector_db as mydb
import analzer as analyzer 

video_url="https://www.youtube.com/watch?v=UiYXwUg23Yw"
video_id=""

st.set_page_config(layout="wide")
st.title("Youtube Video Analyzer")
st.write("provide Youtube URL, I will analyze it and give you a brief summary of the contents.")

#create the main content area
col1, col2 = st.columns([1, 1])

def analyze_video():
    with col1:
        # Extract the Youtube video ID from the URL 
        video_id = YouTube(video_url).video_id

        # Construct the URL of the thumbnail image
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

        # Download the thumbnail image and convert it to a PIL image object
        response = requests.get(thumbnail_url)
        img = Image.open (BytesIO(response.content))

        # Display the thumbnail image in streamlit 
        st.image (img)

    # Column 2
    with col2:
        with st.spinner("Reading Video Contens...")
            mydb.create_db(video_url)
            st.session_state['status']='DB Created'
