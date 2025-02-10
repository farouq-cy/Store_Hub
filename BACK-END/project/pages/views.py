from django.shortcuts import render , redirect
from .models import *
from django.db.models import Count , Max
from .forms import ContactForm
def index(request):
    # جلب المنتجات الأكثر إعجابًا
    top_products = Product.objects.annotate(likes_count=Count('likes__id')).order_by('-likes_count')[:5]
    
    # جلب جميع العروض
    flash_sales = FlashSale.objects.all()

    # تحديد أقرب وقت انتهاء بين كل العروض
    max_time = flash_sales.aggregate(max_end_time=Max('end_date'))['max_end_time'] if flash_sales else None


    return render(request, 'pages/index.html', {
        'products': top_products,
        'flash_sales': flash_sales,
        'max_time': max_time
    })

def about(request):
    return render(request, 'pages/about.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/signup.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        
        return redirect('contact')  # إعادة تحميل الصفحة بعد الإرسال

    return render(request, 'pages/contact.html')








#لو حطيت .get(rating__gte=3) لا يعرض الا المنتجات التي تكون تقييمها 3 او اكبر
#.filter-price__exact=10 view all price10
#contains=10 view all contains 10
#price__range=(10,20) view all between 10-20
#price__in=(10,20) view all between 10-20
#price__in=[10,20] view all between 10-20
