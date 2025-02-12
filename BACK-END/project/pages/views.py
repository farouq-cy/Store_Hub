from django.shortcuts import render , redirect
from .models import *
from django.db.models import Count , Max , Avg
from .forms import *
from django.contrib import messages 
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.db.models import Q

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





@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('index')  # أو أي صفحة تانية بعد تسجيل الدخول
        else:
            messages.error(request, 'Invalid login credentials!')
    else:
        form = CustomLoginForm()

    return render(request, 'pages/login.html', {'form': form})





def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # تحقق من وجود اسم المستخدم والبريد الإلكتروني
            if User.objects.filter(username=username).exists():
                messages.error(request, "اسم المستخدم هذا موجود بالفعل.")
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.error(request, "البريد الإلكتروني هذا مسجل بالفعل.")
                return redirect('register')

            # إذا لم يكن هناك خطأ، قم بإنشاء المستخدم
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # تأكيد الباسورد
            user.save()

            print(f"User Created: {user.username}, {user.email}, {user.role}, {user.PhoneNumber}")

            # تسجيل الدخول بعد التسجيل
            login(request, user)

            messages.success(request, "تم إنشاء الحساب بنجاح!")  # رسالة نجاح

            return redirect('login')  # بعد التسجيل يمكنه الانتقال إلى صفحة تسجيل الدخول

        else:
            print("Form Errors:", form.errors)

    else:
        form = SignUpForm()

    return render(request, 'pages/signUp.html', {'form': form})




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
        
        return redirect('contact')

    return render(request, 'pages/contact.html')






def allproducts(request):
    categories = Category.objects.all()
    colors = [
        ('red', 'Red'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('orangered', 'OrangeRed'),
        ('black', 'Black')
    ]

    products = Product.objects.all()

    # استلام البيانات من `GET` لو الفلترة مفعلة
    selected_categories = request.GET.getlist('category')
    selected_colors = request.GET.getlist('color')

    # تحسين الفلترة باستخدام Q object
    if selected_categories:
        category_filter = Q()
        for cat_id in selected_categories:
            category_filter |= Q(category_id=cat_id)
        products = products.filter(category_filter)

    if selected_colors:
        products = products.filter(color__in=selected_colors)

    # إضافة قائمة من الأرقام للتكرار 5 مرات في القالب
    star_range = products.aggregate(Max('rating'))['rating__max']
    if star_range is None:  # التعامل مع حالة عدم وجود تقييمات
        star_range = 5

    # إضافة أي عناصر أخرى للـ context
    context = {
        'categories': categories,
        'colors': colors,
        'products': products,
    }

    # التحقق إذا كان الطلب هو AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'pages/allproduct_list.html', context)

    return render(request, 'pages/allproduct.html', context)





#لو حطيت .get(rating__gte=3) لا يعرض الا المنتجات التي تكون تقييمها 3 او اكبر
#.filter-price__exact=10 view all price10
#contains=10 view all contains 10
#price__range=(10,20) view all between 10-20
#price__in=(10,20) view all between 10-20
#price__in=[10,20] view all between 10-20
