from  django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from booking.models import Book
from menuitem.models import Menuitem
from buy_now.models import Product
from buy_now.models import CartItem
from django.http import HttpResponseBadRequest
from django.db.models import Sum
from menuitem.models import Feedback
from django.contrib.auth import login,logout
from django.core.paginator import Paginator
from menuitem.forms import MenuItemForm
from offer.models import Offer
from menuitem.models import Itemlist
from django.views.decorators.cache import never_cache
from decimal import Decimal



def home(request):
    menu = Menuitem.objects.all()
    offers = Offer.objects.filter(is_active=True)

    context = {
      
         'home_section': True, 
         'menuitem':menu,
         'offers':offers
                  
    
    }
    return render(request,"index.html",context)
   


def user_login(request):
      print("hhfjfhgij")
     #  user=User.objects.all()
      print(request)
      print("mmihihgbhg")
      if request.method == "POST":
           print("validated user")
           username = request.POST.get('username')
           password = request.POST.get('password')
           user = authenticate(username=username,password=password)
           print("*"*50)
           print(user)
           print("*"*50)
           if user is not None:
             login(request,user)
             if user.is_superuser:
               print("admin to sucessful") 
               return redirect('admin:index')
             
           
             elif getattr(user, 'userprofile', None) and user.userprofile.role == 'blogger':
                 return redirect('list_post')
             else:
               posts= Menuitem.objects.all()
               print("total post",{posts.count()})
               print("validated user")
               return redirect('home')
      
           else:
               print('wrong creds...')
               return redirect('login')
      else:
           print("hghfgjgf")
           return render(request, 'login.html')
      

def user_register(request):
     return render(request,"register.html")
def about(request):
    return render(request,"about.html")
@login_required(login_url='login')
def book(request):
      print("request.user")
      print(request.user.email)
      return render(request,"book.html")
     
@login_required
def menu(request):
     menu= Menuitem.objects.all()
     data={
           
           'menuitem':menu

      }
     return render(request,"menu.html",data)
   

def user_logout(request):
     logout(request)
     return redirect('login')


def list_post(request):
      menu = Menuitem.objects.all()
      user = request.user
      role = getattr(user, 'role', '') 
 # Or use user.userprofile.role

      if role == 'blogger':
        is_list_page = True
        posts_list = Menuitem.objects.filter(author=user).order_by('-id')
      else:
        is_list_page = False
        posts_list = Menuitem.objects.all()

        paginator = Paginator(posts_list, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
   
        return render(request, 'list_post.html', {
         'posts': page_obj,
         'heading': 'My Posts',
         'is_list_page': is_list_page,
         'menuitem':menu
    })


@login_required
def edit_post(request, id):
     item = get_object_or_404(Menuitem, id=id)
     if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')  # Or your listing page
     else:
        form = MenuItemForm(instance=item)
        return render(request, 'edit_post.html', {'form': form})
   

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Menuitem, pk=pk)
    if post.author == request.user:  # optional: ensure only the author can delete
        post.delete()
    return redirect('list_post')


def savedata(request):
  print(f"Request method: {request.method}")
  print(f"Request user: {request.user }")
  en=''
  print("save the data")
  if request.method == "POST":
      name=request.POST.get('name')
      phone=request.POST.get('phone')
      email=request.POST.get('email')
      select=request.POST.get('person')
      date=request.POST.get('date')
      en=Book(name=name,phone_number=phone,email=email,select_person=select,date=date)
      en.save()
      print("save the data")
  return render(request,"index.html")


def cart(request):
     list=CartItem.objects.filter()
     data={
           'cartitem':list,
           'total_price':list.aggregate(Sum('new_price'))['new_price__sum'],
     
             }
     return render(request,"cart.html",data)

def remove_user(request,id):
    if request.method == "POST":
        user = get_object_or_404(CartItem, id=id)

        user.delete()
        return redirect('cart')




def remove_all(request):
  if request.method == "POST":
      user=Product.objects.all()
      user.delete()
      return redirect('cart')
  else:
     return redirect('cart')
 
def calculate_price(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity'))

        item = CartItem.objects.get(id=item_id)
        product_price = item.Product.price
        item.quantity = quantity
        active_offer = Offer.objects.filter(product=item.Product, is_active=True).first()

        if active_offer:
            discount = (product_price * Decimal(active_offer.percentage)) / 100
        else:
            discount = Decimal('0.00')

        item.new_price = (product_price - discount) * item.quantity
        item.save()
     

        return redirect('cart')

def add_quantity(request,id):
     if request.method == "POST":
       item= get_object_or_404(CartItem,id=id)
       item.quantity +=1
       item.new_price=item.Product.price * item.quantity    
       item.save()
       return redirect('cart')


def total_price(request,id):
     print("hfgfgjfj")
     if request.method =="POST":
       item=get_object_or_404(CartItem,id=id)
       cart_items= CartItem.objects.filter(id=id)
       total_price=sum(item.new_price for item in cart_items)
       item.total_price = total_price
       item.save()
       context={
           'cart_items':cart_items,
           'total_price':total_price
           }
       return render(request,'cart.html',context)
     
def feedback(request):
         item=Feedback.objects.all()
         data={
             
             'feedback':item
          }
         return render(request,"feedback.html",data)
def list_post(request):
     menu = Menuitem.objects.all() 
     user = request.user
     blogger = request.user
     if getattr(blogger, 'role', '') == 'blogger':
         is_list_page = True
         posts_list = Menuitem.objects.filter(author=user).order_by('-id')
     else:
         is_list_page = False
     posts = Menuitem.objects.filter(author=request.user) 
     posts_list = Menuitem.objects.all()  
     paginator = Paginator(posts_list, 3) 

     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)   

     return render(request, 'list_post.html', {
         'posts': page_obj,  
         'heading': 'My Posts',        
         'is_list_page': is_list_page,
         'menuitem':menu
          
        
    })
        
     return render(request,"list_post.html")


def blogger(request):
    return render(request,"blogger.html")

def remove_post(request,id):
    if request.method == "POST":
        item = get_object_or_404(Menuitem, id=id)

        item.delete()
        return redirect('list_post')


def category(request,category_name):
    menuitems = Menuitem.objects.filter(item_list__category_name__iexact=category_name)
    categories = Itemlist.objects.all()
    if category_name == 'all':
        menuitems = Menuitem.objects.all()
    else:
        menuitems = Menuitem.objects.filter(item_list__category_name__iexact = category_name)
    
    categories = Itemlist.objects.all()
    return render(request,'menu.html',{
        'menuitems':menuitems,
        'categories':categories,
         'active_category':category_name.lower(),
    })

