from django.shortcuts import render, redirect
import datetime
from django.utils import timezone as django_timezone

# Static values for timer, letter, and paragraph
STATIC_RELEASE_TIME = datetime.datetime(2025, 8, 5, 10, 12, 45, tzinfo=datetime.timezone.utc)
STATIC_LETTER_TEXT = "You will get the Letter Tommorow!!"
STATIC_PARAGRAPH_TEXT = "On this wonderful day, I wish you all the happiness and success in the world. May your day be filled with joy and laughter."

def letter(request):
    return render(request, 'birthday_app/letter.html', {'letter_text': STATIC_LETTER_TEXT})

def countdown(request):
    return render(request, 'birthday_app/index.html', {'release_time': STATIC_RELEASE_TIME})

def surprise(request):
    if django_timezone.now() < STATIC_RELEASE_TIME:
        return redirect('index')
    return render(request, 'birthday_app/surprise.html')

def paragraph(request):
    return render(request, 'birthday_app/paragraph.html', {'paragraph': STATIC_PARAGRAPH_TEXT})
