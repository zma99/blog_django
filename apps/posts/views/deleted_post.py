from django.shortcuts import render
from apps.posts.models import PostReport

def deletedPost(request, pk):
    report = PostReport.objects.filter(post_id=pk).order_by('-created_at').first()
    context = {
        "post_id": pk,
        "report": report,
    }
    return render(request, "deleted_post.html", context)