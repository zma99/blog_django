from django.views.generic import TemplateView
from django.db.models import Count
from apps.posts.models import Post, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Métricas generales
        context["total_posts"] = Post.objects.count()
        context["total_categories"] = Category.objects.count()
        context["total_users"] = User.objects.count()
        context["categories"] = Category.objects.all()

        # 🏆 Categoría destacada (por cantidad de posts)
        context["top_category"] = Category.objects.annotate(num_posts=Count("posts")).order_by("-num_posts").first()

        # 🔥 Post más popular (por visitas)
        context["most_viewed_post"] = Post.objects.order_by("-views").first()

        # 🕒 Último post publicado
        context["latest_post"] = Post.objects.order_by("-creation_date").first()

        return context