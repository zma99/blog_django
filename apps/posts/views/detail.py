from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from apps.posts.models import Post, PostView
from apps.posts.forms.comment_form import CommentForm

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        post = self.object

        # Tracking de vistas (idéntico al tuyo)
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

        context = self.get_context_data(object=post)
        context["comments"] = post.comments.select_related("user").order_by("-created_at")
        context["comment_form"] = CommentForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        post = self.object
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("posts:detail", pk=post.pk)  # o usar self.object.pk

        # Si el form falla, reenviamos con errores y contexto
        context = self.get_context_data(object=post)
        context["comments"] = post.comments.select_related("user").order_by("-created_at")
        context["comment_form"] = form
        return self.render_to_response(context)

    def get_queryset(self):
        return super().get_queryset().prefetch_related('likes')