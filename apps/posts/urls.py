from django.urls import path
from .views.create import CreatePostView
from .views.list import PostListView

app_name = 'posts'

urlpatterns = [
    path('nuevo/', CreatePostView.as_view(), name='post_create'),
    path('list/', PostListView.as_view(), name='list'),
]
