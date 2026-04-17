import streamlit as st
from api_calling import note_generator,audio_transcription,quiz_generator
from PIL import Image

st.title("Note Summary and Quiz Generator")
st.markdown("Upload your notes and get a summary along with quiz questions to test your understanding.")    

st.divider()

with st.sidebar:
    st.header("Controls")

    #image upload and display
    summary_length = st.slider("Summary Length (sentences)", min_value=1, max_value=10, value=5)
    num_quiz_questions = st.slider("Number of Quiz Questions", min_value=1, max_value=10, value=3)
    images = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"],accept_multiple_files=True)
    
    pil_images = []
    for img in images:
        pil_img=Image.open(img)
        pil_images.append(pil_img)



    if images:
        if len(images) > 3:
            st.error("You can upload a maximum of 3 images.")
        else:
            st.subheader("Uploaded Images")
            col=st.columns(len(images))
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
#difficulty
    selected_option=st.selectbox("Select Difficulty Level", options=["Easy", "Medium", "Hard"], index=None)

    pressed=st.button("Generate Summary and Quiz",type="primary")

if pressed:
    if not images:
        st.error("Please upload at least one image to generate summary and quiz.")
    if not selected_option:
        st.error("Please select a difficulty level.")
    if images and selected_option:

        #note
        with st.container(border=True):
            st.subheader("Note Summary")
            
            #this portion below will be replaced by API call

            with st.spinner("Generating summary..."):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)


        #Audio transcript
        with st.container(border=True):
            st.subheader("Audio Transcript")
            #this portion below will be replaced by API call
            with st.spinner("Generating audio transcript..."):

                #clearing the markdown 
                generated_notes =generated_notes.replace("#", "")
                generated_notes =generated_notes.replace("*", "")
                generated_notes =generated_notes.replace("`", "")
                generated_notes =generated_notes.replace("-", "")

                audio_transcript=audio_transcription(generated_notes)
                st.audio(audio_transcript)

        #Quiz
        with st.container(border=True):
            st.subheader(f"Quiz Questions **({selected_option}**)")
            #this portion below will be replaced by API call
            with st.spinner("Generating quiz..."):
                quizzes = quiz_generator(pil_images,selected_option)
                st.markdown(quizzes)