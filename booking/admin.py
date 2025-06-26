from django.contrib import admin
from .models import Book
from .models import Post

admin.site.register(Book)

# Register your models here.
admin.site.register(Post)