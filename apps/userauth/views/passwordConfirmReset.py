from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth import login
from apps.userauth.forms.setNewPasswordForm import SetNewPasswordForm

class PasswordResetConfirmView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError):
            user = None

        if user and default_token_generator.check_token(user, token):
            form = SetNewPasswordForm()
            return render(request, "password_reset_confirm.html", {"form": form, "uidb64": uidb64, "token": token})
        else:
            return render(request, "password_reset_confirm.html", {"invalid": True})
    
    def post(self, request, uidb64, token):
        form = SetNewPasswordForm(request.POST)
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError):
            user = None

        if user and default_token_generator.check_token(user, token):
            if form.is_valid():
                new_password = form.cleaned_data['new_password']
                user.set_password(new_password)
                user.save()
                login(request, user)
                return redirect("profile_view")  # o donde quieras redirigir
        return render(request, "password_reset_confirm.html", {"form": form, "uidb64": uidb64, "token": token})