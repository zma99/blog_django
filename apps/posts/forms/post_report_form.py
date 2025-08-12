from django import forms
from apps.posts.models import PostReport

class PostReportForm(forms.ModelForm):
    class Meta:
        model = PostReport
        fields = ['reason', 'comment']
        widgets = {
            'reason': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-md'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border rounded-md',
                'placeholder': 'Comentario adicional (opcional)',
                'rows': 3
            })
        }