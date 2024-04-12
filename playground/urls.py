from django.urls import path
from . import views

# URL config
urlpatterns = [
    path('hello/', views.say_hello)
]