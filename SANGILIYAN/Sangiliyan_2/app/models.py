from django.db import models
from django.contrib.auth.models import User

# Options pour le statut de l'article
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(help_text="Introduction ou description générale")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

# Ce modèle permet de créer autant d'onglets que tu veux (Histoire, Culture, etc.)
class Section(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=100, help_text="Nom de l'onglet (ex: Histoire)")
    body = models.TextField(help_text="Contenu de cet onglet")
    order = models.IntegerField(default=0, help_text="Ordre d'affichage")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.post.title}"