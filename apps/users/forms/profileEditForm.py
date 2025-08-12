from django import forms
from apps.users.models import Profile

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'requested_editor']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md bg-white'
            }),
            'requested_editor': forms.CheckboxInput(attrs={
                'class': 'mr-2 leading-tight'
            }),
        }
        labels = {
            'avatar': 'Foto de perfil',
            'requested_editor': 'Solicitar rol de editor',
        }