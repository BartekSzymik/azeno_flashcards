from django.urls import path

from . import views

app_name = 'flashcards'

urlpatterns = [
    path('flashcards/', views.FlashCardView.as_view(), name='flashcards'),
]
