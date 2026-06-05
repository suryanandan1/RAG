from django.urls import path
from .views import chat, logout_view

urlpatterns = [
    path("", chat, name="chat"),
    path("logout/", logout_view, name="logout"),
]