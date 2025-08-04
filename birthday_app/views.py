from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Timer
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('letter')  # redirect after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'birthday_app/login.html', {'form': form})


@login_required
def letter(request):
    timer = Timer.objects.first()
    return render(request, 'birthday_app/letter.html', {'letter_text': timer.letter_text})


def logout_view(request):
    logout(request)
    return redirect('login')

def countdown(request):
    timer = Timer.objects.first()
    if not timer:
        return render(request, 'birthday_app/no_timer.html')  # Show a message like “Admin hasn’t set the timer yet.”

    return render(request, 'birthday_app/index.html', {'release_time': timer.release_time})




def surprise(request):
    timer = Timer.objects.first()
    if not timer or timezone.now() < timer.release_time:
        return redirect('countdown')
    return render(request, 'birthday_app/surprise.html')

def paragraph(request):
    timer = Timer.objects.first()
    return render(request, 'birthday_app/paragraph.html', {'paragraph': timer.paragraph_text})

