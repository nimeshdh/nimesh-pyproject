from django.db import models

# Create your models here.


class Users(models.Model):  # Class name should be Capitalized (PEP8 convention)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.CharField(max_length=200, default='N/A')

    def __str__(self):  # Added space after 'def' and colon at the end
        return self.name  # Indented properly
