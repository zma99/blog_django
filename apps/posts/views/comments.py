import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from apps.posts.models import Comment, Post

@login_required
def add_comment(request, post_id):
    if request.method == "POST":
        try:
            print("POST RECIBIDO ✅")
            print("CONTENIDO RECIBIDO:", request.body)
            print("Método HTTP:", request.method)
            data = json.loads(request.body)
            content = data.get("content", "").strip()

            if not content:
                return JsonResponse({"error": "Contenido vacío"}, status=400)

            post = Post.objects.get(pk=post_id)

            comment = Comment.objects.create(
                user=request.user,
                post=post,
                content=content
            )

            return JsonResponse({
                "username": request.user.username,
                "content": comment.content,
                "created_at": comment.created_at.strftime("%d/%m/%Y %H:%M")
            })
        # except Exception as e:
        #     return JsonResponse({"error": str(e)}, status=500)
        except Exception as e:
            print("ERROR EN LA CREACIÓN:", str(e))
            return JsonResponse({"error": str(e)}, status=500)

    print("CONTENIDO RECIBIDO:", request.body)
    print("Método HTTP:", request.method)
    return JsonResponse({"error": "Método no permitido"}, status=405)