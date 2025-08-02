from django import forms
from apps.posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'category',
            'cover',
            'title',
            'abstract',
            'body',
        ]
