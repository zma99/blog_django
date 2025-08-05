
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from apps.posts.models import Post, PostView

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    # context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        post = self.object

        if request.user.is_authenticated:
            # Usuarios registrados: PostView individual
            '''
            # Trackeo de vistas: solo incremento si el registro es nuevo
            # Ignoramo el objeto devuelto de get_or_create con "_" (devulve una tupla)
            _, created = PostView.objects.get_or_create(user=request.user, post=post)
            '''
            _, created = PostView.objects.get_or_create(user=request.user, post=post)
            if created:
                post.views += 1
                post.save(update_fields=["views"])
        else:
            # Usuarios anónimos: control con sesiones
            session_key = f"viewed_post_{post.id}"
            if not request.session.get(session_key):
                post.views += 1
                post.save(update_fields=["views"])
                request.session[session_key] = True

        context = self.get_context_data(object=post)
        return self.render_to_response(context)
    
    def get_queryset(self):
        return super().get_queryset().prefetch_related('likes')

