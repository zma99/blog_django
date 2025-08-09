from django.views.generic import TemplateView
from django.contrib import messages

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



# class ProfileView(TemplateView):
#     template_name = 'profile_view.html'

#     def get(self, request, *args, **kwargs):
#         profile = request.user.profile

#         if profile.requested_editor and profile.rol == 'reader':
#             messages.info(request, "Tu solicitud para ser editor está pendiente de aprobación.")
#         elif profile.requested_editor and profile.rol == 'editor':
#             messages.success(request, "¡Tu rol de editor ha sido aprobado!")
#             profile.requested_editor = False
#             profile.save()

#         return super().get(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['profile'] = self.request.user.profile
#         return context