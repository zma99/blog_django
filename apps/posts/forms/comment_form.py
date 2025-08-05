from django import forms
from apps.posts.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Escribí tu comentario...",
                "class": "w-full p-3 border rounded resize-none focus:outline-none focus:ring-2 focus:ring-indigo-500"
            })
        }
        labels = {
            "content": ""
        }