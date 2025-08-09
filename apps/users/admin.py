from django.contrib import admin
from django.utils import timezone
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'rol', 'requested_editor')
    list_filter = ('rol', 'requested_editor')
    actions = ['aprobar_solicitud_editor']

    @admin.action(description='Aprobar solicitud de editor')
    def aprobar_solicitud_editor(self, request, queryset):
        for profile in queryset.filter(requested_editor=True):
            profile.rol = 'editor'
            # profile.requested_editor = False
            profile.approved_at = timezone.now()
            profile.save()
        self.message_user(request, "Solicitudes aprobadas correctamente.")


    def solicitud_pendiente(self, obj):
        return obj.requested_editor and obj.rol != 'editor'
    solicitud_pendiente.boolean = True
    solicitud_pendiente.short_description = "Solicitud pendiente"

    list_display = ('user', 'rol', 'requested_editor', 'solicitud_pendiente')
