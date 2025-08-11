from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from apps.posts.models import Post
from apps.posts.forms.post_form import PostForm

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit.html'

    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        user = self.request.user
        post = self.get_object()
        print("Tipo de is_editor:", type(user.profile.is_editor))

        return user.is_authenticated and user == post.author and user.profile.is_editor()
    
    def form_valid(self, form):
        messages.success(self.request, "✅ Cambios guardados correctamente.")
        print("✅ Formulario válido, redirigiendo a detalle...")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "❌ El formulario tiene errores.")
        print("❌ Formulario inválido:", form.errors)
        return super().form_invalid(form)

