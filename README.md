# Note Summary and Quiz Generator

A Streamlit application that turns note images into three study assets in one flow:

- a concise AI-generated summary
- a spoken audio version of the summary
- a multiple-choice quiz based on the uploaded notes

The app is designed for quick revision. Upload up to three images of handwritten or printed notes, choose a quiz difficulty, and generate study material powered by Google's Gemini model and `gTTS`.

## Features

- Image-based note summarization from uploaded `.jpg`, `.jpeg`, and `.png` files
- Quiz generation with selectable difficulty levels: `Easy`, `Medium`, and `Hard`
- Text-to-speech audio output for the generated summary
- Simple Streamlit interface for fast experimentation and demos
- Multiple image support for combining note pages in a single run

## Demo Flow

1. Upload up to 3 note images.
2. Choose the summary length from the sidebar.
3. Select the quiz difficulty.
4. Click `Generate Summary and Quiz`.
5. Review the generated summary, listen to the audio, and answer the quiz.

## Tech Stack

- `Python`
- `Streamlit`
- `Google Gemini API` via `google-genai`
- `Pillow` for image handling
- `gTTS` for text-to-speech
- `python-dotenv` for environment variable loading

## Project Structure

```text
.
|-- app.py                 # Main Streamlit application
|-- api_calling.py         # Gemini + audio generation helpers
|-- working_image.py       # Standalone image-generation experiment
|-- working_with_audio.py  # Standalone audio-generation experiment
|-- requirement.txt        # Python dependencies
|-- .env                   # Local environment variables (not for commit)
|-- .gitignore
```

## How It Works

### 1. Summary Generation

The app converts uploaded files into PIL images and sends them to Gemini with a prompt asking for a short note-style summary.

### 2. Audio Generation

The generated summary text is cleaned and passed to `gTTS`, which returns an in-memory audio buffer rendered directly in Streamlit.

### 3. Quiz Generation

The same uploaded note images are sent to Gemini again with a quiz prompt and a selected difficulty level.

## Getting Started

### Prerequisites

- Python `3.10+` recommended
- A valid Google Gemini API key

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/note-summary-and-quiz-generator.git
cd note-summary-and-quiz-generator
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirement.txt
```

## Environment Variables

Create a `.env` file in the project root with the following value:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## Run the App

```bash
streamlit run app.py
```

After launching, Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

## Usage Notes

- The app currently accepts image uploads only.
- A maximum of 3 images can be uploaded at a time.
- The UI includes a summary-length slider, but the current backend prompt does not yet use that value dynamically.
- Quiz generation currently depends on prompt behavior from Gemini.

## Example Use Cases

- Convert class notes into revision-friendly summaries
- Turn whiteboard photos into self-test quizzes
- Create quick study audio for passive review
- Build lightweight learning demos with multimodal AI

## Known Limitations

- The quiz prompt in the current implementation is intended to use the selected difficulty, but the string is not formatted dynamically in `api_calling.py`.
- The selected number of quiz questions is exposed in the UI but is not yet applied in the backend prompt.
- Generated output quality depends on image clarity and model response quality.
- `gTTS` requires text-to-speech generation at runtime and may be affected by network availability.

## Future Improvements

- Use the selected summary length in the summarization prompt
- Use the selected number of quiz questions in quiz generation
- Support PDF and audio note inputs
- Add answer keys and scoring
- Export summaries and quizzes as downloadable files
- Improve prompt design for more consistent structured output

## Security

- Do not commit your `.env` file or API keys.
- Rotate your API key immediately if it is ever exposed.

## Contributing

Contributions are welcome. If you'd like to improve the prompts, UI, output formatting, or add new input formats, feel free to fork the repo and open a pull request.

## License

Choose a license before publishing publicly. If you have not added one yet, consider `MIT` for a simple open-source option.
