from django.db import models

# Create your models here.

# Productos de café
class Product(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField()
    description = models.TextField()
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
