from django import forms

class SetNewPasswordForm(forms.Form):
    new_password = forms.CharField(
        label="Nueva contraseña",
        min_length=8,
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Ingresá tu nueva contraseña"
        })
    )
    confirm_password = forms.CharField(
        label="Confirmar contraseña",
        min_length=8,
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Confirmá la nueva contraseña"
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("new_password")
        p2 = cleaned_data.get("confirm_password")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data