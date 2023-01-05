from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=60)
    content = models.TextField(null=False)
    price = models.CharField(max_length=10)
    image = models.ImageField(null=True, blank=True)
    discount = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name