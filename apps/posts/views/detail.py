
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from apps.posts.models import Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'