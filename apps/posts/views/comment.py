from django.views import View
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.utils.timezone import localtime
from apps.posts.models import Comment
from apps.posts.forms.comment_form import CommentForm


class CommentCreateAjaxView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post_id
            comment.user = request.user
            comment.save()

            html = render_to_string('comments/partial_comment.html', {'comment': comment}, request=request)
            return JsonResponse({'success': True, 'html': html})
        return JsonResponse({'success': False, 'error': 'Comentario inválido'})


class CommentUpdateAjaxView(View):
    def post(self, request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if comment.user != request.user:
            return HttpResponseForbidden("No tenés permiso para editar este comentario.")

        new_content = request.POST.get('content', '').strip()
        if new_content:
            comment.content = new_content
            comment.save()
            return JsonResponse({
                'success': True,
                'content': comment.content,
                'edited_at': localtime(comment.updated_at).strftime('%d/%m/%Y - %H:%M')  # 👈 esta línea
            })
        return JsonResponse({'success': False, 'error': 'Contenido vacío'})
    


class CommentDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        comment_id = request.POST.get('id')

        try:
            comment = Comment.objects.get(id=comment_id)

            # if request.user.profile.is_auditor or request.user == comment.user:
            if request.user.profile.is_auditor:
                comment.delete()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'No tenés permiso para eliminar este comentario.'}, status=403)

        except Comment.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Comentario no encontrado.'}, status=404)