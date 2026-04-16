from google import  genai
from dotenv import load_dotenv
import os

#loading environment variables from .env file
load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini API client
client = genai.Client(api_key=my_api_key)


#note generator
def note_generator(images):

    prompt = """Summarize the picture in note format at max100 words make sure to add necessary markdown to differentiate different sections."""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text