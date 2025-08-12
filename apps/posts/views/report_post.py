from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from apps.posts.models import Post
from apps.posts.forms.post_report_form import PostReportForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.posts.models import PostReport
from django.contrib import messages



@method_decorator(login_required, name='dispatch')
class ReportPostView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = PostReportForm()
        return render(request, "report_post.html", {"form": form, "post": post})

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        # Verificar si el usuario ya reportó este post
        if PostReport.objects.filter(post=post, reported_by=request.user).exists():
            messages.warning(request, "Ya has reportado este post.")
            return redirect("posts:detail", post_id=post.id)

        report = PostReport(post=post, reported_by=request.user)
        form = PostReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            messages.success(request, "Reporte enviado correctamente.")
            return redirect('posts:detail', pk=post.id)

        return render(request, "report_post.html", {"form": form, "post": post})
