from django.views import View
from django.http import JsonResponse, HttpResponseForbidden
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