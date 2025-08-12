from django.views.generic import TemplateView
from apps.posts.models import Post, Category
from django.contrib.auth import get_user_model

User = get_user_model()


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_posts"] = Post.objects.count()
        context["total_categories"] = Category.objects.count()
        context["total_users"] = User.objects.count()
        context["categories"] = Category.objects.all()
        return context
