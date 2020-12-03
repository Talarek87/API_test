from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=1000)
    cont_art = models.CharField(max_length=1000)
    picture = models.CharField(max_length=1000)

    def __str__(self):
        return self.title