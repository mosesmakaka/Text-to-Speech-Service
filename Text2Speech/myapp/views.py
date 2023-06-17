from django.http import HttpResponse
from gtts import gTTS
import os

def text_to_speech(request):
    # Path to the transcript file
    transcript_file = os.path.join(os.path.dirname(__file__), 'transcript.txt')

    # Read the transcript from the file
    with open(transcript_file, 'r') as file:
        transcript = file.read()

    # Create a gTTS object and specify the language
    tts = gTTS(text=transcript, lang='en')

    # Save the generated speech as an audio file
    audio_file = os.path.join(os.path.dirname(__file__), 'output.wav')
    tts.save(audio_file)

    # Return a response indicating the success
    return HttpResponse("Text to speech conversion completed. Audio file saved.")

def play_audio(request):
    # Path to the audio file
    audio_file = os.path.join(os.path.dirname(__file__), 'output.wav')

    # Play the audio file using aplay command
    os.system('aplay -q {}'.format(audio_file))  # Adjust the command based on your system

    # Return a response indicating the success
    return HttpResponse("Audio file played.")

