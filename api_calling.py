import io


from click import prompt
from google import  genai
from dotenv import load_dotenv
import os

from gtts import gTTS

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

def audio_transcription(text):
    speech = gTTS(text=text, lang='en', slow=False)

    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer

def quiz_generator(image,difficulty):
    prompt = """Generate a quiz based on the {difficulty} content of the image.make sure add markdown to differentiate the options. The quiz should consist of 5 questions with multiple-choice answers. The difficulty level of the quiz should be based on the user's selection (Easy, Medium, Hard). Please provide the questions and answer options in a clear format."""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[image, prompt]
    )
    return response.text