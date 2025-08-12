from django import forms
from django.contrib.auth.models import User

class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        label="Correo electrónico",
        max_length=254,
        widget=forms.EmailInput(attrs={
            "class": "w-full px-4 py-2 mt-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Ingresa tu correo registrado"
        })
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No existe ningún usuario con ese correo.")
        return email