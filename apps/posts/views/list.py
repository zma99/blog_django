from django.views.generic.list import ListView
from django.db.models import Count, Q
from apps.posts.models import Post, Category

class PostListView(ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        slug = self.kwargs.get('slug')  # categoría por slug
        order = self.request.GET.get('order', 'recent')  # orden por defecto
        category_slug = self.request.GET.get('category')
        search_query = self.request.GET.get('q')    # Búsqeuda de posts

        queryset = Post.objects.all()

        # Filtro por categoría (slug en URL)
        if slug:
            queryset = queryset.filter(category__slug=slug)

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        # Ordenamiento
        if order == 'views':
            queryset = queryset.order_by('-views')
        elif order == 'likes':
            queryset = queryset.order_by('-likes')
        elif order == 'comments':
            queryset = queryset.annotate(num_comments=Count('comments')).order_by('-num_comments')
        elif order == 'recent':
            queryset = queryset.order_by('-creation_date')
        elif order == 'oldest':
            queryset = queryset.order_by('creation_date')

        if search_query:
            queryset = queryset.filter(
            Q(title__icontains=search_query) |
            Q(body__icontains=search_query) |
            Q(author__username__icontains=search_query)
        )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_slug = self.request.GET.get('category')
        slug = self.kwargs.get('slug')

        if slug:
            category = Category.objects.filter(slug=slug).first()
            context['current_category'] = category.name if category else slug

        context['selected_category'] = category_slug
        context['selected_order'] = self.request.GET.get('order', 'recent')
        context['order_options'] = [
            ('recent', 'Más reciente'),
            ('oldest', 'Más antiguo'),
            ('views', 'Más visitas'),
            ('likes', 'Más gustados'),
            ('comments', 'Más comentados'),
        ]
        context['categories'] = Category.objects.all()
        context['search_query'] = self.request.GET.get('q', '')

        return context