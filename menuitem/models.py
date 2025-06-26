from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('blogger', 'Blogger'),
        ('user', 'User'),
    ]

    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"




# Create your models here.
class Menuitem(models.Model):
     author = models.ForeignKey(
     settings.AUTH_USER_MODEL,
     on_delete=models.CASCADE,
     related_name='menu_posts'  # Add this to avoid clashes if you have another Post model in a different app
    )
     item_title=models.CharField(max_length=100)
     item_description=models.CharField(max_length=200)
     item_price = models.IntegerField()
     item_list = models.ForeignKey("Itemlist", verbose_name=("item_list"), on_delete=models.CASCADE, null=True)
     item_image = models.ImageField(upload_to='images/', blank=True, null=True)
     created_at = models.DateTimeField(auto_now_add=True)
   
class Itemlist(models.Model):
    category_name=models.CharField(max_length=100)
    


    def __str__(self):
        return self.category_name

class Feedback(models.Model):
    user_name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    rating=models.IntegerField()













