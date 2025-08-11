from django.db import models
from django.core.exceptions import ValidationError
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User


# CATEGORIA
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



# POST
class Post(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name="Categoría",
        default=1
    )
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )
    cover = models.ImageField(
        upload_to="covers_posts_images/", null=True, blank=True, verbose_name="Portada"
    )
    title = models.CharField(max_length=50, verbose_name="Título")
    abstract = models.TextField(max_length=300, verbose_name="Resumen")
    # body = models.TextField(verbose_name="Cuerpo")
    body = CKEditor5Field(config_name='default')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    likes = models.ManyToManyField(
        User, related_name="likes", blank=True, verbose_name="Me gusta"
    )
    views = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old = Post.objects.get(pk=self.pk)
            if old.cover and old.cover != self.cover:
                old.cover.delete(save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post")  # Evita duplicados



class PostReport(models.Model):
    REASON_CHOICES = [
        ('inapropiado', 'Contenido inapropiado'),
        ('ofensivo', 'Lenguaje ofensivo'),
        ('spam', 'Spam o publicidad'),
        ('otro', 'Otro'),
    ]

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reports')
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if PostReport.objects.filter(post=self.post, reported_by=self.reported_by).exists():
            raise ValidationError("Ya has reportado este post.")


    def __str__(self):
        return f"Reporte de {self.post.title} por {self.reported_by.username}"



# COMENTARIO
class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comentario de {self.user} en {self.post}"
