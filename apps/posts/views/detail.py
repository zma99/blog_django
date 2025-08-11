from django.shortcuts import redirect
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.http import Http404
from apps.posts.models import Post, PostView
from apps.posts.forms.comment_form import CommentForm

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            self.redirect_to_deleted = True
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if getattr(self, 'redirect_to_deleted', False):
            return redirect('posts:deleted_post', pk=self.kwargs.get("pk"))

        post = self.object

        # Tracking de vistas
        if request.user.is_authenticated:
            _, created = PostView.objects.get_or_create(user=request.user, post=post)
            if created:
                post.views += 1
                post.save(update_fields=["views"])
        else:
            session_key = f"viewed_post_{post.id}"
            if not request.session.get(session_key):
                post.views += 1
                post.save(update_fields=["views"])
                request.session[session_key] = True

        # Verificación de reporte
        user_has_reported = False
        if request.user.is_authenticated:
            user_has_reported = post.reports.filter(reported_by=request.user).exists()

        # Comentarios y paginación
        all_comments = post.comments.select_related("user").order_by("-created_at")
        paginator = Paginator(all_comments, 5)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)

        context = self.get_context_data(object=post)
        context.update({
            "comments": page_obj.object_list,
            "has_next": page_obj.has_next(),
            "next_page": page_obj.next_page_number() if page_obj.has_next() else None,
            "comment_form": CommentForm(),
            "user_has_reported": user_has_reported
        })
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if getattr(self, 'redirect_to_deleted', False):
            return redirect('posts:post_eliminado', pk=self.kwargs.get("pk"))

        post = self.object
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("posts:detail", pk=post.pk)

        context = self.get_context_data(object=post)
        context["comments"] = post.comments.select_related("user").order_by("-created_at")
        context["comment_form"] = form
        return self.render_to_response(context)

    def get_queryset(self):
        return super().get_queryset().prefetch_related('likes')