from django.db import models
from django.contrib.auth.models import AbstractUser

# نموذج Roles
class Role(models.Model):
    RoleName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.RoleName

# نموذج Users
class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    PhoneNumber = models.CharField(max_length=15, blank=True, null=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)

    # تغيير related_name لتجنب التعارض
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

# نموذج Products
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم المنتج", blank=True, null=True, default="منتج بدون اسم")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر", default=0.00)

    image = models.ImageField(upload_to='products/', verbose_name="صورة المنتج", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="اللون", blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='product_likes', blank=True, verbose_name="اللايكات")
    rating = models.FloatField(
        default=0,
        verbose_name="التقييم"
    )
    
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

# نموذج Orders
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    Quantity = models.IntegerField()
    OrderDate = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    DeliveryAgent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')

    def __str__(self):
        return f"Order {self.id} - {self.Status}"

# نموذج Reports
class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('Sales', 'Sales'),
        ('Inventory', 'Inventory'),
        ('Financial', 'Financial'),
    ]
    ReportType = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    GeneratedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    GeneratedDate = models.DateTimeField(auto_now_add=True)
    ReportData = models.TextField()

    def __str__(self):
        return f"Report {self.id} - {self.ReportType}"

# نموذج DeliveryAssignments
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

    def __str__(self):
        return f"Assignment {self.id} - {self.Status}"