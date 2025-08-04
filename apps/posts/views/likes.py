from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.posts.models import Post
from django.http import JsonResponse


class PostLikeView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)

        liked = False
        if request.user != post.author:
            if request.user in post.likes.all():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
                liked = True

        return JsonResponse({
            'liked': liked,
            'likes_count': post.likes.count()
        })
