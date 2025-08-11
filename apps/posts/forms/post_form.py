from django import forms
from apps.posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'abstract', 'category', 'cover', 'body']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Título del post'
            }),
            'abstract': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border rounded-md h-24 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Resumen breve...'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'cover': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md bg-white'
            }),
            'body': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border rounded-md h-48 resize-y focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Contenido completo...'
            }),
        }