from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from apps.users.models import Profile

class SignupForm(forms.ModelForm):
    first_name = forms.CharField(
        required=False,
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'})
    )
    last_name = forms.CharField(
        required=False,
        label='Apellido',
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'})
    )
    avatar = forms.ImageField(
        required=False,
        label='Foto de perfil',

    )
    password1 = forms.CharField(
        label='Contraseña (*)',
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'})
    )
    password2 = forms.CharField(
        label='Confirmar contraseña (*)',
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'})
    )
    request_editor_role = forms.BooleanField(required=False, label="Solicitar rol de editor")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar', 'request_editor_role']
        labels = {
            'username': 'Nombre de usuario (*)',
            'email': 'Correo electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")

        first = cleaned_data.get("first_name", "").strip()
        last = cleaned_data.get("last_name", "").strip()
        if not first and not last:
            raise ValidationError("Debes completar al menos el nombre o el apellido.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.first_name = self.cleaned_data.get("first_name", "")
        user.last_name = self.cleaned_data.get("last_name", "")

        if commit:
            user.save()
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.requested_editor = self.cleaned_data.get("request_editor_role", False)
            if self.cleaned_data.get("avatar"):
                profile.avatar = self.cleaned_data["avatar"]
            profile.save()

        return user