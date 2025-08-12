# users/urls.py
from django.urls import path
from .views import ProfileView, ProfileUpdateView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile_view'),
    path('edit/', ProfileUpdateView.as_view(), name='edit_profile'),

]