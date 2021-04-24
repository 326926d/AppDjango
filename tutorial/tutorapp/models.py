from django.db import models


class Tutors(models.Model):
    name = models.CharField(max_length=255)
    disciple = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


# Create your models here.
