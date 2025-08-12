from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

from apps.users.models import Profile
from apps.users.forms.profileEditForm import ProfileEditForm

class ProfileView(TemplateView):
    template_name = 'profile_view.html'
    context_object_name = 'profile'

    def get(self, request, *args, **kwargs):
        self.profile = request.user.profile  # Guardamos el perfil para usarlo luego

        if self.profile.requested_editor and self.profile.rol == 'reader':
            messages.info(request, "Tu solicitud para ser editor está pendiente de aprobación.")
        elif self.profile.requested_editor and self.profile.rol == 'editor':
            messages.success(request, "¡Tu rol de editor ha sido aprobado!")
            self.profile.requested_editor = False
            self.profile.save()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = getattr(self, 'profile', self.request.user.profile)
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('user:profile_view') 

    def get_object(self, queryset=None):
        # Asegura que el usuario solo edite su propio perfil
        return self.request.user.profile

