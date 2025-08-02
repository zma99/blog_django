from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=[
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('reader', 'Reader'),
    ], default='reader')

    def is_editor(self):
        return self.rol == "editor"

    def __str__(self):
        return f'{self.user.username} - {self.rol}'