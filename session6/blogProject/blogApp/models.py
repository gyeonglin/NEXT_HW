from django.db import models

# Create your models here.
class Name(models.Model) :
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

class Article(models.Model) :
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__ (self) :
        return self.title
