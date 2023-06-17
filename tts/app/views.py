from django.shortcuts import render
from django.http import HttpResponse
from .utils import text_to_speech

def text_to_speech_view(request):
    # Path to the transcript file
    transcript_file = 'path/to/transcript.txt'

    # Call the text_to_speech function with the transcript file path
    output_file = text_to_speech(transcript_file)

    # Return the audio file as the response
    with open(output_file, 'rb') as file:
        response = HttpResponse(file.read(), content_type='audio/wav')
        response['Content-Disposition'] = 'attachment; filename="output.wav"'
        return response

