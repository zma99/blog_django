from django.views.generic.list import ListView
from apps.posts.models import Post, Category

class PostListView(ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = Post.objects.all().order_by('-creation_date')
        if slug:
            queryset = queryset.filter(category__slug=slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        if slug:
            category = Category.objects.filter(slug=slug).first()
            context['current_category'] = category.name if category else slug
        return context