from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    rol = models.CharField(
        max_length=20,
        choices=[
            ("admin", "Admin"),
            ("auditor", "Auditor"),
            ("editor", "Editor"),
            ("reader", "Reader"),
        ],
        default="reader",
    )
    requested_editor = models.BooleanField(default=False)
    requested_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    avatar = models.ImageField(
        upload_to="users/profile/avatars/",
        default="users/profile/avatars/uknown-avatar.png",
        null=True,
        blank=True,
    )

    def is_editor(self):
        return self.rol == "editor"
    
    def is_auditor(self):
        return self.rol == "auditor"
    
    def is_not_auditor(self):
        return self.rol != "auditor"

    def __str__(self):
        return f"{self.user.username} - {self.rol}"
