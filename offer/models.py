from django.db import models
from buy_now.models import Product 

# Create your models here.
class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='offers')
    title = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField() 
    image = models.ImageField(upload_to='offers/', blank=True,null=True)
 
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.percentage}% on {self.product.name}"
    