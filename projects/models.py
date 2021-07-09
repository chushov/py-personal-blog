from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=76)
    description = models.TextField(max_length=150)
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to="static/img")
