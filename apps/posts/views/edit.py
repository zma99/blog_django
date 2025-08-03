from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from apps.posts.models import Post
from apps.posts.forms.post_form import PostForm

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit.html'
    success_url = reverse_lazy('posts:list')

    def test_func(self):
        return self.request.user == self.get_object().author and self.request.user.profile.is_editor

