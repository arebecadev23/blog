from django.db import models

# Create your models here.
from django.db import models

#ao riara classe Post, consigo 
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo