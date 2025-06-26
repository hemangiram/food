from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    name= models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

def __str__(self):
    return self.name


class CartItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    new_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

   

# Create your models here.
