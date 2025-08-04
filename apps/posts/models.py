from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Categoría')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    cover = models.ImageField(upload_to='covers_posts_images/', null=True, blank=True, verbose_name='Portada')
    title = models.CharField(max_length=50, verbose_name='Título')
    abstract = models.TextField(max_length=300, verbose_name='Resumen')
    body = models.TextField(verbose_name='Cuerpo')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    likes = models.ManyToManyField(User, related_name="likes", blank=True, verbose_name='Me gusta')
    views = models.IntegerField(default=0)

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
        unique_together = ('user', 'post')  # Evita duplicados
