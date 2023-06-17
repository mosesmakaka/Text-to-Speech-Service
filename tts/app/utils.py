from gtts import gTTS
import os

def text_to_speech(transcript_file):
    # Read the transcript from the file
    with open(transcript_file, 'r') as file:
        transcript = file.read()

    # Create a gTTS object and specify the language
    tts = gTTS(text=transcript, lang='en')

    # Save the generated speech as an audio file
    output_file = 'output.wav'
    tts.save(output_file)

    return output_file
