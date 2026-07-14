from django.db import models
from django.db.models.fields import DateField
from django.forms import CharField


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=15)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name