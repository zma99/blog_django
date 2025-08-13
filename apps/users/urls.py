# users/urls.py
from django.urls import path
from .views import ProfileView, ProfileUpdateView, UserPostsView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile_view'),
    path('edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('my-posts/', UserPostsView.as_view(), name='user_posts'),
]