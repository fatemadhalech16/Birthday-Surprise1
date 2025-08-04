from django.urls import path
from . import views

urlpatterns = [
    path('', views.countdown, name='countdown'),
    path('surprise/', views.surprise, name='surprise'),
    path('paragraph/', views.paragraph, name='paragraph'),
    path('letter/', views.letter, name='letter'),
]
