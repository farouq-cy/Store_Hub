from django.contrib import admin
from .models import Role, User, Product, Order, Report, DeliveryAssignment

# تسجيل نموذج Role
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('RoleName',)  # الحقول المعروضة في القائمة
    search_fields = ('RoleName',)  # إمكانية البحث

# تسجيل نموذج User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'PhoneNumber', 'CreatedAt')  # استخدم 'role' بدلاً من 'Role'
    list_filter = ('role', 'CreatedAt')  # استخدم 'role' بدلاً من 'Role'
    search_fields = ('username', 'email', 'PhoneNumber')  # إمكانية البحث

# تسجيل نموذج Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'color', 'rating','image', 'total_likes')
    search_fields = ('name', 'color')
    list_display_links = ['name']

# تسجيل نموذج Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'Product', 'Customer', 'Quantity', 'Status', 'OrderDate')  # الحقول المعروضة في القائمة
    list_filter = ('Status', 'OrderDate')  # الفلاتر
    search_fields = ('Product__ProductName', 'Customer__username')  # إمكانية البحث
    list_display_links = ['Product']

# تسجيل نموذج Report
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'ReportType', 'GeneratedBy', 'GeneratedDate')  # الحقول المعروضة في القائمة
    list_filter = ('ReportType', 'GeneratedDate')  # الفلاتر
    search_fields = ('ReportType', 'GeneratedBy__username')  # إمكانية البحث

# تسجيل نموذج DeliveryAssignment
@admin.register(DeliveryAssignment)
class DeliveryAssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'Order', 'DeliveryAgent', 'Status', 'AssignedDate')  # الحقول المعروضة في القائمة
    list_filter = ('Status', 'AssignedDate')  # الفلاتر
    search_fields = ('Order__id', 'DeliveryAgent__username')  # إمكانية البحث

admin.site.site_header = 'STOREHUB'
admin.site.site_title = "STOREHUB"