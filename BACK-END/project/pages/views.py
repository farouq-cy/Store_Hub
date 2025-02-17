from django.shortcuts import render , redirect
from .models import *
from django.db.models import Count , Max 
from .forms import *
from django.contrib import messages 
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth.decorators import *

def index(request):

    top_products = Product.objects.annotate(likes_count=Count('likes__id')).order_by('-likes_count')[:5]
    
    flash_sales = FlashSale.objects.all()

    max_time = flash_sales.aggregate(max_end_time=Max('end_date'))['max_end_time'] if flash_sales else None


    return render(request, 'pages/index.html', {
        'products': top_products,
        'flash_sales': flash_sales,
        'max_time': max_time
    })


from django.shortcuts import get_object_or_404


@login_required
def wishlist(request):
    liked_products = Product.objects.filter(likes=request.user).select_related("saler")
    random_products = Product.objects.exclude(likes=request.user).order_by('?')[:4]
    for product in random_products:
        product.star_list = range(int(round(product.rating))) 


    return render(request, 'pages/wishlist.html', {
        'liked_products': liked_products,
        'random_products': random_products
    })
@login_required
def toggle_like(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user in product.likes.all():
        product.likes.remove(request.user)  
        liked = False
    else:
        product.likes.add(request.user)  
        liked = True
    for product in product:
        product.togel_like = range(int(round(product.rating))) 
    return JsonResponse({'liked': liked, 'likes_count': product.likes.count()})

def about(request):
    return render(request, 'pages/about.html')





def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'pages/onepro.html', {'product': product})












@csrf_exempt
def user_login(request):
    if request.method == "POST":
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)

            if user and isinstance(user, User):
                login(request, user)
                messages.success(request, "تم تسجيل الدخول بنجاح!")
                return redirect('index')
            else:
                messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة.")
    else:
        form = CustomLoginForm()
    
    return render(request, 'pages/login.html', {'form': form})





def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            role = form.cleaned_data['role']
            phone_number = form.cleaned_data['phone_number']

            if User.objects.filter(username=username).exists():
                messages.error(request, "اسم المستخدم هذا موجود بالفعل.")
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.error(request, "البريد الإلكتروني هذا مسجل بالفعل.")
                return redirect('register')

            user = form.save(commit=False)  # نحفظ المستخدم بدون حفظ نهائي
            user.set_password(form.cleaned_data['password1'])
            user.save()  # نحفظ المستخدم عشان يتسجل في الداتابيز

            # إنشاء الـ UserProfile وربطه بالمستخدم
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.role = role
            profile.phone_number = phone_number
            profile.save()

            # تسجيل الدخول للمستخدم
            login(request, user)

            messages.success(request, "تم إنشاء الحساب بنجاح!")  
            return redirect('index')  

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
    colors = ['red', 'green', 'yellow', 'blue', 'orangered', 'black']


    products = Product.objects.all()
    selected_category = request.GET.get('category')
    selected_color = request.GET.get('color')

    filters = Q()
 
    if selected_category:
        
        filters &= Q(category__name=selected_category)

    if selected_color:
        filters &= Q(color=selected_color)

    if filters:
        products = products.filter(filters)

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'colors': colors,
        'products': page_obj.object_list,
        'page_obj': page_obj,
    }

    return render(request, 'pages/allproduct.html', context) 





#لو حطيت .get(rating__gte=3) لا يعرض الا المنتجات التي تكون تقييمها 3 او اكبر
#.filter-price__exact=10 view all price10
#contains=10 view all contains 10
#price__range=(10,20) view all between 10-20
#price__in=(10,20) view all between 10-20
#price__in=[10,20] view all between 10-20
