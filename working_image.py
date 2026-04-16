import streamlit as st
from google import  genai
from dotenv import load_dotenv
from PIL import Image
import os

#loading environment variables from .env file
load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")
# Initialize the Gemini API client
client = genai.Client(api_key=my_api_key)

images = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"],accept_multiple_files=True)
print(type(images))

if images:
    pil_images = []
    for img in images:
        pil_img=Image.open(img)
        pil_images.append(pil_img)


    prompt = """Summarize the picture in note format at max100 words make sure to add necessary markdown to differentiate different sections."""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[pil_images, prompt]
    )
    st.markdown(response.text)