from django.db import models

# Create your models here.

class Document(models.Model):
    doc = models.FileField()
