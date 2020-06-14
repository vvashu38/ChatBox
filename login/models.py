from django.db import models

# Create your models here.

class chat(models.Model):
    dm = models.TextField(default="Hey")
    un = models.TextField()