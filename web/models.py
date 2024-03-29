from django.db import models


# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    topic = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title