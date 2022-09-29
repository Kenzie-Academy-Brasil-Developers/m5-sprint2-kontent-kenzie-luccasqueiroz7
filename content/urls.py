from django.urls import path
from . import views

urlpatterns = [
    path("contents/", views.ContentView.as_view()),
]
