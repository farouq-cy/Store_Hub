from django.shortcuts import render 
from .models import *
from django.db.models import Count
def index(request):
    top_products = Product.objects.annotate(likes_count=Count('likes__id')).order_by('-likes_count')[:5]
    return render(request, 'pages/index.html', {'products': top_products, 'flash_sales': FlashSale.objects.all()})

def about(request):
    return render(request, 'pages/about.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/signup.html')








#لو حطيت .get(rating__gte=3) لا يعرض الا المنتجات التي تكون تقييمها 3 او اكبر
#.filter-price__exact=10 view all price10
#contains=10 view all contains 10
#price__range=(10,20) view all between 10-20
#price__in=(10,20) view all between 10-20
#price__in=[10,20] view all between 10-20
