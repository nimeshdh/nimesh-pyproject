from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # ✅ Add this line


    def __str__(self):
        return self.name
