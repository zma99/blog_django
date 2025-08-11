from django.contrib import admin
from .models import Post, Comment, PostReport

admin.site.register(Post)
admin.site.register(Comment)

@admin.register(PostReport)
class PostReportAdmin(admin.ModelAdmin):
    list_display = ('post', 'reported_by', 'reason', 'comment', 'created_at')
    list_filter = ('reason',)
    actions = ['eliminar_post_reportado']

    @admin.action(description='🗑️ Eliminar post relacionado')
    def eliminar_post_reportado(self, request, queryset):
        eliminados = 0
        for reporte in queryset:
            post = reporte.post
            if post:
                post.delete()
                eliminados += 1
        self.message_user(request, f"Se eliminaron {eliminados} post(s) relacionados.")
