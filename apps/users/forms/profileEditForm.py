from django import forms
from apps.users.models import Profile

class ProfileEditForm(forms.ModelForm):
    
    first_name = forms.CharField(
        label='Nombre',
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
        })
    )

    last_name = forms.CharField(
        label='Apellido',
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
        })
    )

    email = forms.EmailField(
        label='Email',
        required=False,
        disabled=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 bg-gray-100 border border-gray-300 rounded-md shadow-sm text-gray-500 cursor-not-allowed'
        })
    )

    username = forms.CharField(
        label='Nombre de usuario',
        required=False,
        disabled=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 bg-gray-100 border border-gray-300 rounded-md shadow-sm text-gray-500 cursor-not-allowed'
        })
    )

    class Meta:
        model = Profile
        fields = ['avatar', 'requested_editor']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'hidden'}),
            'requested_editor': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded'
            }),
        }
        labels = {
            'avatar': 'Foto de perfil',
            'requested_editor': 'Solicitar rol de editor',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Accedemos al usuario desde el profile instanciado
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
            self.fields['username'].initial = self.instance.user.username


    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.first_name = self.cleaned_data.get('first_name', user.first_name)
        user.last_name = self.cleaned_data.get('last_name', user.last_name)
        if commit:
            user.save()
            profile.save()
        return profile
    