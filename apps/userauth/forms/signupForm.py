from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from apps.users.models import Profile

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'})
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'})
    )

    request_editor_role = forms.BooleanField(required=False, label="Solicitar rol de editor")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'request_editor_role']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'}),
        }

    def clean(self):
        '''
        Compara y valida que la contraseña en ambos campos coincidan         
        '''

        cleaned_data = super().clean()
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise ValidationError("Las contraseñas no coinciden.")
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)   # Crea la instancia pero no la guarda aún
        user.set_password(self.cleaned_data["password1"])   # hashea la contraseña
        if commit:
            user.save() # Guarda en BD
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.requested_editor = self.cleaned_data.get("request_editor_role", False)
            profile.save()
        return user
    