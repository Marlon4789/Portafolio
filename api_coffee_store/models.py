from django.db import models

# Create your models here.

# Productos de café
class Product(models.Model):
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    image_url = models.URLField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    
