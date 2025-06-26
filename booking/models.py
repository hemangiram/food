from django.db import models
from django.conf import settings

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100,null=False, blank=False)
    phone_number=models.IntegerField()
    email=models.EmailField(max_length=20,blank=True, null=True, default=None)
    select_person=models.IntegerField()
    date=models.DateField(max_length=20)

def __str__(self):
    return self.name

class Post(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    image=models.ImageField(name="images/" )
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)




    