from django.urls import path, include
from myapp.views import text_to_speech, play_audio

urlpatterns = [
    path('', text_to_speech, name='text_to_speech'),  # Default path
    path('text-to-speech/', text_to_speech, name='text_to_speech'),
    path('play-audio/', play_audio, name='play_audio'),
]
