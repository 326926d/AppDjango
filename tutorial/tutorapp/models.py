from django.db import models

class Message(models.Model):
    greetings = models.CharField(max_length=200)

# Create your models here.
