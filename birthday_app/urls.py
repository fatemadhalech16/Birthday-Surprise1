from django.urls import path
from . import views

urlpatterns = [
    path('', views.countdown, name='countdown'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('surprise/', views.surprise, name='surprise'),
    path('paragraph/', views.paragraph, name='paragraph'),
    path('letter/', views.letter, name='letter'),
]
