
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings
from apps.userauth.forms.passwordResetForm import PasswordResetForm

class PasswordResetView(View):
    def get(self, request):
        form = PasswordResetForm()
        return render(request, "password_reset.html", {"form": form})

    def post(self, request):
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            reset_link = request.build_absolute_uri(f"/auth/reset/{uid}/{token}/")

            send_mail(
                subject="Restablecer contraseña",
                message=f"Usá este enlace para restablecer tu contraseña:\n{reset_link}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )

            return render(request, "password_reset.html", {
                "form": form,
                "success": "Se ha enviado un correo con instrucciones para restablecer tu contraseña."
            })

        return render(request, "password_reset.html", {"form": form})