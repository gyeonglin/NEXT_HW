from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, default=None)
    content = models.TextField(default=None)

    def __str__(self):
        return self.title

