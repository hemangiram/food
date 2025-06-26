"""
URL configuration for hotelmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home,name='home'),
    path('login/', user_login,name='login'),
    path('register/', user_register,name='register'),
    path('about', about,name='about'),
    path('book', book,name='book'),
    path('menu', menu,name='menu'),
    path('logout', user_logout,name='logout'),
    path('list/post', list_post,name='list_post'),
    path('save', savedata,name='save'),
    path('cart',cart,name='cart'),
    path('cart1/<int:id>/', remove_user,name='remove_user'),
   # path('cart2/<int:id>',total,name='total'),
    path('cart1',remove_all,name='remove_all'),
    path('totalprice', total_price,name='total'),
    path('update/<int:id>/', add_quantity,name='update'),
    path('productprice',  calculate_price,name='calculate_price'),
    path('feedback', feedback,name='feedback'),
    path('list_post', list_post,name='list_post'),
    path('blogger', blogger,name='blogger'),
    path('edit_post/<int:id>/', edit_post, name='edit_post'),
    path('delete_post/<int:id>/', delete_post, name='delete_post'),
    path('remove_post/<int:id>', remove_post,name='remove_post'),
    path('category/<str:category_name>/', category,name='categories')



]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





