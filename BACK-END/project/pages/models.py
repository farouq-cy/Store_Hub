from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('delivery_agent', 'Delivery Agent'),
        ('saler', 'Saler'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='user')
    PhoneNumber = models.CharField(max_length=15, blank=True, null=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)

   
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self): 
        return self.username

    class Meta:
        verbose_name = "مستخدم"
        verbose_name_plural = "المستخدمين"

#نموذج Product
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="التصنيف")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "تصنيفات"


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم المنتج", blank=True, null=True, default="منتج بدون اسم")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر", default=0.00)
    saler = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    image = models.ImageField(upload_to='products/', default='default.jpg', verbose_name="صورة المنتج", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="اللون", blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='product_likes', blank=True, verbose_name="اللايكات")
    color = models.CharField(max_length=50, choices=[
        ('red', 'Red'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('orangered', 'OrangeRed'),
        ('black', 'Black')],
        default="black", verbose_name="اللون")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="التصنيف")
    rating = models.FloatField(default=0, verbose_name="التقييم")

    def __str__(self):
        return self.name

    def total_likes(self):
        return self.likes.count()

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "منتجات"

    def _str_(self):
        return self.name

    def total_likes(self):
        return self.likes.count()

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "منتجات"
        ordering = ['-rating']

# نموذج Order
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    Product = models.ForeignKey(Product, verbose_name="المنتج", on_delete=models.CASCADE)
    Customer = models.ForeignKey( User,verbose_name="العميل" ,on_delete=models.CASCADE, related_name='orders')
    Quantity = models.IntegerField(verbose_name="كمية", default=1)
    OrderDate = models.DateTimeField(verbose_name="تاريخ الطلب" ,auto_now_add=True)
    Status = models.CharField( verbose_name="حالة الطلب" ,max_length=20, choices=STATUS_CHOICES, default='Pending')
    DeliveryAgent = models.ForeignKey(User, verbose_name="وكيل التوصيل", on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')

    def _str_(self):
        return f"Order {self.id} - {self.Status}"
    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "طلبات"

# نموذج Report
class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('Sales', 'Sales'),
        ('Inventory', 'Inventory'),
        ('Financial', 'Financial'),
    ]
    ReportType = models.CharField(max_length=20, verbose_name="نوع التقرير",choices=REPORT_TYPE_CHOICES)
    GeneratedBy = models.ForeignKey(User,verbose_name="المستخدم" ,on_delete=models.CASCADE, related_name='reports')
    GeneratedDate = models.DateTimeField(auto_now_add=True)
    ReportData = models.TextField(verbose_name="بيانات التقرير")

    def _str_(self):
        return f"Report {self.id} - {self.ReportType}"

    class Meta:
        verbose_name = "تقرير"
        verbose_name_plural = "تقارير"

# نموذج DeliveryAssignment
class DeliveryAssignment(models.Model):
    STATUS_CHOICES = [
        ('Assigned', 'Assigned'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    Order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='assignments')
    DeliveryAgent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments')
    AssignedDate = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Assigned')

    def _str_(self):
        return f"Assignment {self.id} - {self.Status}"

    class Meta:
        verbose_name = "تعيين التوصيل"
        verbose_name_plural = "تعيينات التوصيل"


#نموذج لعمل FLASH SALES لاستخدامها في الصفحة الرئيسية
class FlashSale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    #سعر المنتج القديم و السعر بعد الخصم يورثه من كلاس برودكت
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "فلاش سيل"
        verbose_name_plural = "فلاش سيلات"

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

    class Meta:
        verbose_name = "رسالة"
        verbose_name_plural = "رسائل"

