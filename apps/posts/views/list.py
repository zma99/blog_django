from django.views.generic.list import ListView
from apps.posts.models import Post

class PostListView(ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.all().order_by('-creation_date')