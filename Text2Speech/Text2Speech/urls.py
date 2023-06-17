from django.urls import path
from myapp.views import tts_view

urlpatterns = [
    path('', tts_view, name='tts'),
]

