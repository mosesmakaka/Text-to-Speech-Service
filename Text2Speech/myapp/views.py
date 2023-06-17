from django.shortcuts import render
from django.http import HttpResponse
import os
from gtts import gTTS

def tts_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            # Generate the audio file
            tts = gTTS(text)
            audio_file = 'audio.mp3'
            tts.save(audio_file)

            # Get the absolute path of the audio file
            audio_path = os.path.join(os.getcwd(), audio_file)

            return render(request, 'tts.html', {'audio_path': audio_path})

    return render(request, 'tts.html')
