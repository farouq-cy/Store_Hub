from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# تسجيل نموذج User
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'PhoneNumber', 'CreatedAt')  # الحقول المعروضة في القائمة
    list_filter = ('role', 'CreatedAt')  # الفلاتر
    search_fields = ('username', 'email', 'PhoneNumber')  # إمكانية البحث
    readonly_fields = ('CreatedAt',)  # حقل للقراءة فقط

    # Action لتغيير دور اليوزر
    actions = ['make_delivery_agent', 'make_saler']

    @admin.action(description="Mark selected users as Delivery Agent")
    def make_delivery_agent(self, request, queryset):
        queryset.update(role='delivery_agent')

    @admin.action(description="Mark selected users as Saler")
    def make_saler(self, request, queryset):
        queryset.update(role='saler')

# تسجيل نموذج Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'color', 'rating', 'image', 'total_likes', 'category')  # الحقول المعروضة في القائمة
    search_fields = ('name', 'color')  # إمكانية البحث
    list_display_links = ['name']  # الروابط القابلة للنقر
    list_filter = ('rating', 'color')  # الفلاتر
    readonly_fields = ('total_likes',)  # حقل للقراءة فقط

    # دالة علشان نحسب عدد اللايكات
    def total_likes(self, obj):
        return obj.likes.count()
    total_likes.short_description = 'Total Likes'  # عنوان العمود في الـ Admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



# تسجيل نموذج Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'Product', 'Customer', 'Quantity', 'Status', 'OrderDate')  # الحقول المعروضة في القائمة
    list_filter = ('Status', 'OrderDate')  
    search_fields = ('Product__name', 'Customer__username')
    list_display_links = ('Product',)
    readonly_fields = ('OrderDate',)  # حقل للقراءة فقط

    # Action لتغيير حالة الطلبات
    actions = ['mark_as_completed']

    @admin.action(description="Mark selected orders as Completed")
    def mark_as_completed(self, request, queryset):
        queryset.update(Status='Completed')

# تسجيل نموذج Report
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'ReportType', 'GeneratedBy', 'GeneratedDate')  # الحقول المعروضة في القائمة
    list_filter = ('ReportType', 'GeneratedDate')  # الفلاتر
    search_fields = ('ReportType', 'GeneratedBy__username')  # إمكانية البحث
    readonly_fields = ('GeneratedDate',)  # حقل للقراءة فقط

# تسجيل نموذج DeliveryAssignment
@admin.register(DeliveryAssignment)
class DeliveryAssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'Order', 'DeliveryAgent', 'Status', 'AssignedDate')  # الحقول المعروضة في القائمة
    list_filter = ('Status', 'AssignedDate')  # الفلاتر
    search_fields = ('Order__id', 'DeliveryAgent__username')  # إمكانية البحث
    readonly_fields = ('AssignedDate',)  # حقل للقراءة فقط

    # Action لتغيير حالة التعيين
    actions = ['mark_as_delivered']

    @admin.action(description="Mark selected assignments as Delivered")
    def mark_as_delivered(self, request, queryset):
        queryset.update(Status='Delivered')

@admin.register(FlashSale)
class FlashSaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'start_date', 'end_date', 'old_price', 'new_price', 'rating')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone', 'message')



# إعدادات عامة للـ Admin
admin.site.site_header = 'STOREHUB'
admin.site.site_title = "STOREHUB"
admin.site.index_title = "Welcome to STOREHUB Admin Panel"
